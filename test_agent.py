"""Tests for the agent funding system."""

import json
import os
import tempfile
from pathlib import Path
from unittest import mock

import pytest

import agent as ag


@pytest.fixture(autouse=True)
def tmp_db(tmp_path):
    """Redirect DB_FILE to a temp path for each test."""
    db = tmp_path / "agents.json"
    with mock.patch.object(ag, "DB_FILE", db):
        yield db


def test_create_agent():
    a = ag.create_agent("Alice")
    assert a["name"] == "Alice"
    assert a["balance"] == 0.0
    assert len(a["id"]) == 8


def test_add_funds():
    a = ag.create_agent("Bob")
    updated = ag.add_funds(a["id"], 50.0)
    assert updated["balance"] == 50.0


def test_add_funds_accumulates():
    a = ag.create_agent("Carol")
    ag.add_funds(a["id"], 25.0)
    ag.add_funds(a["id"], 75.0)
    assert ag.get_agent(a["id"])["balance"] == 100.0


def test_add_funds_rejects_negative():
    a = ag.create_agent("Dave")
    with pytest.raises(ValueError):
        ag.add_funds(a["id"], -10.0)


def test_add_funds_rejects_zero():
    a = ag.create_agent("Eve")
    with pytest.raises(ValueError):
        ag.add_funds(a["id"], 0)


def test_fund_unknown_agent():
    with pytest.raises(KeyError):
        ag.add_funds("nope1234", 10.0)


def test_transaction_history():
    a = ag.create_agent("Frank")
    ag.add_funds(a["id"], 10.0, note="first deposit")
    ag.add_funds(a["id"], 20.0, note="second deposit")
    txns = ag.get_transactions(a["id"])
    assert len(txns) == 2
    assert txns[0]["amount"] == 10.0
    assert txns[1]["note"] == "second deposit"


def test_list_agents():
    ag.create_agent("G1")
    ag.create_agent("G2")
    agents = ag.list_agents()
    assert len(agents) == 2
    names = {a["name"] for a in agents}
    assert names == {"G1", "G2"}


def test_get_unknown_agent():
    with pytest.raises(KeyError):
        ag.get_agent("deadbeef")


def test_record_buy_moves_cost_to_spent():
    a = ag.create_agent("Hank")
    ag.add_funds(a["id"], 200.0)
    updated = ag.record_buy(a["id"], 74.0, note="SOFI call")
    assert updated["spent"] == 74.0
    assert updated["balance"] == 200.0  # balance untouched; remaining = 126


def test_record_buy_rejects_overspend():
    a = ag.create_agent("Iris")
    ag.add_funds(a["id"], 50.0)
    with pytest.raises(ValueError):
        ag.record_buy(a["id"], 60.0)


def test_record_sell_books_profit():
    a = ag.create_agent("Jack")
    ag.add_funds(a["id"], 200.0)
    ag.record_buy(a["id"], 85.0, note="IRDM call")
    updated = ag.record_sell(a["id"], 130.0, 85.0, note="IRDM TP hit")
    assert updated["spent"] == 0.0
    assert updated["balance"] == 245.0  # 200 + 45 profit
    assert updated["realized_pnl"] == 45.0


def test_record_sell_books_loss_and_worthless_expiry():
    a = ag.create_agent("Kate")
    ag.add_funds(a["id"], 200.0)
    ag.record_buy(a["id"], 100.0)
    updated = ag.record_sell(a["id"], 0.0, 100.0, note="expired worthless")
    assert updated["spent"] == 0.0
    assert updated["balance"] == 100.0
    assert updated["realized_pnl"] == -100.0


def test_record_sell_rejects_basis_exceeding_open_positions():
    a = ag.create_agent("Liam")
    ag.add_funds(a["id"], 200.0)
    ag.record_buy(a["id"], 50.0)
    with pytest.raises(ValueError):
        ag.record_sell(a["id"], 80.0, 60.0)


def test_record_sell_tags_closed_trade():
    a = ag.create_agent("Mia")
    ag.add_funds(a["id"], 200.0)
    ag.record_buy(a["id"], 100.0)
    ag.record_sell(a["id"], 140.0, 100.0, setup="EP", grade="A+")
    (t,) = ag.closed_trades(a["id"])
    assert t["cost_basis"] == 100.0
    assert t["pnl"] == 40.0
    assert t["setup"] == "EP"
    assert t["grade"] == "A+"


def test_trade_stats_empty():
    a = ag.create_agent("Noah")
    ag.add_funds(a["id"], 100.0)  # credits without cost_basis are not trades
    s = ag.trade_stats(a["id"])
    assert s["trades"] == 0
    assert s["win_rate"] == 0.0


def test_trade_stats_expectancy_streak_and_grades():
    a = ag.create_agent("Olga")
    ag.add_funds(a["id"], 1000.0)
    for proceeds, grade in [(150.0, "A+"), (70.0, "A"), (75.0, "A")]:
        ag.record_buy(a["id"], 100.0)
        ag.record_sell(a["id"], proceeds, 100.0, grade=grade)
    s = ag.trade_stats(a["id"])
    assert s["trades"] == 3
    assert s["wins"] == 1 and s["losses"] == 2
    assert s["avg_win_pct"] == pytest.approx(0.50)
    assert s["avg_loss_pct"] == pytest.approx(-0.275)
    assert s["expectancy_pct"] == pytest.approx((0.50 - 0.30 - 0.25) / 3)
    assert s["total_pnl"] == pytest.approx(-5.0)
    assert s["losing_streak"] == 2
    assert s["by_grade"]["A"]["trades"] == 2
    assert s["by_grade"]["A+"]["expectancy_pct"] == pytest.approx(0.50)


def test_trade_stats_last_n():
    a = ag.create_agent("Pete")
    ag.add_funds(a["id"], 1000.0)
    for proceeds in (50.0, 150.0, 130.0):
        ag.record_buy(a["id"], 100.0)
        ag.record_sell(a["id"], proceeds, 100.0)
    s = ag.trade_stats(a["id"], last=2)
    assert s["trades"] == 2
    assert s["win_rate"] == 1.0
    assert s["losing_streak"] == 0


def _close(agent_id, proceeds, basis=100.0):
    ag.record_buy(agent_id, basis)
    ag.record_sell(agent_id, proceeds, basis)


def test_trade_stats_dollar_metrics_and_outlier_share():
    a = ag.create_agent("Quinn")
    ag.add_funds(a["id"], 1000.0)
    for proceeds in (400.0, 110.0, 60.0):
        _close(a["id"], proceeds)
    s = ag.trade_stats(a["id"])
    assert s["avg_win_usd"] == pytest.approx(155.0)
    assert s["avg_loss_usd"] == pytest.approx(-40.0)
    assert s["profit_factor"] == pytest.approx(310.0 / 40.0)
    assert s["top_win_share"] == pytest.approx(300.0 / 270.0)


def test_trade_stats_profit_factor_undefined_without_losses():
    a = ag.create_agent("Rita")
    ag.add_funds(a["id"], 1000.0)
    _close(a["id"], 150.0)
    assert ag.trade_stats(a["id"])["profit_factor"] is None


def test_drawdown_level_one_loss_in_a_thin_record_is_not_a_brake():
    # The 2026-10 lockout: a single graded loss read as "negative expectancy".
    a = ag.create_agent("Sam")
    ag.add_funds(a["id"], 1000.0)
    _close(a["id"], 65.0)
    assert ag.drawdown_level(a["id"])["level"] == 0


def test_drawdown_level_two_then_three_losses():
    a = ag.create_agent("Tess")
    ag.add_funds(a["id"], 1000.0)
    _close(a["id"], 150.0)
    _close(a["id"], 70.0)
    _close(a["id"], 70.0)
    assert ag.drawdown_level(a["id"])["level"] == 1
    _close(a["id"], 70.0)
    assert ag.drawdown_level(a["id"])["level"] == 2


def test_drawdown_level_two_cools_off_without_a_trade():
    from datetime import datetime, timedelta, timezone

    a = ag.create_agent("Uma")
    ag.add_funds(a["id"], 1000.0)
    for _ in range(3):
        _close(a["id"], 70.0)
    later = datetime.now(timezone.utc) + timedelta(days=ag.LEVEL_2_COOL_OFF_DAYS + 1)
    assert ag.drawdown_level(a["id"], now=later)["level"] == 1


def test_drawdown_level_negative_expectancy_needs_a_sample():
    a = ag.create_agent("Vic")
    ag.add_funds(a["id"], 2000.0)
    for proceeds in (60.0, 105.0, 60.0, 105.0, 60.0, 105.0):
        _close(a["id"], proceeds)
    d = ag.drawdown_level(a["id"])
    assert d["level"] == 1 and d["losing_streak"] == 0


def test_drawdown_level_winner_resets():
    a = ag.create_agent("Wes")
    ag.add_funds(a["id"], 1000.0)
    _close(a["id"], 70.0)
    _close(a["id"], 70.0)
    _close(a["id"], 180.0)
    assert ag.drawdown_level(a["id"])["level"] == 0
