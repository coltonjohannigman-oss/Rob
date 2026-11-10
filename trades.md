# Robbin Trade Journal

One entry per closed trade, appended at close. Open positions tracked at the bottom.
Grade the setup honestly after the fact — this is how the system learns.

Format: **Ticker contract | setup type | entry → exit | P&L | what went right / wrong**
From 2026-09-27 on, each entry also records its SETUP SCORECARD at entry
(V/S/C/RS/R = total, grade) and contract count, so `python cli.py stats` can audit quality by grade.
Trades 1-11 predate the scorecard and are ungraded in the stats. (Until 2026-11-10 they were
missing from the stats entirely — see the process note of that date.)

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

### 4. MRNA $65P Jul 17 — EP-Down / breakdown — CLOSED 2026-07-13 ✅ +$29 (+18.7%)
- **Entry:** $1.55 x1, 2026-07-10 (order 6a511da4) | **Exit:** $1.84, stop-limit $1.95/$1.80 (order 6a54ea36)
- **Right:** Ratcheted the stop up into the move and let the trigger do the selling. Clean, unemotional exit.
- **Wrong:** Nothing structural. Exit landed just under the 30% band because the ratchet was set tight.

### 5. WULF $18P Jul 31 — EP-Down / breakdown — CLOSED 2026-07-16 ✅ +$47 (+42.7%)
- **Entry:** $1.10 x1, 2026-07-14 (order 6a569290, owner-placed in-app after the agent's $1.05 limit missed)
- **Exit:** $1.57 limit, 2026-07-16 (order 6a591131)
- **Right:** +42.7% is dead-center in the 30-80% band on a 2-day hold. Textbook put trade: took it fast, per the
  put-specific rule to bias toward the 30-50% end.
- **Wrong:** The agent's original $1.05 limit missed and the owner had to place the fill. Re-price discipline was slow.

### 6. SLB $53C Aug 21 — Momentum — CLOSED 2026-07-24 ✅ +$24 (+20.0%)
- **Entry:** $1.20 x1, 2026-07-24 (order 6a636dda) | **Exit:** $1.44, same day (order 6a638ca9)
- **Right:** Quick, clean scalp; cancelled the stop and took the limit rather than round-tripping it.
- **Wrong:** +20% is BELOW the 30-80% band — sold early without the band being reached. Profitable but off-process.

### 7. GDX $85C Aug 21 — Momentum/Trend — CLOSED 2026-08-07 ✅ +$325 (+130.0%)
- **Entry:** $2.50 x1, 2026-08-05 (order 6a736b32) | **Exit:** $5.75 limit, 2026-08-07 (order 6a75df48)
- **Right:** Best trade in the book by a wide margin. Gold-miner trend trade held through a 2-day rip; the
  stop was cancelled and the position exited on a limit into strength, not a panic bid.
- **Wrong — PROCESS FLAG:** +130% is far outside the 30-80% default band. Riding past 80% is only permitted by
  the LETTING A WINNER RUN checklist (catalyst + Qullamaggie structure + sector leadership + holding the 10-day
  EMA), and there is **no session record that the checklist was ever applied**. The outcome was excellent; the
  process was not documented. A repeat of this without the checklist is gambling that happened to pay.

### 8. OCUL $11C Sep 18 x2 — CLOSED 2026-08-18 ❌ -$100 (-62.5%)
- **Entry:** $0.80 x2, 2026-08-17 (order 6a83210d) | **Exit:** $0.30, stop-market $0.60 (order 6a832155)
- **Wrong — WORST TRADE IN THE BOOK.** The stop was set correctly at $0.60 (a -25% trigger, inside the hard-stop
  rule). It filled at $0.30. The contract gapped down overnight and the stop-market triggered into a vacuum,
  realizing **-62.5% on a position whose stop was set at -25%**.
- **Rule this proves with real money:** "Stops do NOT protect through gaps" and "stop-market on a wide-spread
  contract fills below the trigger." On a thin, low-priced contract ($0.80 premium), half-the-spread slippage is
  not the right model — the real slippage was 50% of the trigger price. On sub-$1.00 contracts a stop-market is
  closer to a suggestion than a floor. Size for that, or don't hold them overnight.

### 9. NXE $12C Sep 18 x2 — CLOSED 2026-08-17 ❌ -$30 (-30.0%)
- **Entry:** $0.50 x2, 2026-08-17 (order 6a8322f1) | **Exit:** $0.35, stop-market $0.40 (order 6a8326c3), same day
- **Right:** The hard stop did its job — cut at -30%, the outer edge of the 25-30% rule, and the trade was dead
  within hours. Losing small is the system working.
- **Wrong — SIZING/CONCENTRATION FLAG:** NXE and OCUL were opened **13 minutes apart on 2026-08-17** ($260 of
  premium across two speculative sub-$1.00 contracts) and BOTH were stopped out inside 24 hours for a combined
  -$130. Two same-day entries into thin, low-priced contracts is a correlated bet on one market condition, not
  two independent trades.

### 10. AMLX $40C Sep 18 — CLOSED 2026-08-20 ✅ +$60 (+30.8%)
- **Entry:** $1.95 x1, 2026-08-19 (order 6a85b7b1) | **Exit:** $2.55 GTC limit, 2026-08-20 (order 6a87055e)
- **Right:** +30.8% is the bottom edge of the band, taken on a 1-day hold. Stop was cancelled to free the
  contract for the take-profit (the one-order-per-contract swap), and the TP actually filled.
- **Wrong:** The stop->TP swap left the position unprotected while the TP worked. Acceptable here (it filled
  next morning) but it is the same unhedged window that cost the GRND trade five hours of drift.

### 11. XPEV $11P Sep 18 x2 — CLOSED 2026-08-25 ❌ -$20 (-20.4%)
- **Entry:** $0.49 x2, 2026-08-24 (order 6a8c8b4c) | **Exit:** $0.39 limit, 2026-08-25 (order 6a8da717)
- **Right:** Thesis stop honored early — cancelled the $0.36 stop and exited on a limit at -20%, INSIDE the
  25-30% hard stop rather than waiting for it. Losing small, on purpose. This is the discipline the book wants.
- **Wrong:** Nothing. Correct trade, wrong outcome. The put thesis simply did not work.

### 12. PENG $80C Oct 16 — Episodic pivot (day 2) — CLOSED 2026-10-07 ❌ -$75.09 (-34.9%)
- **Scorecard at entry:** graded B+ by the session (IV 94%, about -9%/day theta); entered on the
  owner's explicit override. x1 contract, $215.04 = 21% of $1,023.65.
- **Entry:** $2.15 x1, 9:31 AM CT (order 6ac657ae). **Exit:** stop $1.50 / limit $1.35 filled at
  $1.40, 12:35 PM CT (order 6ac657e8). Net proceeds $139.95 after a $0.05 fee. Hold time 3h04m.
- **Thesis:** FQ4 revenue +68%, EPS +133%, FY27 guidance +40%; gap from $60.71 to $76.10 on 15–21M
  shares (avg 2.3M).
- **Wrong:** A -2.9% pullback in the stock became a -35% loss in the option (delta ~70%, IV ~15%,
  theta ~11% of the loss). At 90%+ IV, a single contract sized at 21% of the account cannot
  survive normal post-gap noise. The stop also filled $0.10 under its trigger. Declining the
  ratchet to ~$1.85 at +21% cost about $30–40. Once a position is green, decide where you want
  to be out; "a tighter stop might get hit" is not a reason to leave it low.
- **Right:** The setup read was correct and the named risk is the one that hit. PENG closed +13%
  that day with the gap intact. The thesis was fine and the instrument still failed.
- **Bookkeeping:** this trade was booked on the divergent branch `claude/trade-feature-k6dyxg`
  and backfilled into this ledger on 2026-10-08 (buy $215.04 / sell $139.95, `--setup EP --grade B`).
- **Post-mortem grade:** C (execution). Owner-override trades get logged at the session's grade.

## Open positions

(none — 100% cash. Ledger $948.56; broker cash $904.56 on 2026-11-10. The $44.00 gap is not
trading: no option or equity fills since PENG on 10/7. It looks like a transfer out and
NEEDS OWNER CONFIRMATION before the ledger is adjusted.)


---

## Process notes (not closed trades)

### 2026-09-23 — The put bounce-entry rule missed an entire trend (NVO)
The PERSONA's EP-DOWN rule prefers the bounce entry: "Buy puts on the breakdown day or — usually
better — on the first weak bounce into the declining 10/20-day EMA." On NVO this week that
preference cost the whole move.

- 9/21: NVO -7.7% to $39.89 on 2.7x volume, light long-term targets. Oct 16 $40P = $1.44.
  Passed on the flush; waited for a bounce-rejection at the declining 10-day EMA ($43.69).
- 9/22: $39.56. No bounce. 9/23: $38.24, new lows. Same put = **$2.21, up 53%**.
- The bounce never came. Three sessions, no rally above even the prior day's high.

**The observation:** the bounce entry works on choppy breakdowns that retrace into the EMA. It
structurally CANNOT fill on the strongest downtrends — the ones that go straight down are exactly
the ones that never bounce. The rule therefore self-selects into weaker setups and misses the best
ones. Waiting also gets worse over time: by 9/23 the remaining downside to the Feb-April base
($35-39) had shrunk to a few percent, so the trade got less attractive while the thesis got MORE
right.

**Not changing the rule unilaterally — this is the owner's call.** One instance is not proof; the
rule exists because flush entries do get shaken out (see the OCUL gap, trade #8). A candidate
amendment worth testing: on an EP-Down where volume confirms AND put IV is NOT inflated (NVO's was
34%, cheap), allow a half-size breakdown-day entry rather than requiring the bounce, and keep the
full-size bounce entry as the add. That preserves the IV discipline while not forfeiting trends
that never retrace.

### 2026-09-23 — Position sizing, not direction, was the real VKTX constraint
VKTX gapped +35% on 9/22 (VK2735 maintenance data). Passed: the Oct 16 $40 call cost $350 = 45% of
buying power, over the 40% aggressive cap, with IV at 79.5%.

What happened next is the useful part. The call went $3.90 (9/22 close) -> $2.19 (9/23 morning,
-44%) -> $4.875 (9/23 afternoon). Buying at $3.90 would have been *directionally right* — it is up
25% from there now — but a 25-30% hard stop would have fired on the morning flush, realizing a
~$100-115 loss, and then watched the recovery.

**The lesson:** at 79% IV, a position sized at ~50% of the account cannot survive its own noise.
The stop distance the rules require is narrower than the contract's normal daily range. That makes
the trade un-holdable at that size *regardless of whether the thesis is right*. The sizing cap did
not just limit loss here — it correctly identified a trade this account cannot carry.

Two directional predictions were also wrong and are worth logging honestly: IV was predicted to
crush post-event and instead rose (79.5% -> 83.2%), and the 9/23 morning reversal off $42.92 was
called distribution at resistance when it was a shakeout before a push through.

**UPDATE 2026-09-24 — the VKTX note above was written mid-move and needs its ending.**
The stock round-tripped the entire gap in three sessions: $30.11 (9/21 close) -> $42.92 (9/23 high)
-> **$35.90 (9/24 morning)**, which is below Tuesday's $36.34 low, the level named as the kill
trigger. The gap failed and the setup is retired.

Full arc of the Oct 16 $40 call: $3.50 (9/22 open) -> $3.90 (9/22 close) -> $2.19 (9/23 am) ->
$4.875 (9/23 pm) -> $4.05 (9/23 close) -> **$1.43 (9/24 am)**.

So the 9/23 claim that a Tuesday entry "would have been directionally right" was itself a
mid-move artifact — it was right for about four hours. From the $3.90 entry the contract is now
**-63%**. Every path loses: hold through and you are down 63%; respect the hard stop and you are
out at -25/30% on the 9/23 morning flush. There was no version of this trade that worked.

The sizing cap was the binding constraint and it was correct, but note WHY it was correct. It was
not because the direction was wrong on day one — the stock did go up. It was because a 79%-IV
contract at ~50% of the account has a daily range wider than its own stop. The account could never
have held it long enough to find out whether the thesis was right, and the thesis turned out to be
wrong anyway.

**Standing lesson: on a post-binary-event gap, IV staying elevated is not a signal that more upside
is coming. It is the market pricing a two-sided distribution. Both tails were live here and the
down tail won.** The 9/22 prediction of an IV crush and the 9/23 reading of the reversal were both
wrong, in opposite directions, within 24 hours of each other. When a name generates two confident
and contradictory reads that fast, that is itself evidence the setup is unreadable — and unreadable
is a pass, not a coin flip.

### 2026-11-10 — Persona review: why nothing traded for five weeks, and what the record really says

No position since PENG on 10/7, and no trade Robbin graded A himself since XPEV on 8/24. Eight
sessions and one autopilot window ended "no trade". Causes, biggest first:

**1. The drawdown brake was on because of a bookkeeping bug, and it could not release.**
`cli.py stats` counts only closing transactions that carry a `cost_basis`. The first eleven
closes were recorded (or backfilled on 9/21) without one, so from 10/8 the stats read
"1 trade, 0W/1L, expectancy -34.9%" — PENG alone. That satisfied "negative expectancy over the
last 10 closed trades", so every session from 10/23 ran A+ only at 15% ($142). The true last
ten were 6W/4L, +$295, with a losing streak of two. Under the rule as written the brake should
never have been on.
Once on, it was absorbing: release needed a closed winner; a winner needed an A+ (9/10); a
counter-regime trade caps at 8 and a no-catalyst pullback in CHOP caps at 8. In a falling market
only a with-regime put with a hard catalyst, 2x volume and perfect structure could trade — at
$142. Nobody caught that the stats line said "1 trade" while this journal listed twelve.
*Fixed:* the eleven closes now carry cost basis and P&L (stats: 12 trades, 8W/4L, +$349.91,
ties to the ledger); the brake is replaced by a size-only ladder that the stats command prints;
"A+ only" is banned as a rule form; a data check precedes any reading of the stats.

**2. The funnel was aimed at stocks the account cannot buy.** The cap was $142-$285 of premium.
A 3-4 week near-the-money option costs roughly 4-6% of the share price, so the real ceiling was
a ~$30-55 stock. The focus list was DELL ($563), PLTR, ANET, BE, CRWD; sessions worked up MRVL,
BA, LITE, MELI, FICO and ARGX and then wrote "unaffordable". *Fixed:* a price ceiling computed
from the cap at the top of each session and applied to the scanners, plus an ETF sleeve.

**3. The extension limit made every episodic pivot untradeable.** A 15-20% gap sits 3-8 ADR from
the 10-day EMA; the EMA needs about two weeks to catch up; pipeline entries age out in 10
sessions. Seven EP / EP-down names were logged 10/23-11/2 and none reached a legal entry.
*Fixed:* a post-gap flag (3+ sessions inside the gap-day range) counts as the base.

**4. The primary funnel was scored on the wrong volume rule.** "Leaders pulling back" became the
main call source on 10/8, but VOLUME still required 2x average on the trigger — a breakout
signature. A good pullback is quiet. *Fixed:* volume is scored by setup type; the trend
pullback is now a defined fourth setup.

**5. Sessions were sparse.** None between 10/8 and 10/23 (DOCU broke out unwatched), none
between 11/2 and 11/10 (QQQ went 681 → 647 → 679). Robbin only looks when /trade is sent. Not
fixed by a persona edit — it needs a scheduled session, which is the owner's call.

**What the gates got right and wrong, 10/23 → 11/9 (close to close unless noted):**

| Name | Dir | Blocked by | Then | Verdict |
|---|---|---|---|---|
| PBR | put | extension, "ADR < 4% → A+ only", brake | $22.50 → $18.35 (-18%), never bounced | missed — the second NVO |
| NU | put | extension, brake | $12.59 → $11.61 low area → $12.36 | nothing lost; a scratch |
| XYL | put | extension, liquidity | $88.23 → $99.26 (+13%) | gate right — would have lost |
| BA | put | extension, price | $168 → $172, range $165-179 | gate right — no trade there |
| CCI | call | counter-regime, brake | broke $91.45 on 11/4, back to $87.83 | gate right — failed breakout |
| TENB | call | gap-day, extension, regime | $51.78 → $43.67 (-16%) | gate right |
| GMAB | call | counter-regime, brake | $44.67 → $57.29 in one day (10/28) | missed, but a 2-session flag in RISK-OFF |
| QQQ / index | put | never scored | $725 (10/28) → $647 (11/5), -11% | missed — the regime call was right and unused |

So the gates were not simply too tight: they kept Robbin out of four losers. What failed was
that nothing with-regime could get through either. The changes above open the with-regime side
(PBR by the flag rule, the index by the ETF sleeve) without touching the counter-regime blocks
that worked. This table is seven names and one index; it is a first pass-audit entry, not proof.

**What the twelve closed trades say** (now that the stats can see them): 8 wins, 4 losses,
+$349.91, profit factor 2.55 — and GDX (+$325) is 93% of it. Without GDX: eleven trades, +$25,
average win +$36, average loss -$56. Planned stops were -25/30%; realized losses averaged -37%
(OCUL -62.5% through a gap). Three wins closed below the 30% band (SOFI +13.5%, MRNA +18.7%,
SLB +20%). The honest summary is "one runner and a slightly negative grind", and the one runner
was held without the run-checklist being applied. Losses need to stop at -1R and part of each
A+ needs room to reach +2R.

**Reasoning errors worth naming so they are not repeated:**
- *One loss → four rules.* PENG (an owner override of a B+) produced the gap-day rule, the
  extension limit, the EP structure re-score and the funnel switch in one commit. Each was
  defensible alone; nobody checked what they did together, or against past winners.
- *A split of eleven trades cited as evidence.* The gap-day rule's "Why" compared day-1 entries
  (-$101) to later entries (+$391). GDX is $325 of the second number. Removed from the persona.
- *A known problem left open.* The 9/23 NVO note said the bounce-only put entry "structurally
  cannot fill on the strongest downtrends" and left it as "the owner's call". The 10/8 changes
  then tightened the same side. PBR repeated NVO five weeks later.
- *Only false positives were measured.* Losses got post-mortems; passes got one line and were
  forgotten. There is now a Pass audit in pipeline.md.
- *"No trade" was never treated as a result.* Eight in a row raised no flag. There is now a
  tripwire at eight.

**Left for the owner (not changed here):**
- The 30% per-trade ceiling. At 30% size and realized losses of -37%, one loss costs about 11%
  of the account, against the 1-2% that Tharp and Minervini work with. The ladder trims size
  after losses; it does not change the ceiling.
- Option level. The agent account is Level 2 (long calls and puts only). Debit spreads would
  roughly halve the cost and the IV exposure of every trade and widen the affordable universe
  several-fold, but need Level 3.
- A scheduled daily session, so that triggers are seen on the day they fire.
- The $44.00 ledger-vs-broker gap noted under Open positions.
