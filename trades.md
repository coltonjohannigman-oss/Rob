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

## Open positions

### GDX $85C Aug 21 — Momentum/EP breakout (gold miners) — OPEN
- **Entry:** $2.50 x1, 2026-08-05 ~11:56 AM CT (order 6a736b32, filled below the $2.52 limit).
- **Cost basis:** $250. **Stop:** working stop-market $1.75 GTC (order 6a736b57 — 30% hard stop, loose end of the band; assume ~$0.10 slippage on a stop-market → ~$1.65 fill).
- **Thesis:** GDX broke out 8/5 — gapped $77.92 → open $82.20, closed $83.68 on 40.7M vol (~2x avg), clearing the July range. Holding above the breakout and well above the 10-day EMA (~$77.5). Thesis stop: a volume close back below ~$82 (breakout) / ~$78 (10-day EMA).
- **Status (8/6 ~8:40 AM CT):** GDX $83.20 (-0.6%), normal day-2 consolidation. Option mark $2.295 (bid 2.19/ask 2.40), delta 0.43, IV 44.7%, OI ~24.9k. P&L -$20.50 (-8.2%). Not in profit band — hold, no TP action.
- **Bookkeeping note:** this position was opened in the prior session but never logged; recorded to the ledger 8/6 (cli buy $250) with a +$99.50 reconciling credit to align ledger free cash to broker buying power ($589.36).
