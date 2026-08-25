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

---

## Backfilled 2026-08-24 — trades 4-10

These seven round-trips were executed 2026-07-10 → 2026-08-20 but never recorded in
`agents.json` or journaled here. Reconstructed on 2026-08-24 from broker order records
(entry/exit prices and dates are exact); the *theses* are inferred from the chart and the
order pattern, not from contemporaneous notes — treat the grades as best-effort, not gospel.
Reconstruction cross-checks against the broker's own realized-P&L buckets ($190 + $255 = $445).

### 4. MRNA $65P Jul 17 — EP-down / breakdown — CLOSED 2026-07-13 ✅ +$29 (+18.7%)
- **Entry:** $1.55 x1, 2026-07-10 (order 6a511da4) — **Exit:** $1.84, stop-limit $1.95/$1.80 (order 6a54ea36)
- **Right:** Puts worked; the stop was ratcheted up into profit and did its job on the reversal.
- **Wrong:** Exited at +18.7%, below the 30-80% band — the ratchet was set tight enough that a
  normal pullback took it. Protection that fires before the band is protection set too close.

### 5. WULF $18P Jul 31 — EP-down / breakdown — CLOSED 2026-07-16 ✅ +$47 (+42.7%)
- **Entry:** $1.10 x1, 2026-07-14 (order 6a569290, **placed by owner in-app**) — **Exit:** $1.57 (order 6a591131)
- **Right:** Textbook. +42.7% is dead-center in the 30-80% band, held two sessions, clean exit.
  Three stop orders were cancelled/re-placed as it worked — the ratchet was managed properly here.

### 6. SLB $53C Aug 21 — momentum — CLOSED 2026-07-24 ✅ +$24 (+20.0%)
- **Entry:** $1.20 x1, 2026-07-24 — **Exit:** $1.44 the same day (order 6a638ca9)
- **Wrong:** Opened and closed inside one session at +20%, under the band, on a *swing* structure
  (4-week expiry). Either it was a day trade that should have used a short-dated contract, or a
  swing that got sold on the first green candle. The stop (6a6374d2) was cancelled ~1h41m before
  the sale, so this was a discretionary exit, not a stop-out.

### 7. GDX $85C Aug 21 — momentum / trend — CLOSED 2026-08-07 ✅ +$325 (+130.0%)
- **Entry:** $2.50 x1, 2026-08-05 — **Exit:** $5.75, 2026-08-07 (order 6a75df48)
- **Right:** The account's best trade to date. Gold-miner trend, held two sessions, +130%.
- **Honest note:** +130% is *well* past the 80% band. That is only legitimate if the LETTING A
  WINNER RUN checklist was consciously cleared at the time. No note survives saying it was, so
  this has to be logged as a band override that happened to pay — outcome, not necessarily process.
  A repeat of this sizing/exit behavior on a weaker chart is how the account gives it all back.

### 8. OCUL $11C Sep 18 x2 — CLOSED 2026-08-18 ❌ −$100 (−62.5%)
- **Entry:** $0.80 x2, 2026-08-17 — **Exit:** $0.30 x2, stop-market $0.60 (order 6a832155)
- **Wrong — the most expensive lesson in the log.** The stop was set correctly at $0.60 (−25%,
  inside the hard-stop rule). It filled at **$0.30 — a −62.5% loss, 37 points worse than intended.**
  A stop-*market* order on an 80-cent contract with a wide spread does not protect 25%; it
  protects "whatever the book has." The persona already warns that stop-markets fill below the
  trigger, but the slippage assumption (half the spread) was wildly optimistic here.
- **Rule note:** on sub-$1.00 contracts, a stop-market's real floor is far below its trigger.
  Either size assuming a total loss, or use a stop-*limit* and accept gap risk.

### 9. NXE $12C Sep 18 x2 — CLOSED 2026-08-17 ❌ −$30 (−30.0%)
- **Entry:** $0.50 x2, 2026-08-17 — **Exit:** $0.35 x2, stop-market $0.40, **same day** (order 6a8326c3)
- **Wrong:** Same slippage pattern (trigger $0.40 = −20%, filled $0.35 = −30%) and the same
  sub-$1.00 contract problem. Stopped out within hours of entry, which means the entry was into
  the noise, not off a level. Opened the same day as OCUL — two fresh positions in one session,
  both dead inside 24 hours.

### 10. AMLX $40C Sep 18 — EP (Ph3 LUCIDITY) — CLOSED 2026-08-20 ✅ +$60 (+30.8%)
- **Entry:** $1.95 x1, 2026-08-19 — **Exit:** $2.55, 2026-08-20 (order 6a87055e)
- **Right:** Clean. Real catalyst, +30.8% lands just inside the band, one-day hold. The stop
  (6a85b7d4) was cancelled first to free the contract — the one-order-per-contract lock handled
  correctly this time.

### Aggregate for the backfilled block
Seven trades, 5 wins / 2 losses, **net +$355**. But the shape matters more than the total:
GDX (+$325) is essentially the entire block. Strip it and the other six net **+$30**. Two of the
three losing/flat clusters (OCUL, NXE) share one root cause — stop-market slippage on sub-$1.00
contracts — and were opened on the same day. The winners that followed the band (WULF, AMLX)
behaved exactly as designed.

---

### 11. XPEV $11P Sep 18 x2 — Breakdown/downtrend (mis-graded) — CLOSED 2026-08-25 ❌ −$20.18 (−20.6%)
- **Entry:** $0.49 x2, 2026-08-24 2:29 PM CT (order 6a8c8b4c). Original $0.47 limit missed; re-priced ONCE to
  $0.49 at the mid per the missed-limit policy, then left alone.
- **Exit:** $0.39, 2026-08-25 9:30 AM CT (order 6a8da717) — discretionary cut ahead of the $0.36 stop.
- **Thesis as written:** volume break of the 3-week $11.54–12.33 shelf to new 3-month lows on ~3.5x volume,
  in a persistent downtrend ($17.89 Jun 2 → $11.35) with clean lower highs.

- **Wrong — and this is the whole lesson: I graded the setup without its catalyst.** I filed it as a
  technical breakdown (bearish setup 2) when it was in fact an earnings gap, i.e. an EP-down (setup 1).
  XPeng reported Q2 on 8/24 pre-market: revenue missed ~3-4%, net loss RMB1.34B vs RMB512M expected
  (nearly triple YoY), Q3 revenue guided ~13% under consensus. I only found this out on 8/25, *after*
  the position was underwater, because I ran the technical scanners and never ran a news screen.
- **What the news would have told me:** the same report carried deliveries +65% sequentially, gross margin
  20.7%, a $6.3B valuation on the robotics arm, and a consensus price target of $24.99 against an $11.35
  stock. That is not a tape with no bid — it is a *contested* one. Contested tapes chop; they don't trend.
  Puts need sellers with no opposition, and this had a live bull narrative the whole time.
- **The tell was visible on day 1 and I under-weighted it.** The entire move happened in the first 45
  minutes ($11.83 → $11.28), then five hours of $11.10–11.40 chop on fading volume. I wrote the words
  "gap-and-stall, not a trending breakdown" in the session log and held anyway. The WMT backtest run that
  same morning had *just* shown that post-breakdown drift front-loads and the stall is the tell. I proved
  the point on one trade and ignored it on another the same day.

- **Right — the damage control worked:** sizing was 12% of budget (half the 20% conservative cap) precisely
  because I'd flagged the contract-volume gate as marginal at entry; that decision is why this is a $20 loss
  and not a $60 one. The re-price policy was honored (one re-price, at mid, then stop chasing). And cutting
  at $0.39 beat the $0.36 stop-market: on a 23%-wide spread that stop fills nearer $0.34 (≈ −30%), so the
  discretionary exit saved roughly $11 on 2 contracts — the OCUL slippage lesson actually applied in time.
- **Note:** the owner independently took 8 contracts of the same strike in the personal account (4x size,
  no stop). Robbin's sizing is not advice for the personal account and never has been — flagged live, twice.

- **Rule note — NEWS IS NOT OPTIONAL.** The PERSONA's SCANNING section lists news/catalysts as item 3 and
  political/influential commentary as item 5. Running only the technical scanners is a half-scan. From
  2026-08-25: no setup gets graded, and no ticket gets presented, until its catalyst is identified by name.
  If the catalyst can't be found, that fact itself is the grade.

## Open positions

(none — 100% cash as of 2026-08-25, $773.65)
