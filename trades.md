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

### 4. SLB $53C Aug 21 — Episodic pivot (earnings) — CLOSED 2026-07-24 ✅ +$24 (+20%)
- **Entry:** $1.20 x1, 2026-07-24 8:56 AM CT (order 6a636dda)
- **Exit:** $1.44 — take-profit at 11:02 AM CT (order 6a638ca9), ~2 hours held
- **Thesis:** Q2 beat ($0.55 vs $0.52) gapped SLB +8-9% out of a month-long $45-48 base, reclaiming
  the 10/20-day EMAs. Graded B: modest catalyst, downtrend-reversal (not new highs), running into
  50-day SMA resistance at $51.5.
- **Right:** Pricing discipline paid — held a $1.20 limit through a +9% opening run instead of chasing
  to mid, and a pullback filled us at the limit. Read the stall correctly: SLB flattened under $52/50d
  exactly as flagged, so banked +20% rather than hoping for the 30-50% band. Tight spread at exit let
  the sell fill instantly near mid.
- **Wrong:** Took profit at +20%, just shy of the 30% band floor — a hair early by the letter of the
  rule, though justified by B-grade + resistance + selling into the bid. Bigger question: was a B-grade
  worth entering at all? It was the only liquid, real setup on the board (RNG's chart was better but its
  options were dead; THC priced out) and the owner wanted deployment. Net: a clean, fast, disciplined
  scalp on a mediocre setup — exactly what a B should be.
- **Rule note:** RNG (A-grade EP, +27% to new highs) was untradeable on option liquidity — OI 0-232,
  spreads 33-58%. Good chart ≠ tradeable trade. Same lesson as the size-out on THC.

## Open positions

(none — 100% cash)
