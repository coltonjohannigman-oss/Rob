"""AI trading brain — Claude-powered agentic options trader."""

import json
from typing import Any

import anthropic

import robinhood as rh_api
from agent import add_funds, get_agent, spend_budget

MODEL = "claude-opus-4-8"

SYSTEM_PROMPT = """\
You are an autonomous options trading agent operating within a strict budget.
You have access to real Robinhood market data and can place real option orders.

Rules:
- Never spend more than the allocated agent budget.
- Each contract controls 100 shares; cost = ask_price * 100 * quantity.
- Always check current positions and market data before trading.
- Use limit orders priced at or slightly above the ask for buys, at or slightly below bid for sells.
- Think carefully before placing any order — trades are real and cannot be undone instantly.
- When done, summarize what you did (or decided not to do) and why.
"""

TOOLS = [
    {
        "name": "get_stock_quote",
        "description": "Get current price and bid/ask for a stock symbol.",
        "input_schema": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string", "description": "Ticker symbol, e.g. AAPL"}
            },
            "required": ["symbol"],
        },
    },
    {
        "name": "get_nearby_expirations",
        "description": "List available option expiration dates within N weeks.",
        "input_schema": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "weeks_out": {"type": "integer", "description": "How many weeks to look ahead (default 4)"},
            },
            "required": ["symbol"],
        },
    },
    {
        "name": "get_options_chain",
        "description": "Get the options chain for a symbol on a given expiration date.",
        "input_schema": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "expiration_date": {"type": "string", "description": "YYYY-MM-DD"},
                "option_type": {"type": "string", "enum": ["call", "put"]},
            },
            "required": ["symbol", "expiration_date", "option_type"],
        },
    },
    {
        "name": "get_open_positions",
        "description": "Get all currently open option positions.",
        "input_schema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "get_agent_budget",
        "description": "Get the agent's current allocated budget and amount already spent.",
        "input_schema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "buy_option",
        "description": "Place a limit buy order for an option contract. Cost = limit_price * 100 * quantity.",
        "input_schema": {
            "type": "object",
            "properties": {
                "option_id": {"type": "string", "description": "The option contract ID from the chain"},
                "quantity": {"type": "integer", "description": "Number of contracts"},
                "limit_price": {"type": "number", "description": "Per-share limit price (e.g. 1.50 = $150/contract)"},
                "rationale": {"type": "string", "description": "Why you are making this trade"},
            },
            "required": ["option_id", "quantity", "limit_price", "rationale"],
        },
    },
    {
        "name": "close_position",
        "description": "Place a limit sell order to close an existing long option position.",
        "input_schema": {
            "type": "object",
            "properties": {
                "option_id": {"type": "string", "description": "The option contract ID"},
                "quantity": {"type": "integer", "description": "Number of contracts to close"},
                "limit_price": {"type": "number", "description": "Per-share limit price to sell at"},
                "rationale": {"type": "string", "description": "Why you are closing this position"},
            },
            "required": ["option_id", "quantity", "limit_price", "rationale"],
        },
    },
]


def _execute_tool(name: str, inputs: dict, agent_id: str, confirm: bool) -> Any:
    if name == "get_stock_quote":
        return rh_api.get_stock_quote(inputs["symbol"])

    if name == "get_nearby_expirations":
        return rh_api.get_nearby_expirations(inputs["symbol"], inputs.get("weeks_out", 4))

    if name == "get_options_chain":
        return rh_api.get_options_chain(inputs["symbol"], inputs["expiration_date"], inputs["option_type"])

    if name == "get_open_positions":
        return rh_api.get_open_option_positions()

    if name == "get_agent_budget":
        agent = get_agent(agent_id)
        return {
            "allocated": agent["balance"],
            "spent": agent.get("spent", 0.0),
            "remaining": agent["balance"] - agent.get("spent", 0.0),
        }

    if name == "buy_option":
        cost = inputs["limit_price"] * 100 * inputs["quantity"]
        agent = get_agent(agent_id)
        remaining = agent["balance"] - agent.get("spent", 0.0)
        if cost > remaining:
            return {"error": f"Insufficient budget. Cost ${cost:.2f} exceeds remaining ${remaining:.2f}"}

        print(f"\n[TRADE REQUEST] BUY {inputs['quantity']} contract(s) @ ${inputs['limit_price']:.2f}/share (${cost:.2f} total)")
        print(f"  Rationale: {inputs['rationale']}")

        if confirm:
            answer = input("Approve this trade? [y/N] ").strip().lower()
            if answer != "y":
                return {"status": "rejected", "reason": "User declined"}

        order = rh_api.buy_option(inputs["option_id"], inputs["quantity"], inputs["limit_price"])
        spend_budget(agent_id, cost, note=f"buy {inputs['quantity']}x @ {inputs['limit_price']}: {inputs['rationale']}")
        print(f"  Order placed: {order.get('id', 'unknown')}")
        return {"status": "placed", "order_id": order.get("id"), "cost": cost}

    if name == "close_position":
        print(f"\n[TRADE REQUEST] CLOSE {inputs['quantity']} contract(s) @ ${inputs['limit_price']:.2f}/share")
        print(f"  Rationale: {inputs['rationale']}")

        if confirm:
            answer = input("Approve this trade? [y/N] ").strip().lower()
            if answer != "y":
                return {"status": "rejected", "reason": "User declined"}

        order = rh_api.close_option_position(inputs["option_id"], inputs["quantity"], inputs["limit_price"])
        print(f"  Order placed: {order.get('id', 'unknown')}")
        return {"status": "placed", "order_id": order.get("id")}

    return {"error": f"Unknown tool: {name}"}


def run_trading_session(agent_id: str, trade_idea: str = "", confirm: bool = True) -> str:
    """Run an AI trading session. Returns the final summary."""
    rh_api.login()

    client = anthropic.Anthropic()

    user_content = "Review my portfolio and budget, then look for good options trading opportunities."
    if trade_idea:
        user_content += f"\n\nI have an idea for you to consider: {trade_idea}"

    messages = [{"role": "user", "content": user_content}]

    print(f"\n[AI] Starting trading session for agent {agent_id}...")
    if trade_idea:
        print(f"[AI] Trade idea: {trade_idea}")

    while True:
        response = client.messages.create(
            model=MODEL,
            max_tokens=8096,
            thinking={"type": "adaptive"},
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
        )

        tool_calls = [b for b in response.content if b.type == "tool_use"]
        text_blocks = [b for b in response.content if b.type == "text"]

        for block in text_blocks:
            if block.text.strip():
                print(f"\n[AI] {block.text.strip()}")

        if response.stop_reason == "end_turn" or not tool_calls:
            final_text = next((b.text for b in text_blocks if b.text.strip()), "Session complete.")
            return final_text

        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for call in tool_calls:
            print(f"\n[TOOL] {call.name}({json.dumps(call.input, separators=(',', ':'))})")
            result = _execute_tool(call.name, call.input, agent_id, confirm)
            print(f"  → {json.dumps(result, separators=(',', ':'))[:200]}")
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": call.id,
                "content": json.dumps(result),
            })

        messages.append({"role": "user", "content": tool_results})
