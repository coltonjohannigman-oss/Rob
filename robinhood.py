"""Robinhood connectivity layer — login, cash, options trading."""

import os
from datetime import date, timedelta

import robin_stocks.robinhood as rh


def login() -> None:
    username = os.environ["RH_USERNAME"]
    password = os.environ["RH_PASSWORD"]
    rh.login(username, password, expiresIn=86400, store_session=True)


def get_cash_balance() -> float:
    profile = rh.load_account_profile()
    return float(profile["cash"] or 0.0)


def get_open_option_positions() -> list[dict]:
    positions = rh.get_open_option_positions()
    results = []
    for p in positions:
        qty = float(p.get("quantity", 0))
        if qty <= 0:
            continue
        results.append({
            "option_id": p.get("option"),
            "symbol": p.get("chain_symbol"),
            "qty": qty,
            "avg_price": float(p.get("average_price") or 0),
            "type": p.get("type"),  # "long" or "short"
        })
    return results


def get_options_chain(symbol: str, expiration_date: str, option_type: str) -> list[dict]:
    """Return options chain for symbol. option_type: 'call' or 'put'."""
    chains = rh.find_options_by_expiration(symbol, expiration_date, optionType=option_type)
    results = []
    for c in chains:
        results.append({
            "id": c.get("id"),
            "strike_price": float(c.get("strike_price") or 0),
            "expiration_date": c.get("expiration_date"),
            "type": c.get("type"),
            "ask_price": float(c.get("ask_price") or 0),
            "bid_price": float(c.get("bid_price") or 0),
            "volume": int(c.get("volume") or 0),
            "open_interest": int(c.get("open_interest") or 0),
            "implied_volatility": float(c.get("implied_volatility") or 0),
            "delta": float(c.get("delta") or 0),
            "gamma": float(c.get("gamma") or 0),
            "theta": float(c.get("theta") or 0),
        })
    return results


def get_nearby_expirations(symbol: str, weeks_out: int = 4) -> list[str]:
    """Return available expiration dates up to weeks_out weeks from today."""
    chains = rh.get_chains(symbol)
    all_dates = chains.get("expiration_dates", [])
    cutoff = (date.today() + timedelta(weeks=weeks_out)).isoformat()
    return [d for d in all_dates if d <= cutoff]


def get_stock_quote(symbol: str) -> dict:
    q = rh.get_stock_quote_by_symbol(symbol)
    return {
        "symbol": symbol,
        "price": float(q.get("last_trade_price") or q.get("last_extended_hours_trade_price") or 0),
        "ask": float(q.get("ask_price") or 0),
        "bid": float(q.get("bid_price") or 0),
    }


def buy_option(option_id: str, quantity: int, limit_price: float) -> dict:
    """Place a limit buy order for an option contract."""
    order = rh.order_buy_option_limit(
        positionEffect="open",
        creditOrDebit="debit",
        price=round(limit_price, 2),
        symbol=None,
        quantity=quantity,
        expirationDate=None,
        strike=None,
        optionType=None,
        timeInForce="gfd",
        jsonify=True,
        optionId=option_id,
    )
    return order


def close_option_position(option_id: str, quantity: int, limit_price: float) -> dict:
    """Place a limit sell order to close a long option position."""
    order = rh.order_sell_option_limit(
        positionEffect="close",
        creditOrDebit="credit",
        price=round(limit_price, 2),
        symbol=None,
        quantity=quantity,
        expirationDate=None,
        strike=None,
        optionType=None,
        timeInForce="gfd",
        jsonify=True,
        optionId=option_id,
    )
    return order
