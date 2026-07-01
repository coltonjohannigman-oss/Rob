---
description: Bounded autonomous trading window — Robbin buys and sells without per-order confirmation
---

AUTOPILOT MODE — a bounded standing authorization from the account owner to trade WITHOUT
per-order confirmation, granted for a fixed window. Outside this mode, confirmation is always
required. Argument: window length in minutes (default 60). Example: `/autopilot 60`.

**Account:** Agentic account `452369101`. **Ledger:** `python cli.py balance b7763d77`.
**Persona:** Read `brain.py` PERSONA first — every rule applies in autopilot, especially the
liquidity rubric, portfolio caps, binary-event restrictions, and bookkeeping.

**Session start:**
1. Fresh quote for wall-clock time (report Central Time). Compute the window end time.
2. Ledger + broker reconcile, position and stop audit — same as /trade steps 1-3.
3. Send a push notification: autopilot engaged, window end time, current positions.

**The cycle — repeat every ~10 minutes (ScheduleWakeup, ~600s), until the window ends:**
1. EXITS FIRST — for each open position, against live marks:
   - Take-profit: if inside its profit band and momentum is NOT confirming higher (volume
     fading, structure stalling), SELL at the mid. If the extreme-confidence checklist holds,
     trail instead per PERSONA.
   - Stop ratchet: raise stops per trailing rules (never lower them).
   - Thesis stop: breakout level lost / catalyst dead → sell immediately at the mid,
     do not wait for the hard stop.
2. SCAN — both saved scanners + watchlist trigger check. Volume gate first.
3. GRADE — any candidate gets the full workup before entry: 90-day history (mandatory),
   5-factor check, liquidity rubric, portfolio caps, binary-event rule.
4. ENTER without asking when a setup fully qualifies:
   - Default sizing: conservative cap (20% of remaining). The 40% aggressive cap requires an
     A+ grade (all Qullamaggie legs present) — state the grade in the log.
   - Maximum 2 NEW positions per window.
   - Place the stop order the same cycle as the fill. No unprotected positions, ever.
5. BOOK — after any fill: `python cli.py buy/sell ...`, update trades.md on closes, commit and
   push state, and send a push notification (one line: what, price, P&L or stop level).
6. If nothing to do, do nothing — cash remains a position. Log the cycle in one line.

**Hard limits (cannot be overridden inside a window):**
- All PERSONA risk caps: max 3 concurrent positions, 60% deployed, never average down.
- No new entries within the binary-event restriction (final session before a macro print,
  or 30 min before any scheduled market-moving release).
- Never spend beyond the ledger's remaining balance.
- Any user message during the window that says stop/halt/pause ends autopilot immediately.

**Window end (or user abort):**
1. Confirmation mode reverts to ON automatically — say so explicitly.
2. Final audit: positions, stops, ledger reconcile, push state to git.
3. Send a push notification with the handoff summary: trades made, P&L, open positions,
   working stops, and anything that needs a human decision.

**Honest constraints to restate at session start:** if the cloud container dies mid-window,
the cycles stop silently — broker-side GTC stops keep protecting every position, and silence
on your phone means no fills happened. The push-per-fill is the heartbeat.

$ARGUMENTS
