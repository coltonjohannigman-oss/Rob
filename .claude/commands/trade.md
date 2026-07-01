---
description: Run an options trading session for the Agentic Robinhood account
---

Run an options trading session using the Robinhood MCP tools.

**Account:** Agentic account `452369101` (the only agentic-allowed, options-enabled account).
**Timezone:** Report all times in CENTRAL TIME. You have no clock — read the wall-clock time
from the timestamp of a fresh quote (e.g. SPY) at session start, and never state a time from a
stale quote.

**Persona & rules:** Read `brain.py` and follow the `PERSONA` block exactly — it is the single
source of truth for strategy, setups (Qullamaggie episodic pivot / momentum / short squeeze),
stop losses, profit-taking, pricing discipline, liquidity exceptions, portfolio caps, binary
events, broker mechanics, and bookkeeping. Do not improvise around it.

**Process — every session, in order:**
1. Read the `PERSONA` in `brain.py`. Get a fresh quote to establish the current time.
2. **Ledger:** `python cli.py balance b7763d77` — then reconcile against live broker buying
   power (`get_portfolio`). If they disagree, say so and resolve before trading.
3. **Positions & stop audit:** list open positions AND working orders. Every position must have
   a working stop at the right level; flag any that are unprotected or whose stop lags the
   PERSONA's trailing rules.
4. **Take-profit duty:** for each open position, compare the current mark to its profit band
   (30-80% default). If a position is in the band, proactively present the take-profit case with
   dollar numbers and a recommendation — do not wait to be asked. Apply the binary-event and
   decision-latency rules from the PERSONA.
5. **Watchlist triggers:** check the saved watchlists (their descriptions carry the trigger
   levels, e.g. OUST pullback zone, RSI breakout level) and report trigger status.
6. **Scan:** run the saved scanners (Daily Gainers / Episodic Pivot Watch, and High Options
   Volume / Smart Money Flow) per the persona's 5-factor criteria and the three proven setups.
   Volume confirmation is the first gate (premarket relative volume is meaningless — see
   PERSONA broker mechanics). **Pull at least 90 days of price history before grading any
   setup** — no grade without the chart.
7. If a trade qualifies, run `review_option_order` and present the full details — strike,
   expiry, delta, cost, liquidity (OI / volume / spread %), the setup it matches, sizing vs.
   the 20%/40% caps, portfolio-cap check, and the thesis with its stop and profit plan.
8. **Wait for my explicit confirmation before placing any order.** (Confirmation stays ON until
   I say otherwise. The one standing exception, per PERSONA: raising a stop to protect a 40%+
   gain when I am unreachable.)
9. **After any fill:** record it immediately (`python cli.py buy/sell ...`), set/verify the
   stop, update `trades.md` on closes, then commit and push `agents.json` + `trades.md` to the
   working branch so state survives the container.
10. If nothing qualifies, say so plainly — cash is a position. Do not manufacture a trade.

**Scheduling note:** in-session scheduled check-ins die if the cloud container idles out. When
one is set, always tell the user the fallback: "if you don't hear from me by <time>, send
/trade". At session start, check `CronList` and re-arm any standing check-in that was lost.

$ARGUMENTS
