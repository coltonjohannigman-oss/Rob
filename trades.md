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

### 4. MRNA $65P Jul 17 — Bearish swing (put) — CLOSED 2026-07-13 ✅ +$29 (+18.7%)
- **Entry:** $1.55 x1, 2026-07-10 (order 6a511da4)
- **Exit:** $1.84 — stop-limit $1.95/$1.80 fired 2026-07-13 (order 6a54ea36)
- **Right:** A ratcheted stop ($1.25 → $1.95) converted an open put gain into a booked one. MRNA
  fell $76.56 → $67.01 over the window; the trailing stop banked it instead of round-tripping.
- **Wrong:** Nothing structural. Exit was mechanical, which is the point.
- *(Reconstructed from broker order history — this trade was never written to the ledger live.)*

### 5. WULF $18P Jul 31 — Bearish swing (put) — CLOSED 2026-07-16 ✅ +$47 (+42.7%)
- **Entry:** $1.10 x1, 2026-07-14 (order 6a569290, placed_agent=**user** — owner's entry)
- **Exit:** $1.57 limit, 2026-07-16 (order 6a591131)
- **Right:** +42.7% lands squarely in the 30-80% band and the put was taken FAST, exactly as the
  PUT-SPECIFIC rule demands ("bias toward the 30-50% end; bear moves get ripped back").
- **Wrong:** Nothing. Two-day hold, clean exit. The stop was cancelled to free the contract for
  the sell (one-order-per-contract lock) — the correct sequencing.
- *(Reconstructed from broker order history.)*

### 6. SLB $53C Aug 21 — Day trade — CLOSED 2026-07-24 ✅ +$24 (+20.0%)
- **Entry:** $1.20 x1, 2026-07-24 (order 6a636dda)
- **Exit:** $1.44, same day ~11:02 AM CT (order 6a638ca9)
- **Right:** Same-session in-and-out at +20%; no overnight theta on a 4-week contract.
- **Wrong:** +20% is below the 30-80% band. Defensible on a day trade, but the stop at $0.85 was
  cancelled ~90 seconds before the sell — a brief unprotected window that keeps recurring.
- *(Reconstructed from broker order history.)*

### 7. GDX $85C Aug 21 — Momentum/Trend — CLOSED 2026-08-07 ✅ +$325 (+130.0%)
- **Entry:** $2.50 x1, 2026-08-05 (order 6a736b32)
- **Exit:** $5.75 limit, 2026-08-07 (order 6a75df48)
- **Thesis:** Gold-miner ETF momentum. Two-day hold, more than doubled.
- **Right:** The single best trade in the book. Letting this one run past the 80% band was correct
  — GDX was a confirmed trend with sector leadership, which is exactly the LETTING A WINNER RUN
  exception rather than a violation of the band.
- **Wrong:** The $1.75 stop was cancelled ~2.5 min before the exit; the position rode unprotected
  briefly. Also, at $250 entry this was ~24% of budget — above the 20% conservative cap.
- *(Reconstructed from broker order history.)*

### 8. NXE $12C Sep 18 x2 — CLOSED 2026-08-17 ❌ -$30 (-30.0%)
- **Entry:** $0.50 x2 ($100), 2026-08-17 (order 6a8322f1)
- **Exit:** stop-market $0.40 fired @ $0.35, SAME DAY (order 6a8326c3)
- **Right:** The stop existed and it worked. -30% is the hard-stop band, not a catastrophe.
- **Wrong:** Entered and stopped out within ~3.5 hours — the entry was not a real setup, or the
  stop was far too tight for the contract's spread. A stop placed 20% below entry on a sub-$1
  option is inside the noise band; it was always going to fire on a wiggle.
- *(Reconstructed from broker order history.)*

### 9. OCUL $11C Sep 18 x2 — CLOSED 2026-08-18 ❌ -$100 (-62.5%)
- **Entry:** $0.80 x2 ($160), 2026-08-17 (order 6a83210d)
- **Exit:** stop-market $0.60 fired @ **$0.30** on 2026-08-18 (order 6a832155)
- **Wrong — the expensive lesson:** the stop TRIGGER was $0.60 (a planned -25%) but the FILL was
  $0.30 — a **50% slippage gap**, turning a -25% stop into a -62.5% loss. The stock gapped down
  overnight and the stop-market filled into the post-gap book, exactly as the PERSONA's broker-
  mechanics note warns ("stops do NOT protect through gaps; stop-market on a wide-spread contract
  fills below the trigger"). Two contracts doubled the damage.
- **Rule note:** this is the worst trade in the book and the only one where the loss materially
  exceeded the planned stop. On sub-$1 contracts held overnight, a stop-market is close to
  worthless as protection — size is the only real risk control.
- *(Reconstructed from broker order history.)*

## Open positions

### AMLX $40C Sep 18 2026 x1 — Episodic Pivot (day 2) — OPENED 2026-08-19
- **Entry:** $1.95 x1 = $195 (order 6a85b7b1, filled 9:03:29 AM CT)
- **Stop:** stop-market $1.40 GTC (order 6a85b7d4, state=confirmed) — approx -28% of entry.
  This working order HOLDS THE CONTRACT and blocks manual sells until cancelled.
- **Thesis:** Phase 3 LUCIDITY hit 8/18 — avexitide in post-bariatric hypoglycemia met the
  FDA-agreed primary endpoint (55% reduction in Level 2/3 hypoglycemic events) and ALL
  secondaries. NDA planned by end of 2026. Gap 8/18 from a tight 6-session base ($21.28-$23.73)
  through the prior $24.60 swing high on ~16x average volume, closing at the top of the range.
  Day 2 held and extended above the gap-day high.
- **Sizing:** $195 = 18.9% of the $1,033.93 budget — under the 20% conservative cap.
  Delta 0.42, OI 5,712, spread 10% at entry. No liquidity exception needed.
- **Profit plan:** 30-80% band = $2.54 (+$59) to $3.51 (+$156). Single contract, so ONE exit
  in the band — no scaling out. Trailing past 80% only if the LETTING A WINNER RUN checklist
  passes on all four legs.
- **Known risks:** entry was day-2 extension, not the breakout candle or a 10-day EMA pullback
  (the EMA sits near $25, weeks away) — the weakest valid form of the EP entry. Stop-market on
  a wide-spread contract will slip; assume roughly half the spread. Stops do NOT protect
  through an overnight gap (see the OCUL post-mortem above).
