#!/usr/bin/env python3
"""CLI for the agent funding system."""

import argparse
import sys

from agent import add_funds, create_agent, get_agent, get_transactions, list_agents


def cmd_create(args):
    agent = create_agent(args.name)
    print(f"Created agent '{agent['name']}' (id: {agent['id']})")


def cmd_fund(args):
    try:
        agent = add_funds(args.id, args.amount, note=args.note or "")
        print(f"Added ${args.amount:.2f} to '{agent['name']}' — new balance: ${agent['balance']:.2f}")
    except (KeyError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_balance(args):
    try:
        agent = get_agent(args.id)
        spent = agent.get("spent", 0.0)
        remaining = agent["balance"] - spent
        print(f"Agent '{agent['name']}' (id: {agent['id']})")
        print(f"  Allocated: ${agent['balance']:.2f}  |  Spent: ${spent:.2f}  |  Remaining: ${remaining:.2f}")
    except KeyError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_list(args):
    agents = list_agents()
    if not agents:
        print("No agents found.")
        return
    for a in agents:
        spent = a.get("spent", 0.0)
        remaining = a["balance"] - spent
        print(f"  {a['id']}  {a['name']:<20}  allocated: ${a['balance']:.2f}  remaining: ${remaining:.2f}")


def cmd_history(args):
    try:
        txns = get_transactions(args.id)
        if not txns:
            print("No transactions.")
            return
        for t in txns:
            sign = "+" if t["amount"] >= 0 else ""
            note = f"  ({t['note']})" if t["note"] else ""
            print(f"  {t['timestamp']}  {sign}${t['amount']:.2f}{note}")
    except KeyError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_rh_cash(args):
    try:
        from dotenv import load_dotenv
        load_dotenv()
        import robinhood as rh_api
        rh_api.login()
        cash = rh_api.get_cash_balance()
        print(f"Robinhood cash balance: ${cash:.2f}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_rh_fund(args):
    """Allocate cash from Robinhood account into an agent's budget."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
        import robinhood as rh_api
        rh_api.login()
        cash = rh_api.get_cash_balance()
        if args.amount > cash:
            print(f"Error: Robinhood cash balance (${cash:.2f}) is less than requested ${args.amount:.2f}", file=sys.stderr)
            sys.exit(1)
        agent = add_funds(args.id, args.amount, note=f"funded from Robinhood cash (available: ${cash:.2f})")
        print(f"Allocated ${args.amount:.2f} from Robinhood to agent '{agent['name']}' — new budget: ${agent['balance']:.2f}")
        print(f"Remaining Robinhood cash: ${cash - args.amount:.2f} (note: transfer must be done manually in Robinhood app)")
    except (KeyError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_positions(args):
    try:
        from dotenv import load_dotenv
        load_dotenv()
        import robinhood as rh_api
        rh_api.login()
        positions = rh_api.get_open_option_positions()
        if not positions:
            print("No open option positions.")
            return
        for p in positions:
            print(f"  {p['symbol']}  {p['type']}  qty={p['qty']}  avg=${p['avg_price']:.2f}  id={p['option_id']}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_trade(args):
    try:
        from dotenv import load_dotenv
        load_dotenv()
        from brain import run_trading_session
        summary = run_trading_session(
            agent_id=args.id,
            trade_idea=args.idea or "",
            confirm=not args.auto_approve,
        )
        print(f"\n[SESSION SUMMARY]\n{summary}")
    except (KeyError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Agent funding system")
    sub = parser.add_subparsers(dest="command", required=True)

    p_create = sub.add_parser("create", help="Create a new agent")
    p_create.add_argument("name", help="Agent name")
    p_create.set_defaults(func=cmd_create)

    p_fund = sub.add_parser("fund", help="Add money to an agent")
    p_fund.add_argument("id", help="Agent ID")
    p_fund.add_argument("amount", type=float, help="Amount to add (USD)")
    p_fund.add_argument("--note", help="Optional note for the transaction")
    p_fund.set_defaults(func=cmd_fund)

    p_balance = sub.add_parser("balance", help="Check agent balance")
    p_balance.add_argument("id", help="Agent ID")
    p_balance.set_defaults(func=cmd_balance)

    p_list = sub.add_parser("list", help="List all agents")
    p_list.set_defaults(func=cmd_list)

    p_history = sub.add_parser("history", help="Show transaction history for an agent")
    p_history.add_argument("id", help="Agent ID")
    p_history.set_defaults(func=cmd_history)

    p_rh_cash = sub.add_parser("rh-cash", help="Show Robinhood investing account cash balance")
    p_rh_cash.set_defaults(func=cmd_rh_cash)

    p_rh_fund = sub.add_parser("rh-fund", help="Allocate cash from Robinhood to an agent")
    p_rh_fund.add_argument("id", help="Agent ID")
    p_rh_fund.add_argument("amount", type=float, help="Amount to allocate (USD)")
    p_rh_fund.set_defaults(func=cmd_rh_fund)

    p_positions = sub.add_parser("positions", help="Show open Robinhood option positions")
    p_positions.set_defaults(func=cmd_positions)

    p_trade = sub.add_parser("trade", help="Run an AI trading session for an agent")
    p_trade.add_argument("id", help="Agent ID")
    p_trade.add_argument("--idea", help="A trade idea or thesis to give the AI")
    p_trade.add_argument("--auto-approve", action="store_true", help="Skip confirmation prompts before placing orders")
    p_trade.set_defaults(func=cmd_trade)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
