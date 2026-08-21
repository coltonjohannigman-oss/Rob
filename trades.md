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
- **Entry:** $1.55 x1, 2026-07-10 (order 6a511da4)
- **Exit:** $1.84 — stop-limit ($1.95 trigger / $1.80 limit) filled 2026-07-13 (order 6a54ea36)
- **Right:** The stop was ratcheted UP into profit ($1.25 → $1.95 trigger), converting an open put
  into a locked +18.7%. The ratchet-into-profit discipline worked exactly as designed.
- **Wrong:** Exited below the 30% band because the trailing stop caught a bounce first. Acceptable
  — put rules explicitly bias toward taking profit faster on bear trades.

### 5. WULF $18P Jul 31 — Breakdown put (owner-initiated entry) — CLOSED 2026-07-16 ✅ +$47 (+42.7%)
- **Entry:** $1.10 x1, 2026-07-14 — **placed by the owner in-app** (order 6a569290), after the
  agent's own $1.05 limit (6a5682a9) failed to fill and was cancelled.
- **Exit:** $1.57 limit, 2026-07-16 (order 6a591131)
- **Right:** +42.7% lands squarely in the 30-80% band and was taken, not held. Stop was ratcheted
  twice ($0.80 → $1.05/$0.95 stop-limit → $1.30) before the profit target got there first.
- **Wrong:** The agent's entry limit was too far below the mid and missed; the owner had to reach in
  and pay up $0.05 to get filled. Cost nothing here, but the re-price-once rule exists for this.

### 6. SLB $53C Aug 21 — Momentum breakout — CLOSED 2026-07-24 ✅ +$24 (+20.0%)
- **Entry:** $1.20 x1, 2026-07-24 (order 6a636dda)
- **Exit:** $1.44, same day ~2 hours later (order 6a638ca9); stop $0.85 cancelled to free the contract
- **Right:** Fast, clean, no drawdown. Took the money and moved on.
- **Wrong:** Closed at +20%, below the 30% band, on a swing-dated contract with 4 weeks left. This
  was an unforced early exit — no thesis break, no stop trigger, just impatience.
- **Grade: B.** Profitable but the exit was not rule-driven.

### 7. GDX $85C Aug 21 — Momentum / sector trend — CLOSED 2026-08-07 ✅ +$325 (+130.0%)
- **Entry:** $2.50 x1, 2026-08-05 (order 6a736b32)
- **Exit:** $5.75 limit, 2026-08-07 (order 6a75df48); stop $1.75 cancelled first to free the contract
- **Thesis:** Gold-miner ETF trending hard; liquid, tight-spread chain.
- **Right:** The single best trade in the account's history — +130% in two sessions, and it was
  actually TAKEN rather than held for more. Riding past the 80% band was justified here by a
  confirmed sector trend, and the exit still came fast.
- **Wrong:** Nothing on execution. Worth noting the position was unprotected between cancelling the
  stop and the limit filling — the one-order-per-contract lock again.
- **Grade: A.**

### 8. OCUL $11C Sep 18 x2 — Breakout attempt — CLOSED 2026-08-18 ❌ -$100 (-62.5%)
- **Entry:** $0.80 x2, 2026-08-17 (order 6a83210d)
- **Exit:** $0.30 x2 — stop-market $0.60 filled at $0.30, 2026-08-18 (order 6a832155)
- **Wrong — two separate rule failures:**
  1. **The stop-market gapped through.** Trigger was $0.60; fill was $0.30. That is a 50% slippage,
     not the "half the spread" the PERSONA assumes. On a sub-$1 biotech contract a stop-market is
     effectively unprotected — the loss doubled versus the intended -25%.
  2. **Sizing.** 2 contracts at $160 was fine on the 20% cap, but doubling up on an illiquid
     low-priced contract meant the slippage hit twice.
- **Lesson:** on contracts under ~$1.00 with thin books, a stop-market does not deliver the hard
  stop. Either size to survive a gap to near-zero, or accept the contract cannot be stop-protected.
- **Grade: D.**

### 9. NXE $12C Sep 18 x2 — Uranium breakout — CLOSED 2026-08-17 ❌ -$30 (-30.0%)
- **Entry:** $0.50 x2, 2026-08-17 (order 6a8322f1)
- **Exit:** $0.35 x2 — stop-market $0.40 filled at $0.35, same day (order 6a8326c3)
- **Right:** Stop fired at -30%, close to the intended hard-stop band, and the loss was cut same-day
  without hesitation. Slippage was only $0.05 here.
- **Wrong:** Entered and stopped out inside a single session — the entry was chasing intraday
  strength that had not actually confirmed. Two positions opened the same morning (OCUL + NXE),
  both breakouts, both failed: correlated risk taken on in one shot.
- **Grade: C.** The exit was disciplined; the entry was not.

### 10. AMLX $40C Sep 18 — Episodic pivot (Ph3 LUCIDITY data) — CLOSED 2026-08-20 ✅ +$60 (+30.8%)
- **Entry:** $1.95 x1, 2026-08-19 (order 6a85b7b1), stop $1.40 GTC set same session
- **Exit:** $2.55 limit, 2026-08-20 (order 6a87055e); stop cancelled first to free the contract
- **Thesis:** Phase 3 LUCIDITY readout 8/18 sent the stock +64% through $24.60 on 16.9x volume — a
  textbook episodic pivot with a genuine catalyst.
- **Right:** Real catalyst, real volume, stop set the same session as the fill, and the exit at
  +30.8% took the bottom of the profit band rather than round-tripping. Clean rule-following.
- **Wrong:** IV crush was the drag the whole way — the stock rose 7.6% on 8/19 while the option went
  nowhere. Buying premium into a post-binary-event IV spike costs you even when you are right on
  direction. This is the case the PERSONA's advisory playbook flags for a debit spread instead.
- **Grade: A-.**

## Open positions

(none — 100% cash as of 2026-08-21; broker cash $793.83)
