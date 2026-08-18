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

### 4. MRNA $65P Jul 17 — EP-down / breakdown (PUT) — CLOSED 2026-07-13 ✅ +$29 (+18.7%)
- **Entry:** $1.55 x1, 2026-07-10 (order 6a511da4)
- **Exit:** $1.84 — stop-limit ratcheted to trigger $1.95 / limit $1.80, filled $1.84 (order 6a54ea36)
- **Right:** The ratchet did its job — a stop that had been raised into profit converted the move
  into a locked gain instead of a round-trip. Put taken on the 30-50% bias per the put rules.
- **Wrong:** Exited at +18.7%, below the 30% band floor. The ratchet was set tight enough that it
  fired on noise rather than on a thesis break. Tight is right on puts, but a stop set inside the
  profit band pre-empts the band.

### 5. WULF $18P Jul 31 — EP-down / breakdown (PUT) — CLOSED 2026-07-16 ✅ +$47 (+42.7%)
- **Entry:** $1.10 x1, 2026-07-14 (order 6a569290 — **owner-placed in-app**, after the agent's
  $1.05 limit at 6a5682a9 never filled and was cancelled)
- **Exit:** $1.57 limit (order 6a591131), 2026-07-16
- **Right:** +42.7% is a clean hit inside the 30-80% band, and on the 30-50% end the put rules ask
  for. Two-day hold, no drama.
- **Wrong:** Nothing on the exit. Worth noting the entry only happened because the owner paid up
  $0.05 over the agent's limit — the "never overpay" rule cost the agent this entry, and the owner
  had to take it manually. A $0.05 miss on a $1.10 contract is inside the noise; the re-price-once
  rule should have been used here.

### 6. SLB $53C Aug 21 — Momentum/trend — CLOSED 2026-07-24 ✅ +$24 (+20.0%)
- **Entry:** $1.20 x1, 2026-07-24 (order 6a636dda)
- **Exit:** $1.44 limit (order 6a638ca9) — same day, ~2 hours later. The $0.85 stop (6a6374d2) was
  cancelled to free the contract for the take-profit.
- **Right:** Fast, clean, positive. Liquid large-cap underlying, tight spread — no liquidity
  exception needed.
- **Wrong:** +20% is below the 30-80% band. Sold the first pop on a large-cap trend name rather
  than letting it reach the band. This is the second exit in three trades that landed under the
  band floor — a pattern, not a one-off.

### 7. GDX $85C Aug 21 — Momentum/trend (gold miners) — CLOSED 2026-08-07 ✅ +$325 (+130.0%)
- **Entry:** $2.50 x1, 2026-08-05 (order 6a736b32)
- **Exit:** $5.75 limit (order 6a75df48), 2026-08-07. Stop $1.75 (6a736b57) cancelled to free the
  contract for the sale.
- **Right:** Best trade in the book by a wide margin — and the only one that ran past 80%. Sector
  leadership (gold miners trending), liquid ETF underlying, tight spreads, two-day hold. The
  decision to let it run instead of banking 50% was worth +$200 over the band exit.
- **Wrong:** Honestly — the run past 80% was never explicitly graded against the LETTING A WINNER
  RUN checklist in a session note, so it worked without being formally justified. Right outcome,
  undocumented process. If it had reversed there would have been no rule to point at.

### 8. NXE $12C Sep 18 x2 — Momentum breakout attempt — CLOSED 2026-08-17 ❌ -$30 (-30.0%)
- **Entry:** $0.50 x2 = $100, 2026-08-17 10:09:47 AM CT (order 6a8322f1)
- **Exit:** $0.35 x2 = $70 — stop-market $0.40 fired 1:28 PM CT the **same day** (order 6a8326c3)
- **What actually happened (intraday tape):** NXE sat dead flat at $10.28-10.38 on ~15-35k per
  10min until 9:20 AM CT, when it exploded — 940k shares in ten minutes — and ran $10.365 → $11.258
  by 9:50 AM CT (+8.6% in 30 minutes on ~2.5M shares). The $12 call went **$0.20 → $0.55 (+175%)**
  over those same 30 minutes. **The fill came at $0.50 at 10:09 AM — 20 minutes after the contract
  set its high of day at $0.55, i.e. within 9% of the top of a vertical move.**
  It never traded above $0.50 again. Faded all afternoon to $0.38.
- **Wrong — this is a pure entry error.** Bought the top of a parabolic 30-minute spike. The
  PERSONA already says "tight bases before breakouts are better than extended ones" and the
  parabolic rules say never buy into the vertical move itself. A 30-minute, +175% option move IS
  the vertical move. There was no base, no consolidation, no pullback — just a chase.
- **Right — the stop was correct and is vindicated.** Fired at -30%, the top of the allowed band,
  with only $0.05 of slippage on the $0.40 trigger (a normal half-spread). The contract marks
  **$0.275 today — the stop beat holding by $15.** Do not "fix" this stop.
- **Grade: F on entry, A on exit.**

### 9. OCUL $11C Sep 18 x2 — Episodic pivot attempt — CLOSED 2026-08-18 ❌ -$100 (-62.5%)
- **Entry:** $0.80 x2 = $160, 2026-08-17 9:56 AM CT (order 6a83210d)
- **Exit:** $0.30 x2 = $60 — stop-market $0.60 fired 8:31:26 AM CT next morning, **96 seconds after
  the opening bell** (order 6a832155)
- **The entry was NOT a spike chase** (an earlier version of this post-mortem said it was; the
  intraday tape says otherwise). OCUL gapped to $10.81, ran to $11.16 by 8:50 AM CT, then faded for
  an hour. The fill at 9:56 AM came with the stock at ~$10.62 — near the session low at that
  moment, an hour into a downtrend of lower highs. The real entry error is subtler and worse:
  **bought an OTM ($11) strike while the underlying was below it and making lower highs.** Volume
  confirmation existed for the 8:30 AM move, not for the 9:56 AM entry. The post-entry peak was
  $1.03 (+28.75%) — it never even reached the 30% profit band.
- **The stop is what destroyed this trade, and the numbers are unambiguous.** Minute bars for
  8/18, the minute the stop fired:
  | Time (CT) | Contract |
  |---|---|
  | 8:30 | $0.68 |
  | **8:31** | open 0.68, high 0.68, **low 0.55**, close 0.58 ← **filled here at $0.30** |
  | 8:32-8:34 | $0.60 |
  | 8:41-8:43 | $0.68 |
  | 8:44 | $0.73 / $0.70 |
  **The fill was $0.30 when the lowest price the contract traded that minute was $0.55, and it was
  back at $0.70 thirteen minutes later.** 45% below the minute's own low.
- **It was NOT illiquidity and NOT IV crush.** This contract has **open interest of 14,744** and a
  current spread of $0.60/$0.70 (15% of mark) — it comfortably passes every liquidity gate in the
  PERSONA. And the option only drifted $0.80 → $0.73 (close) → $0.68 (open) overnight: about -15%,
  ordinary theta plus a 1.6% down move in the stock. IV today is 69%, not a crush artifact.
- **The single cause: a GTC stop-market order was live during the opening auction.** Robinhood
  triggers option stops off the bid/mark, not the last trade. In the first 90 seconds the book is
  thin and the spread is at its widest, the bid momentarily printed at-or-below $0.60, the stop
  converted to a market order, and it swept whatever was resting — $0.30.
- **Counterfactuals, entry $160:**
  | Exit | Value | P&L |
  |---|---|---|
  | Actual stop-market fill $0.30 | $60 | **-$100 (-62.5%)** |
  | Fair value at trigger ($0.58) | $116 | -$44 (-27.5%) |
  | Mark now ($0.65) | $130 | -$30 (-18.8%) |
  **~$56 of the $100 loss was pure execution damage — not thesis, not IV, not the stock.** The
  intended -25% stop delivered -62.5%.
- **Grade: C- on entry, F on exit mechanics.**

### Bookkeeping note — 2026-08-18
Trades 4-9 were **backfilled in this session**. They were executed live between 2026-07-10 and
2026-08-18 but never recorded: the ledger and this journal both stopped at the GRND close on
2026-07-07, and nothing was committed for six weeks. The reconstruction came from broker order
history and ties to broker cash within $0.93. The process failure is itself the lesson — the
BOOKKEEPING rule ("record it immediately, commit and push so state survives the session") was not
followed, and six weeks of trade history had to be rebuilt from the broker instead of read from
the repo.

## Open positions

(none — 100% cash as of 2026-08-18 8:40 AM CT)
