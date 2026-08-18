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

### 4. MRNA $65P Jul 17 — Bearish swing (long put) — CLOSED 2026-07-13 ✅ +$29 (+18.7%)
- **Entry:** $1.55 x1, 2026-07-10 (order 6a511da4) | **Exit:** stop-limit $1.95/$1.80 filled @ $1.84 (order 6a54ea36)
- **Right:** Ratcheted stop did its job — locked a gain instead of round-tripping.
- **Wrong:** Exited via stop, not a chosen target; +18.7% is below the 30-80% band. The stop was doing the deciding.

### 5. WULF $18P Jul 31 — Bearish swing (long put) — CLOSED 2026-07-16 ✅ +$47 (+42.7%)
- **Entry:** $1.10 x1, 2026-07-14 — **owner-placed** (order 6a569290, placed_agent=user) | **Exit:** $1.57 (order 6a591131)
- **Right:** +42.7% lands squarely in the 30-80% band. Clean two-day put trade.
- **Note:** Owner opened, agent closed. Worth flagging that mixed authorship happened without a ledger entry.

### 6. SLB $53C Aug 21 — Momentum — CLOSED 2026-07-24 ✅ +$24 (+20.0%)
- **Entry:** $1.20 x1, 2026-07-24 (order 6a636dda) | **Exit:** $1.44 same day, ~2h later (order 6a638ca9)
- **Right:** Quick, clean, no damage.
- **Wrong:** +20% is UNDER the 30-80% band — sold early on a swing thesis with no stop-out or thesis break. Took a scalp on a position sized as a swing.

### 7. GDX $85C Aug 21 — Momentum/Trend runner — CLOSED 2026-08-07 ✅ +$325 (+130.0%)
- **Entry:** $2.50 x1, 2026-08-05 (order 6a736b32) | **Exit:** $5.75, 2026-08-07 (order 6a75df48)
- **Thesis:** Gold-miner trend leg. Stop $1.75 (order 6a736b57) was cancelled 8/7 immediately before the sell.
- **Right:** Best trade in the book by a distance. Rode past the 80% band on a real trend — the LETTING A WINNER RUN exception used correctly.
- **Wrong:** Nothing on execution. But it was never written down, so the account's biggest win was invisible to the ledger for 11 days.

### 8. NXE $12C Sep 18 x2 — Momentum — CLOSED 2026-08-17 ❌ −$30 (−30.0%)
- **Entry:** $0.50 x2, 2026-08-17 (order 6a8322f1) | **Exit:** stop-market $0.40 filled @ $0.35 same day (order 6a8326c3)
- **Wrong:** Entered and stopped out inside three hours. A setup that dies same-day was not a setup — the entry was premature, not the stop too tight. Hard stop hit its −30% ceiling exactly.

### 9. OCUL $11C Sep 18 x2 — Momentum — CLOSED 2026-08-18 ❌ −$100 (−62.5%)
- **Entry:** $0.80 x2, 2026-08-17 (order 6a83210d) | **Exit:** stop-market $0.60 filled @ **$0.30**, 8:31 AM CT 8/18 (order 6a832155)
- **Wrong:** The worst trade in the book, and the damage was mechanical, not directional. Stop triggered at $0.60 and filled at **$0.30 — 50% slippage**, blowing straight through the −25/30% hard-stop ceiling to −62.5%.
- **RULE LESSON:** The persona assumes stop-market slippage ≈ half the spread. That is far too optimistic on a thin sub-$1 contract at the open. On low-OI contracts under ~$1, a stop-market is not a stop — it is a market order that fires at the worst moment. Use a stop-LIMIT, or size assuming the stop does not hold.

## Bookkeeping incident — 2026-08-18

Trades 4-9 were executed at the broker between 2026-07-10 and 2026-08-18 but **never recorded**. The
ledger sat at $739.86 / +$90 realized while the broker held $1,033.93. Backfilled this session from
broker order history; reconciled to $1,034.86 vs broker $1,033.93 (Δ $0.93 = regulatory fees).
Six round-trips, net +$295. The BOOKKEEPING rule exists to prevent exactly this — it was not followed
for five weeks, including on the account's largest winner (GDX, +$325) and largest loser (OCUL, −$100).

## Open positions

(none — 100% cash, $1,034.86 available)
