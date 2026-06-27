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
    agent = {"id": agent_id, "name": name, "balance": 0.0, "created_at": _now()}
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


def get_agent(agent_id: str) -> dict:
    data = _load()
    if agent_id not in data["agents"]:
        raise KeyError(f"Agent '{agent_id}' not found")
    return data["agents"][agent_id]


def spend_budget(agent_id: str, amount: float, note: str = "") -> dict:
    """Record that the agent spent money on a trade (reduces remaining budget)."""
    if amount <= 0:
        raise ValueError("Amount must be positive")
    data = _load()
    if agent_id not in data["agents"]:
        raise KeyError(f"Agent '{agent_id}' not found")
    agent = data["agents"][agent_id]
    if amount > agent["balance"] - agent.get("spent", 0.0):
        raise ValueError("Insufficient budget")
    agent.setdefault("spent", 0.0)
    agent["spent"] += amount
    data["transactions"].append(
        {
            "id": str(uuid.uuid4())[:8],
            "agent_id": agent_id,
            "amount": -amount,
            "type": "debit",
            "note": note,
            "timestamp": _now(),
        }
    )
    _save(data)
    return agent


def list_agents() -> list[dict]:
    return list(_load()["agents"].values())


def get_transactions(agent_id: str) -> list[dict]:
    data = _load()
    if agent_id not in data["agents"]:
        raise KeyError(f"Agent '{agent_id}' not found")
    return [t for t in data["transactions"] if t["agent_id"] == agent_id]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()
