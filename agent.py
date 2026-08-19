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


def record_sell(agent_id: str, proceeds: float, cost_basis: float, note: str = "") -> dict:
    """Record a closing trade: releases the cost basis and books realized P&L.

    proceeds may be 0 (position expired worthless). cost_basis must match the
    open cost recorded by record_buy so the books stay balanced.
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
    data["transactions"].append(
        {
            "id": str(uuid.uuid4())[:8],
            "agent_id": agent_id,
            "amount": proceeds,
            "type": "credit",
            "note": note,
            "timestamp": _now(),
        }
    )
    _save(data)
    return agent


def reconcile(agent_id: str, broker_buying_power: float, note: str = "") -> dict:
    """Force the ledger's free cash to match the broker's authoritative buying power.

    The ledger is a manual write-ahead log: nothing writes to it automatically, so
    it silently freezes whenever a fill happens outside a recording session (a stop
    firing unattended, an owner's in-app trade, or a session that died before
    `git push`). This books the whole unexplained difference as ONE adjustment so
    the books match the broker again.

    `spent` (open cost basis) is deliberately left alone — broker buying power
    already excludes open positions, so remaining (balance - spent) is the figure
    that must match. `realized_pnl` is also left alone: an unexplained adjustment
    is not trading profit, and folding it into P&L would corrupt the performance
    record. Reconstruct and record real trades with record_buy/record_sell when
    you can identify them; use this only for the residue.
    """
    if broker_buying_power < 0:
        raise ValueError("Broker buying power cannot be negative")
    data = _load()
    if agent_id not in data["agents"]:
        raise KeyError(f"Agent '{agent_id}' not found")
    agent = data["agents"][agent_id]
    remaining = agent["balance"] - agent.get("spent", 0.0)
    delta = round(broker_buying_power - remaining, 2)
    if delta == 0:
        return agent
    agent["balance"] = round(agent["balance"] + delta, 2)
    data["transactions"].append(
        {
            "id": str(uuid.uuid4())[:8],
            "agent_id": agent_id,
            "amount": delta,
            "type": "credit" if delta > 0 else "debit",
            "note": note or f"Reconcile to broker buying power ${broker_buying_power:.2f}",
            "timestamp": _now(),
        }
    )
    _save(data)
    return agent


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
