"""Trading brain — session runner for the Claude Code MCP-based agent.

Trading sessions are driven by Claude Code directly, which has live MCP access
to your Robinhood account. Call run_trading_session() to print the prompt you
should paste into Claude Code to start a session.
"""

from agent import get_agent


def run_trading_session(agent_id: str, trade_idea: str = "", confirm: bool = True) -> str:
    """Print the Claude Code prompt to kick off a trading session."""
    agent = get_agent(agent_id)
    spent = agent.get("spent", 0.0)
    remaining = agent["balance"] - spent

    lines = [
        f"Run a Robinhood options trading session for agent '{agent['name']}' (id: {agent_id}).",
        f"Budget: ${agent['balance']:.2f} allocated, ${spent:.2f} spent, ${remaining:.2f} remaining.",
    ]
    if trade_idea:
        lines.append(f"Trade idea: {trade_idea}")
    if confirm:
        lines.append("Ask me to confirm before placing any order.")
    else:
        lines.append("Auto-approve mode: place orders without asking for confirmation.")

    prompt = "\n".join(lines)
    print("\nPaste the following into Claude Code to start your trading session:\n")
    print("─" * 60)
    print(prompt)
    print("─" * 60)
    return prompt
