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
        print(f"Agent '{agent['name']}' (id: {agent['id']}) — balance: ${agent['balance']:.2f}")
    except KeyError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_list(args):
    agents = list_agents()
    if not agents:
        print("No agents found.")
        return
    for a in agents:
        print(f"  {a['id']}  {a['name']:<20}  ${a['balance']:.2f}")


def cmd_history(args):
    try:
        txns = get_transactions(args.id)
        if not txns:
            print("No transactions.")
            return
        for t in txns:
            note = f"  ({t['note']})" if t["note"] else ""
            print(f"  {t['timestamp']}  +${t['amount']:.2f}{note}")
    except KeyError as e:
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

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
