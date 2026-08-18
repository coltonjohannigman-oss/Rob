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
- **Entry:** $0.50 x2 = $100, 2026-08-17 9:04 AM CT (order 6a8322f1)
- **Exit:** $0.35 x2 = $70 — stop-market $0.40 fired 1:28 PM CT the **same day** (order 6a8326c3)
- **Thesis:** NXE gapped up and ran to $11.26 on 14.8M shares (~4x average).
- **Wrong:** Bought a spike, not a base. NXE opened $10.44, spiked to $11.258, and faded to close
  $10.75 — the entry was near the high of a gap-up day, ~35 minutes after the open. The $12 strike
  was never in the money at any point. Hard stop did its job at exactly -30%, the top of the
  allowed band.
- **Right:** The stop was in place and it fired without hesitation. Loss capped at the rule.

### 9. OCUL $11C Sep 18 x2 — Episodic pivot attempt — CLOSED 2026-08-18 ❌ -$100 (-62.5%)
- **Entry:** $0.80 x2 = $160, 2026-08-17 8:56 AM CT (order 6a83210d)
- **Exit:** $0.30 x2 = $60 — stop-market $0.60 fired 8:31 AM CT next morning, one minute after the
  open, filling at HALF the trigger (order 6a832155)
- **Thesis:** OCUL gapped to $10.80 and ran to $11.195 on 11.15M shares (~5.6x average).
- **Wrong — the worst trade in the book, and worth reading twice:**
  1. **Bought day-1 event IV.** Entry was 26 minutes into a 5.6x-volume event day. Overnight IV
     crush alone did most of the damage.
  2. **The stock never confirmed.** OCUL faded from $11.195 to close $10.65 — a reversal candle on
     huge volume — and the $11 strike closed OUT of the money. That was a thesis break on the
     entry day and should have triggered a discretionary exit, not a wait for the stop.
  3. **The stop was not the protection it looked like.** Stop-market $0.60 was set for a -25% loss.
     It filled at $0.30 for -62.5%. The stock was only -1.6% that morning — this was NOT a stock
     gap. The option collapsed on IV crush while OTM, and the stop-market then filled deep into the
     wide opening spread. **A stop-market on a sub-$1 wide-spread contract is not a -25% stop; it
     is an uncapped stop.**
  4. **Sizing.** 2 contracts / $160 was the largest position taken since GRND, on the least
     confirmed setup.
- **Right:** Nothing to defend on this one.
- **Rule notes generated:** (a) never open on day 1 of an event-volume gap — wait for the pullback
  entry the EP rule already prescribes; (b) an OTM strike closing out-of-the-money on entry day is
  a thesis stop; (c) prefer stop-LIMIT over stop-market on contracts under ~$1.50 or with spreads
  over ~20%, accepting the risk of no fill over the certainty of a terrible one.

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
