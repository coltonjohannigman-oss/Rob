"""Robinhood connectivity — now handled via Claude Code MCP tools.

All live market data and order placement is done through the Robinhood MCP
server connected to Claude Code. This module is kept as a placeholder;
the actual implementation lives in the Claude Code session.
"""


def login() -> None:
    """No-op — authentication is handled by the MCP server."""
    pass


def get_cash_balance() -> float:
    raise NotImplementedError(
        "Use Claude Code to check your cash balance: 'What is my Robinhood cash balance?'"
    )


def get_open_option_positions() -> list[dict]:
    raise NotImplementedError(
        "Use Claude Code to check positions: 'Show my open option positions.'"
    )


def get_options_chain(symbol: str, expiration_date: str, option_type: str) -> list[dict]:
    raise NotImplementedError("Use Claude Code to query options chains.")


def get_nearby_expirations(symbol: str, weeks_out: int = 4) -> list[str]:
    raise NotImplementedError("Use Claude Code to query expiration dates.")


def get_stock_quote(symbol: str) -> dict:
    raise NotImplementedError("Use Claude Code to get quotes.")


def buy_option(option_id: str, quantity: int, limit_price: float) -> dict:
    raise NotImplementedError("Use Claude Code to place option orders.")


def close_option_position(option_id: str, quantity: int, limit_price: float) -> dict:
    raise NotImplementedError("Use Claude Code to close option positions.")
