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
