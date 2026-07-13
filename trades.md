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

### 4. MRNA $65P Jul 17 — Parabolic exhaustion / EP-down — CLOSED 2026-07-13 ✅ +$28.74 (+18.5%)
- **Entry:** $1.55 x1, 2026-07-10 (order 6a511da4). Session died before bookkeeping; backfilled 7/13.
- **Exit:** $1.84 — ratcheted stop-limit $1.95/$1.80 fired 8:43 AM CT 7/13 (order 6a54ea36),
  five minutes after placement, on the first bounce off the $65.70 morning low.
- **Thesis:** Parabola $46→$85.60 (+85%/3wk) cracked 7/7-7/8; entered the 7/10 breakdown
  (-11% on 2x vol). Peaked +45.5% ($2.255 mark) at 8:35 AM CT 7/13.
- **Right:** The setup itself (A-grade EP-down); the stop ratchet reflex — MRNA V-bounced to
  $69+ within the hour and the 65P would have bled toward worthless. +18.5% beat every price
  available after 8:43. The never-round-trip rule worked exactly as written.
- **Wrong:** At the +45% decision point the persona said bank it (puts bias 30-50%, exhaustion
  = day-trade rules); ride-with-stop was chosen instead and cost ~$41 vs the $2.25 mid exit.
  Also: on a 27%-wide spread, a stop trigger at the bid ($1.95 vs $2.255 mark) is effectively
  a market order on the first flicker — either accept that or bank at the mid; there is no
  free "let it ride" on wide-spread contracts.
- **Rule note:** "take profits FASTER on puts" validated — violent bear-market bounces are the
  persona's stated reason, and this one arrived in minutes.

## Open positions

(none — 100% cash)
