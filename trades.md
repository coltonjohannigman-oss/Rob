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

### 4. MRNA $65P Jul 17 — EP-Down / breakdown — CLOSED 2026-07-13 ✅ +$29 (+18.7%)
- **Entry:** $1.55 x1, 2026-07-10 (order 6a511da4) | **Exit:** $1.84, stop-limit $1.95/$1.80 fired (order 6a54ea36)
- **Right:** Ratcheted stop ($1.25 → $1.95) did its job and banked the move automatically.
- **Wrong:** Exited via stop rather than a planned target — +18.7% is below the 30-80% band. The stop was doing take-profit duty, which means the profit plan was never really set.

### 5. WULF $18P Jul 31 — EP-Down / breakdown — CLOSED 2026-07-16 ✅ +$47 (+42.7%)
- **Entry:** $1.10 x1, 2026-07-14 (order 6a569290 — owner-placed after the agent's $1.05 limit missed) | **Exit:** $1.57 (order 6a591131)
- **Right:** Textbook. Entry near the money, exit at +42.7% — dead center of the 30-80% band. Best-executed trade of the untracked run.
- **Wrong:** Agent's $1.05 limit was a penny-pinch that missed; owner had to step in to get filled. Lesson: on a thesis you believe, pay the mid.

### 6. SLB $53C Aug 21 — Momentum — CLOSED 2026-07-24 ✅ +$24 (+20.0%)
- **Entry:** $1.20 x1, 2026-07-24 (order 6a636dda) | **Exit:** $1.44 same day, ~2h later (order 6a638ca9)
- **Right:** Quick, clean, positive.
- **Wrong:** +20% is below the 30-80% band — sold early on a swing thesis with no day-trade justification. Left the setup before it could work.

### 7. GDX $85C Aug 21 — Momentum / sector trend — CLOSED 2026-08-07 ✅ +$325 (+130.0%)
- **Entry:** $2.50 x1, 2026-08-05 (order 6a736b32) | **Exit:** $5.75, 2026-08-07 (order 6a75df48)
- **Thesis:** Gold miners breaking out with gold heading toward $4,400+.
- **Right:** THE trade of the account — +130% in two sessions, and it alone carries the entire realized P&L. Riding past 80% was correct here: gold-miner leadership, volume, and a clean trend all held, which is exactly what the LETTING A WINNER RUN checklist is for.
- **Wrong:** Nothing on execution. Worth noting the $1.75 stop was cancelled to free the contract for the limit sell — the usual one-order-per-contract dance.

### 8. OCUL $11C Sep 18 — Biotech breakout — CLOSED 2026-08-18 ❌ -$100 (-62.5%)
- **Entry:** $0.80 x2, 2026-08-17 (order 6a83210d) | **Exit:** $0.30 x2, stop-market $0.60 fired @ $0.30 (order 6a832155)
- **Wrong:** The worst trade in the book, and on two counts. First, a $0.60 stop on a $0.80 entry is a 25% stop — correct in intent — but the stop-market filled at $0.30, HALF the trigger. That is the wide-spread slippage the PERSONA warns about, and on a low-priced contract it turned a -25% rule into a -62.5% reality. Second, this was sized x2 alongside NXE the same day.
- **Rule note:** On contracts under ~$1.00 with wide spreads, a stop-market is not a 25% stop — it is an unbounded one. Use a stop-LIMIT or accept a smaller size.

### 9. NXE $12C Sep 18 — Uranium momentum — CLOSED 2026-08-17 ❌ -$30 (-30.0%)
- **Entry:** $0.50 x2, 2026-08-17 (order 6a8322f1) | **Exit:** $0.35 x2, stop-market $0.40 fired @ $0.35 (order 6a8326c3), SAME DAY
- **Wrong:** Stopped out hours after entry — the entry was into noise, not a confirmed breakout. Two same-day entries (this + OCUL) on 8/17 both stopped within 24h; that is a sizing-and-patience failure, not bad luck.
- **Right:** The stop was honored immediately and the loss stayed at -30%.

### 10. AMLX $40C Sep 18 — Biotech catalyst — CLOSED 2026-08-20 ✅ +$60 (+30.8%)
- **Entry:** $1.95 x1, 2026-08-19 (order 6a85b7b1) | **Exit:** $2.55 next day (order 6a87055e)
- **Right:** +30.8% is just inside the profit band; took it and left. The $1.40 stop was cancelled to free the contract for the take-profit — correct sequencing.

### 11. XPEV $11P Sep 18 — EP-Down / breakdown — CLOSED 2026-08-25 ❌ -$20 (-20.4%)
- **Entry:** $0.49 x2, 2026-08-24 (order 6a8c8b4c; initial $0.47 limit cancelled and re-priced once) | **Exit:** $0.39 x2 (order 6a8da717)
- **Right:** Cut at -20.4%, inside the hard-stop band, and cancelled the $0.36 stop to exit on a limit rather than eat stop slippage — the OCUL lesson applied correctly one week later.
- **Wrong:** Thesis didn't develop; exited within a day. Puts on a name that wasn't actually breaking down.

---

## Untracked-run post-mortem (2026-07-10 → 2026-08-25)

Eleven closed trades all-time, +$425 realized, which ties exactly to the broker. But the honest read:
- **8 of 11 winners, yet ONE trade (GDX, +$325) is 76% of all profit.** Strip GDX out and the other ten trades net +$100 combined. The edge is thin and concentrated.
- **Two winners were sold below the 30-80% band** (MRNA +18.7%, SLB +20%, GRND +33% was fine) — the band is being under-shot on the upside and respected on the downside, which caps compounding.
- **Stop-market slippage on sub-$1 contracts is the single biggest mechanical leak** (OCUL: -62.5% on a -25% stop).
- **Bookkeeping failed completely for ~7 weeks.** Eleven trades executed, zero recorded, nothing committed. Backfilled 2026-09-03.

## Open positions

(none — 100% cash, $773.65 buying power as of 2026-09-03 10:28 AM CT)
