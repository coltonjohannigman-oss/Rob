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
   **Quality:** `python cli.py stats b7763d77` and `--last 10` — report the one-line summary
   and whether the PERSONA's DRAWDOWN BRAKE is on.
   **Regime:** SPY/QQQ vs. their 10/20-day EMAs → RISK-ON / CHOP / RISK-OFF, stated in one line.
3. **Positions & stop audit:** list open positions AND working orders. Every position must have
   a working stop at the right level; flag any that are unprotected or whose stop lags the
   PERSONA's trailing rules.
4. **Take-profit duty:** for each open position, compare the current mark to its profit band
   (30-80% default). If a position is in the band, proactively present the take-profit case with
   dollar numbers and a recommendation — do not wait to be asked. Apply the binary-event and
   decision-latency rules from the PERSONA.
5. **Pipeline & watchlist triggers:** read `pipeline.md` first — for each entry, report
   triggered / not yet / invalidated, and re-score any that triggered. Then check the saved
   watchlists (their descriptions carry trigger levels) and the focus-universe watchlist for
   setups in formation.
6. **Scan BOTH directions:** run the saved scanners — Daily Gainers / Episodic Pivot Watch,
   High Options Volume / Smart Money Flow, and **Daily Losers / Breakdown & EP-Down Watch**
   (bearish setups are long PUTS per the PERSONA's BEARISH SETUPS section). Volume
   confirmation is the first gate either way (premarket relative volume is meaningless — see
   PERSONA broker mechanics). **Pull at least 90 days of price history before grading any
   setup** — no grade without the chart. Score every serious candidate on the PERSONA's
   SETUP SCORECARD and present a ranked shortlist (top 3, per-factor scores shown).
7. If a trade grades A or A+, run `review_option_order` and present the full details — strike,
   expiry, delta, cost, contract count, liquidity (OI / volume / spread %), the per-factor
   scorecard, sizing vs. the grade cap, portfolio caps + heat, reward:risk, the ADR, the entry
   trigger (opening-range high/low) and the low-of-day stop anchor with its option-price
   equivalent, and the thesis with its profit plan (including the scale-out plan on 2+ contracts).
   B grades go into `pipeline.md` with their upgrade trigger, and get a price alert.
8. **Wait for my explicit confirmation before opening any position or making a discretionary
   sell.** (Confirmation stays ON until I say otherwise. The scoped exceptions live in the
   PERSONA's ORDER MANAGEMENT AUTHORIZATION and DECISION LATENCY sections: managing orders on
   existing positions — stop ratchets, take-profit adjustments, stop↔TP swaps — is authorized
   without per-change confirmation, with a push notification for every change.)
9. **After any fill:** record it immediately (`python cli.py buy/sell ...`, with `--setup` and
   `--grade` on sells), set/verify the stop, update `trades.md` on closes, then commit and push
   `agents.json` + `trades.md` + `pipeline.md` to the working branch so state survives the
   container. Update `pipeline.md` at session end even when nothing traded.
10. If nothing qualifies, say so plainly — cash is a position. Do not manufacture a trade.

**Scheduling note:** in-session scheduled check-ins die if the cloud container idles out. When
one is set, always tell the user the fallback: "if you don't hear from me by <time>, send
/trade". At session start, check `CronList` and re-arm any standing check-in that was lost.

$ARGUMENTS
