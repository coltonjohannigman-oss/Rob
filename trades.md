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

### 4. MRNA $65P Jul17 — EP-Down / breakdown put — CLOSED 2026-07-13 ✅ +$29 (+18.7%)
- **Entry:** $1.55 x1, 2026-07-10 (order 6a511da4). **Exit:** stop-limit $1.95/$1.80 filled @ $1.84, 2026-07-13 (order 6a54ea36).
- **Right:** Bearish thesis paid; the stop-LIMIT (not stop-market) avoided the slippage that later gutted OCUL.
- **Wrong:** Exited below the 30% band on a mechanical stop rather than a target. Small win, but the put never got room.

### 5. WULF $18P Jul31 — Breakdown put — CLOSED 2026-07-16 ✅ +$47 (+42.7%)
- **Entry:** $1.10 x1, 2026-07-14 — **placed by the OWNER in-app** (order 6a569290), not by Robbin.
- **Exit:** $1.57 limit, 2026-07-16 (order 6a591131). Clean exit inside the 30-80% band.
- **Note:** Owner-originated entry, agent-managed exit. The division of labor worked.

### 6. SLB $53C Aug21 — Momentum breakout — CLOSED 2026-07-24 ✅ +$24 (+20.0%)
- **Entry:** $1.20 x1, 2026-07-24 (order 6a636dda). **Exit:** $1.44, same day (order 6a638ca9).
- **Wrong:** Exited at +20%, below the 30-80% band, on a day trade that was never framed as one.
  The oil/Iran catalyst was flagged fragile in the watchlist — taking the quick win was defensible,
  but the trade had no pre-declared plan, and that is the actual error.

### 7. GDX $85C Aug21 — Momentum / trend — CLOSED 2026-08-07 ✅ +$325 (+130.0%)
- **Entry:** $2.50 x1, 2026-08-05 (order 6a736b32). **Exit:** $5.75, 2026-08-07 (order 6a75df48).
- **Right:** The best trade in the account's history. Gold-miner trend was the strongest theme on the
  board and the position was allowed to run past the 80% band — the LETTING A WINNER RUN checklist
  earning its place. The $1.75 stop was cancelled and replaced by a live exit at the top.
- **Lesson:** This single trade (+$325) exceeds the sum of every other closed trade. Position size,
  not hit rate, produced it.

### 8. OCUL $11C Sep18 — Breakout attempt — CLOSED 2026-08-18 ❌ -$100 (-62.5%)
- **Entry:** $0.80 x2, 2026-08-17 (order 6a83210d). **Exit:** stop-MARKET $0.60 filled @ **$0.30**, 2026-08-18 (order 6a832155).
- **Wrong:** THE WORST TRADE ON RECORD, and the loss was mechanical, not directional. A $0.60 stop on a
  $0.80 entry is a -25% stop — inside the rules. It filled at $0.30, a **-62.5% realized loss**: the
  stop-market gapped through the trigger on a wide-spread, low-priced contract. The persona already
  warns "stop-market on a wide-spread contract fills below the trigger" and "stops do NOT protect
  through gaps." Both warnings fired at once and the loss was 2.5x the intended risk.
- **Rule note:** On sub-$1.00 contracts a stop-market is not risk control, it is a market order with a
  delay. Use stop-LIMIT (as MRNA did) or accept that the real risk is the whole premium.

### 9. NXE $12C Sep18 — Breakout attempt — CLOSED 2026-08-17 ❌ -$30 (-30.0%)
- **Entry:** $0.50 x2, 2026-08-17 (order 6a8322f1). **Exit:** stop-market $0.40 filled @ $0.35, same day (order 6a8326c3).
- **Wrong:** Opened same-day alongside OCUL — two speculative sub-$1 breakout calls at once. Both
  failed within 24 hours. Stopped out in three hours; the setup was never confirmed by volume.

### 10. AMLX $40C Sep18 — Episodic pivot — CLOSED 2026-08-20 ✅ +$60 (+30.8%)
- **Entry:** $1.95 x1, 2026-08-19 (order 6a85b7b1). **Exit:** $2.55, 2026-08-20 (order 6a87055e).
- **Right:** Textbook execution. Entered, stop set at $1.40, then the stop was cancelled and the
  position sold into strength at +30.8% — the low end of the band, taken cleanly. No agonizing.

### 11. XPEV $11P Sep18 — Breakdown put — CLOSED 2026-08-25 ❌ -$20 (-20.4%)
- **Entry:** $0.49 x2, 2026-08-24 (order 6a8c8b4c). **Exit:** $0.39 limit, 2026-08-25 (order 6a8da717).
- **Right:** Cut at -20% by a discretionary limit exit BEFORE the $0.36 stop-market could fill worse —
  exactly the lesson OCUL taught, applied one week later. Small, controlled loss.

---

## Bookkeeping incident — 2026-09-02

Trades 4 through 11 were executed between 2026-07-10 and 2026-08-25 but were **never recorded** in
`agents.json` or this journal. They were reconstructed on 2026-09-02 from the broker's own order
history and verified against `get_realized_pnl`: reconstructed total **+$425** ties exactly to the
broker's reported all-time realized P&L of **+$425** (June +$55, July +$135, August +$235).

The ledger had been carrying `realized_pnl: $90` and a balance of `$739.86` — stale since 2026-07-07.
After the backfill the ledger read $1,074.86 against live broker cash of **$773.65**, leaving a
**$301.21 residual that trading activity does not explain** (every fill is now accounted for). It was
booked as a reconciling debit to anchor the ledger to the broker. Most likely an owner withdrawal or
an overstated funding credit in the original ledger — **flagged for owner review, unresolved.**

**Process fix:** the persona's BOOKKEEPING rule ("record it in the ledger immediately") was not
followed for eight consecutive trades. Every session must now reconcile ledger realized P&L against
`get_realized_pnl` before trading, not just cash against buying power.

## Open positions

(none — 100% cash, $773.65 buying power)
