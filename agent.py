"""Agent funding system — manage balances for named agents."""

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

DB_FILE = Path("agents.json")


def _load() -> dict:
    if DB_FILE.exists():
        return json.loads(DB_FILE.read_text())
    return {"agents": {}, "transactions": []}


def _save(data: dict) -> None:
    DB_FILE.write_text(json.dumps(data, indent=2))


def create_agent(name: str) -> dict:
    data = _load()
    agent_id = str(uuid.uuid4())[:8]
    agent = {
        "id": agent_id,
        "name": name,
        "balance": 0.0,
        "spent": 0.0,
        "realized_pnl": 0.0,
        "created_at": _now(),
    }
    data["agents"][agent_id] = agent
    _save(data)
    return agent


def add_funds(agent_id: str, amount: float, note: str = "") -> dict:
    if amount <= 0:
        raise ValueError("Amount must be positive")
    data = _load()
    if agent_id not in data["agents"]:
        raise KeyError(f"Agent '{agent_id}' not found")
    data["agents"][agent_id]["balance"] += amount
    data["transactions"].append(
        {
            "id": str(uuid.uuid4())[:8],
            "agent_id": agent_id,
            "amount": amount,
            "type": "credit",
            "note": note,
            "timestamp": _now(),
        }
    )
    _save(data)
    return data["agents"][agent_id]


def record_buy(agent_id: str, cost: float, note: str = "") -> dict:
    """Record an opening trade: cost moves from remaining budget into open cost basis."""
    if cost <= 0:
        raise ValueError("Cost must be positive")
    data = _load()
    if agent_id not in data["agents"]:
        raise KeyError(f"Agent '{agent_id}' not found")
    agent = data["agents"][agent_id]
    remaining = agent["balance"] - agent.get("spent", 0.0)
    if cost > remaining:
        raise ValueError(f"Cost ${cost:.2f} exceeds remaining budget ${remaining:.2f}")
    agent["spent"] = agent.get("spent", 0.0) + cost
    data["transactions"].append(
        {
            "id": str(uuid.uuid4())[:8],
            "agent_id": agent_id,
            "amount": -cost,
            "type": "debit",
            "note": note,
            "timestamp": _now(),
        }
    )
    _save(data)
    return agent


def record_sell(
    agent_id: str,
    proceeds: float,
    cost_basis: float,
    note: str = "",
    setup: str = "",
    grade: str = "",
) -> dict:
    """Record a closing trade: releases the cost basis and books realized P&L.

    proceeds may be 0 (position expired worthless). cost_basis must match the
    open cost recorded by record_buy so the books stay balanced. setup and grade
    tag the closed trade so trade_stats can measure quality by setup type/grade.
    """
    if proceeds < 0:
        raise ValueError("Proceeds cannot be negative")
    if cost_basis <= 0:
        raise ValueError("Cost basis must be positive")
    data = _load()
    if agent_id not in data["agents"]:
        raise KeyError(f"Agent '{agent_id}' not found")
    agent = data["agents"][agent_id]
    spent = agent.get("spent", 0.0)
    if cost_basis > spent + 1e-9:
        raise ValueError(f"Cost basis ${cost_basis:.2f} exceeds open cost basis ${spent:.2f}")
    pnl = proceeds - cost_basis
    agent["spent"] = spent - cost_basis
    agent["balance"] += pnl
    agent["realized_pnl"] = agent.get("realized_pnl", 0.0) + pnl
    txn = {
        "id": str(uuid.uuid4())[:8],
        "agent_id": agent_id,
        "amount": proceeds,
        "type": "credit",
        "note": note,
        "timestamp": _now(),
        "cost_basis": cost_basis,
        "pnl": pnl,
    }
    if setup:
        txn["setup"] = setup
    if grade:
        txn["grade"] = grade
    data["transactions"].append(txn)
    _save(data)
    return agent


def closed_trades(agent_id: str) -> list[dict]:
    """Closing transactions (those carrying a cost_basis), oldest first."""
    return [t for t in get_transactions(agent_id) if "cost_basis" in t]


def trade_stats(agent_id: str, last: int = 0) -> dict:
    """Win rate, average win/loss and expectancy over closed trades.

    last > 0 restricts the stats to the most recent N closed trades.
    Returns an empty-trade summary (trades == 0) when nothing has closed yet.
    """
    trades = closed_trades(agent_id)
    if last > 0:
        trades = trades[-last:]
    returns = [t["pnl"] / t["cost_basis"] for t in trades]
    wins = [r for r in returns if r > 0]
    losses = [r for r in returns if r <= 0]
    streak = 0
    for t in reversed(trades):
        if t["pnl"] > 0:
            break
        streak += 1
    by_grade: dict[str, list[float]] = {}
    for t, r in zip(trades, returns):
        by_grade.setdefault(t.get("grade", "ungraded"), []).append(r)
    n = len(trades)
    return {
        "trades": n,
        "wins": len(wins),
        "losses": len(losses),
        "win_rate": len(wins) / n if n else 0.0,
        "avg_win_pct": sum(wins) / len(wins) if wins else 0.0,
        "avg_loss_pct": sum(losses) / len(losses) if losses else 0.0,
        "expectancy_pct": sum(returns) / n if n else 0.0,
        "total_pnl": sum(t["pnl"] for t in trades),
        "losing_streak": streak,
        "by_grade": {
            g: {"trades": len(rs), "expectancy_pct": sum(rs) / len(rs)}
            for g, rs in sorted(by_grade.items())
        },
    }


def get_agent(agent_id: str) -> dict:
    data = _load()
    if agent_id not in data["agents"]:
        raise KeyError(f"Agent '{agent_id}' not found")
    return data["agents"][agent_id]


def list_agents() -> list[dict]:
    return list(_load()["agents"].values())


def get_transactions(agent_id: str) -> list[dict]:
    data = _load()
    if agent_id not in data["agents"]:
        raise KeyError(f"Agent '{agent_id}' not found")
    return [t for t in data["transactions"] if t["agent_id"] == agent_id]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()
