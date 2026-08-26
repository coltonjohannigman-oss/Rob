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

### 4. MRNA $65P Jul 17 — Bearish swing (puts) — CLOSED 2026-07-13 ✅ +$29 (+18.7%)
- **Entry:** $1.55 x1, 2026-07-10 (order 6a511da4)
- **Exit:** $1.84 — stop-limit $1.95/$1.80 filled @ $1.84 (order 6a54ea36), 2026-07-13
- **Right:** The ratcheted stop-limit ($1.25/$1.10 → $1.95/$1.80) banked the move instead of round-tripping it. Using stop-LIMIT rather than stop-market got a fill *above* the limit, no slippage.
- **Wrong:** +18.7% is below the 30-80% band — the trailing stop took it out early. Acceptable: the stop did its job, the band is a target not a guarantee.

### 5. WULF $18P Jul 31 — Bearish swing (puts) — CLOSED 2026-07-16 ✅ +$47 (+42.7%)
- **Entry:** $1.10 x1, 2026-07-14 — placed by the OWNER in-app after the agent's $1.05 limit missed
- **Exit:** $1.57 limit (order 6a591131), 2026-07-16
- **Right:** Clean +42.7%, squarely inside the 30-80% band, 2-day hold. The owner's decision to pay $1.10 rather than wait at $1.05 is what got the trade on at all.
- **Wrong:** Nothing. This is the model default trade.

### 6. SLB $53C Aug 21 — Day trade — CLOSED 2026-07-24 ✅ +$24 (+20.0%)
- **Entry:** $1.20 x1, 2026-07-24 (order 6a636dda)
- **Exit:** $1.44, same session ~2 hours later (order 6a638ca9)
- **Right:** Fast in-and-out, no overnight theta. Stop was cancelled to free the contract for the sell — correct handling of the one-order-per-contract lock.
- **Wrong:** +20% is under the band. On a same-day exit that is fine, but it shows the day-trade path tends to clip winners short.

### 7. GDX $85C Aug 21 — Momentum/Trend (gold miners) — CLOSED 2026-08-07 ✅ +$325 (+130.0%)
- **Entry:** $2.50 x1, 2026-08-05 (order 6a736b32)
- **Exit:** $5.75 limit, 2026-08-07 (order 6a75df48) — the $1.75 stop was cancelled first to free the contract
- **Right:** THE trade of the account so far — +130% in two sessions, and it alone is worth more than every other closed trade combined. Riding past the 80% band was correct here: gold miners were the leading theme, the trend was intact, and the position was let run rather than clipped at +50%.
- **Wrong:** Nothing on the outcome. Worth noting the position was $250 — about a third of the account at the time, i.e. aggressive-cap sizing. It earned it, but that is the size that would have hurt most had it gone the other way.

### 8. NXE $12C Sep 18 — Breakout attempt — CLOSED 2026-08-17 ❌ -$30 (-30.0%)
- **Entry:** $0.50 x2, 2026-08-17 (order 6a8322f1)
- **Exit:** $0.35 — stop-market $0.40 fired, filled @ $0.35 (order 6a8326c3), SAME DAY
- **Wrong:** Entered and stopped out within ~3 hours. A breakout that fails inside the same session was never a breakout — this was an entry taken before the move confirmed.
- **Rule note:** stop-market trigger $0.40, fill $0.35 — 12.5% slippage below the trigger on a sub-$1 contract.

### 9. OCUL $11C Sep 18 — Breakout attempt — CLOSED 2026-08-18 ❌ -$100 (-62.5%)
- **Entry:** $0.80 x2, 2026-08-17 (order 6a83210d)
- **Exit:** $0.30 — stop-market $0.60 fired, filled @ $0.30 (order 6a832155), next morning
- **Wrong:** The worst trade in the book, and the loss was NOT a -25/-30% stop-out: the stop was correctly placed at $0.60 (-25%), but the stop-market filled at $0.30 — **half the trigger price**. The gap-down opened below the trigger and the market order filled into a vacuum.
- **Rule note — the real lesson:** on sub-$1 contracts a stop-MARKET is not a risk cap. The persona already assumes "slippage ≈ half the spread"; this filled 50% below trigger. Cheap contracts gap straight through stops. Either size so a total loss is tolerable, or use stop-LIMIT (as MRNA did, which filled clean).
- **Also wrong:** NXE and OCUL were both opened on 2026-08-17 within an hour of each other and both stopped out immediately. Two same-day entries into a tape that was not cooperating — the portfolio cap allowed it, but judgment should not have.

### 10. AMLX $40C Sep 18 — Momentum — CLOSED 2026-08-20 ✅ +$60 (+30.8%)
- **Entry:** $1.95 x1, 2026-08-19 (order 6a85b7b1)
- **Exit:** $2.55 limit, 2026-08-20 (order 6a87055e) — $1.40 stop cancelled first to free the contract
- **Right:** +30.8% is the bottom edge of the band, taken cleanly on a 1-day hold. Textbook "don't get greedy."
- **Wrong:** Nothing material.

### 11. XPEV $11P Sep 18 — Bearish swing (puts) — CLOSED 2026-08-25 ❌ -$20 (-20.4%)
- **Entry:** $0.49 x2, 2026-08-24 (order 6a8c8b4c; initial $0.47 limit missed, re-priced once to $0.49 — correct per the re-price policy)
- **Exit:** $0.39, 2026-08-25 (order 6a8da717) — the $0.36 stop was cancelled and the position sold at limit instead
- **Right:** Cut at -20%, inside the hard-stop band, before it became a -60% problem. Exiting at a limit rather than letting the stop-market fire avoided a repeat of the OCUL slippage.
- **Wrong:** The thesis did not work and the position was closed in one day — fine. The re-price to $0.49 bought in 4% worse; marginal.

---

## Session note — 2026-08-26 (no trade)

**ANF +27% earnings gap: A-grade setup, PASSED on structure — and the reason generalizes.**

ANF gapped $108.90 → ~$137 (+26%) on earnings, clearing the $118.97 summer high to fresh
52-week highs, after a tight 6-session base at $103-112. Volume 201K shares in the first
5 minutes against a ~1.1M average full day. That is a textbook Episodic Pivot and it passed
the setup checklist outright.

It was still a pass, because **every tradeable expression of it failed**:
- Strikes near the new price had no open interest — $145C OI 73, $150C OI 61, $155C OI 17,
  $160C OI 14 — with spreads of 46-115% of mark.
- The only strike with real OI was the deep-ITM $120C (OI 882, 11.9% spread) at $19.35 mark
  = **$1,935 per contract, 2.5x the entire account.**
- The best compromise, the $140C (0.48 delta, 13.3% spread), still had OI 296 / volume 11 and
  cost $675 = **87% of the account** — more than double the 40% aggressive cap.
- The liquidity rubric resolves this explicitly: when every OTM strike fails the OI test, take
  the liquid ITM strike **or skip the trade entirely**. The liquid ITM strike is unaffordable,
  so: skip.

**The generalizable lesson: a big overnight gap destroys its own option chain for a small
account.** All the open interest sits at yesterday's strikes, which the gap turns deep ITM and
unaffordable; the strikes near the new price are empty because nobody owned them yesterday.
So the better the gap, the worse the tradeable liquidity. For this account size, EP setups are
tradeable on the *pullback to the 10-day EMA* — by which point OI has built at the new strikes —
far more often than on the gap day itself. Chase the gap and you pay in spread and size, or you
do not get on at all.

Also screened and passed: **BZ** (+13.5%, breakout to 90-day highs, but $20C OI 3 / 150% spread
and $17.5C OI 382 / 54% spread — fails OI and spread simultaneously, which the rubric forbids
flexing together); **PLAB** (+12%, and the *best* liquidity of the day — $35C OI 2,847,
volume 1,022, 7.7% spread, 0.37 delta, $130 = 17% of account — but the setup is a bounce into
3-month resistance, not a breakout: it is 38% below its pre-crash May level, below the $34.50
range high, and had fallen 8 straight sessions into today. Good contract, wrong chart);
**SYRE** (-13%, but the 90-day trend is UP and it made highs 6 sessions ago — a first break,
not a downtrend, and put IV is blown out); **DKS** (collapsed -30.6% on 8/25 on 38.8M volume
and never bounced — the watchlist's "wait for a bounce into the falling 10d EMA" entry is
now ~45% above spot and effectively unreachable; the -20%-flush rule blocks it regardless).

Cash is a position. No trade.

## Open positions

(none — 100% cash, $773.65 buying power)

_Ledger note 2026-08-26: the $301.21 cash gap found during the backfill was confirmed by the
owner as a withdrawal. Realized P&L (+$425.00) ties out exactly to the broker across all 11
closing trades — no trades were missing, and the books are clean as of this date._
