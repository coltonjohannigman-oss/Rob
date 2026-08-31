# Robbin Trade Journal

One entry per closed trade, appended at close. Open positions tracked at the bottom.
Grade the setup honestly after the fact — this is how the system learns.

Format: **Ticker contract | setup type | entry → exit | P&L | what went right / wrong**

---

## Closed trades

### 1. IRDM $55C Jul 17 — Momentum/Trend — CLOSED 2026-06-29 ✅ +$45 (+52.9%)
- **Entry:** $0.85 (split bid/ask after $0.80 limit missed), 2026-06-29
- **Exit:** $1.30 take-profit (user-set), same day
- **Thesis:** Breakout through 52-week high $53.83 on volume; only liquid strike within budget.
- **Right:** Volume-confirmed breakout; TP at +53% inside the 30-80% band; fast clean win.
- **Wrong:** No automated stop while TP order occupied the single order slot (Robinhood limitation) — acceptable same-day, risky overnight.

### 2. SOFI $18.5C Jul 17 — Catalyst swing (NFP) — CLOSED 2026-07-02 ✅ +$10 (+13.5%)
- **Entry:** $0.74 x1, 2026-06-29 (order 6a427819)
- **Exit:** $0.84 — stop-market $0.85 fired 9:03 AM CT on a post-NFP whipsaw (order 6a456baf)
- **Thesis:** Fintech momentum into NFP Jul 2. NFP came in market-friendly (SPY new highs) but
  SOFI itself chopped: dipped through the stop at 9:03, bounced to $0.925 by 9:09, then rolled
  over to $0.735 by 9:35.
- **Right:** The ratcheted stop ($0.55 → $0.74 → $0.85) converted a +45% peak into a locked
  +13.5% exit that beat every later price. Discipline > prediction — the whipsaw exit was the
  best available outcome once the peak was missed.
- **Wrong:** The real error happened 2026-07-01: peaked +45% ($1.075) and the sell decision
  waited. The binary-event rule (lock half or exit when +30% within 24h of an event) now exists
  because of this trade. Also: autopilot cycles 2-3 read quotes only and missed that the stop
  had already fired — fixed by checking positions/order states every cycle.

### 3. GRND $15C Jul 17 — Episodic pivot base breakout — CLOSED 2026-07-06 ✅ +$35 (+33.3%)
- **Entry:** $1.05 x1, 2026-07-01 (order 6a45274e; original $0.95 limit missed, re-priced once to mid)
- **Exit:** $1.40 — owner sold in-app at 1:02 PM CT (order 6a4bbd46), after cancelling the
  agent's $1.50 TP to free the contract (two of the owner's sell attempts failed first against
  the one-order-per-contract lock).
- **Thesis:** 2-week base $13–15 breakout on 1.7–1.9x volume, 25.5M low float. Held 3 sessions;
  stock never closed below $15.
- **Right:** Volume-confirmed entry worked; +33% lands inside the 30–80% band; the owner's $1.40
  exit filled while the agent's $1.50 never did — a bird in hand.
- **Wrong:** Nothing major. Entry used the liquidity exception (20% spread, 0.69 delta) and paid
  for it in mark-to-market noise all week. The stop→TP swap left 5 hours of unprotected drift
  (accepted tradeoff, owner's call).
- **Rule note:** exception rubric documented in PERSONA 2026-07-01 traces to this trade.

### 4. MRNA $65P Jul 17 — EP-down / breakdown put — CLOSED 2026-07-13 ✅ +$29 (+18.7%)
- **Entry:** $1.55 x1, 2026-07-10 (order 6a511da4) — **Exit:** $1.84, stop-limit $1.95/$1.80 (order 6a54ea36)
- **Right:** A ratcheted stop-limit did the work and banked the gain without a discretionary decision.
- **Wrong:** Exited via stop rather than a chosen target — fine, but it means the thesis was never really tested.

### 5. WULF $18P Jul 31 — put swing — CLOSED 2026-07-16 ✅ +$47 (+42.7%)
- **Entry:** $1.10 x1, 2026-07-14 — **placed by the owner in-app** (order 6a569290), not by Robbin
- **Exit:** $1.57, 2026-07-16 (order 6a591131, agentic)
- **Right:** +42.7% is squarely in the 30-80% band; taken in two days with no round-trip risk.
- **Note:** Owner-originated entry, agent-managed exit. The division of labour worked well here.

### 6. SLB $53C Aug 21 — intraday momentum — CLOSED 2026-07-24 ✅ +$24 (+20.0%)
- **Entry:** $1.20 x1, 8:56 AM CT — **Exit:** $1.44, 11:02 AM CT, same session (orders 6a636dda / 6a638ca9)
- **Right:** Quick, clean, no overnight theta.
- **Wrong:** +20% is *below* the 30-80% band — banked early. Defensible on a day trade, but this is the
  pattern to watch: taking 20% on winners while losers run to -62% is how an edge gets inverted.

### 7. GDX $85C Aug 21 — momentum/trend runner — CLOSED 2026-08-07 ✅ +$325 (+130.0%)
- **Entry:** $2.50 x1, 2026-08-05 (order 6a736b32) — **Exit:** $5.75, 2026-08-07 (order 6a75df48)
- **Thesis:** Gold miners in a powerful uptrend; gold spot running toward $4,500/oz.
- **Right:** The single best trade of the account's life, and the one time the LETTING A WINNER RUN
  exception was actually earned — real macro driver, sector leadership, trend intact. The stop
  (order 6a736b57) was cancelled at 8:33 AM CT and the sell filled three minutes later at 8:36:
  a deliberate stop→exit swap, not a lapse.
- **Wrong:** Nothing. +130% on a $250 basis paid for every loser in August combined.

### 8. OCUL $11C Sep 18 x2 — biotech breakout — CLOSED 2026-08-18 ❌ -$100 (-62.5%)
- **Entry:** $0.80 x2, 2026-08-17 (order 6a83210d) — **Exit:** $0.30 x2, 2026-08-18 (order 6a832155)
- **The stop was set at $0.60 (-25%, correct). It filled at $0.30 — a 50% slippage gap.**
- **Wrong:** This is the worst trade the account has taken, and the loss was NOT the thesis — it was
  execution. A stop-market on a $0.80 contract with a wide spread does not fill near the trigger; it
  fills wherever the book is when it triggers, and overnight it triggers on the open print. A -25%
  planned risk became -62.5% realized.
- **Rule note (new):** on any contract under ~$1.00 or with a spread wider than ~15%, a stop-market
  held overnight is not a stop — it is a market order at an unknown price. Either size so a total
  loss is acceptable, or manage the exit manually intraday. Do not pretend the stop is protection.

### 9. NXE $12C Sep 18 x2 — uranium breakout — CLOSED 2026-08-17 ❌ -$30 (-30.0%)
- **Entry:** $0.50 x2, 9:09 AM CT — **Exit:** $0.35 x2, stop-market $0.40 fired 1:28 PM CT, same day
- **Right:** Stop fired the same session and capped the loss near plan (-30% vs -25% intended, $0.05
  of slippage). Cut fast, no averaging down.
- **Wrong:** Entered NXE and OCUL within 13 minutes of each other — two speculative small-cap breakouts
  opened back to back, both of which failed within a day. That is one concentrated bet, not two trades.

### 10. AMLX $40C Sep 18 — biotech momentum — CLOSED 2026-08-20 ✅ +$60 (+30.8%)
- **Entry:** $1.95 x1, 2026-08-19 — **Exit:** $2.55 take-profit, 2026-08-20 (order 6a87055e)
- **Right:** Textbook. +30.8% is the bottom of the profit band, taken the next session. The stop
  (order 6a85b7d4, $1.40) was cancelled to free the contract for the TP — the one-order-per-contract
  dance handled correctly this time.

### 11. XPEV $11P Sep 18 x2 — EP-down put — CLOSED 2026-08-25 ❌ -$20 (-20.4%)
- **Entry:** $0.49 x2, 2026-08-24 (order 6a8c8b4c; initial $0.47 limit missed, re-priced once to $0.49)
- **Exit:** $0.39 x2, 2026-08-25 — stop $0.36 cancelled and closed manually at the limit instead
- **Right:** Cut at -20%, *inside* the -25/30% hard stop, without waiting for the stop to fire. Given
  the OCUL lesson one week earlier, closing manually on a cheap contract rather than trusting a
  stop-market was exactly the right adjustment. Small loss, correctly taken.

---

## Bookkeeping note — 2026-08-31

Trades 4-11 were executed but never recorded in `agents.json`; the ledger had been frozen at the
2026-07-07 state (11 trades of history, only 3 booked). Backfilled this session from broker order
records. Realized P&L now ties exactly to the broker: **+$425 all-time** (June +$45, July +$145,
August +$235), across 11 closed trades — 8 winners, 3 losers.

A separate **-$301.21** adjustment was posted to bring ledger cash to the broker's actual $773.65.
This is a funding overstatement that predates 2026-07-07: the ledger had credited $649.86 of
deposits and "reconciliation" entries, but the broker's cash implies only ~$348.65 of real net
deposits. It is not attributable to any trade — most likely the `alloc0003` (+$75.96) and
`rebal001` (+$73.90) reconciliation credits double-counted money already in the balance.
**Owner should confirm the actual deposit/withdrawal history.** Broker buying power is authoritative
and is what all sizing now uses.

## Open positions

(none — 100% cash as of 2026-08-31, $773.65 buying power)
