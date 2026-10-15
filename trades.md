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

## Open positions

(none — 100% cash as of 2026-09-21)


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

---

## Session note — Friday 2026-10-02 (no trade)

**The scanner fix worked, and it immediately changed what I can see.** First session with the
`$5-75` price filter removed from all three scans. The gainers scan went from the handful of thin
small caps it had been returning to **110 matches**, and the list was overwhelmingly
semiconductors and semicap equipment: SYNA +14%, MXL +13.7%, IMOS +10.8%, WOLF +9.1%, CRDO +8.7%,
PENG +8.6%, VECO +8.1%, ALGM +7.3%, ACLS/NVTS +7.1%, ONTO/SMTC +6.8%, ARM +6.2%, TER +6.1%,
ENTG +5.6%, MPWR +5.5%, STM/ON +5.2%, SITM/MTSI +5.0%, KLIC/DIOD +4.8%, INTC +4.6%, LSCC +4.5%,
COHU/RMBS +4.2%, AMD +4.2%. SMH +2.94%. Four sessions of calling this tape "dead" were a
measurement artifact, exactly as suspected. The blind spot was real and it was mine.

Three names graded, three different disqualifications. None of them was "nothing is moving."

**1. SYNA — the best-looking chart on the board, and completely untradeable.**
Structure was textbook episodic pivot: three-month downtrend $137 -> $93, base at $88-$106 through
September, an accumulation day 10/1 ($101 -> $106.15 on 1.01M shares, ~2x normal), then a +14% gap
on **2,656,026 shares in the first 30 minutes — about 5.9x an entire average day** (prior six
sessions averaged ~451K). On structure and volume alone I would have graded this A+.

It is an all-cash acquisition. onsemi amended its 6/25 merger agreement on 10/1, converting from
all-stock to **all-cash at $123/share** (~$5.7B), after an unsolicited competing proposal on 9/2.
Debt financing fully committed (~$2.45B, Morgan Stanley), no financing condition, US antitrust
already cleared. Stock $121.08. **Upside is $1.92, permanently.** The 5.9x volume was merger-arb
funds taking the spread, not institutional accumulation. No call has convexity under a hard cap.

This is the WBD deal-pin trap a second time, and it is the clearest argument yet for why the
catalyst check runs BEFORE the grade. Structure alone said A+; the catalyst said zero.

**2. MXL — clean momentum structure, options fail the gate by 10x.**
Genuine flag breakout: bottomed $57.59 (9/1), ran to $93.84 (9/25) = +63%, tight four-day flag at
$90-$93, broke to $104.78. Legitimate Qullamaggie continuation setup. Nov 20 calls:

| Strike | Mark | Spread | OI | IV |
|---|---|---|---|---|
| $105 | $16.80 | 10.7% PASS | **40** FAIL | 111% |
| $110 | $14.55 | **17.2%** FAIL | **330** FAIL | 109% |
| $115 | $11.75 | 7.7% PASS | **40** FAIL | 113% |

Every strike misses the 500 OI minimum badly. The only one with meaningful OI also blows the
spread gate — failing both at once, which the rules never allow me to flex together. Independently
it was a chase: the $105 call closed $9.75 and marked $16.80, **premium already +72% on the day**,
111% IV, break-even $121.80 requiring another +16% to get flat. Fourth time this pattern has killed
a name (CRML, EVER, OCUL, MXL): attractive mid-cap chart, untradeable options.

**3. STX / WDC — the best setup I have found, and I cannot afford it.**
The losers scan was the more valuable of the two today. STX **-11.86%** to $833.35 ($178B cap,
4.75M shares at 1.91x relvol — roughly 2x a full day in 38 minutes), WDC **-10.06%** to $415.49
($150B cap). Semis ripping while storage breaks is not a broad chip rally, it is a violent rotation
*within* tech.

Ran the CTVA check on both before anything else. STX implied prior close $945.57, ratio 1.135 — no
split; $178.1B / $833.39 = 214M shares, consistent with the real count. WDC $150.3B / $416.01 =
361M shares, also consistent. **Both declines real.**

Catalyst is specific and structural: **Toshiba investing ~Y60B ($400M) to double HDD output by
FY2027, targeting 30% share from just over 10%** — new supply aimed directly at the pricing power
that drove STX +240% YTD and WDC +170% YTD. Extended name, real competitive-threat catalyst,
volume confirming, peer confirming. Textbook parabolic exhaustion.

| Contract | Mark | Per contract | Delta | OI | Spread |
|---|---|---|---|---|---|
| STX Nov20 $800p | $66.60 | **$6,660** | -0.383 PASS | 269 FAIL | 7.8% PASS |
| WDC Nov20 $400p | $34.35 | **$3,435** | -0.392 PASS | **924 PASS** | **2.9% PASS** |

The WDC put passes every liquidity gate cleanly and is the best-structured contract I have priced
in nine sessions. It costs **16.8x the $204.73 conservative cap and 3.4x the entire account.** STX
is 32.5x the cap. Both IVs ~70% post-gap, so day-one entry also means paying inflated vol — the
condition the pending EP-Down amendment explicitly excludes. Reaching for a ~$2.04 contract means
roughly a $280 strike at delta ~0.05: a lottery ticket. The rules permit flexing delta only when
every OTM strike fails OI, not to force an unaffordable name into the account.

### The finding worth the owner's attention

**Account size, not judgment, is now the binding constraint on the best opportunities.** Two of the
last three sessions had their strongest setup blocked purely by affordability — VKTX by position
size, STX/WDC by contract price. At $1,023.65 with a 20% cap of $204.73, I can only buy contracts
under ~$2.04/share, which systematically confines me to low-priced underlyings with thin option
books. That is precisely the population that produced CRML, EVER, OCUL and NXE.

So the nine-session no-trade record is not one thing. Early on it was partly a broken scanner.
Today it is that the two best setups on a genuinely active tape were a merger arb and a pair of
$3,400-6,700 contracts. I am not going to widen the cap to fix this — that is the owner's call, not
mine. Flagging it as a decision rather than acting on it.

**Also unchanged and still awaiting a ruling:** the $301.21 funding gap, the SOFI 50-share trim,
and the EP-Down half-size breakdown-day amendment. The STX setup is exactly the case that amendment
was written for, and it went untaken today for affordability rather than for the bounce rule — so
the amendment still has not been tested either way.

### Watch triggers set

- **STX** — no entry on day one of a -12% break. The thesis is a multi-quarter supply story, so it
  has time. Watch for a bounce toward **$880-$900** (broken shelf / 10-day EMA) that stalls and
  rolls over. Unaffordable at current premiums regardless; tracking it to test the thesis, and
  actionable in the individual account where capital is not the constraint.
- **PLTR** — touched the $192.59 confirmation level and failed it. 1,674,815 shares in the first 30
  minutes against a ~20M full-day average: ~8% of a day's volume in ~8% of the session, i.e. flat,
  not expanding. It printed $194.78 then faded to $192.40, below its own open. Level reached,
  volume absent. Recommendation unchanged at ~$191.35 entry / $184.50 stop for the individual
  account, but it is not confirmed.
- **ACN** — the decline is fully vindicated. Peaked $227.41 intraday Thursday where I passed,
  closed $212.30, now **$202.58, -4.58%**. That is roughly **-10.9% from the point I declined to
  chase**, and it appears in today's LOSERS scan. Second time this week (with VKTX) that declining
  day one of a gap was correct. Still watching for the first pullback that holds, but it has not
  stopped going down yet.
- **IONQ** — unchanged: close through $48 on 25M+ shares, or $42-43 holding and turning up. Retire
  below $40. $44.73 today, no trigger.

**Cash is a position. Nine sessions, zero trades, and today the tape was not the problem.**

### Friday 10/2 close (2:31 PM CT, 29 min to bell)

Account unchanged: $1,023.65 all cash, no positions, no working orders. No trade taken.

| | Close-ish | vs prior close |
|---|---|---|
| PLTR | $189.08 | **-0.50%** |
| ACN | $199.20 | -6.17% |
| STX | $850.98 | -10.00% |
| WDC | $416.11 | -10.04% |
| SMH | $631.64 | +2.24% |
| SYNA | $121.60 | +14.56% |

**PLTR: setup failed, recommendation retired.** It printed $194.78 in the morning, rejected the
$192.59 confirmation level on flat volume (1.67M shares in the first 30 min vs a ~20M full-day
average), and closed **red at $189.08**. That is a failed breakout, not a pending one, and the
$191.35 entry I had standing is now above the market. Retiring it rather than leaving a stale buy
level in the journal. A fresh setup needs a new base, not a re-poke of this one. Worth noting the
morning volume read called this correctly in real time — the level was reached and the volume was
absent, and the volume was the part that mattered.

**ACN: falling knife, still not a pullback.** $199.20, through $200, now **-12.4% below the
$227.41 Thursday high where I declined to chase.** Three straight sessions down. The "first
pullback that holds" has not started — nothing to buy, and the decline is now emphatically
vindicated rather than merely lucky.

**STX: partial absorption, thesis intact.** Recovered off the $833.35 morning low to $850.98 but
still -10% on the day. Not a close at the low (which would be clean continuation) and not a
recovery into the green either. Monday's bounce-failure zone stays **$880-$900** (broken shelf /
10-day EMA); a stall and roll there is the entry if it comes. Still unaffordable in this account at
$3,435-6,660 per contract — tracking the thesis, actionable only in the individual account.

**Semis held.** SMH closed +2.24% off an intraday +2.94%. A sector move that holds into the bell is
a live theme for Monday, not a one-day rotation. MXL finished +14.0% near its high — the structure
was right, the option book is still the problem.

**SYNA closed $121.60, grinding toward the $123 cash price.** Exactly the arb-pin behavior the
morning read predicted. Good confirmation that reading the catalyst before the chart was the right
call, not excessive caution.

Nine sessions, zero trades. Today the tape was alive and the three best setups were a merger arb,
an untradeable option book, and a $3,435 contract against a $204.73 cap.

---

## Session note — Monday 2026-10-05 (no trade)

9:06 AM CT. Ledger reconciles exactly: $1,023.65 allocated / $1,023.65 remaining against $1,023.65
live broker buying power. No positions, no working orders, nothing unprotected. Realized +$425.00.

### The thesis I was most confident about went against me

Friday I built a detailed bearish case on STX/WDC and called it "the best setup I have found in nine
sessions." Today, one session later:

| Contract | Fri official close | Now | |
|---|---|---|---|
| WDC Nov20 $400p | $32.93 | $22.73 | **-31.0%** |
| STX Nov20 $800p | $60.50 | $43.65 | **-27.9%** |

STX bounced to $898.08 (+5.78%), WDC to $440.76 (+6.13%). **Had the account been large enough to
take the trade, I would be stopped out at a loss right now** — both contracts are at or through the
25-30% hard stop. On Friday I wrote that account size rather than judgment was blocking my best
idea. The constraint saved me from it.

I want the conclusion stated carefully, because the self-flattering version and the
self-flagellating version are both wrong. One draw does not vindicate the cap; a cap that blocks
good and bad setups indiscriminately is not justified by a single instance, and the question should
be settled on the distribution of outcomes. What this session actually establishes is narrower and
more useful: **my confidence in that thesis was miscalibrated**, and two independent guardrails
caught it — affordability, and the bounce-entry rule I had been complaining was structurally
broken. The bounce rule was right here. A -10% break that fully retraces in one session is exactly
what the rule exists to avoid buying.

**And it refines the pending amendment rather than killing it.** The proposed EP-Down half-size
breakdown-day entry was conditioned on "volume confirms AND put IV is NOT inflated." Friday's put
IV was ~70% post-gap, which I judged inflated at the time — so **the amendment's own guard clause
would have excluded this trade.** The guard did its job. That is evidence the amendment is sensibly
designed, not evidence against it. Still the owner's call; the record now has one real test of it.

Thesis status: weakened, not dead. A -10% break retraced in a session means the market is reading
Toshiba's FY2027 capacity as immaterial against AI storage demand. **If STX reclaims $945.57 the
breakdown has failed outright** and the thesis is retired. Unaffordable here regardless
($4,365-6,660/contract vs the $204.73 cap).

### Board state

**PTC — deal-pinned, and caught before the chart.** +34.84% to $194.21 on 7.95x relative volume
and 3.96x relative options volume. A +35% gap on a mature $14-23B enterprise software name has one
overwhelming explanation, so I checked the catalyst first: **all-cash Schneider Electric
acquisition at $205/share** ($22.6B, 42.3% premium to the $144.03 prior close). Upside is $10.79
(+5.56%) and that is the permanent ceiling. Third deal-pin in a week after WBD and SYNA. The
difference from Friday is that the catalyst check ran before the structure grade — that is the
process working rather than luck, and it is the direct payoff of the SYNA lesson.

**Friday's semi rotation reversed outright.** My own stored test was "follow-through is the setup, a
gap-and-fade means Friday was a one-day rotation." It failed that test: CRDO -5.1% (was +8.7%),
IMOS -6.4% (was +10.8%), WOLF -7.9% (was +9.1%), MXL -1.05%, SMH -0.46%. Storage bounced while
semis faded — the Friday rotation ran in reverse in both directions, which is mean reversion, not a
regime. Worth noting the MXL liquidity failure that frustrated me Friday also kept me out of a name
that is now red while its sector leaders are down 5-8%.

**UMC — the one genuinely interesting name, ungraded by rule.** -10.83% to $23.425 on a $63.5B cap,
9.33M shares in ~40 min against a ~11M daily average (~85% of a full day), 3.81x relative options
volume. Structure is a clean failed breakout: new high close Friday at $26.27 (best since early
July), two weeks of gains erased in one session. Corporate-action check clears it — implied prior
close $26.27, ratio 1.121, no split signature, and ~2.5B ADS reconciles the market cap. At $23 it
is the rare candidate that is both liquid and affordable.

**But the news lookup did not find today's catalyst.** Results came back stale and generic — a June
BNP Paribas downgrade, August notes, nothing for 10/5. I do not know why it is down 10.8%, and "big
move, cause unknown" is exactly the condition that produced the losses in this journal. It is also
a Taiwanese ADR, so some of the gap may be catching up to an overnight Taipei session rather than a
US-hours breakdown — a structurally different thing. **Not graded. Next session must establish the
cause before UMC can be scored at all.**

**RZAI -37.9%** flagged by the standing hazard rule and skipped: ratio 1.61 is no clean split, but
109K shares on a -38% move is not a tradeable book under any gate.

Others: ACN $198.48 (-0.21%) finally stopped falling after three down sessions, but flat is not a
pullback that holds — still nothing to buy. PLTR $188.42 (-0.17%), confirming Friday's failed
breakout and the retired entry. IONQ $43.15, no trigger. SOFI $16.03, above the $14.88 line, not
re-raising.

Ten sessions, zero trades. Today that is three deal-pins deep in the tape, a one-day rotation that
reversed, and the one real candidate missing its catalyst.

---

## Session note — Tuesday 2026-10-06 (no trade)

9:07 AM CT. $1,023.65 allocated / remaining, matching live buying power. No positions, no orders.

### The bounce-entry rule just settled its own argument, with numbers

Friday I wrote that the put bounce-entry rule "structurally cannot fill on the strongest
downtrends" and proposed an amendment to allow a half-size breakdown-day entry. Monday the STX
bounce reached my $880-$900 zone (closed $887.09). Today it is rolling over: STX $836.98 (-5.65%),
WDC $418.90 (-5.15%). The trigger I defined on Friday has fired. Same contracts, two entry dates:

| Entry | STX Nov20 $800p | WDC Nov20 $400p |
|---|---|---|
| Friday breakdown day | $60.50 -> $57.15 = **-5.5%** | $32.93 -> $28.28 = **-14.1%** |
| Monday bounce failure | $40.05 -> $57.15 = **+42.7%** | $21.33 -> $28.28 = **+32.6%** |

**The breakdown-day entry is still underwater even after the move went my way.** The bounce entry
is up 33-43% on an identical thesis from a cost basis 34% cheaper. The rule I complained about is
the rule that would have made this trade work, and the amendment's "put IV not inflated" guard
would have correctly blocked the Friday entry at ~70% IV.

I want my own role stated accurately: **I did not call the entry at Monday's bounce high.** Monday
I said the trigger was unmet because the stock was ripping +5.78% rather than stalling. That was
correct, and today confirms it — but the rule earned this, not my timing. The honest version is
that a mechanical rule outperformed my discretionary read of the same chart on both Friday (when I
wanted to be short early) and Monday (when I thought the thesis was breaking down).

Caveat against my own case: today's roll is on **1.73M shares vs 4.75M on Friday's break**. A
bounce failure on lighter volume than the initial break is less emphatic, and I am not going to
pretend otherwise just because the direction suits the thesis.

Unaffordable regardless: **$5,715 and $2,827.50 per contract against the $204.73 cap.** So the
setup I built, the trigger I defined, and the rule that vindicated it all worked, and the account
could not participate in any of it. That is the cap question with the opposite sign from Monday,
and both signs belong in the record.

### Five flow artifacts in one week

**UMC — catalyst found, and it disqualifies the setup.** On 10/5 UMC priced **$1.8B of unsecured
overseas convertible bonds**; the -10.8% was convertible-arbitrage hedging and dilution, as arb
desks shorted stock against the new paper. That is a mechanical one-time supply event, not business
deterioration — the bearish mirror of a merger-arb pin. An EP-Down needs a thesis that compounds;
convert hedging decays. Not a setup. (Separately the fundamentals are weak — 4-analyst consensus
Sell, $18.49 target — but the proximate cause of the gap was flow, and the gap is what I would
have been trading.) $23.42 today, -2.09%.

**OPCH — acquisition.** +32.76% on 8.98x relative volume and 6.67x options flow. **CD&R and
McKesson at $32.05/share**, ~$5.8B, 51/49 split. Stock $31.025, so upside is $1.025 (+3.3%) and
capped. Checked the catalyst before the chart; cost about two minutes instead of an hour.

So this week: **WBD, SYNA, PTC and OPCH deal-pinned, UMC convert-driven.** Every large-gap candidate
I examined was a flow or structure artifact, and every one looked clean on structure alone. The
standing insight: in this regime my gainers scan is substantially an M&A announcement detector, and
the catalyst check is not a formality on top of the process — it is the single highest-yield step in
it. Five for five.

### Rest of the board

Losers list is ~27 of 35 biotech — a broad sector drawdown, nothing name-specific to grade.
**AVBP -59.56% on 12.996x relative volume** flagged by the hazard rule: ratio 2.47 and 118M shares
reconcile, so it is a real collapse rather than a split, almost certainly a failed readout. Per the
VKTX lesson a post-binary-event biotech is unreadable, and puts after a -60% move have no
risk/reward left. Skipped.

SMH $638.78 (+0.77%) and SPY $779.77 (+0.64%) — semis recovered again after Monday's fade. Two
reversals in two sessions is chop, not a theme; the Friday rotation call stays retired.
**PLTR $191.78 (+1.26%)**, back near the $192.59 level it failed. One green day is not a new base —
holding the retirement rather than resurrecting a level that already broke once.
ACN $194.32 (-0.38%), still drifting; no pullback that holds. IONQ $44.38 (+3.28%), below $48.
SOFI $16.02, above the $14.88 line.

Eleven sessions, zero trades.

---

## Session note — Wednesday 2026-10-07 (no trade, but a real setup for once)

8:49 AM CT. $1,023.65 allocated/remaining vs $1,023.65 buying power. No positions, no orders.
Owner pushed: "cmon let's find something today." Fair — twelve sessions is a lot. The right
response is to work harder, not to lower a gate, and today there was finally something to work on.

### PENG — the first genuine setup in twelve sessions, and a near miss

Catalyst is fundamental and compounding, not a deal or a flow artifact: **FQ4 net sales $567M
(+68% YoY), beating by $46.01M; adjusted EPS $1.00 (+133%); FY2027 guide ~$2.43B revenue (+40%
YoY) and $4.45 EPS, both above consensus.** After five straight flow artifacts (WBD, SYNA, PTC,
OPCH deal-pinned; UMC convert-driven) this is the first catalyst all week that actually compounds.

Structure is a textbook EP: collapsed -51% in July ($89.86 -> $43.70), based $46-$64 for ~2.5
months, accumulation day 10/2 (+7.5% on 2.4x volume), 15.6M shares on 10/6 (~10x normal) into the
print, gapping to $75.685 today. Not extended — still well under the July high. Up 18% while
SMH is -1.91%, so idiosyncratic strength rather than a sympathy tagalong. ~6.5M shares in 20
minutes against a ~1.5M average full day.

**The Nov 20 chain fails OI outright** (131/199/66/25 vs the 500 floor). But the Oct 16 chain is
where the liquidity lives, and one contract clears every gate:

| Oct 16 | Mark | Spread | OI | Vol | Delta | Cost |
|---|---|---|---|---|---|---|
| $75 | $4.50 | 8.9% PASS | 2,210 PASS | 4,428 | 0.522 PASS | $450 |
| **$80** | **$2.825** | **8.8% PASS** | **2,681 PASS** | **2,695** | **0.369 PASS** | **$282.50** |
| $85 | $1.60 | 18.8% FAIL | 614 | 552 | 0.241 FAIL | $160 |
| $90 | $0.875 | 28.6% FAIL | 872 | 621 | 0.148 FAIL | $87.50 |

First contract in twelve sessions to pass OI, volume, spread and delta simultaneously.

**And I am still not taking it.** $282.50 is 27.6% of the account, above the 20% conservative cap
of $204.73. Anything over 20% requires the "exceptional — multiple confluent signals all pointing
the same direction" standard, and PERSONA says to be honest with myself about whether the setup
truly earns it. It does not, for one decisive reason:

**Theta is -0.251/day on a $2.825 premium — -8.9% per day.** A five-day hold costs ~44% of the
premium to decay alone at a flat price; the 25-30% hard stop would trigger on theta in about three
flat sessions. IV is **102.5%** one day after the event that caused it, which is the VKTX lesson
verbatim: elevated IV after a binary event prices a two-sided distribution, not pending upside.

So the signals are not confluent. The *stock* signals are excellent; the *option structure*
signals are bad. Grading it A+ to unlock aggressive sizing would be me wanting the trade, not the
setup earning it. The $85 strike fits the cap at $160 but fails delta AND spread together, which is
never allowed. The $75 passes every gate but costs $450, over even the aggressive cap.

**Honest grade: B+. Good setup, wrong instrument at this account size.** Qullamaggie buys EPs on
day one — but that method buys *shares* with a 2-3% stop, not 9-DTE calls at 102% IV where decay alone
trips the stop. The instrument is the disqualifier here, not timidity, and that distinction matters.

**Plan, not a punt.** The disciplined EP entry is the first pullback that holds. By then IV crushes
off ~102% and the Nov 20 contracts get both cheaper and structurally sound, and their OI should
build off today's volume. Trigger: a pullback into roughly **$66-$70 that holds and turns up**,
then re-check Nov 20 OI against the 500 floor. **Invalidation: a close back below $64.21** (the
pre-gap close) means the gap failed outright and PENG is retired.

### Personal-account advisory (Level 3) — the gap I have been leaving unfilled

PERSONA carries a PERSONAL ACCOUNT ADVISORY playbook requiring that when a setup grades well but
fails Robbin's rules for a reason a spread fixes, I flag it with exact strikes, expiries, debit,
max loss/gain and break-evens. I have been saying "actionable in the individual account" for a
week without ever doing that work. Correcting that. Account ••••1866 confirmed margin /
option_level_3. (The agentic account is option_level_2, so spreads are not even mechanically
available there — the single-leg restriction is doubly binding.)

PENG is precisely structure #1's case: Qullamaggie-quality setup, IV spiked past the buying gate
(97-103%, clearly >80% and event-inflated).

**Cleanest expression — shares.** No IV, no theta, no expiry. For an EP with a multi-week horizon
this is the right instrument and it sidesteps every objection above.

**Leveraged alternative — Oct 16 $75/$85 call debit spread:**
- Buy Oct 16 $75C (~$4.53), sell Oct 16 $85C (~$1.57) -> **net debit ~$2.97 = $297/spread**
- Max loss **$297** (the debit) | Max gain **$703** at $85+ | Break-even **$77.97** (+3.0%)
- Risk/reward ~2.37:1; both legs liquid (OI 2,210 and 614)
- Selling the $85 neutralizes most of the 102% IV and offsets the theta that disqualifies the
  single leg — which is exactly why the playbook exists.
- Honest risks: still a day-one-of-gap entry; 9 DTE; a fade below $75 by 10/16 loses the full
  $297; the short $85 caps upside if it runs hard.
- Nov 20 $75/$85 is the better horizon (~$415 debit, $585 max gain, break-even $79.15) but OI of
  131/66 makes fills unreliable. Grade: Oct 16 structure **A-**, Nov 20 structure **B-** on
  liquidity.

### Rest of the board

**STX thesis fully confirmed and still unaffordable.** Arc: $945.57 -> $848.99 -> bounce $887.09 ->
$805.63 -> **$792.17** (-1.67%), now below the original breakdown low. WDC $402.27 (-2.13%). The
bounce-entry rule continues to be the right call. Contracts remain multiples of the cap.

IONQ **$41.32 (-4.56%)**, closing on the $40 retirement level — if it closes below $40 it is
retired. ACN $195.85 (+1.26%), first real bounce in four sessions but one green day is not a
pullback that holds. PLTR $191.73, flat; entry stays retired. SOFI $15.57. UMC $22.94, still
disqualified. SMH -1.91%, SPY -0.60%.

NWE +6.91% and BKH +6.91% — two utilities moving near-identically, which given the week's pattern
suggests a deal between them. Not chased: neither is affordable or actionable here, and I am not
asserting a merger I did not verify.

Twelve sessions, zero trades — but today the honest reason is narrow and specific: the best setup
of the stretch needed 27.6% of the account in a contract that decays 8.9% a day.

### 10/7 addendum — remaining scans, and a second real candidate

Closing two gaps from the morning run (only the gainers scan had been run, and the watchlists were
stale from 9/24 and 9/28).

**PENG strengthened through the morning.** Now in the options-flow scan at **3.83x relative options
volume**, 9.64M shares (~6x a full average day), and **ATM IV cooled 102.5% -> 88.8%**. The thesis
is getting better, not worse, which is what an EP should do. Grade unchanged at B+ for the agentic
account — the sizing and decay arithmetic has not changed — but if IV keeps compressing while price
holds, the Nov 20 chain becomes the right vehicle and the OI there should build off today's tape.

**BULL (Webull) — a real EP-Down, barred by an explicit rule.** -20.6% to $5.78 on **7.22x relative
volume** (42.7M shares) and 2.43x options flow; it printed -29% at $5.15 intraday. Catalyst is
serious and durable: the **House Select Committee on China** report finds Webull structurally tied
to the Chinese government — ownership architecture, technical workforce, technology infrastructure,
cross-border data routing, corporate financing and compliance — with concerns sharpened since it
began holding customer cash directly in Oct 2025. Ownership and data-routing findings are a
multi-month overhang, not a one-day print. Corporate-action check clears: implied prior close
$7.28, ratio 1.26, no split signature, ~540M shares reconciles the $3.93B cap.

And at $5.78 it is the first bearish candidate all month that would actually be **affordable**.

**Passed anyway, and not as a judgment call.** PERSONA PUT-SPECIFIC RULES: *"Never buy puts after a
-20% single-day flush with IV blown out — that trade is over."* BULL is -20.6% with IV 63.5%. That
is the barred case verbatim. The persona also names the correct entry: *"the first weak bounce into
the declining 10/20-day EMA, when put IV has cooled off the panic print."* Trigger set on the
EP-Down watchlist: a weak bounce into roughly **$6.50-7.00** (the declining 10-day EMA — compute it
properly at trigger time rather than trusting this estimate) that stalls on light volume.
**Invalidation: a close back above the 10-day EMA on volume.**

Worth noting the shape of today: two genuinely good setups, one long and one short, both with real
compounding catalysts — and both declined for *instrument* reasons rather than thesis reasons. PENG
on sizing and decay, BULL on an explicit put rule. That is a materially different kind of no-trade
day than the eleven before it, and both now have defined triggers rather than vague watching.

Watchlists refreshed (both descriptions had been carrying dead VKTX and OCUL triggers for ~10 days).

Still outstanding to the owner: whether to take the PENG Oct 16 $80C anyway — the gate I invoked is
my own A+ sizing judgment, not a hard rule violation, and the liquidity genuinely clears. Asked,
not assumed. No position opened.

---

## POSITION OPENED — Wednesday 2026-10-07, 9:31 AM CT

**First position in twelve sessions.** Owner-authorized above my own sizing gate after I declined it.

### Trade #12 (open) — PENG Oct 16 2026 $80 Call

| | |
|---|---|
| Entry | **$2.15** x1 contract (order 6ac657ae, filled 14:31:10 UTC) |
| Cost | **$215.04** incl. fees |
| Sizing | **21.0%** of $1,023.65 |
| Remaining | $808.61 |
| Stop | **stop $1.50 / limit $1.35 GTC** (order 6ac657e8, state confirmed) |

Limit was $2.20; **filled at $2.15 for $0.05 of price improvement.** PENG had pulled back from
$75.28 to $73.86 in the six minutes between my presenting the trade and placing it, so the
contract cheapened from $2.55 to $2.175 — the sizing came in at 21.0% instead of the 24.9% I
quoted. The pullback worked in the account's favor on entry price.

**Liquidity at entry:** OI 2,681, volume 3,806, spread $0.05 (2.3%), delta 0.326, IV 94.2%.
Note delta had slipped from 0.369 to 0.326 — **below the 0.35 floor** — between presentation and
fill, because the stock fell. I flagged that to the owner before sending rather than quietly
filling through the gate. Every other gate passed with room.

**Thesis — Episodic Pivot.** FQ4 net sales $567M (+68% YoY, beat by $46.01M), adjusted EPS $1.00
(+133%), FY2027 guide ~$2.43B revenue (+40%) and $4.45 EPS, both above consensus. Gapped out of a
2.5-month $46-$64 base built after a -51% July collapse ($89.86 -> $43.70). ~9.6M shares by
mid-morning against a ~1.5M average full day. Not extended — well below the July high. Rising
while SMH was -1.91%, so idiosyncratic strength rather than a sympathy move.

**Exit plan:**
- Hard stop **-30% at $1.50** (resting, GTC). Chose the loose end of the 25-30% band deliberately:
  theta is -0.218/day on a $2.15 entry = **-10.1%/day**, so a -25% stop would be hit by decay alone
  in ~2.5 flat sessions. The looser stop buys the thesis room against its known enemy.
- Thesis stop: **close below $64.21** (pre-gap close) — gap failed, exit regardless of the stop.
- Time stop: **hard exit Oct 14**, two days before expiry. This needs to work in 2-3 sessions.
- Profit: 30-80% band, **biased to 30-50%** given the decay. +30% = $2.80 (+$65); +50% = $3.23
  (+$108). One working order per contract, so the stop and any take-profit cannot both rest —
  take-profit gets managed at check-ins.

**My grade was B+, not A+, and I said so before and after.** I declined this trade twice on my own
sizing gate: at 21% it is over the 20% conservative cap, and the aggressive tier requires an A+ the
setup does not earn because the *instrument* is poor even though the *stock* signals are excellent
(94% IV one day post-earnings, -10.1%/day decay, day one of a gap). The owner overrode that
judgment with explicit authorization, which is their call to make — I presented the full decay math
twice and they took it with eyes open. Recording the disagreement plainly so the post-mortem is
honest either way: **if this wins it is because the catalyst was strong enough to beat a bad
instrument, and if it loses it will most likely be theta and IV rather than direction.** That is
the specific thing to grade later.

### Also found in the individual account (advisory, not executed)

Owner asked for an A-grade idea there and the account turned out to need attention first.
Account ••••1866: $4,414.92 total, $2,510.42 cash, buying power $7,138.28, Level 3.

**PLTR Nov 6 $210/$230 call debit spread is AT ITS STOP — recommended close.** Long $210C paid
$690, short $230C collected $224 = **net debit $466**. Now worth $3.39 net = **$339, or -27.3%**,
inside the 25-30% hard-stop band. The thesis stop has also fired: PLTR is $191.73 and needs
**$214.66 to break even by Nov 6 (+12% in 30 days)** on net spread delta of just **0.163**, ~20%
probability of profit, bleeding ~$6.44/day of net theta. I independently retired the PLTR long
thesis on 10/2 when it rejected $192.59 on flat volume and closed red. Closing recovers ~$339.

**A+ idea — PENG Oct 16 $75/$85 call debit spread.** Meets playbook structure #1's criteria
explicitly: setup checklist passes, IV 91-97% (>80% AND event-inflated), max loss below a normal
position for that account. Net debit ~$3.25 = $325; max gain $675 at $85+; break-even $78.25
(+3.9%); **R/R 2.08:1**. Both legs clear OI and volume ($75C: OI 2,210 / vol 5,657; $85C: OI 614 /
vol 831). Critically it fixes what made the single leg B+: **net theta -1.8%/day vs -8.9%, net vega
0.013 vs 0.045.** Suggested 2 contracts = $650 = 14.7% of that account.

**WDC put spread examined and REJECTED** despite the stronger thesis — honest record of the check:
Nov20 $400/$360 is $1,717.50 (38.9% of the account) at only 1.33:1; $400/$380 is 1.11:1; and both
short legs ($380P, $360P) show **volume of 13**, under the 100 floor. The puts are already rich at
65% IV, so the spreads surrender most of the move. Good thesis, not an A structure.

**SOFI:** 100 shares at $18.10 average, now ~$15.57 (-14%, -$253). Shares are held, so per the
persona a plain covered call beats a PMCC — selling a Nov $18-18.50 call collects premium without
capping below cost basis. Offered, not yet priced.

### 10/7 mid-session (10:39 AM CT) — position management, no second trade

**PENG Oct 16 $80C: +20.9% (+$45.00).** PENG $75.17 (+17.07%), contract mark $2.60 vs $2.15 entry.
Account value $1,068.61. Ledger reconciles exactly: allocated $1,023.65 / open $215.04 / remaining
$808.61 against broker cash $808.61.

Stop order 6ac657e8 verified **confirmed**, exactly one working order on the contract — no
unprotected position, no duplicates. Delta has recovered to **0.369**, back above the 0.35 floor
that it had slipped under at the moment of entry.

Volume is sustaining: **13.8M shares** by 10:39, which at ~33% of the session elapsed is roughly
2.7x the normal pace. That is the single most important confirmation for an EP — the move is not
a one-print gap.

**Take-profit: not triggered.** +20.9% is below the 30-80% band (+30% = $2.795).

**Considered a stop ratchet and declined it.** The position is two hours old; the persona's
trailing rule starts near +50%, and tightening to ~$1.85 now would very likely stop me out on
routine post-gap consolidation, which is the most common price action after an EP. The $1.50 stop
risks $65 = 6.4% of the account, inside tolerance. **Ratchet trigger: at +50% ($3.23), move the
stop to breakeven.** Recording that I weighed it rather than silently leaving it — over-managing a
two-hour-old winner is its own failure mode.

**Breadth was sharply risk-off: 23 gainers vs 293 losers** against a mild SPY -0.41%. That
asymmetry argued against adding a second long regardless of what the scans turned up.

**HESM — genuine EP-Down thesis, untradeable instrument.** -15.59% to $32.66 on **6.49x relative
volume**, $5.08B cap. Catalyst is real and compounding, not flow: FY26 net income guided down to
$650-675M; **FY27 adj EBITDA guided $850-950M against FY26's $1.23-1.25B, a 25-30% decline**;
Bakken tariffs with Chevron revised through 2045; and **Chevron divesting its HESM and DJ Basin
interests for $200M while taking a $3-4B after-tax loss** — a sponsor eating that loss to exit is
the strongest tell in the set. JPMorgan cut to Underweight on 10/2 with a $39 target the stock is
already below; consensus is now Reduce.

Nov 20 puts, every strike:

| Strike | Spread | OI | Delta |
|---|---|---|---|
| $30 | 40.0% FAIL | 114 FAIL | -0.230 FAIL |
| $31 | 25.6% FAIL | 4 FAIL | -0.313 FAIL |
| $32 | 44.1% FAIL | 74 FAIL | -0.401 pass |
| $33 | 32.9% FAIL | 61 FAIL | -0.485 pass |

**Fails OI and spread simultaneously at every strike** — the one combination the rules never allow
flexing. IV is only 39-42%, so the premium is not even rich; the book is simply empty, which is
normal for a midstream LP. Fifth time this pattern has killed a candidate (CRML, EVER, OCUL, MXL,
now HESM). No watchlist trigger set, because setting an entry trigger for a trade that can never be
filled is self-deception — logged as thesis-tracking only.

**BULL: trigger not hit.** -21.06% at $5.75 on **9.21x relative volume** (54.4M shares), but it is
sitting at the lows with no bounce. The entry is a weak bounce into the declining 10-day EMA; that
has not happened. Still barred from a flush-day entry by the persona rule.

**BKH +10.09% / NWE +10.06%** — two utilities moving in near-lockstep on heavy volume (relvol 1.43
and 1.75) for a second consecutive session. Given five deal-pins this week the shape strongly
suggests a transaction between them, but **I did not verify it and am not asserting it.** Not
chased: a pinned deal is untradeable and neither fits the remaining cap cleanly.

Portfolio caps checked: max 3 concurrent, max 2 per sector/theme. At 1 of 3, so room existed — the
pass was on merit, not on a cap.

**Net: one position, working, protected. No second trade.** Conservative sizing on the remaining
$808.61 budget would cap a new position at $161.72, and nothing today cleared the gates anyway.

---

## Trade #12 CLOSED — PENG Oct 16 2026 $80 Call — **-$75.04 (-34.9%)**

| | |
|---|---|
| Entry | $2.15 x1, 9:31 AM CT (order 6ac657ae) |
| Exit | **$1.40**, 12:35 PM CT (order 6ac657e8, stop filled) |
| Cost basis | $215.04 |
| Proceeds | $140.00 |
| **Realized** | **-$75.04, -34.9%** |
| Hold time | **3 hours 4 minutes** |

Stop triggered at $1.50 and filled at **$1.40 — $0.10 below the trigger**, the exact
stop-market/stop-limit slippage the persona warns about. Intended loss was -30%; actual was -34.9%.
The extra 4.9 points is that slippage.

Account after: $948.61 allocated, flat, no working orders. Broker cash $948.56 — the **$0.05 gap is
the exit fee** I did not net into the ledger entry. Note buying power is **$808.61**, not $948.56:
the $139.95 of proceeds does not settle until 10/8. All-time realized P&L now **+$349.96** (from
+$425.00).

### The question I set up at entry: theta/IV or direction?

**Direction, dominantly — with the instrument amplifying it.** PENG ran to $75.69 in the morning
and dipped to roughly $71.7 by 12:35, a **-5.3% intraday reversal off the high**. Decomposing the
$0.75 loss per share at the stop:

| Driver | Approx. contribution |
|---|---|
| Delta (PENG -2.9% from entry) | **~-$0.65 (~70%)** |
| IV (94.2% -> ~91%) | ~-$0.13 (~15%) |
| Theta (~0.45 of a session) | ~-$0.10 (~11%) |

So the stock genuinely went against me; this was not a pure decay death. **But the instrument turned
a -2.9% move in the underlying into a -35% move in the option** — roughly 12:1 effective leverage.
That is precisely why a -30% stop was reachable on an ordinary post-gap pullback, and precisely the
risk I named when I graded this B+ rather than A+. The entry analysis was correct. "Day one of a
gap" plus 94% IV plus -10%/day theta is a configuration where normal consolidation kills the
position before the thesis resolves. PENG closed the day **+13.3% at $72.73** — the gap held, the
thesis is intact, and the option still lost 35%. That gap between "thesis fine" and "position dead"
IS the lesson.

### My actual mistake was the stop ratchet, and it was a reasoning error

At 10:39 the contract was $2.60 (+20.9%). I considered ratcheting the stop from $1.50 to ~$1.85 and
declined, writing: *"tightening to ~$1.85 now would very likely stop me out on routine post-gap
consolidation."*

**That reasoning was backwards.** I was already going to be stopped out by that consolidation — the
$1.50 stop caught it two hours later. The choice was never "stopped out vs. not stopped out"; it was
**"stopped out at $1.85 or stopped out at $1.40."** A ratchet to $1.85/limit $1.70 would have exited
near $1.70-1.80, a loss of roughly **$35-45 instead of $75.04**. Declining the ratchet cost about
**$30-40**.

**The generalizable error: "I might get stopped out" is not an argument for placing a stop lower.**
A stop's job is to define the exit price, not to avoid being triggered. I conflated *avoiding the
trigger* with *protecting the position*, and on a position already in profit those are opposites.
Writing this down as a standing correction: once a position is green, the ratchet question is "where
do I want to be out," never "how do I avoid being taken out."

Honest caveat so this does not overcorrect: in the branch where PENG recovered and ran to $85, the
looser stop is the right one and the ratchet would have been the error. One instance does not
establish "always ratchet." But the *reasoning* I used was faulty independent of the outcome, and
that is the part to fix. Also worth noting the contract is **$1.65 as of 2:31 PM**, above the $1.40
fill — the stop sold near the intraday low. That is the inherent cost of resting stops and not a
reason to stop using them; the stop executed correctly and unattended while I was not watching
between 10:39 and 2:31.

### Grade: C on execution, and the B+ setup call was right

The setup assessment holds up: I identified the instrument risk specifically and in advance, twice
declined the trade on sizing, and the risk I named is the one that materialized. The owner overrode
that judgment with explicit authorization — a legitimate call on genuinely strong stock signals, and
their money — and the override lost $75.04. Recording that plainly, not as vindication but because
the next sizing decision should have an accurate record to work from.

What I would do differently, in order: (1) ratchet the stop at +20% per the corrected logic above;
(2) prefer the **$75/$85 debit spread** structure even in the agentic account if it were Level 3 —
net theta -1.8%/day vs -8.9% would have survived this exact pullback; (3) hold the 20% cap, since
at 21% a -34.9% loss cost 7.3% of the account on a single 3-hour trade.

### Rest of the board at 2:31 PM CT

**BULL $5.98** — bounced off the $5.75 low toward the trigger zone but **not there yet**; the entry
is a weak bounce into the declining 10-day EMA at roughly $6.50-7.00. Closest it has been.
**IONQ $41.27** — above $40, **not retired**. Needs a CLOSE below $40.
**STX $800.52** (-0.63%), thesis intact, still unaffordable. **SPY $777.04** (-0.26%).

Individual account (advisory, unexecuted): PLTR Nov 6 spread still recommended closed; PENG
$75/$85 A+ spread still open as an idea — note it would have *held* through today's pullback where
the single leg did not; SOFI covered call still unpriced.

---

## Session note — Thursday 2026-10-08 (no trade) — I WAS WRONG ON THE PLTR SPREAD

9:13 AM CT. Account flat: $948.56, buying power $948.56 (yesterday's proceeds settled). No positions,
no working orders. Ledger $948.61 vs broker $948.56 — the **$0.05 is the exit fee** from trade #12,
identified, not a mystery, too small to warrant a correcting transaction.

### The PLTR spread: my recommendation cost the owner $220

Yesterday at ~9:28 AM CT I recommended closing the owner's **PLTR Nov 6 $210/$230 call debit
spread** at a -27.3% mark, citing both the hard stop and the thesis stop. They acted on it 32
minutes later, filling at 10:00 AM CT: sold the $210C at $5.57, bought back the $230C at $2.12, net
**$345 credit** against a $466 basis = **realized -$121**.

Today PLTR is **$201.12 (+3.61%)** and that spread is worth **$565 (+21.2%)**. Holding would be
**+$99**. **The advice cost $220.** Order 6ac65758, placed_agent "user".

Three errors, in increasing order of importance:

**1. I conflated two different theses.** My retired PLTR idea was a $191.35 single-leg swing entry
that failed at $192.59 on 10/2. The spread needed PLTR above $214.66 by Nov 6 — a different trade,
different level, 30 days of runway. I cited "I independently retired the PLTR long thesis on 10/2"
as evidence the *spread's* thesis was dead. It was not the same thesis and I had no basis to declare
the move impossible.

**2. I read consolidation as failure.** I wrote that PLTR "has gone nowhere since" 10/2. It was
coiling under $192.59 and broke out two sessions later to $201.12. Four flat sessions is what a base
looks like; I scored it as a dead thesis.

**3. The rule-level error: I applied single-leg stop math to a defined-risk spread.** The 25-30%
hard stop exists because a long option can decay to zero — it is protection against unbounded
premium loss. **A debit spread's max loss is already capped at the debit; the structure IS the risk
control.** Stopping out at -27% mark-to-market on a spread with 30 days left surrenders exactly the
convexity that was paid for. The spread's net delta was **0.163** — far OTM and highly convex to
precisely the move that then happened. Mark-to-market percentage is close to meaningless on a far-OTM
vertical mid-life; it swings violently on small underlying moves (this one went -27.3% to +21.2%, a
48-point swing, on a 4.9% move in PLTR).

**What I would still defend:** at the moment of the advice the mark genuinely was -27.3% and PLTR
genuinely had failed a breakout. In the branch where PLTR drifts into Nov 6, the spread decays toward
zero and the exit looks smart. **One favorable outcome does not prove the recommendation wrong in
expectation**, and I will not pretend otherwise. But errors (1) and (2) were faulty reasoning
regardless of outcome, and (3) is a rule misapplication that would recur on every future spread.

### PERSONA amendment proposed (owner's ruling required, not applied unilaterally)

**Defined-risk spreads should not use the single-leg 25-30% hard stop.** Proposed replacement for
spreads only: exit on (a) **thesis invalidation** — the underlying violates the level the structure
was built around; or (b) **time** — less than ~1/3 of original DTE remains and the underlying has not
made meaningful progress toward the short strike; or (c) a **max-loss budget set at entry** and
accepted as the whole debit. Never on a mid-life mark-to-market percentage. Rationale: the debit IS
the stop, and a vertical's mark is a noisy estimator of its terminal value until late in its life.

This now sits alongside the other open rulings, and note it points the opposite way from Wednesday's
lesson: on **single-leg** positions I under-managed the stop (should have ratcheted); on **spreads**
I over-managed it (should have left it alone). The unifying principle is that the stop discipline has
to match the instrument's risk profile, not be applied uniformly.

### Second consecutive day of a self-inflicted error, and both are now encoded

Wednesday: declined a stop ratchet on reasoning that was backwards, costing ~$30-40.
Thursday: recommended closing a defined-risk spread on single-leg stop math, costing $220.
Both are management errors, not analysis errors — the setups were graded correctly both times. That
is the pattern worth watching: my entry screening is holding up; my **position management** is where
the losses are coming from.

### Board

**PCRX is deal #6** this stretch: +44.05% to $36.30 on **18.69x relative volume** and 19.64x options
flow — **Viatris cash tender at $36.50/share**, ~$1.65B, both boards approved, targeted to close by
end-2026. Upside $0.20 (+0.55%). Pinned. Caught on the first search before any chart work; the
catalyst-first rule has now paid for itself six times (WBD, SYNA, PTC, OPCH, PCRX, plus UMC's
convert flow).

**PENG: resolved as a no, on numbers rather than willpower.** The revenge-re-entry question answered
itself. Nov 20 IV compressed to 74.3% (from ~80%) but OI is still **185-293 against the 500 floor**
with volume **3-35 against the 100 floor**, and the contracts run $400-735 against a $189.71
conservative cap. The Oct 16 $80C I was stopped out of is back to $1.675 — above my $1.40 exit — but
delta has decayed to **0.300** (below the 0.35 floor) with theta at **-12%/day** and 8 days left.
Strictly worse than Wednesday's entry. Not re-enterable. PENG $74.29 (+2.31%), gap intact, kill level
$64.21 unchanged.

**BULL: trigger still not hit.** $5.825 (-1.10%), fourth session pinned near the lows with no bounce.
Entry remains a weak bounce into the declining 10-day EMA.

**IONQ $40.68** — above $40, **not retired**. Needs a CLOSE below $40; it is one bad session away.

Gainers (31) held nothing tradeable: MANE +18.5% and HAE +12.1% are $114-131 stocks too expensive for
the cap; GFUZ +11.8% traded 226K shares; GFS +6.0% is not an EP. **ACN +4.08% to $204.67** is finally
the bounce I was waiting for after $227.41 -> $193.40, but it is day one of that bounce and a $204
underlying does not fit a $189.71 cap. Watching for it to hold.

STX $799.01 (-1.06%), thesis intact, unaffordable. SMH -1.15%, SPY -0.15%.

---

## Session note — Friday 2026-10-09 (no trade) — best-structured candidate yet, passing on the chart

9:07 AM CT. Account flat: $948.56, buying power $948.56 (fully settled). No positions, no working
orders. Ledger $948.61 vs broker $948.56 — the $0.05 exit fee from trade #12, already explained.

### IONQ RETIRED

It closed 10/8 at **$39.45**, below the $40 line I set weeks ago. That is the retirement condition
and I am honoring it: **IONQ is off the watchlist.** $39.42 today. The entry conditions I defined
(close through $48 on 25M+ shares, or $42-43 holding and turning up) were never met and the stock
simply decayed out of range. Clean, uneventful, correctly retired rather than quietly carried.

### BULL: EMA computed properly, and the book fails

I promised to compute the actual 10-day EMA instead of reusing my $6.50-7.00 estimate. Seeding a
10-day SMA at 9/21 (8.711) and iterating forward with k=0.1818 through 10/8's close: **the 10-day
EMA is $6.92.** My estimate was in range but at the top of it.

BULL is **$6.1601 (+3.55%)**, bouncing off the $5.51 low **on declining volume** (81.4M on the
break -> 21.4M -> lighter today). A weak bounce on fading volume is exactly the shape the setup
wants. It sits 11% below the EMA, so the trigger has not fired.

**But the Nov 6 put book fails, and not for the reason I expected:**

| Strike | Mark | Spread | OI | Vol | Delta |
|---|---|---|---|---|---|
| $5.00 | $0.10 | 100% FAIL | 130 FAIL | 0 FAIL | -0.137 FAIL |
| $5.50 | $0.22 | 63.6% FAIL | 293 FAIL | 2 FAIL | -0.256 FAIL |
| $6.00 | $0.41 | **39.0% FAIL** | **1,430 PASS** | **1 FAIL** | **-0.405 PASS** |
| $6.50 | $0.525 | 81.9% FAIL | 229 FAIL | 0 FAIL | -0.625 FAIL |

The $6 strike has real open interest and the right delta, but a **39% spread** — past even the 25%
exception — and volume of 1. I did NOT establish whether another expiry quotes tighter (the Nov 20
$6 strike does not exist, and I declined to map every expiry for an untriggered trade).

**Structural finding worth the owner's attention:** a $0.16 bid/ask is ordinary market-making width,
but on a $0.41 premium it is 39%. **Percentage spread scales inversely with premium**, so the
$189.71 cap that pushes me toward cheap contracts pushes me toward structurally bad percentage
spreads. Expensive contracts fail on cost; cheap ones fail on spread. That is a systematic bind in
the rule set, not a run of bad luck, and it explains a lot of the no-trade record.

### T (AT&T) — the best-structured candidate of the entire stretch, and I am still passing

**The losers scan found the biggest sector event yet: telecom is being repriced.** TMUS **-9.96%**
($183.8B), VZ **-7.76%** ($192.6B), T **-8.62%** ($170.4B), plus LUMN -6.6%, TIGO -4.9%, SHEN -4.9%,
TDS -4.8%, BCE -4.4%, VOD -4.4%, RCI -4.0%, and ASTS -8.0% — on a day SPY is **+0.26%**.

Corporate-action check on all three mega-caps: share counts reconcile (7.50B / 1.19B / 4.50B),
ratios 1.08-1.11, no split signatures. All real.

**Catalyst (checked before any chart work):** SpaceX agreed to buy a nationwide low-band spectrum
portfolio from Grain Management, reportedly **~$8B cash** (WSJ), as a step toward **Starlink
Mobile** — pairing its satellite-to-device constellation with a terrestrial buildout, pending final
FCC approval. Shotwell said in August that Starlink would target VZ/T/TMUS customers; the FCC has
already cleared the direct-to-device constellation; and the three carriers announced a defensive
satellite JV on 10/2. **A funded new entrant with spectrum attacking a three-player oligopoly is a
genuine multi-year thesis — the first structural bearish catalyst I have found all stretch that is
not a deal-pin or a flow artifact.**

Volume confirms. At ~9.7% of the session elapsed: T relvol 0.69 = **~7x normal pace**, VZ 0.92 =
~9.5x, TMUS 0.64 = ~6.6x.

**And the instrument is the best I have priced.** T Nov 20 puts:

| Strike | Mark | Spread | OI | Vol | Delta | IV | Cost |
|---|---|---|---|---|---|---|---|
| $22 | $0.555 | 12.6% PASS | 1,200 PASS | 587 PASS | -0.332 | 31.2% | $55.50 |
| **$23** | **$0.985** | **9.1% PASS** | **1,426 PASS** | **133 PASS** | **-0.494 PASS** | **30.7%** | **$98.50** |

The $23 put clears **every** gate. The two things that killed PENG are both absent: **IV is 30.7%,
not inflated** — the options market is not pricing panic even after an 8.6% drop — and **theta is
-1.0%/day versus PENG's -10%/day**, so the position can breathe for weeks. At $98.50 it is 10.4% of
the account, half the conservative cap. 42 DTE is a proper swing horizon.

That low IV also disarms the usual bounce-entry objection. The persona says wait for the bounce
*"when put IV has cooled off the panic print"* — **T's put IV never spiked**, so the condition the
rule exists to wait for is already satisfied.

**So why pass?** The chart, specifically:

T ran $20.48 -> **$26.72** (9/15) over Jul-Sep, declined to $24.24, bounced to $24.87 yesterday on
53.3M shares, and today gapped to $22.725 — **below every close since July 21.** It cleared 2.5
months of structure in one move. **But it landed directly on the July congestion shelf at
$21.50-$22.30, and the $23 put's break-even of $22.01 sits inside that shelf.**

Buying puts into support is a poor entry regardless of how good the thesis is. You want the break
*through* support, or a failed bounce off it. This is not the day-one reflex that burned me on PENG
— it is a specific technical objection about where the gap stopped. Chance of profit on the $23 put
is **36.7%**, with roughly 2-3x upside if T reaches $21-20 by Nov 20.

**Grade: B+.** Excellent catalyst, excellent instrument, confirmed volume and sector breadth,
poor entry location. **Trigger: a decisive close below $22.00** (through the July shelf, on volume),
**or a weak bounce to $23.50-24.00 that stalls and rolls over.** Either gives a materially better
entry than buying mid-shelf. Thesis invalidation: a close back above **$24.87** (yesterday's close)
means the market has dismissed the SpaceX threat and the gap has been reclaimed.

If the owner wants in today over my recommendation, the ticket is **BUY 1x T Nov 20 2026 $23 put,
limit ~$0.99** (mid), $98.50, 10.4% of the account — and I would set the stop by the thesis
($24.87 reclaim) rather than a tight percentage, given theta is only -1%/day.

### Rest of the board

PENG $72.955 (+1.93%), gap intact, kill level $64.21. Still not re-enterable per yesterday's check.
ACN $206.205 (-1.03%), pulling back after bouncing $193.40 -> $208.36; the bounce held, which is
what I wanted to see, but the stock is too expensive for the cap — individual-account material.
STX $775.41, thesis intact, unaffordable; it has now walked $945.57 -> $775.41 since the break.
SMH -0.19%, SPY +0.26%, SOFI $15.745.

### 10/9 mid-session (9:32 AM CT) — CORRECTION: I overstated the telecom declines

Account flat, $948.56, no positions or working orders. Ledger $948.61 (the $0.05 exit fee).

**T and VZ both went ex-dividend today, and I missed it this morning.** The live quote shows T's
`adjusted_previous_close` at **$24.5925** against an unadjusted `previous_close` of $24.87 — a
**$0.2775** gap, matching AT&T's quarterly dividend. VZ shows **$45.6425 vs $46.35**, a $0.7075 gap
matching Verizon's. TMUS shows no adjustment.

| | Reported this morning | Actual (dividend-adjusted) |
|---|---|---|
| T | -8.62% | **-6.37%** |
| VZ | -7.76% | **-5.69%** |
| TMUS | -9.96% | **-9.62%** (no adjustment, real) |

**This is a specific process miss, not bad luck.** The standing rule from the CTVA trap says
*compare `adjusted_previous_close` to `previous_close`*. I ran the share-count reconciliation —
which correctly cleared all three of a split — but I took the prior close from the **scan's
net-change field**, which is unadjusted. So I performed half the check and skipped the half designed
to catch exactly this. The scan's `% Change` column is computed off the unadjusted close and will
overstate any decline on an ex-dividend date.

**Standing rule, tightened:** the corporate-action check is not complete until
`adjusted_previous_close` has been read from a live quote and compared to `previous_close`. Never
compute a percentage move from a scanner's net-change field alone — it is unadjusted. This matters
most on dividend payers, where ex-div dates manufacture 1-3% of phantom decline.

The thesis survives the correction: TMUS at **-9.62%** is unadjusted and real, and -6% on a $170B
telecom is still a large move. But the magnitudes I presented were inflated by roughly a point, and
anyone sizing off my numbers would have been working from a slightly overstated break.

**T bounced off the July shelf, exactly as predicted.** $22.725 at the open -> **$23.025** now. The
Nov 20 $23 put went **$0.985 -> $0.87 (-11.7%)**, so passing on entry location has saved money
rather than cost it so far. **Neither trigger has fired:** it is moving away from the $22.00 break,
and has not reached the $23.50-24.00 failed-bounce zone. The pass stands on its own reasoning.

Worth noting: the Nov 20 **$22 put's volume jumped to 1,209** from 587 this morning — heavy
positioning for a break of that shelf. Someone else is watching the same level.

**BULL $6.205 (+4.29%)**, third session bouncing on light volume, now 10% below the $6.92 EMA.
Converging on the trigger zone. The 39% spread problem on the Nov 6 book is unresolved; if the
trigger fires, check Oct 23 / Oct 30 / Nov 13 before concluding it is untradeable.

Options-flow scan: 5 hits, nothing tradeable. CON 18.6x options volume on a flat price (positioning,
no move), TAL +2.84%, **TSLA +3.11%** on 3.06x options volume but $386.68 is far over the cap,
SIRI +2.53%, SOLV +1.60%.

PENG $72.32 (+1.05%), gap intact. ACN $206.705 (-0.79%), bounce still holding. SPY +0.33%.

**No trade.**

### 10/9 close (2:30 PM CT) — T trigger NOT fired, shelf held; individual-account advisory specified

Agentic account flat: $948.56, no positions, no working orders.

**T: the shelf held, exactly as the pass predicted.** $22.115 at 2:30, having sat between $22.10
and $22.20 for the prior 2.5 hours. The trigger is a **close below $22.00** — it is 0.5% above with
30 minutes left, so **not fired**. Consolidating ON the $21.50-22.30 shelf is a different thing from
breaking it, and the trigger is the discriminator between the two.

Sector at 2:30, all dividend-adjusted: T **-10.07%**, TMUS **-12.76%**, VZ **-8.54%** (recovered
from -9.66% at midday). TMUS holding near the lows is the cleanest confirmation — it had no
ex-div adjustment to muddy it.

**Honest accounting of what patience cost today:** the Nov 20 $22 put went **$0.485 -> $0.815
(+68%)** and the $23 put **$0.87 -> $1.370 (+57%)** from 9:32. If the trigger fires Monday I pay up.
The analysis was right — the stock stopped at the shelf and held, which is what I said — and the
entry price got worse anyway. **Right call, worse price. Both are true and neither cancels the
other.** What would make the pass wrong is if T never breaks $22 and I never get filled; that is
the risk I accepted, and it is still live.

**Strike selection shifted as the stock fell.** The $22 put is now the correct strike, not the $23:
delta **-0.445** (in the 0.35-0.55 band) versus the $23's **-0.620** (through the ceiling, now ITM),
spread **3.7%** vs 5.1%, and volume **6,953** vs 1,408. Worth noting for the trigger: re-select the
strike at entry rather than reusing the one I first priced.

**BULL $6.335 (+6.47%)** — fourth session bouncing, now 8.4% below the $6.92 EMA. The EMA declines
to roughly **$6.81** on today's close as the old highs roll off, so the two are converging and the
trigger zone could be reached early next week. The 39% spread problem on Nov 6 remains unresolved;
check Oct 23 / Oct 30 / Nov 13 if it triggers.

**PENG $75.05 (+4.86%)** — back above the $2.15-entry level I was stopped out of, gap fully intact.
Not re-enterable (Oct 16 delta decayed, Nov 20 fails OI/volume), but the thesis was right and the
instrument was wrong, which is the trade #12 post-mortem in one line.

### Individual account ••••1866 — advisory specified (Level 3, advisory only, I cannot execute)

Account: **$4,426.82** total, cash **$2,855.32** (PLTR proceeds settled), 100 SOFI worth $1,571.50.
Conservative 20% cap here is **$885.36**, so the constraint that cripples the agentic account does
not bind.

**1. T Nov 20 2026 $22 put, ~$0.82 = $82.** OI 1,200, volume 6,953, spread 3.7%, delta -0.445,
IV 31.0%, theta -1.2%/day, break-even $21.18, 42 DTE. Every gate passes.

**Why I recommend this for the individual account while passing in the agentic one — and this is
not a reversal.** My objection is entry location: T sitting mid-shelf. At **$82 it is 1.9% of a
$4,426 account**, so a bounce to $23 costs roughly $25, or 0.6% of the account. The identical trade
in the agentic account was 8.6% of capital behind a tight stop, where being early is fatal — that is
precisely how trade #12 died. **Same thesis, different sizing, different answer.** Position size is
what converts "early" from fatal to tolerable.

Thesis stop: a close back above **$24.87**. Profit: 30-50% band ($1.07-1.22).

**2. Checked the put debit spread and rejected it.** The Nov 20 $23/$21 runs ~$0.95 net for $1.05
max gain = **1.11:1**. A debit spread exists to solve a premium-cost problem that does not exist in
this account; it caps the upside and buys nothing. Single leg is correct here.

**3. SOFI Nov 20 2026 $18 covered call, collect ~$0.41 = $41.** The income idea I offered twice and
never priced — now priced. OI **17,272**, spread **2.4%**, delta 0.264 (~26% assignment odds).
**2.6% yield in 6 weeks** on the $1,571.50 position. If assigned at $18.00 the effective exit is
**$18.41, above the $18.10 cost basis**, so assignment is a small win rather than a loss booked
below cost. Downside unchanged — the $41 is pure cushion on a position that has been dead money.
Persona prefers a plain covered call over a PMCC when the shares are held, which they are.

---

## Session note — Monday 2026-10-12 (no agentic trade) — owner ACTED on both advisories

9:29 AM CT. Agentic account flat: $948.56, no positions, no working orders. Ledger $948.61 (the
$0.05 exit fee). All-time realized +$349.96.

**Correcting the record: the owner executed BOTH Friday advisories**, which my carry-forward note
had wrongly listed as "not yet acted on."

| Position | Entry | Size | Opened |
|---|---|---|---|
| T Nov 20 $22 put | **$0.79** | **4 contracts = $316.00** | 10/9 12:40 PM CT |
| SOFI Nov 20 $18 call (short) | **-$41.00** credit | 1 contract | 10/9 12:28 PM CT |

The owner took the T put at **4x the size I specced** (I framed 1 contract at ~$82) and got a better fill
than I quoted ($0.79 vs my ~$0.82). At $316 the position is 7.1% of the $4,426 account — inside the
20% cap, so the sizing is defensible.

**But it weakens an argument I used.** I justified the early entry location by writing "$82 is 1.9%
of the account, so a bounce to $23 costs maybe $25." **At 4x that arithmetic is 4x weaker** — a
bounce to $23 now costs roughly $100. The conclusion (sizing makes early entry tolerable) still
holds at 7.1%, but the specific numbers I used to reach it do not describe the position actually
taken. Worth stating plainly so the reasoning is not retroactively credited with more precision
than it had.

### T position status: -15.8%, thesis intact, entry was early as flagged

T **$22.455 (+1.24%)**. Put mark **$0.665** -> 4 x $66.50 = **$266.00** against a $316.00 basis =
**-$50.00 (-15.8%)**; at the bid, -$60 (-19.0%).

**A process point worth keeping:** at 8:32 AM the book was **0.58/0.75 — a 25.6% spread** two
minutes after the open, which would have shown -26.6% and tripped the hard-stop band. By 9:29 it
tightened to 0.64/0.69 (**7.5%**). Refusing to act on the opening print was correct: the
open-auction book is not a valid input to a stop decision. Friday's spread was 3.7%, so 25.6% was
pure noise.

Friday's OFFICIAL close was **$22.18** — above $22.00, so **my agentic trigger never fired.** The
shelf held, which is exactly what the pass predicted, and the owner's position was opened ahead of
the trigger into the mid-shelf location I objected to.

**The sector is bouncing for a second session:** T +1.24%, **TMUS +2.96%**, **VZ +1.96%**. Thesis
stop (close above $24.87) is far away; 39 DTE; theta only -1.6%/day. Nothing to do. The level that
would constitute real damage is **T reclaiming $23.50-24.00** — the top of the shelf and the zone I
had defined as the failed-bounce entry.

**New thesis-negative signal: ASTS +5.1%** to $53.565, bouncing after Friday's -8.0%. ASTS is
satellite-to-phone — if it rallies *alongside* the telecoms rather than against them, the market is
unwinding the entire satellite-disruption trade and reading Friday as an overreaction. That is a
better read on the thesis than T's own price, because ASTS is the pure-play expression of it. Watch
ASTS as the thesis tell.

### BULL: bounce stalled BELOW the trigger zone — not fired, and I am not widening it

Recomputed the EMA off Friday's official $6.31 close rather than reusing the estimate:
EMA = 6.31 x 0.181818 + 6.9202 x 0.818182 = **$6.81**.

BULL topped around **$6.34** and is now **$6.155 (-2.46%)** — it never reached the EMA, stalling
roughly 7% below it.

There is a real argument that a bounce failing *below* a declining EMA is **more** bearish than one
that tags it, and the persona's language ("rejection at the EMA") is about a failed bounce in a
downtrend. But my trigger said "into the EMA," and it did not get there. **Amending a trigger
mid-flight to permit an entry is precisely how discipline erodes**, and I am not doing it. Not
fired. If BULL rolls over from here without tagging $6.81, I will treat the *next* bounce attempt
as the setup rather than rewriting this one.

The Nov 6 book problem is unresolved anyway (39% spread, volume 1), so the trigger question is
partly moot until the premium/spread bind is addressed.

### Board

Gainers (19): nothing tradeable. **WFF +117.6%** on a $515M cap with relvol 0.097 — a micro-cap
pump, hazard territory, skipped without further work. TRAX +7.1% on 4.18x volume (biotech),
CCC +9.6%, MANH +6.9%, SNAP +4.0% — no catalyst worth the effort against a $189.71 cap.

PENG **$77.30 (+1.34%)**, now well above the $2.15-entry level I was stopped out of, gap intact.
SPY $777.89 (-0.09%).

**No agentic trade. Cash is a position.**

---

## Monday, October 12, 2026 — 2:33 PM CT (late-session check)

Prices below are from a live quote at **2:33 PM CT**, ~27 minutes before the bell. Not closes.

### Agentic account 452369101 — flat, reconciled
- Live: total $948.56 | cash $948.56 | buying power $948.56 | no positions | no working orders.
- Ledger: Allocated $948.61 | Open $0.00 | Remaining $948.61 | Realized +$349.96.
- Delta $0.05 = trade #12's exit fee. Reconciled, no action.

### Owner positions — individual ••••1866 (ADVISORY ONLY)

**T Nov 20 2026 $22 put x4** — basis $0.79 = $316.00 (opened 10/9 12:40 PM CT)

| | Price | Value | P&L |
|---|---|---|---|
| Mark | $0.585 | $234.00 | **-$82.00 (-25.9%)** |
| Bid | $0.560 | $224.00 | -$92.00 (-29.1%) |
| Ask | $0.610 | | |

Book: bid 0.56 x63 / ask 0.61 x247. Spread $0.05 = **8.5% of mark** — tight. OI 6,964, volume 2,481.
This is a valid input to a stop decision, unlike Friday's 8:32 AM open-auction print (25.6%).
IV 29.6%, delta -0.373, 39 days to expiry. Morning read was -15.8%; it has roughly doubled the loss intraday.

**SOFI Nov 20 2026 $18 call, SHORT 1** — credit $41.00
- Buy-back $0.305 = $30.50 → **+$10.50** on the call. Delta 0.214, 39 DTE.
- Underlying SOFI $15.2586, **-3.43%** (adj prev close $15.80 = prev close, no corporate action).
- The 100 shares at $18.10 avg are **-$284.14**. Net SOFI package **-$273.64**. The call is doing its job.

### T thesis status — levels intact, but the move today went against the position

T $22.5099, **+1.49%** (adjusted_previous_close $22.18 = previous_close — no corporate action; check complete).

Intraday shape matters more than the close-to-close number:

| Time (CT) | Action | Volume |
|---|---|---|
| 8:30–9:00 | Open $22.255 → **HOD $22.658**, close $22.575 | **3.30M** |
| 9:00–9:30 | Faded to $22.465 | 2.48M |
| 9:30–10:00 | Round-tripped to **$22.2685** — entire gap given back | 1.58M |
| 10:00–2:30 | Ground back to $22.49–22.51 | 0.93–1.33M/bar |

- **$22.00 shelf held** (LOD $22.25). Thesis still needs a break of $22.00 — not close.
- **High of day $22.658.** Nowhere near the $23.50–24.00 "real damage" zone, and far from $24.87 full invalidation.
- The bounce was **sold into**: a full round trip off the high inside 90 minutes on the session's heaviest volume, then a low-volume afternoon grind. That is distribution on a bounce, not accumulation.
- Sector: VZ +2.49% ($42.685), TMUS +2.28% ($151.96). Second straight up session sector-wide.

### ASTS — the thesis tell FAILED its bounce. This is the day's most informative data point.

I named ASTS in advance as the better thesis read than T's own price. Result:

| | Price | Note |
|---|---|---|
| Friday close | $50.965 | after -8.0% |
| 9:29 AM today | $53.565 | +5.1% |
| **HOD (8:30–9:00)** | **$54.670** | +7.3% |
| 2:33 PM | **$51.4496** | **+0.95%** |

ASTS gave back **-5.9% from its high of day** and held barely a point above Friday's close, on an up day for every telecom. Volume front-loaded exactly like T: 3.54M in the opening bar, then 0.30–0.67M.

**Read:** the market is NOT unwinding the SpaceX-disruption trade. Friday's repricing is sticking. The pure play rallied 7% and was sold all day. If this were an overreaction being corrected, ASTS would be the thing that rips — it is the highest-beta expression of the narrative. It didn't.

So today produced a **divergence**: T's price went against the position while the thesis tell confirmed it. Two days of telecom bounce on fading volume with the pure play failing is consistent with an oversold bounce inside a repriced sector, not a reversal.

### The stop decision on the T put — presenting the case

-25.9% on a tight mark is **inside the PERSONA 25–30% hard-stop band** on a single-leg swing. I am not going to launder the PLTR lesson into an excuse here: PLTR was a defined-risk vertical whose mid-life mark is a noisy estimator (it swung 48 points on a 4.9% move). This is a single-leg long put with a two-sided book, 6,964 OI and 2,481 contracts traded. **The mark is reliable and the hard stop genuinely applies.**

**Case to stop now (-$82):**
- The rule exists so I don't rationalize. I am rationalizing-adjacent right now and should say so.
- Entry was into strength — the owner filled at $0.79 at 12:40 PM Friday with T already bouncing. I flagged entry location as the weak part of this advisory and it is now the reason the position is underwater.
- 4x sizing magnified that error. At 1 contract this is -$20.50 and irrelevant; at 4 it is -$82 and 7.1% of a ~$4,400 account.
- Two consecutive adverse sessions on a fresh position.

**Case to hold:**
- Every thesis level is intact. The shelf held, the bounce high was $22.658, and $23.50 is 4.4% away.
- The tell I committed to in advance confirmed the thesis today. That is evidence, not hindsight.
- Volume structure says bounce, not reversal: heaviest print at the high, fading all day, in both names.
- 39 days of time and IV at 29.6% — no decay cliff and no blown-out premium to bleed out of.

**Recommendation: HOLD, with a pre-committed exit line rather than a daily re-judgment.** Exit on whichever comes first:
1. Put marks **≤ $0.55** (-30%, ≈ -$96) on a tight book — the far edge of the band, at a close, not an intraday wick; or
2. **T closes above $23.50** — thesis damage, exit regardless of the premium.

I am explicitly choosing the **loose edge (30%) of a 25–30% band**, and the owner should know that is a choice, not the rule speaking. I'm choosing it because the thesis tell confirmed today and the level structure is untouched. If the owner would rather take -$82 now and re-enter on a failed bounce into the declining EMA with better location, that is a defensible read and I won't argue it — the entry location was my weak spot, not the owner's.

**Nothing here is executable by me. Discretionary sell in ••••1866 is the owner's call, done manually.**

### BULL — trigger still not fired, declined to widen a second time
- $6.26, -0.79% (adj prev close $6.31 = prev close, clean).
- 10-day EMA recomputed off today's price: 6.26 x 0.181818 + 6.81 x 0.818182 = **$6.71** (provisional; recompute on the official close).
- Stock sits **~6.7% below** the EMA. The setup is a weak bounce INTO the declining EMA that stalls. It has not tagged it.
- Trigger NOT fired. Nov 6 book still fails (39% spread, volume 1). If it rolls from here without tagging $6.71, the NEXT bounce attempt is the setup — I am not rewriting this one.

### Owner rulings still outstanding (6)
1. **Defined-risk-spread stop amendment** — spreads exit on thesis invalidation / time / entry-set max loss, never a mid-life mark. Cost $220 on PLTR.
2. **$301.21 funding gap** — unexplained, operationally closed.
3. **SOFI 50-share trim** — now blocked by mechanics: 1 short call covers 100 shares. Selling 50 leaves the call half-uncovered. The call must be closed or rolled first, which costs $30.50 to buy back and gives up the remaining $10.50 of credit. Flagging the interaction, not recommending.
4. **EP-Down breakdown-day half-size amendment** — my recommendation remains **DROP it**. The bounce rule earned its keep Friday and again today.
5. **20% cap** — record unchanged.
6. **Premium/spread bind** — percentage spread scales inversely with premium; the cap pushes toward contracts that fail the spread gate.

### No new trade
Agentic account stays flat. Nothing scanned into a qualifying setup, and I'm not manufacturing one 27 minutes before the bell. Cash is a position.


---

## Tuesday, October 13, 2026 — 6:50 AM CT (premarket news check)

Requested: premarket news. Quote timestamp 11:49:57Z = **6:50 AM CT**, 1h40m to the open.
**The Robinhood news tool is absent from the server's tool list entirely** — not unloaded, absent. All news below is from web search and is disclosed as such.

### Official Monday closes (now settled)

| | Close 10/12 | vs my 2:33 PM read |
|---|---|---|
| T | **$22.49** | $22.5099 |
| VZ | $42.78 | $42.685 |
| TMUS | $151.87 | $151.96 |
| ASTS | $51.46 | $51.4496 |
| BULL | **$6.30** | $6.26 |
| SOFI | $15.23 | $15.2586 |

T closed $22.49. **$22.00 shelf held, HOD $22.658, nowhere near $23.50.** All thesis levels intact.

### THE NEWS THAT MATTERS: Piper Sandler downgraded ASTS, and the stated reason is SpaceX

Overweight → **Neutral**, price target **$98 → $54**. ASTS **$49.40 premarket, -4.00%**.

Piper's cited reasons:
1. Reduced confidence in 2026/2027 satellite **launch pace**.
2. **SpaceX's direct-to-cell push, explicitly including the ~$8B mobile spectrum purchase** — SpaceX could limit launch access for partners like AST, or undercut on price.
3. Still constructive post-2027; argues SpaceX aggression could eventually *increase* operator demand for AST.

**This confirms the thesis rather than contradicting it, and the distinction matters.** Yesterday I wrote that ASTS failing its bounce meant the market was not unwinding the SpaceX repricing. The downgrade is stronger evidence than price action: the sell side is now putting ratings and price targets behind the view that SpaceX's direct-to-cell capability is credible and formidable. A satellite pure-play cut in half on target *because SpaceX is too strong* is not a signal that terrestrial carriers are safe.

**But the counter-evidence is live and I'm not going to bury it:** the carriers are bid premarket while ASTS breaks.

| Premarket | Last | vs close |
|---|---|---|
| T | $22.4386 | **-0.23%** (bid 22.34 / ask 22.50, $0.16 wide) |
| VZ | $43.148 | **+0.86%** |
| TMUS | $153.2769 | **+0.93%** |
| ASTS | $49.40 | **-4.00%** |
| BULL | $6.2514 | -0.77% (bid 6.00 / ask 6.29 — 4.6% wide, garbage) |
| SOFI | $15.20 | -0.20% |

Premarket relative volume is meaningless and these books are thin — standing rule, no conclusions drawn from them. T is flat.

### TWO HARD CATALYST DATES, BOTH INSIDE THE NOV 20 EXPIRY

**1. T reports Q3 earnings Wednesday, October 21, before the open.** Conference call 8:30 AM ET.

**I did not flag this when I specified the advisory on 10/9, and I should have.** Recommending a Nov 20 put without naming a binary earnings event 8 days inside its life is a gap in my own work, not a detail. It changes the position's character:
- The outcome is **idiosyncratic and uncorrelated with the SpaceX thesis**. T can beat on subscriber adds and postpaid churn and rip through $23.50 on numbers that have nothing to do with Starlink.
- IV should rise into the print, which supports the premium modestly.
- Management **will** be asked about Starlink Mobile on the call. The answer is a thesis catalyst in either direction, and it is the one place the two stories collide.
- Practical consequence: the pre-committed exit line has 6 trading sessions to work before the position becomes an earnings bet.

**2. FCC votes October 29 on auctioning spectrum for satellite-to-phone service.** Thesis-aligned, 16 days out, also inside expiry. Separately, SpaceX's Grain Management purchase (up to 14 MHz paired, 800 MHz band) still needs FCC approval — a third pending item with no fixed date.

### Background now filled in on the original catalyst
- FCC cleared SpaceX Oct 7 for up to **15,000** direct-to-phone satellites and **waived** the rule requiring SpaceX to lease airwaves from a carrier.
- Musk claims Starlink Mobile V2 carries **100x** the bandwidth of the current system.
- T, VZ and TMUS formed a satellite/direct-to-device JV last week for underserved coverage — **Starlink notably absent**. That is their defensive answer and it is worth watching.
- Analysts note the network is years out and per-user speed under real load is unproven. That is the bear case against the bear case: a long-dated disruption story does not have to show up in a Nov 20 option.
- One CNBC account puts VZ's Friday close at -8.75%, worst day since July 2002. My own dividend-adjusted figure from live quotes was **-5.69%**; the search itself flags that outlets disagree. I'm keeping my number and not restating theirs as fact.

### No pricing of the T put this morning
Premarket option books are not a valid input and I set that rule myself after the 10/9 open-auction print (25.6% spread would have falsely shown -26.6%). **The put gets priced after the open, on a tight book, against the pre-committed line:** mark <= $0.55 at a close, or T closes above $23.50. Neither can be evaluated at 6:50 AM.

### Other premarket movers — nothing for the agentic account
MU -2.4% on reports of CXMT server-memory architecture (China memory competition). ADBE -1.4%, HSBC to Hold. VFC +3.9% on Piper/Truist upgrades. UNH +2.8% to ~$389 on a raised 2026 profit forecast. All analyst-action or single-headline moves; none is an Episodic Pivot with volume confirmation, and I have not graded any of them. Agentic account remains flat.

### BULL — EMA recomputed off the official close
6.30 x 0.181818 + 6.81 x 0.818182 = **$6.72**. Premarket $6.2514 is **~7% below** it. Never tagged. Trigger not fired, not widened — third time.


---

## Tuesday, October 13, 2026 — 8:48 AM CT (open check) — **STOP TRIGGERED ON THE T PUT**

Quote timestamp 13:48:43Z = **8:48 AM CT**, 18 minutes after the open.

### Agentic account 452369101 — flat, reconciled
$948.56 cash / $948.56 buying power, no positions, **no working orders**. Ledger $948.61; the $0.05 is trade #12's exit fee. Not a gap.

### T put — through the far edge of the band on a TIGHT book

**T Nov 20 2026 $22 put x4** — basis $0.79 = $316.00

| | Price | Value | P&L |
|---|---|---|---|
| **Mark** | **$0.540** | **$216.00** | **-$100.00 (-31.6%)** |
| Bid | $0.520 | $208.00 | -$108.00 (-34.2%) |
| Ask | $0.560 | | |

Book: bid 0.52 x117 / ask 0.56 x8. Spread $0.04 = **7.4% of mark — TIGHT.** Not an open-auction artifact; this is a valid input.
Volume 40 so far (thin this early), **OI 9,002** (up from 6,964 Friday — the contract is accumulating interest). IV 29.6% -> 29.3%, delta -0.355, 38 DTE.

My pre-committed line was "mark <= $0.55 **at a close**." Mark is $0.540. The price threshold is through; the close qualifier is not met at 8:48 AM.

**I am not waiting for the close, and here is why that is not me moving the goalposts.** The close qualifier existed to filter an intraday wick. This is not a wick:
- The book is 7.4% wide with a 117-lot bid. No liquidity distortion.
- -31.6% on mark and -34.2% at the bid are **past the entire PERSONA 25-30% band**, not inside it. Yesterday I explicitly chose the loose 30% edge and flagged that as a choice. The loose edge is now breached.
- The mechanism that justified yesterday's hold has broken (below).
- Waiting until 3:00 PM to re-confirm a number already past my own far edge is precisely the PENG rationalization I wrote a standing correction about.

### The reason I was wrong yesterday: my tell decoupled

Yesterday I held at -25.9% and the single strongest argument I gave was that ASTS failing its bounce confirmed the thesis. Today:

| | ASTS | T |
|---|---|---|
| Mon close | $51.46 | $22.49 |
| 8:48 AM today | **$47.9175 (-6.88%)** | **$22.6006 (+0.49%)** |

**ASTS is down 6.9% and T is up 0.5% in the same 18 minutes.** The correlation that made ASTS a valid proxy for the SpaceX-disrupts-telecom theme is gone. ASTS is trading its own story now — Piper's launch-cadence doubts and the $98 -> $54 target cut — and the market is explicitly NOT extending "SpaceX wins" to "carriers lose." The carriers are being bought: VZ +0.34%, TMUS +1.03%.

**A tell that moves opposite the thing it is supposed to predict is not a tell.** I assigned information to ASTS that it was not carrying, and that misweighting is what produced yesterday's hold. The hold cost $18 (-$82 -> -$100). Small in dollars, but the reasoning error is the thing to record.

### The shelf has now held twice, and that kills the setup

T intraday, 5-min bars:

| Time (CT) | O | H | L | C | Vol |
|---|---|---|---|---|---|
| 8:30 | 22.280 | 22.605 | **22.260** | 22.581 | 543K |
| 8:35 | 22.580 | 22.595 | 22.485 | 22.510 | 352K |
| 8:40 | 22.510 | **22.635** | 22.495 | 22.630 | 384K |

T **gapped down** to $22.28, probed **$22.26**, and reversed to $22.635 inside 18 minutes.

- Monday LOD **$22.25**. Today LOD **$22.26**. Two probes of the same shelf, two sharp reversals.
- The thesis requires a **break of $22.00**. It has not come within 1.2% of it, and the shelf is now a tested double bottom rather than an untested level.
- Third consecutive up session. Opening volume 1.28M/15min is lighter than Monday's 3.30M/30min pace, so this is not a volume thrust — but "it is bouncing on light volume" stops being a bear argument when the bounce has run three sessions and the level you need never got tested.

### RECOMMENDATION: EXIT THE T PUT

Advisory only — this is account ••••1866 and **I cannot execute it; the sell is the owner's to place manually.**

- Sell 4 x T Nov 20 $22P, **limit $0.54** (mid, into a 117-lot bid). Fills at $216.00 → **realized -$100.00 (-31.6%)**.
- If it will not fill, $0.53 → $212.00 (-$104.00, -32.9%). At the bid $0.52 → $208.00 (-$108.00, -34.2%).
- Capital still at risk if held: **$216.00**, against a thesis whose trigger level has held twice and whose tell has decoupled.
- **T reports Q3 before the open Wednesday Oct 21** — 6 sessions away, inside the position, a binary uncorrelated with the SpaceX story. I did not flag this when I specified the trade on 10/9. Holding from here means holding an earnings bet I never priced.

Four things went wrong and only one was the market: entry into strength at $0.79 (my call), 4x sizing on arithmetic I had computed at 1 contract (my error, recorded 10/12), an unflagged earnings date inside the expiry (my omission), and a tell I overweighted (yesterday's hold). The directional read on Friday's catalyst may still prove right after Oct 29 — but this position is not the instrument to express it, and -31.6% is the rule telling me to stop paying to find out.

### Everything else
- **SOFI Nov 20 $18C short 1:** $0.305 to buy back = **+$10.50**, unchanged. SOFI $15.29 (+0.39%); 100 shares at $18.10 = -$281.00. Net package -$270.50. Working as designed, no action.
- **BULL:** $6.33 (+0.48%). EMA **$6.72**. Still ~5.8% below, never tagged. Trigger not fired — fourth session declined to widen it.
- **ASTS** also bouncing off its low intraday ($47.13 -> $48.32), so its own flush is being bought too.
- **Both-direction scan deferred.** The position decision is time-sensitive and I am not burying a stop recommendation under a watchlist. Agentic account stays flat; nothing is being opened without confirmation regardless.

---

## Tuesday, October 13, 2026 — 8:53 AM CT (full /trade session) — **NO TRADE**

Time from a fresh SPY quote: 13:53:17Z = **8:53 AM CT**. SPY $778.30, +0.03% vs the $778.10 close — flat index, themed carnage underneath.

### 1-2. Ledger reconciled
Live broker: total $948.56 | cash $948.56 | **buying power $948.56**. Ledger: Allocated $948.61 | Open $0.00 | Remaining $948.61 | Realized +$349.96.
Delta **$0.05** = trade #12's exit fee. Known, reconciled, not the funding gap.
20% conservative cap = **$189.72**. 40% aggressive cap = $379.44 (requires A+).

### 3-4. Position & stop audit / take-profit duty
**Agentic 452369101: flat.** No positions, no working orders → no stops owed, no take-profit duty. Nothing unprotected.

**Owner's ••••1866 (advisory only):**
- **T Nov 20 $22P ×4** — and **the owner has acted**: a sell order is working, `placed_agent: user`, `agent_initiated: false`, placed 13:52:39Z (8:52 AM CT), **limit $0.54, quantity 1** (not 4). `pending_sell_quantity: 1.0`, processed 0.
  **That is 1 of the 4 contracts I recommended selling, and it is the owner's order — I am not correcting it and did not touch it.** Per PERSONA, an in-app order is the owner's will. Flagging the facts only: it exits a quarter of the position; the other **3 contracts remain unencumbered** (the lock holds only the 1), so they can still be sold manually if he wants. Book at 8:53: bid $0.52 ×32 / ask $0.56 ×8, mark $0.540, spread 7.4%. That $0.54 offer sits $0.02 above the bid, inside the spread — it needs a buyer to come up, and bid size has thinned from 117 to 32 since 8:48.
  Full position at the $0.540 mark: $216.00 vs $316.00 = **-$100.00 (-31.6%)**.
- **SOFI Nov 20 $18C short 1** — $0.295 mark, **$29.50 to buy back vs $41.00 credit = +$11.50 (+28.0% of credit)**. Delta 0.210, IV 55.7%, 38 DTE. SOFI $15.24. 100 shares at $18.10 = -$286.00; net package -$274.50. No change recommended: on a covered call this far OTM, the remaining $29.50 is decay I'd rather collect than pay to close.

### 5. Watchlist trigger status — nothing fired
| List | Trigger | Status |
|---|---|---|
| **EP-Down Watch** (T) | close under **$22.00**, or failed bounce **$23.50-24.00** | **NOT FIRED.** T $22.635. Updated the description today. |
| **BULL** | weak bounce INTO the declining 10d EMA that stalls | **NOT FIRED.** EMA **$6.72**, stock $6.305 — ~6.2% below, never tagged. Declined to widen it a 4th session. |
| Momentum Breakout (PENG) | first pullback $66-70 holding | Retired, not re-enterable. |
| LiDAR & Drone (OUST) | IV cool-off + new base | Thesis dead, puts still blocked (IV ~130%, OI<100). |

### 6. Scans — both directions

**Elapsed-time scaling:** 23 min of a 390-min session = **5.9%** at scan time. A reported relvol of 1.0 is a **~17x** full-day pace. All multiples below are scaled.

**Daily Gainers — Episodic Pivot Watch: 25 items.**

| Ticker | % | Last | Scaled relvol | Verdict |
|---|---|---|---|---|
| BMBL | **+56.8%** | $5.96 | 21x | **DEAL-PINNED — dead** |
| EFXT | +11.8% | $26.93 | **24.5x** | structure without catalyst |
| RZAI | +9.5% | $10.91 | 19x | $556M micro-cap AI, skip |
| MDB | +7.3% | $409.22 | 5.8x | unaffordable |
| INFY/CTSH/GLOB/CNXC/KD/OTEX/WPP | +4-6% | — | 1.1-4.0x | sympathy tagalongs |
| CRM, SMTC, FSLY, FIGS, PBF, HPQ, FIG, LIFE, SDRL | +4-6% | — | 1.5-2.9x | analyst actions, no EP |

**High Options Volume — Smart Money Flow: exactly 1 item, and it was BMBL.** The entire unusual-options-flow signal on the tape today is merger arb. That is the cleanest illustration yet of why this scan cannot be read as institutional accumulation without the catalyst check.

**Daily Losers — Breakdown & EP-Down Watch: 54 items.** Coherent themes, not noise:
- **Crypto miners / AI datacenter:** CIFR -16.9%, APLD -7.3%, IREN -5.6%, CLSK -5.4%, WULF -4.9%, HUT -4.8%, CRWV -4.3%, NBIS -4.7%, RIOT -4.1%, SHAZ -5.0%, WYFI -4.5%, BRUN -4.9%
- **Memory / semis:** STX -5.5%, WDC -5.4%, ACMR -5.4%, SKHY -5.2%, CRDO -5.2%, MU -4.5%, ALAB -4.4%, FLEX -4.3% — the CXMT China server-memory story
- **Space:** ASTS -9.0%, LUNR -4.0%, PL -4.0%
- **Biotech:** SNDX -18.0%, SMMT -6.1%, IBRX -5.1%, LQDA -5.0%, BNTX -4.8%, MRVI -4.7%, TXG -4.5%
- **JNJ -4.4%** on 3.8x — mega-cap, $252.18, premium far past the cap

### THREE MORE CATALYST-CHECK CATCHES — the running count is now NINE

1. **BMBL +56.8% — all-cash acquisition.** Ithaca Holdings, **$6.05/share cash**, $1.3B. Stock $5.96. **Upside permanently capped at $0.09 (+1.5%).** Calls are structurally worthless barring a competing bid. On structure alone this was the single biggest EP on the board with 56.9M shares traded.
2. **CIFR -16.9%, the highest scaled relvol on the losers list (18.7x) — an $850M convertible note offering** plus an exchange of old notes for shares. This is the **UMC pattern**: convert buyers short the stock to hedge delta, producing mechanical selling that stops when the deal prices. A financing event, not the "earnings miss / guidance cut / lost contract" that PERSONA's EP-Down requires. The 90-day chart is a genuine downtrend ($22.11 July 10 → $13.00 Oct 12, -41%), so it belongs on the watchlist — but not bought today.
3. **EFXT +11.8%, the highest scaled relvol anywhere today (24.5x) — and the best *structure* on the board:** Oct 1 gap $22.79 → $25.75 open on 2.10M shares (~5x), then a tight 9-session base $23.47-26.00, now breaking the base high on ~5x pace. That is a textbook Qullamaggie EP-plus-base. **It fails on leg 1: no identifiable catalyst for the Oct 1 gap, and the last reported quarter MISSED both lines** (EPS $0.25 vs $0.31, revenue $582M vs $606.78M est). Structure without a catalyst is precisely the trap the catalyst-first rule exists to catch. Chain exists (Oct 16 / Nov 20 / Dec 18 / Feb 19 / May 21) but I did not price strikes — the setup died upstream of liquidity.

Running tally of flow/structure artifacts the catalyst check has caught: **WBD, SYNA, PTC, OPCH, PCRX (deal-pinned), UMC (convert-arb), BMBL (deal-pinned), CIFR (convert-arb), EFXT (no catalyst) = nine.** This step is not a formality; it is the highest-yield gate in the process by a wide margin.

### FUN — passing, and saying why honestly
Six Flags **-10.7% at $10.64 on 10.5x scaled relvol**, a clean 3-month downtrend ($19.46 → $10.64, -45%) breaking a 2-week bounce. Structurally the best bearish chart on the list.

The catalyst is a **fatal roller coaster accident at a Six Flags park in Georgia** — one person killed, several injured, ride closures across parks. I'm not putting on a position to profit from that. Separately and independently, the trade also fails my rules: a single-incident headline is a legal/PR process with no numbers to anchor a price target or a thesis stop, it is a day-1 flush with IV blown out, and PERSONA's EP-Down wants a catalyst that trends for days-to-weeks off a fundamental trajectory. Both reasons stand on their own.

### The real reason there is no trade: every bearish candidate is a day-1 breakdown
My own 10/6 vindication table settled this empirically — breakdown-day entries on T/VZ gave -5.5% / -14.1% while the failed-bounce entries gave +42.7% / +32.6%. That is why I recommend DROPPING the EP-Down breakdown-day amendment, and it is why I am not buying any of today's 54 losers on day one. The correct action on a themed flush is to write down the bounce trigger and wait for the rejection at the declining EMA.

### And the premium bind again, in its other form
The memory-semi breakdown is the most structurally real move on the tape — a genuine catalyst (CXMT server-memory architecture) with sector-wide breadth. Every name in it is priced out of reach of a $948 account: **MU $944.53, STX $711.97, WDC $366.15, CRDO $190.31, ALAB $309.85.** An ATM put on any of them is multiples of the $189.72 cap. This is outstanding ruling #6 from the other direction: the cap does not only push toward contracts that fail the spread gate, it also excludes the highest-quality setups entirely on share price. Both failure modes come from the same $948 constraint.

### 7-8. Nothing to review, nothing to confirm
No `review_option_order` was run because nothing reached the grading stage with both a catalyst and an affordable, liquid contract. Confirmation mode remains ON; no order was placed in the agentic account.

### 10. NO TRADE — cash is a position
Three scans, 80 rows, three artifacts caught, one setup passed on principle, one real theme priced out of reach. The account stays flat at $948.56. I am not manufacturing a trade on a day whose best long is capped at +1.5% by a merger agreement and whose best short is a fatality.

**Also vindicated:** **WFF -48.1% today** — the $515M micro-cap I skipped Monday at **+117.6%** with relvol 0.097 as a probable pump. It gave back nearly half in one session.

### Proposed seventh owner ruling
**Require an earnings-date check before specifying any option position, and state the date plus whether it lands inside the expiry.** The T put earned this: I specified a Nov 20 put on 10/9 without noting T reports Q3 on **Oct 21, before the open** — a binary uncorrelated with the thesis, sitting 6 sessions inside the position. Not acting on this unilaterally; it is the owner's call like the other six.

### Owner rulings outstanding (now 7)
1. Defined-risk-spread stop amendment (cost $220 on PLTR).
2. The $301.21 funding gap.
3. SOFI 50-share trim — **blocked by mechanics**: 1 short call covers 100 shares, so selling 50 leaves it half-uncovered. The call must be closed or rolled first: $29.50 to buy back, giving up the remaining $11.50 of credit.
4. EP-Down breakdown-day half-size amendment — **recommend DROP**, reinforced again today.
5. The 20% cap.
6. The premium/spread bind — now with a second failure mode (share price excludes the best setups outright).
7. **NEW (proposed):** mandatory earnings-date check before specifying any position.

---

## Tuesday, October 13, 2026 — 9:05 AM CT — individual account review (advisory)

### The 1-contract sell FILLED
Order `6ace37a7`, `placed_agent: user`, filled **$0.54 at 13:53:26Z (8:53 AM CT)**, 1 contract.
**Realized: $54.00 proceeds vs $79.00 basis = -$25.00.** Three contracts remain.

### Full account picture — ••••1866 (margin account)

| | | |
|---|---|---|
| Total value | **$3,785.82** | |
| Cash | **$2,123.82** | **56.1% of the account** |
| Equity | $1,516.50 | 100 SOFI @ $15.165 |
| Options (net) | $144.50 | 3 T puts long, 1 SOFI call short |
| Buying power | $6,365.70 | unleveraged $3,182.85 — **it is a margin account** |

| Position | Basis | Now | P&L |
|---|---|---|---|
| SOFI 100 sh | $18.10 = $1,810.00 | $15.165 = $1,516.50 | **-$293.50 (-16.2%)** |
| SOFI Nov20 $18C short 1 | +$41.00 credit | $28.00 to close | **+$13.00** |
| *SOFI package* | | | **-$280.50** |
| T Nov20 $22P ×3 | $0.79 = $237.00 | $0.575 = $172.50 | **-$64.50 (-27.2%)** |
| T ×1 closed today | $79.00 | $54.00 | **-$25.00 realized** |
| *T total of the original $316* | | | **-$89.50** |

### The remaining 3 puts: the percentage line is NOT triggered right now — say so

Mark **$0.575 = -27.2%**, which is back **inside** the 25-30% band, not through it. My stated line was mark <= $0.55. It isn't. The put rose from $0.540 to $0.575 because T eased from its $22.635 high back to $22.565.

**I am not going to claim the line fired when it didn't.** But the exit recommendation stands, and on the stronger of the two grounds:

PERSONA's **THESIS STOP**: "If the reason you entered is invalidated — stock breaks back below the breakout level, catalyst fizzles, volume dries up — exit immediately **regardless of percentage loss**." All three legs of the entry reason are now gone:
1. The trade needed a **break of $22.00**. T probed $22.25 Monday and $22.26 today and reversed hard both times. Never came within 1.2%. The level is a tested double bottom, not a breakdown candidate.
2. Third consecutive up session, sector-wide.
3. The proxy I used to read the theme **decoupled**: ASTS $46.85, **-8.96%**, while T is **+0.33%**. A tell that moves opposite the thing it predicts is not a tell.
Plus the unpriced binary: **T reports Q3 pre-open Oct 21**, 6 sessions inside the expiry.

The percentage gate is the weaker argument today. The thesis gate is the one that governs, and it does not need -30%.

### NEW: the book depth collapsed — this matters more than the spread %

Bid **$0.55 x1** / ask **$0.60 x641**. Headline spread 8.7% looks fine. **It isn't: there is ONE contract bid and 641 offered.** Volume 85 all day.

That is a one-sided book. Selling 3 contracts into a 1-lot bid fills the first at $0.55 and walks the rest down. **Do not market-sell this.** Post 3 at **$0.57** (just under the $0.575 mark) and let it work; drop to $0.56 if it sits. If only part fills, that is fine — partials beat slippage here.

The depth is also an argument for acting sooner rather than later: liquidity in this contract is thinning while everyone's attention is on earnings, and it will not be better on Oct 20.

### SOFI — hold everything, no action
- The covered call is doing its job: **+$13.00**, delta 0.200, $28.00 of premium left to decay over 38 days. SOFI would need **+18.7%** to $18 to threaten the strike. Collecting the rest beats paying $28.00 to close it.
- **The 50-share trim ruling, updated for a fact I had wrong in emphasis:** this is a *margin* account ($6,365.70 buying power), so a half-uncovered short call is mechanically *possible* — Robinhood would allow it. That does not make it advisable: it converts a covered call into a partially naked call with unbounded upside risk for $13 of remaining credit. If the trim happens, **close the call first ($28.00), then sell the shares.** Still the owner's ruling, not mine.

### Level 3 playbook — no A+ advisory today, and two specific near-misses worth naming

1. **PUT DEBIT SPREAD on the memory-semi breakdown — right structure, wrong day.** MU -4.5% ($944.53), STX -5.5% ($711.97), WDC -5.4% ($366.15), SKHY -5.2%, CRDO -5.2% on the CXMT China server-memory story. This is the most genuinely-catalyzed, broadest move on the tape. A vertical is exactly what fixes the problem here — the obstacle is absolute premium, not IV, and a spread caps the debit. **But a spread fixes cost, not entry timing**, and this is day 1 of the flush. The entry per PERSONA setup #2 is the rejection at the declining 10/20-day EMA. **Flagging the structure now so it is ready if the bounce comes.** No strikes specified, because specifying them on a day-1 flush would be the same error in a nicer wrapper.

2. **PUT CREDIT SPREAD on T — right level, wrong calendar.** T has now defended $22.25/$22.26 twice on volume, the SpaceX catalyst is 3 sessions past, and Nov 20 $22P IV has cooled to 30.2%. That is the shape of the post-event-IV-crush credit spread: sell below a level that already held. **It fails the A+ gate on the event leg** — PERSONA requires "the event to be OVER," and while the SpaceX event is, **T's Oct 21 earnings is a brand-new binary inside the window.** Also worth saying plainly: flipping from long puts to short puts on the same name in the same session, after losing money on the bearish side, is how direction-chasing starts. Not advised.

3. Butterfly: nothing today — no specific price magnet with a specific date.
4. PMCC: not applicable, he owns the 100 SOFI shares (a plain covered call beats a PMCC when the shares are held), and it is already written.

### The 56% cash position is correct today, not idle
Three scans, 80 rows: the best long on the tape is **capped at +1.5% by a merger agreement** (BMBL, Ithaca all-cash $6.05), the top-volume short is **convert-arb hedging** (CIFR's $850M note), the best-structured breakout has **no catalyst** (EFXT), and the cleanest bearish chart is a **fatality** (FUN). Holding $2,123.82 in cash on a day like this is the position, not a failure to find one.

---

## Tuesday, October 13, 2026 — OWNER RULING ADOPTED: the earnings-date check is now in PERSONA

The owner ruled: **include the 7th ruling.** Added to `brain.py` PERSONA as the first bullet of
the **BINARY EVENTS** block (the natural home — that section already governs scheduled prints).
`brain.py` parses clean. This is the first PERSONA change made in this session, and it was made
only on the owner's explicit instruction.

**Rule as written:**
> EARNINGS-DATE CHECK (owner ruling 2026-10-13) — run this BEFORE specifying any position,
> Robbin's own or a personal-account advisory, and state the result in the write-up: find the
> underlying's next confirmed earnings date and say whether it falls inside the chosen expiry.
> Prefer the company's own IR announcement over an estimated date. If it lands inside the
> expiry, do one of three things and say which: pick an expiry that closes before the print,
> size down, or name the print out loud as an accepted risk. Never leave it unsaid. An earnings
> date inside the position is a binary uncorrelated with the setup's thesis — it can invalidate
> a correct directional read on numbers that have nothing to do with it.

Three design choices worth recording:
- **"Before specifying," not "before placing."** The T failure happened at the recommendation
  stage, not the execution stage. Gating on placement would not have caught it, because Robbin
  does not place in the individual account at all.
- **"Confirmed" and "prefer IR over an estimate."** The check is worthless if it accepts a
  scraped estimate. T's Oct 21 came from AT&T's own August 27 release; TipRanks had Oct 28.
- **Three permitted responses, not a prohibition.** Earnings inside an expiry is not
  automatically disqualifying — unsaid earnings is. The rule forces disclosure, not avoidance.

### Running the new rule immediately against the live book — it found something on the first pass

**T Nov 20 $22P x3 (owner, advisory):** Q3 **Wednesday Oct 21, before the open** — AT&T's own
IR announcement, dated 2026-08-27, call 8:30 AM ET. **INSIDE the expiry**, 6 sessions out.
Already flagged this morning; the exit recommendation stands on the thesis stop.

**SOFI Nov 20 $18C, SHORT 1 (owner, advisory) — NOT previously stated, and it should have been:**
Q3 is **UNCONFIRMED**, with sources split: Wall Street Horizon projects **Oct 27 (flagged
UNCONFIRMED)**, ChartRow Oct 27 pre-open, AJ Bell Oct 28; TipRanks and Earnings Whispers say
Nov 2-3. Last year's Q3 landed Oct 28, 2025; Q2 2026 was July 29. Consensus ~$0.17 EPS.
**Every candidate date falls INSIDE the Nov 20 expiry.** Per the rule I am naming it as an
accepted risk rather than recommending a change, and here is the honest read:
- For a *short* call, earnings is the real assignment risk, not theta. $18 is **+18.7%** away
  and delta is 0.200, so a single print would have to be extraordinary — but SOFI is a name that
  moves double digits on prints, and **stops do not protect through gaps.**
- The same print is *why* the $41 credit was available: the call was sold into elevated
  pre-earnings IV (still 55.4%). The structure is not wrong; the date was simply unstated.
- **Action: none.** Hold the covered call. But the date is now on the record, and the owner
  should decide before ~Oct 23 whether he wants to roll it past the print or let it ride.
- **It also constrains the trim ruling further:** closing the call to free 50 shares costs
  $28.00 now and gives up a credit whose main remaining value is the pre-earnings IV. Doing it
  *after* the print would be cheaper. One more reason not to rush that decision.

**Owner rulings outstanding: back to 6.**
1. Defined-risk-spread stop amendment (cost $220 on PLTR).
2. The $301.21 funding gap.
3. SOFI 50-share trim — blocked by mechanics (margin account makes a half-uncovered call
   *possible* but unwise; close the call first), and now also calendar-constrained by the
   late-October print.
4. EP-Down breakdown-day half-size amendment — recommend DROP.
5. The 20% cap.
6. The premium/spread bind, both failure modes.
~~7. Earnings-date check~~ — **ADOPTED 2026-10-13, now live in PERSONA.**

---

## Tuesday, October 13, 2026 — FULL RETROSPECTIVE: 12 closed trades, what went wrong, PERSONA proposals

Owner asked for a look back across the whole book. Nothing below changes PERSONA — these are
proposals. The only PERSONA edit made in this session was ruling #7, on the owner's instruction.

### The record

| # | Trade | Setup | P&L | % |
|---|---|---|---|---|
| 1 | IRDM $55C | Momentum | +$45 | +52.9% |
| 2 | SOFI $18.5C | Catalyst swing | +$10 | +13.5% |
| 3 | GRND $15C | EP base breakout | +$35 | +33.3% |
| 4 | MRNA $65P | EP-Down | +$29 | +18.7% |
| 5 | WULF $18P | EP-Down | +$47 | +42.7% |
| 6 | SLB $53C | Momentum | +$24 | +20.0% |
| 7 | **GDX $85C** | Momentum/Trend | **+$325** | **+130.0%** |
| 8 | OCUL $11C ×2 | Speculative | **-$100** | -62.5% |
| 9 | NXE $12C ×2 | Speculative | -$30 | -30.0% |
| 10 | AMLX $40C | Momentum | +$60 | +30.8% |
| 11 | XPEV $11P ×2 | EP-Down | -$20 | -20.4% |
| 12 | PENG $80C | EP | -$75.04 | -34.9% |

**8-4, 66.7% win rate, +$349.96 realized.** Average win $71.88, average loss $56.26.

### THE HEADLINE NUMBER NOBODY SHOULD MISS

**GDX is +$325 of the +$349.96.** Strip that one trade and the book is **+$24.96 across 11 trades**.
Implied net funding is ~$598.65 ($948.61 allocated less $349.96 realized), so:
- With GDX: **+58.4%**
- Without GDX: **+4.2%** over roughly 3.5 months

And GDX's own post-mortem flags that it rode to +130% with **no session record that the LETTING A
WINNER RUN checklist was ever applied.** So the book's entire profitability rests on one trade taken
off-process. Excluding it, average win drops to **$35.71** against an average loss of **$56.26** — a
**0.63:1** payoff ratio. PERSONA's stated mandate is "lose small and win bigger." The realized
distribution is the inverse of that.

---

## WHAT WENT WRONG — five patterns, each with its dollar cost

### 1. The 30-80% profit band is systematically undershot. **Four of eight winners exited below the floor.**

| Trade | Exit | vs the 30% floor | What the note says |
|---|---|---|---|
| #2 SOFI | **+13.5%** | -16.5 pts | peaked +45%; "the sell decision waited" |
| #4 MRNA | **+18.7%** | -11.3 pts | "just under the band because the ratchet was set tight" |
| #6 SLB | **+20.0%** | -10.0 pts | "BELOW the band — sold early, off-process" |
| #10 AMLX | +30.8% | at the edge | bottom edge, 1-day hold |

Meanwhile losses ran **-20.4%, -30.0%, -34.9%, -62.5%** — the full width of the stop band and past it.
**The band is enforced on the downside and advisory on the upside.** That asymmetry, not the win
rate, is why the book nets +$24.96 ex-GDX on a 67% hit rate.

### 2. Stops do not work on sub-$1.00 contracts, the book proved it with the worst loss, and PERSONA still has the wrong model

**#8 OCUL: stop set at $0.60 (a -25% trigger, correctly inside the rule). It filled at $0.30. -62.5%, -$100.**
PERSONA's BROKER MECHANICS still says: *"assume slippage roughly equal to half the spread when
computing the locked-in floor."* On OCUL the real slippage was **50% of the trigger price.** The
trade's own post-mortem wrote the correct lesson — *"on sub-$1.00 contracts a stop-market is closer
to a suggestion than a floor"* — and **it was never carried into PERSONA.** #9 NXE repeated it
smaller the same week ($0.40 trigger, $0.35 fill).

### 3. Concurrent entries are capped by sector, but the damage came from shared STRUCTURE

**#8 OCUL and #9 NXE were opened 13 minutes apart on 2026-08-17.** Different sectors (biotech,
uranium), so the "max 2 per sector" cap never engaged. Both were sub-$1.00 contracts bought ×2, both
stopped out inside 24 hours, combined **-$130 — 58% of every dollar lost in this book, from one
13-minute decision window.** They were not two trades. They were one bet on thin speculative premium
surviving a session, placed twice.

### 4. Position management, not selection, is where the money goes — and this is now quantified

Entry screening is the strongest part of the system. Nine flow/structure artifacts caught before any
money moved (WBD, SYNA, PTC, OPCH, PCRX deal-pinned; UMC and CIFR convert-arb; BMBL deal-pinned;
EFXT no catalyst), plus VKTX (sizing cap correctly refused an unholdable trade), WFF (skipped at
+117.6%, **-48.1% the next session**), IONQ (retired on its own condition).

Every significant loss, by contrast, is a management failure against a correctly-graded setup:
- **#12 PENG -$75.04.** At +20.9% I declined to ratchet $1.50 → ~$1.85, reasoning tightening would
  stop me out on routine consolidation. **Stopped out anyway at $1.40.** The real choice was $1.85
  vs $1.40. Cost ~$30-40. The thesis was right — PENG closed back above the entry two days later.
- **#2 SOFI.** +45% peak → +13.5% exit, because the decision waited.
- **PLTR advisory, -$220 to the owner.** Applied single-leg percentage-stop math to a defined-risk
  vertical whose mid-life mark swung 48 points on a 4.9% underlying move. Largest single loss
  anywhere in the record, and it was an advisory, so it is not even in the table above.

### 5. THE BIGGEST UNLOGGED FAILURE: I applied a looser standard to the advisory account than to my own

This one is not in the closed-trades table and it should be the headline finding.

On **10/9, in a single session**, I:
1. Graded T **B+** and **PASSED** in the agentic account, on entry location — the gap landed on the
   July congestion shelf at $21.50-22.30.
2. Wrote the discriminator myself: *"Consolidating ON the $21.50-22.30 shelf is a different thing
   from breaking it, **and the trigger is the discriminator between the two.**"*
3. Set the trigger explicitly: **a close below $22.00, or a failed bounce to $23.50-24.00.**
4. Then, **in the same session, with neither trigger fired**, recommended the identical trade in the
   individual account — and justified it on size: *"At $82 it is 1.9% of a $4,426 account, so a
   bounce to $23 costs roughly $25... Position size is what converts 'early' from fatal to tolerable."*

Three things wrong with that:
- **I overrode my own trigger with a sizing argument.** The trigger was the thing I said separated a
  good entry from a bad one. Size does not change where the stock is on the chart.
- **Size makes a bad entry affordable; it does not make it a good entry.** I blurred survivability
  with edge. Those are different claims and I asserted the first to license the second.
- **The arithmetic was computed on 1 contract ($82). I never specified a quantity or a scaling cap.**
  The owner took **4 contracts, $316** — so the "0.6% of the account" bounce cost became ~$100, and
  the position became 7.1% of the account, not 1.9%.

**Outcome: the trigger has still never fired.** T has never closed below $22.00 — it probed $22.25
(10/12) and $22.26 (10/13) and reversed hard both times. The agentic pass was right for three
straight sessions. The advisory, same analyst, same session, looser standard, is **-$89.50** of the
original $316 (-$25.00 realized on the contract sold at $0.54, -$64.50 open on the remaining three).

PERSONA's scope firewall protects the agentic account *from* the advisory section. **Nothing protects
the advisory account from me.**

---

## WHERE PERSONA CAN IMPROVE — 7 proposals, owner's call on every one

### P1. Advisory entries must clear the same trigger as the agentic account, and must name a quantity
Add to PERSONAL ACCOUNT ADVISORY: an advisory may differ from the agentic decision on **structure,
strike, expiry and size** — never on **whether the entry trigger has fired.** If Robbin passes on
entry location or timing, the advisory is a WAIT at the same level, not a BUY at a smaller size.
Every advisory must state an explicit **contract quantity and a do-not-exceed quantity**, because any
sizing-based justification is quantity-dependent and is void if the quantity changes.
*Evidence: the T put. -$89.50 and counting, on a trigger that never fired.*

### P2. Replace the stop-slippage model for low-priced contracts
Amend BROKER MECHANICS: the half-the-spread slippage estimate applies only to contracts above ~$1.50.
**Below ~$1.00, a stop-market is not a floor** — model the realistic fill as roughly half the trigger
price, which means the position must be sized as if **the entire premium is the risk.** If that fails
the 20% cap, the trade is too big. Alternatively don't hold sub-$1.00 contracts overnight at all.
*Evidence: #8 OCUL, -$100, stop at -25% filled at -62.5%. The lesson was written and never adopted.*

### P3. Cap concurrent entries by risk structure, not only by sector
Add to PORTFOLIO RISK CAPS: **maximum one new sub-$1.00-premium contract per session**, and no two
entries in the same session that share a risk structure (thin premium, same-week expiry, top-decile
IV) regardless of sector. Two trades that die to the same market condition are one position.
*Evidence: #8 + #9, 13 minutes apart, -$130 = 58% of all losses.*

### P4. Make an exit below the 30% floor an explicit named exception
Add to TAKING PROFIT: setting a take-profit or ratchet **below the 30% band floor** is an exception
that must be named out loud with its reason, exactly like the liquidity exception. Today the band is
enforced on the stop side and advisory on the profit side, and the record shows it gets undercut in
half of all winners.
*Evidence: #2 +13.5%, #4 +18.7%, #6 +20.0%, #10 +30.8%. Average win ex-GDX $35.71 vs average loss $56.26.*

### P5. The LETTING A WINNER RUN checklist must be written down at the decision, not reconstructed
Add to that checklist: the four legs must be **recorded in the session log at the moment the decision
to ride past 80% is taken.** If it is not written, the 30-80% band applies and the position is closed
in the band. A checklist that can be asserted after the fact is not a gate.
*Evidence: #7 GDX, +130%, +$325 — which is 93% of all profit in the book — with no record the
checklist was ever applied. The outcome was excellent; a repeat without the checklist is a coin flip
that happened to land.*

### P6. Put the two management corrections into PERSONA; they currently live only in trades.md
- **"Once a position is green, the ratchet question is 'where do I want to be out,' never 'how do I
  avoid being taken out.' A stop defines the exit price; it is not there to dodge triggers."**
  *(#12 PENG, ~$30-40.)*
- **Defined-risk spreads exit on thesis invalidation, time remaining, or an entry-set max-loss
  budget — never on a mid-life mark-to-market percentage.** STOP LOSS RULES currently says "25-30% of
  entry cost" with no instrument carve-out, while the advisory section introduces spreads without any
  stop rule of their own. *(PLTR, -$220 — the largest single loss in the record.)*

### P7. CORRECTING MYSELF on the EP-Down bounce rule — the evidence is 1-1, not settled
I have written "recommend DROP the amendment, the bounce rule earned its keep" for several sessions
running. **That overstates it.** The honest tally:
- **Against the bounce rule:** NVO (9/23). The bounce never came. The rule missed **+53%**. And the
  objection was structural, not anecdotal: *"the bounce entry... structurally CANNOT fill on the
  strongest downtrends — the ones that go straight down are exactly the ones that never bounce. The
  rule therefore self-selects into weaker setups and misses the best ones."*
- **For the bounce rule:** T/VZ (10/6). Breakdown-day entries gave -5.5% / -14.1%; failed-bounce
  entries gave +42.7% / +32.6%.

One each. I was weighting the more recent case and calling it resolved.

**A tiebreaker that actually reconciles both, rather than picking one: choose the entry by what lies
beneath the gap.**
- Gap lands **ON identifiable support** (T: the July shelf at $21.50-22.30) → the bounce is likely, so
  **wait** for the break or the failed bounce. T probed that shelf twice and reversed both times —
  exactly the behaviour the rule anticipates.
- Gap lands **in open air**, next support more than ~5-7% below (NVO: nothing until the $35-39 base)
  → the bounce may never come, so a **half-size breakdown-day entry** is justified, with the full-size
  bounce entry kept as the add.

Note this discriminator beats the IV-based one I proposed on 9/23: NVO's put IV was 34% and T's was
30.7%, both cheap, so IV does not separate the cases. **Structure beneath the gap does.** Worth
testing before adoption, but it is the first version of this rule that fits both data points.

---

## WHAT NOT TO "FIX"

The selection gates are the part that works and the temptation after a thin stretch is to loosen them.
Do not. The passes have been right essentially every time: nine flow/structure artifacts caught before
a dollar moved, VKTX correctly refused as unholdable at that size, WFF skipped at +117.6% and down
48.1% the next session, IONQ retired on its own stated condition, BULL's trigger declined four
sessions running.

**The real strategic problem is not the gates, it is the account size.** One agentic position opened
since 9/21 — trade #12, a loss. The $948 budget with a $189.72 cap collides with the gate stack from
both directions: expensive contracts fail the cost cap (MU $944, STX $712, WDC $366 today), cheap ones
fail the percentage-spread gate (BULL's $0.41 premium with an ordinary $0.16 width = 39%). That is
outstanding ruling #6, and it is a bigger question than any rule above: **this account may be too
small to run this process at the frequency that compounds.** That is the owner's call, not mine.

**Owner rulings outstanding: 6 prior + 7 proposed above.** None acted on unilaterally.

---

## Tuesday, October 13, 2026 — 11:09 AM CT (midday check) — owner's 3-lot sell is STALE and unfilled

### Agentic 452369101 — flat
$948.56 / buying power $948.56, no positions, **no working orders**. Ledger $948.61; $0.05 = trade #12's exit fee. Reconciled.

### The owner placed the 3-contract sell at exactly the price I suggested, and the market left it behind

Order `6ace3b0e`, **3 contracts, limit $0.57**, `placed_agent: user`, placed **14:07:10Z = 9:07 AM CT** — two minutes after I recommended $0.57. **processed 0 of 3, still working, GFD.**

It was a fair price when he set it. T has since run another 0.97%.

| | 9:05 AM | **11:09 AM** |
|---|---|---|
| T | $22.565 | **$22.785 (+1.31%)** |
| Put mark | $0.575 | **$0.485** |
| Bid / ask | 0.55 **x1** / 0.60 x641 | **0.47 x128 / 0.50 x127** |
| Spread | 8.7% (one-sided) | **6.2% (two-sided)** |
| Volume | 85 | **444** |

3 contracts, basis $237.00:
- **Mark $0.485 → $145.50 = -$91.50 (-38.6%)**
- Bid $0.47 → $141.00 = **-$96.00 (-40.5%)**

**That $0.57 offer now sits $0.10 above the bid. It is not going to fill at that price today.**

### Two things changed in the owner's favour, and one against

**For:** the book healed. At 9:05 it was bid x1 against ask x641 — I warned against market-selling into that. Now it is **128 up / 127 down with 444 contracts traded**, a genuinely two-sided book that can absorb 3 lots without walking the price. The execution risk I flagged this morning is gone.

**Against:** the position is 11.4 points worse (-27.2% → -38.6%) while the order sat. That is the cost of a limit that the market moved past, and it is the same failure mode as PERSONA's missed-limit re-price policy — which says re-price **once, to no higher than the current mid.**

### RECOMMENDATION: re-price the working order to $0.48. Advisory only — the owner's order, the owner's cancel.

- **Cancel `6ace3b0e` and replace: sell 3, limit $0.48** (just under the $0.485 mark, $0.01 over the bid). → $144.00, **realized -$93.00 (-39.2%)** on the three, **-$118.00 total** across all four contracts.
- Taking the bid at $0.47 instead costs $3.00 more. Not worth chasing; $0.48 into a 128-lot bid should fill.
- **Do not raise the limit hoping for a bounce.** That is the PENG error inverted — the put is falling because the thesis is failing, so waiting for a better exit price means waiting for the thesis to come back, which is the thing three sessions of evidence say is not happening.
- I cannot cancel or replace it. It is `placed_agent: user` and per PERSONA that is the owner's will, not mine to override.

### Thesis status: worse, and now on relative strength

- **T $22.785, a new post-gap high** — above this morning's $22.635 and above Monday's $22.658.
- **SPY is -0.18%.** T is **+1.31% on a down tape.** Relative strength in the name the position is short is additional thesis damage, not noise.
- Levels: **$23.50-24.00 (real damage) is 3.1% away** — not reached. **$24.87 (full invalidation)** — not reached. The thesis needed a close under **$22.00** and T is now 3.6% above it.
- **ASTS $46.945, -8.77%**, while T is +1.31%. Recorded as information only — it is not a tell any more and I am not citing it as confirmation in either direction.

### SOFI — unchanged, hold
$15.12 (-0.72%). Short Nov 20 $18C: mark $0.275, **$27.50 to buy back vs $41.00 credit = +$13.50.** Delta 0.199. 100 shares = -$298.00. Net package **-$284.50**. No action. Earnings (unconfirmed, ~Oct 27-28) remains named as accepted risk per ruling #7; decide by ~Oct 23 whether to roll past it.

### BULL — not fired, fifth session
$6.295 (-0.08%). EMA **$6.72** (recompute on the close). Stock ~6.3% below, never tagged. Trigger not fired; declined to widen it again.

### No new scan
Tape has not changed materially since 8:53 — SPY -0.18%, same themes. This morning's full session stands: no trade. Agentic account flat.

---

## Tuesday, October 13, 2026 — 2:38 PM CT — **T PUT FULLY CLOSED: -$133.00 (-42.1%)**

The T put position is gone. Owner closed all four contracts today, every order `placed_agent: user`.

### The full order sequence

| Order | Qty | Limit | Time (CT) | Outcome |
|---|---|---|---|---|
| `6ace37a7` | 1 | $0.54 | 8:52 placed → **8:53 FILLED** | **-$25.00** |
| `6ace3b0e` | 3 | $0.57 | 9:07 placed → 1:34 PM cancelled | never filled |
| `6ace79a7` | 3 | $0.48 | 1:34 PM → 1:35 PM cancelled | lived 50 seconds |
| `6ace79d8` | 3 | $0.44 | 1:35 PM → 1:35 PM cancelled | lived 27 seconds |
| `6ace79f3` | 3 | **$0.43** | **1:35 PM FILLED** | **-$108.00** |

The owner walked the offer down $0.57 → $0.48 → $0.44 → $0.43 in about 80 seconds and took the fill.

### Final accounting — trade is CLOSED

| | |
|---|---|
| Basis | 4 × $79.00 = **$316.00** |
| Proceeds | $54.00 + (3 × $43.00 = $129.00) = **$183.00** |
| **Realized** | **-$133.00 (-42.1%)** |

Per contract: #1 **-$25.00 (-31.6%)**; #2-4 **-$36.00 each (-45.6%)**.

Execution note, for the record rather than as criticism: $0.43 was about $0.05 under the $0.48 I
recommended at 11:09 and roughly $0.02 under where the contract marks now ($0.450, bid $0.44 ×43).
The walk-down cost roughly **$15.00** versus a filled $0.48. That is the price of certainty on a
position whose thesis had failed, and it is a reasonable thing to pay. The account is flat. **This is not
treated as an error — it is the owner's execution, and getting out beat optimizing the last nickel.**

### POST-MORTEM — T Nov 20 2026 $22 put ×4 | EP-Down (SpaceX spectrum) | **-$133.00 (-42.1%)** | GRADE: D

**Entry:** $0.79 ×4 = $316.00, 10/9 12:40 PM CT (owner-executed, my advisory).
**Exit:** $0.54 ×1 (10/13 8:53 AM), $0.43 ×3 (10/13 1:35 PM).

**Thesis:** SpaceX's ~$8B Grain Management low-band spectrum purchase plus FCC clearance for up to
15,000 direct-to-cell satellites = a funded new entrant attacking a three-player oligopoly. T fell
-6.37% (dividend-adjusted) on 10/9 with sector breadth and ~7x volume pace. The catalyst was real,
and it is still real — this was never a deal-pin or a flow artifact.

**What killed it, in order of blame:**

1. **I recommended an entry my own trigger had not authorized. This is the whole trade.**
   In the same 10/9 session I graded T **B+ and PASSED** in the agentic account on entry location —
   the gap landed on the July congestion shelf at $21.50-22.30 — wrote *"the trigger is the
   discriminator"* between consolidating on the shelf and breaking it, set that trigger at **a close
   below $22.00 or a failed bounce to $23.50-24.00**, and then recommended the same trade in the
   individual account with **neither condition met**, justified on size: *"At $82 it is 1.9% of a
   $4,426 account."* **The trigger never fired, all week.** T probed $22.25 (Mon) and $22.26 (Tue),
   reversed hard both times, and closed higher three sessions running. The agentic pass was right
   every single day the advisory was losing money.

2. **The sizing argument was arithmetic on one contract, and I never named a quantity.**
   "$82, 1.9% of the account, a bounce to $23 costs maybe $25." The position taken was **4 contracts,
   $316** — so the bounce cost ~$100 and the position was 7.1% of the account, not 1.9%. The
   justification did not survive the scaling, and I had written no do-not-exceed line.

3. **Size makes a bad entry affordable; it does not make it a good entry.** I asserted survivability
   and used it to license edge. Those are different claims. The entry was poorly located at 1
   contract and poorly located at 4; only the damage scaled.

4. **I never flagged T's Oct 21 earnings**, sitting 6 sessions inside a Nov 20 expiry. Fixed today as
   owner ruling #7, now live in PERSONA.

5. **I over-weighted a proxy.** ASTS failing its bounce on 10/12 was the strongest argument I gave
   for holding at -25.9%. The next morning ASTS was -6.88% while T was +0.49%, and today ASTS closed
   around -8.1% while T ran +1.71%. The correlation that made it a tell was gone; it was trading
   Piper Sandler's downgrade on its own story. **A tell that moves opposite what it predicts is not a
   tell**, and leaning on it is what produced the one-day hold that cost $18 before the real exit.

**What was right:** the catalyst work (real, verified, share counts reconciled, dividend adjustment
caught and corrected), the instrument selection (every liquidity gate passed — OI 9,002, spread
3.7% at entry, IV 31%, theta -1.2%/day), and **the agentic pass**, which held correctly for four
straight sessions while the advisory bled.

**The lesson in one line:** this was not a bad read of the market. It was a good read entered at a
location I had myself ruled out, at a size I had not specified, under a standard I applied only to
the account I do not control.

**Thesis status: CLOSED and retired.** The SpaceX story may still be vindicated by the FCC's Oct 29
satellite-spectrum vote, but **this instrument is done and I am not re-pitching it.** Any future T
expression starts from a blank grade with the Oct 21 print priced in up front.

### Where that leaves things at 2:38 PM CT

**Agentic 452369101:** flat — $948.56, no positions, **no working orders**. Ledger $948.61; the $0.05
is trade #12's exit fee. Reconciled. **The T loss does NOT touch this ledger** — it was an advisory
trade in the individual account. Agentic realized P&L remains **+$349.96**.

**Individual ••••1866:** T is closed. Only SOFI remains.
- 100 shares @ $18.10, SOFI **$15.20** → **-$290.00**
- Short Nov 20 $18C: $28.50 to buy back vs $41.00 credit = **+$12.50**, delta 0.205
- **Net SOFI package -$277.50.** Hold. No action.
- Earnings (unconfirmed, most likely Oct 27-28) is inside the expiry — named as accepted risk under
  ruling #7. **The roll-or-ride decision wants making by ~Oct 23**, and the 50-share trim is cheaper
  after the print than before it.

**T levels, now academic for the position but kept for the record:** **$22.875, +1.71%**, a new
post-gap high, while SPY is +0.04%. The trade needed a close under $22.00 — T finished 3.9% above it.
$23.50-24.00 is 2.7% away; $24.87 full invalidation is untouched.

**ASTS: $47.29, -8.10%.** Information only. Not a tell, not cited as confirmation.

**BULL: $6.325 (+0.40%).** EMA $6.72 → recomputing on this close gives roughly **$6.65**
(6.325 × 0.181818 + 6.72 × 0.818182), provisional until the official print. Stock ~4.9% below.
**Trigger NOT fired — sixth session, and I have declined to widen it every one of them.**

**No new trade.** Agentic account closes the day flat and 100% cash, which is where it started.

---

## Wednesday, October 14, 2026 — 8:49 AM CT (full session) — **NO TRADE**

Time from a live SPY quote: 13:49:16Z = **8:49 AM CT**, 19 minutes in. Elapsed 4.87% of the session, so the relvol scaling factor today is **×20.5**.

### Ledger reconciled
Broker: $948.56 total / $948.56 buying power, **no positions, no working orders**. Ledger: $948.61 | Open $0.00 | Remaining $948.61 | Realized **+$349.96**. Delta $0.05 = trade #12's exit fee. 20% cap = **$189.72**.

### SOFI — EARNINGS DATE NOW CONFIRMED, and ruling #7's IR-over-estimate preference earned its keep immediately

**Q3 2026: Tuesday, October 27, 2026.** Release ~7:00 AM ET, call 8:00 AM ET. **Confirmed on SoFi's own IR site**, announced via Nasdaq on Sept 29.

That settles a spread the third-party calendars could not: Wall Street Horizon had Oct 27 flagged *unconfirmed*, ChartRow Oct 27, AJ Bell Oct 28, and **TipRanks and Earnings Whispers were wrong at Nov 2-3**. Ruling #7 says prefer company IR over a scraped estimate; had I taken the TipRanks date I would have believed the print fell outside a decision window it actually sits well inside. **8 trading days out, inside the Nov 20 expiry.**

**Position, repriced:**

| | | |
|---|---|---|
| Short Nov 20 $18C ×1 | credit $41.00 | **$22.50 to buy back → +$18.50 (+45.1% of credit)** |
| | | bid $0.22 ×629 / ask $0.23 ×744, delta **0.171**, IV 57.8%, 37 DTE |
| 100 shares @ $18.10 | SOFI **$14.795 (-2.92%)** | **-$330.50 (-18.3%)** |
| **Net package** | | **-$312.00** |

**Recommendation: hold the call now, close it on or before Monday Oct 26.** Advisory only; I cannot execute there.
- 45.1% of the credit captured in 5 of 42 days is ahead of schedule, and $18 is now **21.7% away** at delta 0.171. There is ~$22.50 of premium and ~8 sessions of decay left worth harvesting.
- But carrying a short call **through** the print for the last few dollars is precisely the "unprotected paper gain into a coin-flip" PERSONA's BINARY EVENTS rule exists to prevent, and **stops do not protect through gaps.** The rule's 24-hour trigger binds on Oct 26; I would rather act a day early than discover the gap.
- **Rolling is not the answer.** The next monthly after Nov 20 is Dec 18 — rolling collects more premium but extends exposure for a position whose job (income on dead money) is already 45% done.
- **The 50-share trim is now clearly cheaper after Oct 27 than before it:** closing the call costs $22.50 today, and post-print IV crush should make it cheaper. One more reason that ruling can wait.

Separately and without pushing: the **shares are now -18.3%** and SOFI has fallen every session this week. Whether to hold the equity at all is the owner's call, not a covered-call question.

### Scans — 15 gainers, **93 losers** (vs 54 yesterday), 1 smart-money name

**The breadth number is the headline.** 93 names down >4% while SPY is only **-0.29%** ($775.78). Yesterday it was 54. The index is masking a broadening liquidation.

**Themes on the losers list:**
- **Financials cracking on earnings:** BAC **-7.63%** (9.2x scaled), STT **-7.38%** (5.4x), PGR **-9.50%** (5.1x), SHG -4.73%. Earnings season has begun and the reactions are negative.
- **AI / datacenter, second day:** CRWV **-12.27%** (12.2x), NBIS -8.08% (8.0x), DELL -6.89%, ORCL -6.13%, SMCI -4.61%, HPE -4.82%, CLS -4.60%, AAOI -4.33%, VST -4.39%
- **Crypto miners, third day:** IREN -7.28%, WULF -6.06%, APLD -5.61%, CORZ -5.61%, HUT -4.92%, CIFR -4.89%, RIOT -4.38%, CLSK -4.14%
- **Semis:** WOLF -8.40%, MXL -5.71%, NVTS -5.70%, AOSL -4.22%, ASX -4.05%, SMTC -4.02%, FLEX -4.04%
- **Precious metals selling as a complex:** MUX, NG, SA, CDE, HL, EQX, SKE, SSMR, NEWP, SCZM. Gold miners going down *together* is a liquidation tell, not a rotation.
- Old names behaving as retired: **IONQ -4.64%** ($33.12, retired at $40 — correct call), **PENG -6.70%** ($72.96), **ASTS -5.26%** ($44.591), **FUN -4.40%** ($9.75, still falling after the accident).

### THE CANDIDATES — all three graded and all three passed

**1. LQDA +29.3% at $34.67 — real catalyst, broken chart. PASS, grade C+.**
$380.7M global settlement with United Therapeutics resolving six lawsuits and securing YUTREPIA for PAH. 18.2x scaled relvol on 6.77M shares. This is **not** a deal-pin or a flow artifact — the catalyst is genuine and the relief is real. But the 90-day chart kills it:

| | |
|---|---|
| Jul-Sep 29 | ranged **$65-91** |
| **Sept 30** | open $70.54 → **close $30.26 on 22.95M shares (-57%)** — the Delaware ruling found UTHR's patent valid and infringed |
| Oct 1-13 | consolidated $25.76-30.86 |
| Today | $26.81 → **$34.67**, after a $38.68 premarket high |

- This is a **relief bounce inside a destroyed chart**, not an Episodic Pivot to new highs. The stock is still **51% below where it traded two weeks ago.** PERSONA's momentum setup wants new 52-week highs; this is the opposite pole.
- **The gap is already being sold:** $38.68 premarket → $34.67 now, **-10.4% off the high, 19 minutes in.** Buying a breakout candle that is actively failing is the PENG error.
- **Liquidia is PAYING, not receiving:** $175M due within 30 business days plus two $72.7M installments by early 2027, against a ~$2.0B market cap. That is ~19% of the cap in cash out the door. **A follow-on equity raise is a live risk** — and today's VSTM is the template for exactly that.
- Day-after-a-29%-litigation-gap IV will be enormous, which is the call-side mirror of the put-IV gate.

**2. VSTM +8.6% at $8.09 — ARTIFACT #10. PASS.**
Highest scaled relvol anywhere today by a wide margin: 2.910 reported → **59.7x pace**, 9.98M shares on a $675M cap. On structure alone it is the single most volume-confirmed name on the board.

**It is a $250M equity offering priced at $8.00 — 30,937,500 shares, closing Oct 15.** The stock is $8.09. The volume *is* the distribution. Same family as CIFR's $850M convertible and UMC's convert-arb: **a financing event wearing volume confirmation as a costume**, with price anchored at the deal price.

The accompanying "catalyst" does not survive inspection either: initial VS-7375 Phase 1/2 data showing a 50% confirmed ORR in 2L PDAC — **4 of 8 patients.** n=8 is not PERSONA's "genuinely significant" catalyst, and the company monetized it with a $250M raise the same day. Raising into your own good news is information.

**Running artifact count: ten** — WBD, SYNA, PTC, OPCH, PCRX (deal-pinned), UMC and CIFR (convert-arb), BMBL (deal-pinned), EFXT (no catalyst), **VSTM (equity offering)**.

**3. GFS +5.35% at $49.20 — no catalyst, range-bound, earnings inside the expiry. PASS.**
7.8x scaled relvol on a $26.0B cap, affordable underlying. But:
- **No identifiable Oct 14 catalyst.** Searching turned up a vague TSMC-linked AI deal and an "FDX Fusion" item, both undated, and a report that GFS *fell* 3.4% yesterday.
- Chart is a two-week chop: $67 in July → $43.54 (Sept 15) → $50.99 (Oct 2) → range $46.22-51.45 since. Today is a bounce **inside** the range, below the Oct 2 high. The Oct 8 volume spike (10.47M, high $51.45) already failed once.
- **Ruling #7: GFS reports Q3 on November 4** — inside a Nov 20 expiry. Flagged as required; moot since the setup fails anyway.

**4. SKYD -22.65% at $7.17 — UNRESOLVED, and recorded as unresolved rather than guessed.**
The scanner reports a **$46.7B market cap** down 22.65% on 9.1M shares (7.0x scaled). **Two separate searches could not identify this security or any catalyst** — results suggest Skydance merged with Paramount and trades as PSKY. I have a live conflict between the scanner and every news source I can reach. An unexplained 22% move in a nominally $46.7B company is exactly where artifacts live, so the catalyst gate fails by default. Not traded, not explained, logged honestly as a gap in my data rather than filled in with a guess.

**5. Smart Money Flow: 1 item — KNSL**, 5.67x relative *options* volume but relative share volume 0.048 → **1.0x scaled**, price **-0.84%** at $337.115. Positioning with no move, and over the cap. Same shape as the CON hit on 10/9. Pass.

### BULL — not fired, and now moving away
Tuesday's official close **$6.31**. EMA recomputed: 6.31 × 0.181818 + 6.72 × 0.818182 = **$6.6455 ≈ $6.65**. Stock **$6.20 (-1.74%)** → **6.7% below** and widening, not converging. It is rolling over without ever having tagged the EMA, so per my own rule **the NEXT bounce attempt is the setup.** Trigger not fired, seventh session, not widened.

### NO TRADE — and the tape is the reason, not timidity
15 gainers and 93 losers. The best long on the board is a relief bounce 51% below its own two-week-old price, already fading 10% off its high, by a company that owes $175M in cash within 30 business days. The highest-volume name anywhere is a share offering. The one semi that moved has no catalyst and earnings inside the expiry. The only smart-money hit is positioning without a move.

**Agentic account stays flat at $948.56, 100% cash.** On a day when breadth is collapsing underneath a flat index and earnings season is starting badly, cash is the position.

---

## Wednesday, October 14, 2026 — 2:37 PM CT (close check) — **400 LOSERS. Revising the SOFI call to CLOSE NOW.**

### The tape: this became a liquidation
**SPY $769.09, -1.15%** — it was -0.29% at 8:49 AM. And the losers scan went **54 (Tue) → 93 (this morning) → 400 now.**

Mega-caps being liquidated, not drifting:

| | | |
|---|---|---|
| SKYD | **-24.70%** (adjusted) | $46.7B |
| CRWV | -16.05% | $42.9B |
| DELL | -11.57% | $364B |
| NBIS | -10.96% | $56.2B |
| CIEN | -10.30% | $56.8B |
| AFRM | -10.09% | $26.3B |
| **ORCL** | **-9.00%** | **$434.1B** |
| BE | -9.00% | $77.6B |
| FLEX | -9.33% | $41B |
| CLS | -9.16% | $44.8B |
| HOOD | -8.81% | $99.4B |
| LITE | -8.61% | $89.5B |

A 9% day in a $434B company is not a rotation. **This is the AI-infrastructure/datacenter complex being sold, plus fintech.** The agentic account sat through it 100% in cash, which is the system working rather than luck.

### SOFI — I am REVISING my own recommendation: close the call NOW, not Oct 26

**SOFI $14.150, -7.15%.**

| | | |
|---|---|---|
| 100 shares @ $18.10 | $1,415.00 | **-$395.00 (-21.8%)** |
| Short Nov 20 $18C | $15.50 mid to buy back vs $41.00 credit | **+$25.50 (+62.2% of credit)** |
| | bid $0.15 ×711 / ask $0.16 ×433, delta **0.128**, IV 60.2%, volume 6,473 | |
| **Net package** | | **-$369.50** |

**Action: buy to close 1 SOFI Nov 20 $18C, limit $0.16.** Fills immediately into that book. Realized **+$25.00 (+61.0% of credit)**; at the $0.155 mid it is +$25.50.

**Why I am changing my mind, stated plainly.** This morning I said hold until Oct 26. That was wrong on my own rules:
- **62.2% of the credit captured is squarely inside the 30-80% band**, and PERSONA says of the band: *"take profit in the 30-80% gain range and exit. Don't get greedy."* The band does not say "wait for the far edge."
- **Tuesday's retrospective named this exact failure as the single biggest leak in the whole book** — "the band is enforced on the downside and advisory on the upside," with four of eight winners exiting below the 30% floor because the exits were undisciplined. Having identified that two days ago, holding a winner *inside* the band for 8 more sessions to squeeze maybe $5-8 more — into an earnings print — would be the same error wearing a different hat.
- Delta is **0.128** with the strike **27.2% away**. The remaining $15.50 is almost pure time value; there is very little left to harvest and the only way to lose it is an event.
- Closing now also frees all 100 shares immediately, so **the 50-share trim ruling becomes mechanically unblocked today** rather than after Oct 27.

Advisory only — I cannot execute in ••••1866.

Separately, said once: the **shares are now -21.8%** and SOFI has fallen every session this week. That is a question about holding the equity, which the covered call does not answer.

### Today's names — the record

| | 8:49 AM | 2:37 PM | Read |
|---|---|---|---|
| **LQDA** | $34.67 | **$33.60** (+25.3% on day) | **Fade continued** — now **-13.1% off the $38.68 premarket high.** The C+ pass held. No equity-raise announcement yet; still watching, since $175M is due within 30 business days. |
| **VSTM** | $8.09 | **$7.905** | **Confirmed precisely. It is now BELOW the $8.00 offering price.** A stock that cannot hold its own deal price is distribution, not demand. Artifact #10 stands. |
| **GFS** | $49.20 | **$49.14** (+5.22%) | Flat since the open, still inside the $46.22-51.45 range. Pass stands. |
| **ASTS** | $44.591 | **$42.405 (-9.90%)** | Information only. Third straight heavy down day. Not a tell, not cited. |

### SKYD — RESOLVED, and it is the corporate-action rule's best day yet

It is **Paramount Skydance Corp**, renamed to SKYD after the Warner Bros. Discovery merger closed Oct 7. The catalyst is a **warrant distribution**: one warrant per Class B share held Oct 5, **strike $12**. Today is the ex-warrant date. If all **471 million** warrants were exercised that is ~**$5.65B** raised and heavy dilution, on top of **$78.9B pro forma net debt**.

**Running the rule properly, because this is exactly what it is for:**

| | |
|---|---|
| `previous_close` | **$9.27** |
| `adjusted_previous_close` | **$9.0763** |
| Adjustment | **$0.1937** — the warrant detaching |
| Scanner's unadjusted move | **-26.11%** |
| **True adjusted move** | **-24.70%** |

**And here is the honest nuance, which matters more than a clean "artifact" label:** the check caught a **1.4-percentage-point overstatement**, so the number I reported this morning was wrong and is now corrected. But unlike the T/VZ ex-dividend case, **the adjustment does not explain the move** — $0.19 of a $2.42 decline. **The remaining 24.7% is genuine dilution repricing.** So this is a real catalyst, not a phantom.

Which makes it a textbook EP-Down candidate — **and PERSONA explicitly forbids today's entry:** *"Never buy puts after a -20% single-day flush with IV blown out — that trade is over."* -24.70% in one session. **Pass, and watch for the bounce into the declining EMA.**

### BULL — broke $6, now 10% below the EMA
**$5.985 (-5.15%)**, through $6.00. EMA **$6.65** → stock is now **10.0% below** and widening fast. It is rolling over decisively without ever having tagged the EMA, which is precisely the case my own rule covers: **the NEXT bounce attempt is the setup, not this one.** Provisional EMA on tonight's close ≈ **$6.53**. Trigger not fired, seventh session, not widened — and the gap is now wide enough that widening it would be absurd.

### Agentic account — flat, and that was the right call
$948.56 / $948.56 buying power, no positions, **no working orders**. Ledger $948.61 ($0.05 exit fee). Realized **+$349.96**.

**No trade.** On a day with 400 names down more than 4%, ORCL -9% on $434B, and the one high-volume gainer trading below its own offering price, cash is not caution — it is the position. **Tomorrow's posture: a third broadening day, now confirmed at the index level, argues for staying flat regardless of what any single chart looks like.** More bank earnings land Thursday.

**Running artifact count: ten confirmed** (WBD, SYNA, PTC, OPCH, PCRX deal-pinned; UMC, CIFR convert-arb; BMBL deal-pinned; EFXT no catalyst; VSTM equity offering), **plus SKYD as a partial** — a real catalyst whose headline percentage the corporate-action check corrected by 1.4 points.

---

## Thursday, October 15, 2026 — 8:48 AM CT (full session) — **NO TRADE. Posture rule governs.**

Time from a live SPY quote: 13:47:46Z = **8:48 AM CT**, 18 min in. Elapsed 4.6%, so today's relvol scaling factor is **×21.7**.

### Ledger reconciled, account flat
Broker $948.56 / $948.56 buying power, no positions, **no working orders**. Ledger $948.61 ($0.05 = trade #12's exit fee). Realized **+$349.96**. 20% cap **$189.72**.

### THE MACRO IS THE STORY, and it reframes the whole week

**Wednesday's CPI came in hotter than expected**, reviving Fed rate-hike fear. Wednesday closed Dow -49, **S&P -1.1%, Nasdaq -1.9%.** October hike odds spiked to ~58% intraday post-CPI before settling back near 30%.

**The AI-capex unwind has gone global: Nikkei -5%, Kospi into a bear market**, with money flowing into Treasuries.

That single frame explains every piece of this week's tape — the AI-infrastructure liquidation, the bid in staples/insurance/pharma, and the bid in homebuilders and mortgage names (a bond rally is a rate-sensitive rally). **This is a macro regime event, not a stock-picking tape.**

### Breadth: better than Wednesday's close, nowhere near stabilized

| | Tue | Wed 8:49 AM | Wed close | **Thu 8:48 AM** |
|---|---|---|---|---|
| Losers >4% | 54 | 93 | **400** | **195** |
| Gainers >4% | — | 15 | — | **74** |
| SPY | — | -0.29% | **-1.15%** | **-0.42%** |

**Morning to morning the losers roughly doubled: 93 → 195.** My own posture test from last night was explicit — grade normally only if *losers back under ~100 AND SPY positive AND mega-caps bid*. **All three fail.** Third straight day of the same complex being sold:

RKLB **-13.18%** ($37.8B), NBIS -10.11%, IREN -9.29%, AAOI -9.09%, VG -8.93%, DELL -8.79%, LITE -8.70%, HPE -7.86%, BE -7.83%, SMCI -7.52%, CRWV -7.45%, FIX -7.45%.

**So the posture rule governs and I am not grading entries today.** I wrote that instruction specifically so a clean-looking chart could not talk me out of cash on this tape, and it is doing its job.

*Data note: BIO.B showed -28.1% with relvol 0.000 — a thin B-share class on a stale print, not a real move. Excluded.*

### ARTIFACT #11 — and the highest-relvol name on the board was merger arb again

**PAG (Penske Automotive) +8.46% at $211.26** had **53.2x scaled relvol**, far and away the heaviest on the tape.

**It is a take-private: $212.00 per share in cash, ~$16.3B, Motown Acquisition Corp (Penske Corporation + Mitsui & Co.).** Stock $211.26 against a $212.00 deal price → **upside capped at $0.74, or +0.35%.**

That is the second time a deal-pin has presented as the single most volume-confirmed name on the board (BMBL on 10/13 was the first). **Running count: eleven** — WBD, SYNA, PTC, OPCH, PCRX, BMBL, **PAG** (deal-pinned), UMC and CIFR (convert-arb), EFXT (no catalyst), VSTM (equity offering), plus SKYD as a partial.

**And it corrects a read I was about to commit.** The gainers list showed SAH +8.69%, GPI +6.73%, ABG +6.40%, LAD +6.32%, AN +5.54%, KMX +4.22% alongside PAG, and I was going to call the whole group a defensive rotation. **The search found no broad auto-dealer rally — PAG is deal-specific.** The most likely explanation for the rest is **read-across: the group being re-rated on one deal's multiple.** That is a sympathy move off an M&A print, which PERSONA disqualifies outright ("the strongest name in the move, not a sympathy tagalong") — and here the "strongest name" is pinned at $212 by contract. **The entire top of the gainers list is downstream of a single merger.**

The genuinely defensive part of the rotation is real and separate: staples (CPB +5.47%, CAG +5.06%, GIS +4.83%, KMB +4.06%, SFM +4.46%), insurance (BRO +4.70%, MRSH +4.56%, AJG +4.20%, ERIE +4.33%), pharma (AZN +4.20%, TAK +4.16%), and rate-sensitives (LEN +4.22%, NVR +4.03%, RKT +5.08%, PFSI +4.74%). All low-beta, mostly high-priced, and structurally poor option candidates at a $189.72 cap.

**Smart Money Flow: 1 item — CMBT**, 2.15x relative *options* volume with price **-3.21%** and share relvol scaling to only 3.0x. Positioning on a down move, no thrust. Pass.

### SOFI — the call is still open, and a full session of waiting produced nothing

No orders placed yesterday or today; the short call is still on.

| | | |
|---|---|---|
| Short Nov 20 $18C | **$15.50 to buy back vs $41.00 credit** | **+$25.50 (+62.2%)** |
| | bid $0.15 ×356 / ask $0.16 ×406, delta **0.129**, IV 59.7% | |
| 100 shares @ $18.10 | SOFI **$14.245 (+0.18%)** | **-$385.50 (-21.3%)** |
| **Net package** | | **-$360.00** |

**The useful new fact: it closed Wednesday at $0.16 and marks $0.155 now. A full trading session of waiting earned approximately $0.00** — SOFI ticked up just enough to offset theta. That is the concrete version of the argument I made yesterday: there is very little left in this contract and the only thing that can still move it meaningfully is the **Oct 27 print (confirmed, SoFi IR, ~7:00 AM ET release)**, 7 trading days out and inside the Nov 20 expiry.

**Recommendation unchanged, stated once: buy to close 1 contract at a $0.16 limit → +$25.00 realized.** 62.2% of the credit is inside the 30-80% band PERSONA says to take rather than squeeze. Closing also frees all 100 shares, unblocking the trim ruling. Advisory only.

### Carry-overs — recorded, not re-graded
- **SKYD $7.055** vs a $7.06 close — **flat. It stabilized the session after the warrant went ex**, which is what a mechanical adjustment does once it is absorbed. Stays on EP-Down watch; entry is the failed bounce into the declining EMA only, never the flush.
- **LQDA $34.085** (closed $33.94). Holding its settlement gap but still ~13% under the $38.68 premarket high and ~51% below its pre-ruling level. No equity raise announced yet; $175M is still due within 30 business days.
- **VSTM $7.85** (closed $7.71) — **below its $8.00 offering price for a second session.** The offering closes today. Artifact #10 confirmed twice over.
- **BULL $5.95 (-1.98%).** EMA recomputed off the official **$6.07** close: 6.07 × 0.181818 + 6.65 × 0.818182 = **$6.54**. Stock **9.0% below** and still rolling over without ever having tagged it. **Trigger not fired, eighth session, not widened.** Per my own rule the NEXT bounce attempt is the setup.
- **ASTS / T**: ASTS information only; T closed and retired, not re-pitched.

### NO TRADE
The heaviest-volume gainer is capped at +0.35% by a merger agreement, the rest of the gainers list is sympathy to that same deal or low-beta defensives priced past the cap, the only options-flow hit is positioning on a down move, and the losers list doubled overnight inside a global AI unwind triggered by a hot CPI print. **Agentic account stays flat at $948.56, 100% cash.** That is the posture the tape earns, not caution for its own sake.

---

## Thursday, October 15, 2026 — 12:03 PM CT (manual /trade) — **NO TRADE. VSTM graded properly and failed on the book.**

Time from a live SPY quote: 17:03:43Z = **12:03 PM CT**. Elapsed 54.6% of the session → relvol scaling factor **×1.83**.

### Ledger reconciled, account flat
Broker $948.56 / $948.56 buying power, no positions, **no working orders**. Ledger $948.61 ($0.05 = trade #12's exit fee). Realized **+$349.96**. 20% cap **$189.72**.
`CronList` is empty — it tracks a different mechanism than my Routines. The 2:38 PM CT check-in (`trig_01B2yLJrgEcj3gTHnByXgCWm`) is still armed.

### THE OWNER CLOSED THE SOFI CALL — the individual account is now options-flat

Order `6ad10771`, buy to close 1 contract, **executed $0.18 at 17:03:45Z = 12:03 PM CT** (same minute as this session's opening quote). `placed_agent: user`. The owner first posted $0.18 (`6ad10734`), cancelled, re-posted at $0.19, and filled at $0.18.

| | |
|---|---|
| Credit collected | **+$41.00** |
| Cost to close | **-$18.00** |
| **Realized** | **+$23.00 (+56.1% of credit)** |

**Honest note on the timing, stated once and not belabored:** my recommendation yesterday afternoon and again this morning was a **$0.16 limit for +$25.00**. SOFI rallied **+2.34%** this morning, lifting the call from $0.155 to $0.18, so waiting from the first recommendation cost **$2.00**. The decision to take 56% of the credit rather than hold into the Oct 27 print was the right one and he made it; the $2 is noise and worth recording only because the whole argument I made was *that waiting earns nothing*. It earned -$2.

**Consequences:**
- **All option positions in ••••1866 are now zero.** The 100 SOFI shares are unencumbered.
- **The 50-share trim ruling is mechanically unblocked** — no call to close or roll first. Stating that as a fact; I am not pushing the trim.
- Shares: 100 @ $18.10 → SOFI **$14.5529 (+2.34%)** = **-$354.71 (-19.6%)**. All-in SOFI package including the call: **-$331.71**.
- The Oct 27 print is now irrelevant to an option position and matters only to the shares.

### Breadth: the tape turned at the index level, but the liquidation is in day three

| | Wed AM | Wed close | Thu AM | **Thu 12:03 PM** |
|---|---|---|---|---|
| Gainers >4% | 15 | — | 74 | **301** |
| Losers >4% | 93 | 400 | 195 | **136** |
| SPY | -0.29% | -1.15% | -0.42% | **+0.01%** |

**Gainers now outnumber losers better than 2:1** — a real improvement, and SPY has clawed back to flat from -0.42%.

**But the AI-infrastructure complex is still being sold for a third consecutive session:** RKLB **-11.00%** ($37.8B), MTSI -10.51%, DELL -8.69%, COHR -7.06%, ASX -7.06% ($102.2B), VRT -6.93%, TER -6.61%, P -7.41%. The index is flat *because the rotation nets out*, not because selling stopped.

Against my own morning test (losers under ~100 AND SPY positive AND mega-caps bid), **two of three still fail.** So the posture softens from "do not grade" to **"grade, but the bar stays high"** — and I did grade the one name that earned it.

### VSTM — the setup finally qualified. The option book does not. PASS.

**And I need to correct my own call from Wednesday.** I labeled this **artifact #10** — a $250M offering priced at $8.00 with the stock at $8.09, the volume being distribution rather than demand. That read was **right for two sessions** ($7.85-8.09, below the deal price) and is **wrong about the outcome**. The offering closed today, the overhang cleared, and the stock broke out:

| | |
|---|---|
| Sept 24 - Oct 13 | consolidated **$7.32-8.60**, a three-week base |
| Oct 13 | $7.45 close (offering leak) |
| **Oct 14** | open $8.00, **low $6.70**, **high $8.955**, close $7.71 on **33.76M shares** (~13x the ~2.5M baseline) |
| **Now** | **$9.115, +18.2%** — through the $8.955 Oct 14 high, through the $8.645 Sept high, and **$1.11 above the $8.00 deal price** |

That is a **breakout to a 3-month high on the whole 90-day chart**, which is a different thing from distribution. The mechanism I described was real; the conclusion I drew from it was too strong. **Recording it as a partial artifact, not a clean one.**

**A methodology catch worth keeping:** the scanner showed VSTM **relvol 0.204 → 0.37x scaled, i.e. below normal.** That is wrong. Back out the denominator: 6.87M / 0.204 ≈ **33.7M implied average** — the 30-day average is contaminated by yesterday's single 33.76M offering print. Against the true pre-event baseline of ~2.5M/day, today's 6.87M at 54.6% elapsed is a ~12.6M full-day pace, or **~5x**. **Standing refinement: the session after a volume explosion, the scanner's relative-volume denominator is polluted — compute from raw volume against the pre-event baseline instead of trusting relvol.**

**Setup grade on the chart: B+/A-.** Real catalyst (VS-7375 Phase 1/2 KRAS G12D, 50% confirmed ORR in 2L PDAC — though **n=8**, which I still weigh against it), $250M raise **complete** so the balance sheet is funded and the dilution is behind it, tight three-week base, breakout on ~5x volume holding above the breakout level.

**Then the instrument killed it. Every Nov 20 call fails:**

| Strike | Mark | Bid/Ask | Spread % | OI | Vol | Delta | IV | Cost | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| $8 | $1.800 | 0.10 / 3.50 | **188.9%** | 143 | 2 | 0.696 | 116% | $180 | FAIL spread, OI, vol, delta |
| **$9** | **$0.975** | **0.65 / 1.30** | **66.7%** | **4,740** | **249** | **0.558** | **86%** | **$97.50** | **FAIL spread, delta** |
| $10 | $0.650 | 0.30 / 1.00 | **107.7%** | 161 | 1 | 0.412 | 90% | $65 | FAIL spread, OI, vol |
| $11 | — | 0.00 / 2.90 | no bid | 67 | 0 | 0.029 | 32% | — | FAIL everything |

The **$9 strike is the only one with real depth** — OI 4,740, volume 249 — and its **spread is 66.7% of mark**. The liquidity exception rubric tops out at **25%** and requires OI > 1,000 plus size at the cap plus a mid limit. **66.7% is 2.7x past even the exception ceiling.** There is no reading of the rubric that permits it. Delta 0.558 is also fractionally over the 0.55 band edge, and **IV at 86-116%** is exactly the "buying expensive premium" PERSONA warns against.

*Data note: the $11 call shows `mark_price` $1.45 against a $0.00 bid and 0.029 delta — a broken/stale mark. Not a real quote.*

**This is outstanding ruling #6 — the premium/spread bind — in its purest form yet. The chart finally cleared every gate and the book was untradeable.** Not a near miss on conviction; a hard structural fail.

**Ruling #7 applied:** VSTM's Q3 date is **NOT confirmed** and the sources conflict — TipRanks says **Nov 11** (self-labeled an estimate), CNBC says **Nov 2 (est)**. Q2 landed Aug 6 and Q1 May 7, both ~5 weeks post-quarter, pointing to early November. **Either date falls inside a Nov 20 expiry, and the chain offers no expiry between Oct 16 and Nov 20**, so "pick an expiry that closes before the print" was not even available. Moot given the book fails, but the check ran and is on the record.

### Rest of the board
- **RGC +30.33% at $10.57 on a $4.01B market cap** — Regencell Bioscience, 2.2x scaled relvol. A multi-billion valuation on a micro-revenue TCM company with a known pump profile. Pass without further work.
- **PAG $211.305 against the $212.00 take-private** — **confirmed capped**, as called this morning. Artifact #11 behaving exactly as a deal-pin does.
- **LQDA $34.95 (+2.98%)** — holding the settlement gap. Still no follow-on raise announced; $175M remains due within 30 business days.
- **SKYD $7.215 (+2.19%)** — stabilized for a second session after the warrant went ex. Promoted onto the EP-Down watchlist (description updated), **failed-bounce-into-the-declining-EMA entry only, never the flush.**
- **T retired.** Watchlist description rewritten to replace the dead T thesis with SKYD.

### BULL — first session it has CONVERGED on the EMA instead of widening
**$6.175 (+1.73%)**, back above $6.00. EMA **$6.54** (recomputed off the official $6.07 close). Stock is now **5.6% below** — against 9.0% yesterday and 10.0% Wednesday. **This is the first convergence in the whole sequence.**

The setup is a weak bounce INTO the declining EMA that stalls and rolls over. It is now approaching that zone for the first time. **Trigger still NOT fired — eighth session — and not widened.** If it reaches ~$6.50 and stalls on fading volume, that is the setup and I will price the book then. The Nov 6 chain failed at a 39% spread on volume 1; Oct 23 / Oct 30 / Nov 13 get checked if it triggers.

### NO TRADE
One name earned a full grade today and it failed on an untradeable options book, which is the honest reason — not conviction, not the tape. The agentic account stays flat at **$948.56, 100% cash.**

---

## Thursday, October 15, 2026 — 12:12 PM CT — LEVEL 3 ADVISORY REVIEW (individual ••••1866)

Owner asked whether there is anything for the individual account, Level 3 included. Worked all four
playbook structures. **One dated recommendation, and one finding that the playbook needs amending for.**

### Account state
Options: **zero** (the owner closed the SOFI call at $0.18 this morning, +$23.00). Equity: **100 SOFI @ $18.10
avg, now $14.5529 = -$354.71 (-19.6%)**, fully unencumbered. All-in SOFI package **-$331.71**.

---

## VSTM — I checked whether a spread fixes it. It does not, and the reason matters.

The Level 3 trigger is specific: flag an advisory when a setup grades well **"but fails Robbin's rules
for a REASON A SPREAD FIXES"** — the named case being IV spiked past the buying gate. VSTM looked like
a perfect fit: chart graded B+/A-, and **IV 86-116%** is exactly the OUST/AVAV problem.

**So I priced every vertical. They are all worse than the single leg I already rejected.**

Full Nov 20 call book, live:

| K | mark | bid | ask | spread % | OI | vol | delta | IV |
|---|---|---|---|---|---|---|---|---|
| $7 | $2.350 | 1.95 | 2.75 | 34.0% | 55 | 0 | 0.831 | 102% |
| $8 | $1.800 | 0.10 | 3.50 | **188.9%** | 143 | 2 | 0.696 | 116% |
| **$9** | **$0.975** | **0.65** | **1.30** | **66.7%** | **4,740** | **249** | 0.558 | 86% |
| $10 | $0.650 | 0.30 | 1.00 | **107.7%** | 161 | 1 | 0.412 | 90% |
| $11 | — | **0.00** | 2.90 | **no bid** | 67 | 0 | 0.029 | 32% |
| $12 | — | **0.00** | 2.85 | **no bid** | 1 | 0 | 0.023 | 43% |

Verticals at **realistic** fills — buy the ask, sell the bid, because you do not get the mid on a
contract with volume 0-2:

| Spread | Debit | Width | Max gain |
|---|---|---|---|
| $9/$10 | **$1.00** | $1.00 | **$0.00** |
| $7/$9 | **$2.10** | $2.00 | **-$0.10** |
| $8/$10 | **$3.20** | $2.00 | **-$1.20** |
| $9/$11, $9/$12 | — | — | **cannot be opened — short leg has no bid** |

At mids the $9/$10 reads a tidy 2.08:1. **At fillable prices it pays the entire width for zero upside.**
The two wider spreads cost *more than they can ever be worth*. And the strikes you would actually want
to sell — $11, $12 — **have no bid at all**.

### THE FINDING, and a proposed eighth amendment

**The Level 3 playbook assumes the failure mode is expensive premium. VSTM's failure mode is an empty
book — and a multi-leg structure strictly worsens that, because you cross the bid/ask twice instead of
once.** A spread converts an IV problem into a width problem. It cannot convert a liquidity problem
into anything but a bigger liquidity problem.

**Proposed P8 (owner's call, not acted on):** add a gate to the PERSONAL ACCOUNT ADVISORY section —
*before* flagging any multi-leg structure, verify the short leg has a real two-sided market and price
the structure at **realistic fills (buy the ask, sell the bid), never at mids**. If the structure is
only attractive at mids, it is not attractive. A spread fixes IV; it never fixes depth.

**VSTM is a PASS for both accounts.** Same conclusion, now tested against the structure that was
supposed to rescue it rather than assumed.

---

## The other three structures, worked honestly

**2. BUTTERFLY** — needs "a specific target AND a specific date, not a general direction." Nothing on
the board has one. **PAG** is the only name with a hard price anchor ($212.00 take-private) and that is
precisely why options there are a theta donation: the stock will sit at $211-212 until the deal closes
and every long option decays against a pinned underlying. **Pass.**

**3. CREDIT SPREAD** — "post-event IV crush: sell a put spread below defended support right after a
binary event resolves. A+ requires the event to be OVER and the level to have already held on volume."
Two candidates, both failing:
- **SKYD $7.215.** The warrant event *is* over and ~$7.00 has now held two sessions. But selling puts
  here would be **directionally opposite to my own EP-Down watchlist entry on the same ticker** — I have
  it flagged as a short candidate on 471M warrants at a $12 strike against $78.9B pro forma net debt.
  Writing puts under a name I am watching for a breakdown is incoherent. **Pass, and the contradiction
  is the reason.**
- **LQDA $34.95.** The settlement is over and the gap has held three sessions. But the level is the gap
  itself, not a tested shelf, and **Liquidia owes $175M in cash within 30 business days** — a follow-on
  equity raise is live risk, which is the worst thing that can happen under a short put. **Pass.**

**4. PMCC** — explicitly excluded by the playbook: "only flag when the owner does NOT already own 100
shares." The owner holds them. **Not applicable.**

---

## THE ONE RECOMMENDATION: re-write the SOFI covered call AFTER Oct 27, not before

This is the genuine idea on the board, and it has a date.

**Why it works.** The owner holds 100 unencumbered SOFI shares at an $18.10 basis against a $14.55 tape —
dead money he has already decided to hold. The last covered call turned that into **+$23.00 in six
days.** Writing another is the same trade.

**Why the date is the whole point.** **Q3 earnings are CONFIRMED for Tuesday, Oct 27** (SoFi's own IR,
~7:00 AM ET release, 8:00 AM ET call). Writing a call *into* the print is what I advised against
yesterday, and it would be inconsistent to turn around and recommend it now. **Writing it the day
after** is the opposite trade and is structurally the better one: post-event IV crush is exactly
condition #3 of the playbook, and a short option is the side that *benefits* from the collapse in
implied volatility rather than paying for it.

**The plan, to execute on or after Wednesday Oct 28:**
- Sell 1 covered call, **Dec 18 expiry** (Nov 20 will be ~3 weeks out by then — too little premium).
- **Strike selection rule, not a fixed number:** pick the strike with delta **0.20-0.30** (the last one
  was 0.264 at open and worked), OI > 1,000, spread < 15% of mark. Do not reach for premium by going
  closer to the money.
- **Do not price it now.** IV will reprice completely through the print; today's chain tells you nothing
  about Oct 28's. I will price it that morning.
- **The trade-off, stated plainly:** a call at a $16-17 strike caps recovery on the shares at that
  level. With the basis at $18.10 that would still be exiting below cost if assigned. That is the cost of
  the income, and it is the owner's call whether dead money earning 2-3% per six weeks beats keeping the full
  upside on a position that has fallen every session this week.

**Also now unblocked, as a fact and not a push:** with no call against the shares, the **50-share trim
ruling** can be executed any time. It costs nothing to wait for the print either.

### Nothing else qualifies
Of 301 gainers and 136 losers, the only name whose chart earned a full grade was VSTM, and it fails for
both accounts on a book that no structure repairs. **No advisory flagged beyond the dated SOFI plan.**

---

## Thursday, October 15, 2026 — 12:20 PM CT — TECH SWEEP. **ERIC is the best setup of the week and it fails ruling #6 by 7 points.**

Owner asked specifically about tech. Pulled every tech name off both scans (301 gainers / 136 losers) and graded the affordable ones. Elapsed 57.7% → relvol scaling **×1.73**.

### The tech tape is cleanly bifurcated, and it fits the macro frame exactly

**SOLD — the entire semicap and hardware complex, not just AI-datacenter:**
| | |
|---|---|
| Semicap equipment | AMAT **-4.16%** ($354B), LRCX **-5.25%** ($359B), TER -6.61%, KEYS -6.38%, ONTO -7.07%, FORM -7.94%, ACMR -7.85%, COHU -8.33%, AEIS -8.11%, ENTG -4.88%, MKSI -4.58%, UCTT -4.84%, ICHR -4.16%, ACLS -4.31% |
| Analog / RF / specialty | SMTC **-14.19%**, MTSI -10.51%, AXTI -10.11%, MXL -8.56%, SITM -8.28%, IMOS -7.73%, LSCC -7.35%, AMKR -4.69%, NVTS -4.70%, ASX -7.06% ($102B) |
| Mega-cap semis | AMD **-4.24%** ($932B), INTC -4.24% ($519B) |
| Optical / networking | COHR -7.06%, AAOI -6.14%, LITE -5.54%, **ANET -6.25% ($246B)** |
| Hardware / infra | DELL -8.69%, HPE -6.42%, VRT -6.93%, FLEX -5.91%, CLS -5.46%, SMCI -4.95%, PLXS -4.69% |
| Software | NET -4.54% |

**BOUGHT — software and IT services:**
APPN **+10.72%**, QNT +10.14%, ERIC **+9.20%**, KD +7.76%, TTD +6.61%, INTU +6.25%, GLOB +6.05%, INFY +5.57%, EPAM +5.30%, ADSK +5.40%, HUBS +5.38%, NCNO +5.36%, PRGS +5.26%, FDS +5.00%, CTSH +4.88%, AGYS +5.10%.

**That is a rotation *within* tech — out of capex-heavy semis and hardware, into asset-light software and services.** It is the same hot-CPI / AI-capex-unwind frame, one level down.

### Affordability screen kills most of it immediately
Of the names being bought, only **ERIC $10.46** and **INFY $12.12** are cheap enough for a near-ATM option to fit under the **$189.72** cap. APPN $42.57, EPAM $120.71, INTU $329.85, ADSK $243.63, HUBS $238.40, FDS $304.22 — all out on premium. Same bind, every day.

### INFY — my 10/13 read is now CONFIRMED, not inferred. PASS.
On 10/13 I passed on the IT-services cluster as **sympathy tagalongs to an overseas earnings cycle** (HCL Tech / TCS Q2 lifting Nifty IT), not leaders. Checked it properly today:
- **Infosys has NOT reported. Q2 FY27 is October 23** — board meets Oct 22-23, results and a possible interim dividend after. So today's +5.57% is **not its own catalyst**; it is the third session of sympathy to the Indian IT tape. The leadership test was right.
- **The overhang got worse, not better:** the **US Department of Labor has HALTED new and pending PERM filings for Infosys amid federal probes**, with zero certified PERM filings Oct 2025 - Jun 2026.
- **Ruling #7:** earnings **Oct 23 is inside a Nov 20 expiry**, 6 sessions out, with a guidance revision as the central question.
Three independent reasons to pass. **PASS.**

### ERIC — a real Episodic Pivot, the cleanest ruling #7 outcome possible, and it still fails the book

**Catalyst (verified, and it is genuinely significant):** Q3 reported **today** — adjusted EBITA **SEK 10.1B vs SEK 7.93B expected (+27% beat)**, net sales **SEK 59.5B vs SEK 55.4B expected**, **organic growth +7%**, Networks (the largest segment) **+9% to SEK 38.7B**, plus an announced simplification of the operating structure.

**Ruling #7 — the best possible answer:** the print is **BEHIND** the position, not inside it. Next report is Q4 in late January, well outside a Nov 20 expiry. This is the first candidate all week where the earnings check comes back clean rather than as an accepted risk.

**Corporate-action check complete:** `adjusted_previous_close` **$9.58** = `previous_close` **$9.58**. No adjustment. The +9.20% is real.

**Chart (90 days):** $11.72 on July 13 → gapped down July 14 → ground down to **$9.035 (Oct 1)** → based **$9.035-9.62 for two weeks** → Oct 13 pushed to $9.71 on 18.1M (2.5x) → **today $10.4615**. That is a genuine base breakout on an earnings catalyst, and at $10.4615 it has **cleared the August-September congestion highs ($10.39 Aug 25, $10.44 Sept 17)**. Volume relvol 1.358 → **2.3x scaled**, inside PERSONA's 2-5x band. IV **29.4%** — not inflated, which is rare on an earnings day.

**Then the book:**

| K | mark | bid × size | ask × size | width | spread % | OI | vol | delta | IV | 1× cost |
|---|---|---|---|---|---|---|---|---|---|---|
| $9 | $1.500 | 1.40 ×**1065** | 1.60 ×194 | $0.20 | 13.3% ✓ | **120** ✗ | **31** ✗ | null | null | $150.00 |
| **$10** | **$0.675** | **0.60 ×1409** | **0.75 ×135** | **$0.15** | **22.2%** ✗ | **624** ✓ | **116** ✓ | **0.718** ✗ | **29.4%** ✓ | **$67.50** |
| $11 | $0.200 | 0.15 ×1239 | 0.25 ×81 | $0.10 | **50.0%** ✗ | **158** ✗ | 334 ✓ | 0.328 ✗ | 29.7% | $20.00 |
| $12 | — | **0.00** | 0.10 | — | no bid ✗ | 22 ✗ | 505 | 0.035 ✗ | 22.8% | — |

**The $10 strike is the trade and it fails by one gate.** Spread **22.2%** against a 15% requirement. The exception rubric permits up to 25% — but **only if OI > 1,000, and OI is 624.** So the flex is not available and this is a hard pass, not a judgment call. Delta 0.718 is also outside the band (that one *would* be permissible, since every OTM strike fails the OI test, which the rubric explicitly allows).

### THIS IS OUTSTANDING RULING #6, AND IT IS NO LONGER THEORETICAL

I flagged on 10/9 that **percentage spread scales inversely with premium**: "a $0.16 bid/ask is ordinary market-making width, but on a $0.41 premium it is 39%." ERIC is the cleanest possible demonstration:

- The width is **$0.15** — one normal increment on a $10 underlying.
- The depth is **1,409 contracts bid against 135 offered.** This is not an illiquid contract. It is a *cheap* contract with an ordinary absolute spread.
- A 15% gate on a $0.675 premium means a **maximum $0.10 width** — tighter than the market makes on most sub-$1 contracts at any liquidity level.
- With 1,409 on the bid, the realistic round-trip friction is nearer **$0.05-0.07**, not the $0.15 the quoted percentage implies. **Percentage spread off the quoted bid/ask overstates friction when the book is deep, because you fill near the mid.**
- Size would have been trivial: **2 contracts at $0.675 = $135.00, or 14.2% of the account** — comfortably inside the 20% cap, which is the other condition the exception wants.

**I am passing because the rule says pass and I do not override PERSONA unilaterally.** But this is the strongest single piece of evidence yet that the 15%/25%-of-mark spread gate is mis-specified for low-premium contracts, and the owner now has a concrete case with real numbers rather than an abstraction. **A possible fix, for the owner to rule on: measure the spread gate in absolute ticks or against book depth, not purely as a percentage of mark — e.g. allow a spread up to the greater of 15% of mark or $0.10, provided the bid depth exceeds 10x the intended position size.** On ERIC that would have been 1,409 against 2 contracts.

### Bearish tech — nothing entered, one name to the watchlist
**SMTC -14.19% at $137.52** on **2.5x scaled relvol** is the heaviest tech breakdown on the board. It fails on both counts: it is a **day-1 flush**, which my own 10/6 table says to skip in favour of the failed bounce into the declining EMA, and at $137.52 a put is far past the cap. The whole semicap complex has the same problem — **AMAT $428, LRCX $271.85, TER $335.70, KEYS $334.82, ONTO $224.34, ANET $183.21** are all unaffordable. Adding SMTC to the EP-Down watch with the standard bounce-entry condition.

### NO TRADE
The best tech setup of the week — real catalyst, cleared base, 2.3x volume, 29.4% IV, affordable underlying, earnings already behind it — **passes every gate except one, and the one it fails is the rule the owner already has an open ruling on.** That is the honest answer. Agentic account stays flat at **$948.56**.

---

## Thursday, October 15, 2026 — 12:27 PM CT — LARGE-CAP LEVEL 3 SWEEP + **you doubled SOFI**

Owner asked for a Level 3 trade worth doing, on larger stocks. Two things to report: a position change
I found while auditing, and the sweep itself.

### FIRST — the SOFI position doubled and I did not know until now

Order `6acfe661`, **BUY 100 SOFI at $14.2199**, filled **Wed Oct 14 at 20:30:25Z = 3:30 PM CT**,
extended hours, `placed_agent: user`.

| | |
|---|---|
| Position now | **200 shares @ $16.16 average** (was 100 @ $18.10) |
| Cost | $3,232.00 |
| Value at $14.6299 | $2,925.98 |
| **Unrealized** | **-$306.02 (-9.5%)** |

The original 100 are **-$347.01**; the new 100 are **+$41.00**. Averaging down moved the percentage from
-19.6% to -9.5% and the dollar loss improved by $41 because the adds are green.

**Rule check, stated once:** PERSONA's "NEVER AVERAGE DOWN" is written about *options* — "Options expire.
Adding to a loser compounds the damage." Shares have no expiry and no theta, so this is not a rule
violation. It is the owner's call, made in-app, and I treat it as the owner's will.

**Two consequences that matter:**
1. **200 shares = TWO covered calls** after Oct 27, not one. The income plan I specified doubles.
2. **Cash is now $812.66**, down from $2,123.82. Total account $3,735.66; buying power $5,165.73 on
   margin, $2,582.87 unleveraged. **20% conservative cap = $747.13.** A defined-risk spread of a few
   hundred dollars fits; much more does not.

---

## THE LARGE-CAP SWEEP — and the gate that killed almost everything was earnings

The AI-capex / semicap complex is the only large-cap group with a real, broad, verified catalyst right
now. The owner's account can reach these names through defined-risk spreads where mine cannot touch them on
premium. So I ran ruling #7 across the group first, because a Nov 20 expiry is the only sensible swing
window and the whole sector reports inside it:

| Name | Price | Today | Earnings | Inside Nov 20? |
|---|---|---|---|---|
| **VRT** | $207.39 | -6.93% | **CONFIRMED Oct 28**, pre-open | **YES** — fails |
| **ANET** | $183.10 | -6.31% | **CONFIRMED Nov 3**, post-close | **YES** — fails |
| LRCX | $271.85 | -5.25% | late Oct | YES — fails |
| TER | $335.70 | -6.61% | late Oct | YES — fails |
| AMAT | $428.06 | -4.16% | mid-Nov | YES — fails |
| **DELL** | **$462.37** | **-10.15%** | **~Nov 24 (NOT confirmed)** | **NO — a Nov 20 expiry closes before it** |

**DELL is the only large-cap in the complex where ruling #7's first and best response — "pick an expiry
that closes before the print" — is actually available.** Every other name forces you to accept an
earnings binary inside the position, which is the exact mistake the T put taught.

**The caveat, and it is load-bearing:** Dell has **not** confirmed the date. MarketBeat estimates
**Tuesday Nov 24**, and Dell's FQ3 call last year was Nov 25 — a consistent late-November pattern. But
ruling #7 prefers company IR over an estimate, and **if Dell announces anything earlier than Nov 20 the
entire argument collapses.** That has to be re-checked before any entry.

### But DELL is not a trade TODAY, and the reason is my own proposed P7

DELL, 90 days: ranged $369-494 through July-August → **Sept 2 earnings gap** (opened $462.05, closed
$492.20 on **36.7M shares**) → ran to **$595.51 (Sept 18)** → held $536-595 for a month → **Oct 14 broke
it, closing $507.93** → **today $462.37.**

| Move | |
|---|---|
| Oct 13 close → now | **-19.2%** |
| Sept 18 high → now | **-22.4%** |

**And look where it stopped: $462.37, against the Sept 2 gap open of $462.05.** It has retraced the
entire post-earnings advance and is sitting **exactly on the gap origin**, with the Sept 1 pre-earnings
low at **$421.89** a further 8.8% below.

That is **support, not open air** — which is precisely the discriminator I proposed as **P7** on Tuesday:
*gap lands ON identifiable support → wait for the break or the failed bounce; gap lands in open air →
half-size breakdown-day entry.* By my own rule, **DELL says WAIT.** It is also day 2 of a violent flush
with IV blown out, and buying long premium into that is the OUST/AVAV problem.

### So why not sell premium instead? Because the event is not over.

Structure #3 (credit spread) exists for **post-event IV crush** and requires *"the event to be OVER and
the level to have already held on volume."* Neither holds:
- The CPI print is past, but **the AI-capex unwind is actively running** — day 3-4, and it has gone
  global (Nikkei -5%, Kospi into a bear market). Selling premium into an in-progress liquidation is
  picking up pennies in front of it.
- DELL is **touching** $462 for the first time today. It has not "already held." A level is support when
  it has been tested and rejected, not when price first arrives.

### HONEST ANSWER: no A+ Level 3 trade right now. The problem is timing, not candidates.

Every setup in the group is 2-4 days late into a flush that is still moving — the worst moment for both
sides of premium. **Long premium: IV too high. Short premium: direction still running.** That is not a
trade, it is a coin flip with a spread on it.

### THE PLAN — DELL Nov 20 put debit spread, trigger-based, to arm not to place

Specified now so it is ready, priced at the trigger because today's IV tells you nothing about the
trigger day's.

**Trigger — either one:**
- **(a) A decisive close below $421.89** (the Sept 1 pre-earnings low — that breaks the whole gap and
  puts it in open air, which flips P7 to "go"), **or**
- **(b) A bounce to $505-525** (the Oct 14 close / broken range floor) **that stalls and rolls over** —
  the failed-bounce entry, which is the better of the two.

**Structure at trigger:** Nov 20 **put debit spread**, long strike near the money, short strike ~8-10%
below. Why a vertical rather than a single leg: IV will still be elevated, and **selling the lower strike
recovers the inflated premium** — condition #1 of the playbook. And **the debit IS the stop**, which is
the PLTR lesson: a defined-risk structure cannot be shaken out of a correct thesis by noise.

**Sizing:** debit at or under **$400**, well inside the $747.13 cap and inside the $812.66 cash. Max loss
= the debit, known at entry.

**Before entering, two checks that can kill it:**
1. **Re-confirm Dell's earnings date from Dell IR.** If it lands on or before Nov 20, abandon the Nov 20
   expiry — the whole edge here is that the print falls outside.
2. **Apply P8 from this morning:** price the spread at **realistic fills (buy the ask, sell the bid)**,
   not mids. DELL's chain is deep enough that this should be fine, unlike VSTM — but check it, do not
   assume it.

**Kill the idea entirely if:** DELL reclaims **$507.93** on volume (the broken floor recovered = the
breakdown failed), or the AI-capex complex turns and holds for two sessions.

### Nothing else flagged
VRT and ANET are structurally similar and better-priced, and **both are disqualified on confirmed
earnings inside the expiry** — no spread fixes a binary you have chosen to sit through. The semicap
equipment names (AMAT, LRCX, TER, KEYS, ONTO) have the same problem plus late-October prints.
**No advisory placed. The DELL plan is armed, not recommended for today.**

---

## Thursday, October 15, 2026 — 12:37 PM CT — DELL SPREAD PRICED (advisory, trigger NOT fired)

Owner asked for the actual price. **DELL $464.765** — it has bounced off the $462 low since the earlier
read. Here is the live Nov 20 put book and every vertical that fits the cap, priced at **realistic
fills** per P8, not mids.

### The chain — and this is the opposite of VSTM

| K | mark | bid × size | ask × size | spread % | OI | vol | delta | IV |
|---|---|---|---|---|---|---|---|---|
| 470 | $39.125 | 38.70 ×6 | 39.55 ×8 | **2.2%** | 782 | 217 | -0.472 | 64.5% |
| 460 | $33.800 | 33.25 ×28 | 34.35 ×9 | **3.3%** | 1,692 | 1,221 | -0.430 | 64.5% |
| 450 | $29.050 | 28.65 ×40 | 29.45 ×6 | **2.8%** | 1,448 | 395 | -0.388 | 64.7% |
| 430 | $20.925 | 20.45 ×12 | 21.40 ×74 | **4.5%** | 898 | 172 | -0.306 | 65.3% |
| **420** | **$17.475** | **17.05 ×11** | **17.90 ×70** | **4.9%** | **1,025** | **230** | **-0.268** | **65.6%** |
| 410 | $14.425 | 13.90 ×85 | 14.95 ×84 | 7.3% | 429 | 782 | -0.231 | 65.9% |
| **400** | **$11.675** | **11.25 ×119** | **12.10 ×74** | **7.3%** | **2,466** | **499** | **-0.197** | **65.9%** |

**Every spread is 2.2-7.3% against a 15% gate.** OI 429-2,466, volume 172-1,221. This chain is deeply
liquid — the P8 check passes without strain, unlike VSTM where it failed outright.

**And the structurally important fact: IV is 64.5-65.9% and essentially FLAT across strikes.** DELL's
normal is well under this, so the flush has inflated premium — condition #1 of the playbook. The flat
skew is what makes the vertical actually work: **selling the lower leg recovers premium at the same
inflated IV you pay on the upper leg.** If the skew were steep, the short leg would recover far less and
the structure would neutralize nothing. Worth stating because that is the condition, not an assumption.

### The verticals that fit — $747.13 cap, $812.66 cash

| Spread | Debit | Cost | Max gain | R:R | Break-even | Move needed | Fits? |
|---|---|---|---|---|---|---|---|
| **420 / 400** | **$6.65** | **$665** | **$1,335** | **2.01:1** | **$413.35** | **-11.1%** | **YES** |
| 420 / 410 | $4.00 | $400 | $600 | 1.50:1 | $416.00 | -10.5% | YES |
| 430 / 400 | $10.15 | $1,015 | $1,985 | 1.96:1 | $419.85 | -9.7% | no |
| 430 / 410 | $7.50 | $750 | $1,250 | 1.67:1 | $422.50 | -9.1% | no |
| 460 / 420 | $17.30 | $1,730 | $2,270 | 1.31:1 | $442.70 | -4.7% | no |

**My pick if it triggers: the $420/$400 at a $6.65 debit or better.** Best R:R of the two that fit, and
the $400 leg has the deepest book on the board (OI 2,466, 119 on the bid), so the short side fills.

### THIS is the Level 3 case in one number
**A single-leg Nov 20 $420 put costs $1,790 — 2.4× the conservative cap.** Unaffordable. The $420/$400
spread gets the same directional exposure for **$665**, and **max loss $665 ≤ the $747.13 a single leg at
the cap would have risked** — playbook condition #3 satisfied exactly. That is a spread doing the job the
playbook describes, as opposed to VSTM where it made things worse.

### THE TRIGGER HAS NOT FIRED — and the price is the reason to wait, not just the chart

DELL is **$464.765**, bouncing off $462.37, still sitting on the Sept 2 gap open of **$462.05**. Per P7
that is support, so the entry condition is unmet. But the pricing makes the case sharper than the chart
alone:

- **Route (b) — a bounce to $505-525 that stalls — makes this exact spread materially CHEAPER.** At
  DELL ~$510 the $420 put drops from ~$17.90 toward $10-12 and the $400 toward $6-8, so the debit falls
  from $6.65 to roughly **$4.00-4.50**. Same $20 width, same max value — **R:R improves from 2.01:1 to
  roughly 3.5:1.**
- **Route (a) — a close below $421.89 — makes it MORE expensive.** The $420 goes near-the-money (~$28-32)
  and the debit widens toward $10-12. Still workable, worse value.

**So waiting for the failed bounce is both the technically correct entry and the economically better one.
Route (b) is strictly superior to route (a), and that is the answer to "what price": not today's.**

### The honest requirement
Break-even on the $420/$400 is **$413.35**, which is **below the Sept 1 pre-earnings low of $421.89.**
This trade does not pay for a drift — **it needs DELL to break its pre-earnings base and keep going.**
That is coherent with the thesis (gap fill to the pre-earnings shelf) but it is a real condition, not a
gentle one, and it is why the entry price matters so much.

### Unchanged pre-entry checks
1. **Re-confirm Dell's earnings date from Dell IR.** The entire edge is that a Nov 20 expiry closes
   before the print (~Nov 24, unconfirmed). If Dell announces on or before Nov 20, abandon this expiry.
2. **Kill the idea** if DELL reclaims **$507.93** on volume, or the AI-capex complex turns and holds two
   sessions.

**Advisory only — I cannot execute in ••••1866, and I am not recommending entry today.**

---

## Thursday, October 15, 2026 — 12:41 PM CT — **DELL TICKET + FULL CALENDAR** (advisory, armed not placed)

Owner asked for the exact dates and contracts. **DELL $465.41.**

### THE TICKET — one 2-leg order, not two separate orders

**DELL Nov 20 2026 $420 / $400 PUT DEBIT SPREAD × 1**

| Leg | Action | Contract |
|---|---|---|
| Long | **BUY TO OPEN** | **DELL 11/20/2026 $420 PUT** |
| Short | **SELL TO OPEN** | **DELL 11/20/2026 $400 PUT** |

**Place it as a single vertical/spread order in Robinhood** (Trade Options → select both strikes → it builds the spread). **Do not leg in with two separate orders** — legging a vertical means paying both bid/asks and carrying naked directional risk between fills.

**Limit price (net debit):**

| | Debit | Cost | Max gain | R:R | Break-even |
|---|---|---|---|---|---|
| Mid-to-mid | $5.63 | $563 | $1,438 | 2.56:1 | $414.38 |
| **Target limit** | **$6.00** | **$600** | **$1,400** | **2.33:1** | **$414.00** |
| **Do not exceed** | **$6.50** | **$650** | **$1,350** | **2.08:1** | **$413.50** |

**Start at $6.00 and work up only to $6.50.** PERSONA: *"place limit orders at or below the midpoint... Never overpay just because the ask is posted there."* Above $6.50 the R:R degrades below 2:1 and the trade stops being worth the entry risk.

**Max loss = the debit = $600.** That is the entire risk, known at entry, and it is the stop — no percentage stop on a vertical (the PLTR lesson).

**Smaller alternative if $600 is too much:** the **$420/$410** at a **$3.25** limit = **$325** cost, $675 max gain, 2.08:1, break-even $416.75. Same thesis, half the size, slightly worse R:R, and a thinner short leg (OI 429 vs 2,466).

### THE CALENDAR — every date that matters

| Date | What happens | Action |
|---|---|---|
| **Thu Oct 15 (today)** | DELL $465.41, sitting on the Sept 2 gap open ($462.05). **Trigger NOT fired.** | **Do nothing** |
| **Mon Oct 19 – Fri Nov 13** | Watch window. **Route (b):** bounce to **$505-525** that stalls and rolls over ← *preferred, and cheaper*. **Route (a):** decisive close below **$421.89** ← works, costs more | Enter on either |
| **Tue Oct 27** | **SOFI earnings** (confirmed, SoFi IR, ~7:00 AM ET) | Separate position — no action on DELL |
| **Wed Oct 28** | **SOFI covered-call window opens** — now **2 contracts** (200 shares), Dec 18, delta 0.20-0.30 | Price it that morning |
| **Wed Oct 28** | **VRT reports** (confirmed, pre-open) | **First real tell on the AI-capex complex** |
| **Tue Nov 3** | **ANET reports** (confirmed, post-close) | **Bigger tell.** A weak ANET guide is the thesis confirming |
| **Fri Nov 13** | **LAST SENSIBLE ENTRY.** Inside a week to expiry a vertical stops behaving — gamma dominates and there is no time for the move | If untriggered by here, the Nov 20 idea is dead |
| **Fri Nov 20** | **Expiry.** Both legs settle | Must be closed or expired by then |
| **~Tue Nov 24** | **Dell earnings — UNCONFIRMED.** The entire edge is this landing *after* Nov 20 | **Re-verify from Dell IR before entering** |

### THE EXIT PLAN, set now so it is not improvised later

- **Profit target: close at 70-80% of max value** — roughly **$14.00-16.00** on the $20 width, i.e. **+$800 to +$1,000** on a $600 debit. Do not hold for the last dollar; a vertical's final value only arrives at expiry and the mark is a poor estimator until then.
- **Thesis stop (not a mark-to-market percentage):** exit if **DELL closes above $507.93** — the broken range floor reclaimed means the breakdown failed. This is the proposed spread-stop amendment applied: *thesis invalidation, time, or the entry-set max loss — never a mid-life mark.*
- **Time stop: Fri Nov 13.** If DELL has not broken $421.89 by then, close for whatever it is worth. Do not ride a vertical into expiry week on hope.
- **Max loss stop:** none needed. The $600 debit **is** the stop.

### Why these strikes and not others
- **$420 long:** delta **-0.268**, OI **1,025**, volume 230, spread 4.9%. Sits just under the **Sept 1 pre-earnings low of $421.89** — the level the thesis needs broken, so the long leg is placed exactly where the move has to go.
- **$400 short:** delta -0.198, **OI 2,466 — the deepest book on the chain**, volume 503, spread 7.3%. Deep enough that the short side fills reliably, which is what killed VSTM.
- **IV 65.0% / 66.3% on the two legs — near-identical.** The flat skew is what makes the vertical neutralize the flush-inflated premium rather than just capping gains.
- **$420 single leg alone costs $1,795** — 2.4× the $747.13 cap. The spread is the only way this position exists in that account.

### The honest requirement, restated
Break-even **$414.00** is **below the Sept 1 low of $421.89**. **This does not pay for a drift — DELL has to break its pre-earnings base and keep going.** That is why route (b) matters: entering after a failed bounce cuts the debit to roughly $4.00-4.50 and lifts R:R toward 3.5:1, which is the difference between needing a big move and needing a moderate one.

**Advisory only. I cannot execute in ••••1866, and the trigger has not fired — this is the ticket to have ready, not an instruction to place today.**

---

## Thursday, October 15, 2026 — 12:48 PM CT — **DELL THESIS CHALLENGED. I AM DOWNGRADING MY OWN SETUP.**

Owner asked why I think DELL has farther to fall. Good question, and checking it properly changed my
answer. **I found the actual catalyst — and it argues against me more than for me.**

### I was wrong that this was sector/macro only. There IS a Dell-specific catalyst.

**Barclays downgraded Dell, HPE and NetApp to Equal Weight on Oct 14.** Analyst Tim Long's argument:

> *"We believe the strong enterprise revenues are more of a function of memory costs than a move to
> enterprise AI at this time."*

The substance: Dell is **passing rising DRAM/NAND costs through to customers**, which inflates the
revenue line without selling more systems. **AI server operating margins are ~5%** — thin. Barclays
expects **meaningful deceleration over the next two years as memory prices normalize.**

**That is a real, structural, multi-quarter argument about revenue QUALITY, not a sentiment wobble.** It
also explains the breadth I was attributing to macro — HPE and NetApp were cut in the same note. I
should have found this before writing a ticket, and I did not. That is the process miss.

### And then the part that undercuts me badly

| | |
|---|---|
| **Barclays' price target** | **$574** (cut from $603) |
| **DELL now** | **$465.41** |
| **The downgrade's own target is 23% ABOVE the current price** | |
| Barclays still models AI server revenue | **tripling to $75bn this fiscal year** |
| Dell's reported AI server backlog | **$95 BILLION** |

**A downgrade to *Equal Weight* with a target 23% above spot is not a bearish call.** It says "fairly
valued, stop paying up for more upside." The stock has fallen **19% past that analyst's own target.**

Two sources also attribute part of the move to **insider selling**, which is a flow fact, not a thesis.

### HONEST RE-GRADE: this is a C+ thesis, not the B+ my ticket implied

What I actually have:
- ✅ A real catalyst with a substantive structural argument (revenue is cost pass-through at 5% margins)
- ✅ Sector-wide breadth confirming the same logic is being applied across HPE, NetApp, and the complex
- ✅ A real macro accelerant (hot CPI → yields → AI-capex unwind, now global)
- ❌ **The bear note's own target is 23% above spot**
- ❌ **$95B backlog and revenue tripling to $75bn — the bull case is intact inside the bear note**
- ❌ Price sitting **on** support ($462.05 gap open, $421.89 base below)
- ❌ **Break-even $414 needs another -11% after -22%** — a 33% total decline on a downgrade to *neutral*

**Three of those six are disqualifying-grade objections. I would not open this today even if the trigger
had fired, and I should say so plainly rather than defend a ticket I spent two messages pricing.**

### The self-criticism, stated directly

**By pricing the ticket in that much detail, I made a C+ thesis look like conviction.** The detail was
responsive to what was asked for, but thoroughness reads as confidence and that was misleading. The
honest framing I should have led with: *"this is a watch item with a structure attached, not a call."*

That is the same failure mode as the T put in a different costume — there I let a sizing argument license
an entry my own trigger had refused; here I let a well-specified structure stand in for a thesis that was
not strong enough to carry it. **Both times the detail outran the conviction.**

### WHAT I NOW RECOMMEND

**Do not place the DELL spread on a break of $421.89 (route a).** That route needs DELL to fall through
its pre-earnings base to pay, and I no longer believe the evidence supports asking for that.

**Route (b) only — a failed bounce to $505-525 — and even then at half size (the $420/$410 at ~$3.25,
$325 risk, not the $600 version).** The reason route (b) survives: if DELL rallies 9-13% and *fails*,
that failure is itself new evidence — it would mean the market rejected the $574-target argument, which
is exactly the information my thesis currently lacks. Entering on that is buying confirmation. Entering
on a break of support is buying hope.

**And the live possibility I should name rather than bury: with a $95B backlog, revenue tripling, and a
price 19% below the downgrading analyst's own target, the bounce may well be the real move.** I am not
pitching a long — there is no reversal signal, the tape is still falling, and PERSONA does not buy knives
— but if DELL reclaims **$507.93** the bear case is finished and I will say so without hedging.

### Updated status
**DELL: watch item, not a trade. Thesis C+. Route (a) withdrawn. Route (b) at half size only, and only
if the bounce actually fails.** Ticket details from 12:41 PM stand as mechanics; the conviction behind
them does not.

---

## 2026-10-15 — MEAN-REVERSION / "OUT OF BOUNDS" SCREEN (owner request, 12:57 PM CT)

Owner asked, alongside the DELL downgrade: *look for other possible Level 3 trades — stocks that have
dropped or risen out of bounds and are looking at a correction.* This is a **mean-reversion** request,
and the first honest thing to record is that **PERSONA contains no mean-reversion setup.** All three
long frameworks (EP, Momentum/Trend, Short Squeeze) and two of the three bearish inversions are
**continuation** patterns. The only reversal framework in the book is Parabolic Exhaustion, and it
requires the crack to have already happened. So extension alone cannot produce a trade here — it can
only produce a watch list plus a trigger. I am writing it that way on purpose.

### The screen, re-based on LIVE prices (not the Oct 14 closes I first computed)

EMAs are computed through the Oct 14 close and decline slightly each session, so treat the EMA columns
as approximate. Volume is raw vs the 30-day average, then projected to a full session (12:57 PM CT =
267 of 390 minutes elapsed = 68.5%, so x1.46).

| Sym  |    Live | vs 10dEMA | vs 20dEMA |  Today | Vol vs 30d | projected | 52wk high |  off high |
|------|---------|-----------|-----------|--------|------------|-----------|-----------|-----------|
| RGC  |  $10.40 |  **+41.1%** |  **+50.5%** | **+28.2%** |   7.59x    | **11.1x** |    $69.00 |   -84.9%  |
| ASTS |  $43.75 |    -17.0% |    -22.0% |  +3.82% |   1.10x    |    1.61x  |   $133.86 |   -67.3%  |
| NBIS | $181.00 |    -16.6% |    -18.7% |  -2.69% |   2.04x    |    2.98x  |   $299.86 |   -39.6%  |
| CRWV |  $67.79 |    -15.7% |    -18.7% |  +3.06% | **2.87x**  | **4.19x** |   $150.40 |   -54.9%  |

**Correction to my own first pass:** on Oct 14 closes I ranked ASTS as the most extended name down
(-20.0% vs its 10d EMA) and had RGC at only +10.0% up. Live, that ordering is wrong in both directions
— today's session moved RGC to +41.1% and lifted ASTS/CRWV off their lows. **RGC is now the most
extended name on the board by a factor of two, and it is extended UP.** The screen had to be re-based
before any conclusion; this is the same stale-denominator trap as the relvol pollution note.

**All four put in a violent intraday reversal today**, off the low: CRWV **+13.9%**, NBIS **+10.8%**,
ASTS **+9.7%**. ASTS ($39.87) and CRWV ($59.51) both set **new 52-week lows this morning** and reversed.
NBIS did not — its 52-week low is $73.52 from Feb 5, and it is still +146% above it.

That simultaneity matters and cuts against treating these as separate ideas: **CRWV and NBIS are one
AI-infrastructure trade with two tickers, not two setups.** Sizing both would be doubling a single bet.

### RGC — the most extended name, and NOT a trade. Disqualified on the book, not on the chart.

Regencell Bioscience: $5.19B market cap, **10 employees**, no revenue, P/E -343.6, **P/B 301.3**, float
**56.1M of 495.9M shares = 11.3%** (founder holds the rest). Intraday range today $7.72-$11.12, a 44%
swing. 52-week high $69.00 (Jan 8), 52-week low $4.51 (Jul 17).

PERSONA's Parabolic Exhaustion rule is explicit: **never buy puts into the vertical move itself; enter
only after the first crack, ideally on the failed lower-high bounce.** RGC is +28% today. There is no
crack. So the chart says watch, not trade.

**But the option book says never, and that is the stronger finding.** RGC Nov 20 $10 put, live:

- bid **$1.00** / ask **$4.80** — a $3.80 spread on a $2.90 mark = **131% of mark**
- open interest **0**, volume **0**
- IV **253.8%**
- At the ask you pay **$480** for a contract holding **$40** of intrinsic value. $440 is premium.
  RGC must fall to **$5.20 by Nov 20 — another -50% — just to double.**

There is no price at which this expresses the thesis. A 131%-of-mark spread on zero open interest is not
a wide market, it is **no market**. So RGC does not go on the watch list either: **it is out of scope
permanently for an options account**, and writing a trigger I could never act on would be theatre.

**New finding worth a ruling (P9): extension is a screen, not a setup, and a tradeable book is a
precondition, not a detail.** The most extended name on the board is the one whose options cannot be
traded at any price. Check the book before building the thesis — I priced the put *after* writing up
the chart, and had the book been checked first, RGC would never have reached the write-up.

**Ruling #7 on RGC — cannot be satisfied.** The earnings tool returns a single stale row (labelled
"2022 Q1", dated 2026-06-15, unverified). RGC is a Hong Kong foreign private issuer filing 20-F, which
reports semi-annually rather than quarterly, so there is likely no quarterly print to fear — but I could
not confirm the schedule and am not going to pretend otherwise. Moot given the disqualification above.

### CRWV — the one real candidate. Grade C. Conditional ticket only.

CoreWeave, $37.3B cap, at $67.79 after a new 52-week low of $59.51 this morning and a +13.9% intraday
reversal on **4.19x projected volume**. That is genuine capitulation volume with a genuine reversal bar.

**For:** new 52-week low reversed hard; the heaviest volume in the set; -54.9% from the high; a
complex-wide washout; and a clean expiry that dodges the print (below).

**Against, and it is enough to stop the trade:** it is **day one with no follow-through**; CRWV sits
**below both the 10d (~$78) and 20d (~$81) EMAs**, so buying calls is **counter-trend**; the decline has
a live, un-refuted bearish thesis (AI-capex financing, debt load, the memory-cost margin argument);
at -55% off the high every prior bounce has failed, and this would be at least the third. **No PERSONA
long framework fits "bounced off a 52-week low on heavy volume."**

**Grade C.** I am grading before pricing this time, which is the specific order I got wrong on DELL.

**Ruling #7 — the binding constraint.** CRWV Q3 is scheduled **Mon Nov 9, post-close, UNVERIFIED**
(history 11/10/25, 2/26/26, 5/7/26, 8/11/26 — all pm, highly consistent, so plausible but tentative).
Nov 6 is the **last expiry that closes before the print** (1 session clear). Nov 13 and Nov 20 both
contain it. **This hands the idea a hard shelf life: the trigger must fire by ~Oct 27 or the trade stops
existing, because rolling out crosses the print.** A time stop set by the calendar, not by my discretion.

**Pre-priced ticket — CRWV Nov 6 $70/$80 call debit spread, at realistic fills (P8: buy ask, sell bid):**

| | |
|---|---|
| Buy $70C | ask **$5.30** (OI 1,111, vol 1,959, spread 4.8% of mark, delta 0.494) |
| Sell $80C | bid **$2.03** (OI 808, vol 649, spread **16.7%** of mark, delta 0.269) |
| Net debit | **$3.27 = $327/spread** |
| Max loss / max gain | **$327 / $673 — 2.06:1** |
| Breakeven | **$73.27 (+8.1%)** |
| Max profit at | **≥$80 (+18.0%)** |
| IV both legs | **90.2% / 90.1% — flat, no skew edge** |
| Size | 1 spread $327; 2 = $654 under the $747.13 cap |

**P8 earns its keep again:** mid-to-mid this spread is $2.96 ($296). Realistic fills are **$327 — 10.5%
worse.** Pricing it at mids would have understated the cost by $31/spread and the reward:risk by a fifth.

**Two gate failures to state rather than bury:** the short leg's spread is **16.7% of mark, over the 15%
gate**, and flat IV across strikes means the spread is pure directional financing — there is no vol edge
being harvested, only 38% of the debit financed by selling the $80.

**TRIGGER — not met today.** A daily close above today's high of **$68.04** on volume at or above the
30-day average (33.9M), confirming the reversal bar; better, a close above **$72**, reclaiming the
breakdown shelf. **If it has not fired by Mon Oct 27, the idea is dead — do not roll to Nov 13/20.**

The reason this is written as a trigger and not a recommendation: the most expensive error in the book
is the 10/9 T put, where I named a trigger, graded the agentic entry a pass on it, and then recommended
the same trade in the individual account with the trigger unmet. Cost $133, grade D. **CRWV is that
same shape, caught earlier.** Entry on confirmation or no entry.

### ASTS and NBIS — no ticket

**ASTS** $43.75, new 52-week low $39.87 today, -67.3% from the high — the deepest drawdown in the set,
but **projected volume only 1.61x.** A 52-week low that reverses on average volume is not capitulation;
it is a pause. No ticket, and the existing SpaceX-disruption thesis (Piper $98→$54) is unrefuted.

**NBIS** $181.00, -16.6% below its 10d EMA on 2.98x projected volume, but **down -2.69% today** — the
only name in the set still falling, and not at a 52-week low. Nothing has turned. It is also the same
trade as CRWV; if either is ever taken it is one position, not two.

### Bottom line for the owner

**No Level 3 trade qualifies today.** One pre-priced conditional ticket (CRWV Nov 6 70/80 at $327,
2.06:1) that requires a close above $68.04 on average volume by Oct 27 and dies after that. RGC is the
most extended name on the board and is permanently out of scope because its options have no market.
Cash is a position.

### Disclosure

**Catalyst check incomplete on both names.** The Robinhood news tool is absent from this server's tool
list, and web search returned nothing current for either move — all RGC coverage was 2025 (the 38-for-1
June 2025 split, the 60,000% run, $0 revenue 2021-2025, short interest ~3% of float so not a squeeze,
and a later -74% drawdown — which corroborates the manipulation profile but says nothing about today),
and nothing at all for CRWV's new low. **I could not confirm why either name moved today.** For CRWV
that is a real gap in a thesis I graded C; it is one more reason the trigger has to carry the entry.

---

## 2026-10-15 — LONG-TERM LONGS / SHORTS (owner question, 1:06 PM CT)

Owner asked whether any **long-term** shorts or longs look good. Answering requires naming a gap first.

### The framework gap, stated before anything else

**PERSONA has no long-term framework.** It is a swing system end to end: 3-10 day holds, a 5-7 day time
stop, and all three long frameworks (EP, Momentum/Trend, Short Squeeze) plus two of the three bearish
inversions are **continuation** patterns read off daily bars. Nothing in the book grades a multi-quarter
thesis. So everything below is **outside the book** and should carry less weight than a swing call, not
more. I am not going to dress a 27-month view in the authority of a system built for 7-day holds.

### The agentic account cannot hold a long-term position — verified, not assumed

Agentic 452369101: **$948.56, all cash, flat.** 20% cap = **$189.71**. And it is **option_level_2 — no
spreads.** So a long-term position there must be a *single long option*, and the cheapest credible
long-dated contract on a liquid name (SOFI Jan 2028 $15 call) is **$400 at the ask — 2.1x the cap.**

**The agentic account is a swing account by construction, not by preference.** Long-dated ideas can only
ever be advisory in the individual account (Level 3, cap $747.13). Worth knowing so the question does not
come up again.

### Ruling #7 reads differently on long-dated positions — proposed P10

Ruling #7's three permitted responses are: shorter expiry before the print, size down, or name the risk.
**Response (1) is structurally impossible for a long-dated position** — a Jan 2028 spread contains roughly
five earnings reports by construction. There is no expiry that avoids them.

But that is not purely a cost, and I had the sign wrong on my first pass: **duration converts one binary
into an average of five.** A Nov 6 position lives or dies on the Nov 9 print; a Jan 2028 position cannot
be killed by any single report. That is a genuine argument *for* long-dated structures and against the
swing instinct that earnings exposure is always a defect. **P10: for positions spanning more than two
prints, ruling #7 is satisfied by naming the count, not by trying to dodge it.**

### LONG-DATED LONG — SOFI Jan 2028 $15/$25 call spread. Structure A. Thesis C+. Not recommended.

SOFI set a **new 52-week low of $13.875 this morning**, now **$14.7232 (+3.54%)**, which is **-55.0% from
its $32.73 high of Nov 12 2025.** Profitable: **P/E 29.98, P/B 1.657**, $19.0B cap, 6,100 employees.

Priced at realistic fills (P8: buy ask, sell bid):

| | |
|---|---|
| Buy Jan 2028 $15C | ask **$4.00** — OI **37,904**, vol 1,832, spread **1.26% of mark**, delta 0.650 |
| Sell Jan 2028 $25C | bid **$1.57** — OI 17,598, vol 875, spread 3.13% of mark, delta 0.343 |
| Net debit | **$2.43 = $243/spread** |
| Max loss / max gain | **$243 / $757 — 3.11:1** |
| Breakeven | **$17.43 (+18.4%)** |
| Max profit at | **>=$25 (+69.8%)**, 27 months out |
| **Net theta** | **-0.0003/day — effectively zero** |
| **Net vega** | **+0.0005 — effectively zero** |
| Size | 3 spreads = $729 under the $747.13 cap; 1 = $243 |

**This is the best-structured vehicle I have priced in this account, period.** The short leg cancels
essentially all theta and all vega, leaving a near-pure directional bet with no bleed. And **P8 cost only
2.1% here** ($243 realistic vs $238 at mids) against **10.5% on CRWV** — the difference is entirely
liquidity. A 37,904-OI book with a 1.26% spread means mids are nearly real. Worth recording as the
counter-example to RGC: same methodology, opposite verdict, because the book is genuinely there.

**Why I am not recommending it anyway:**

1. **I have a P/E and a chart, not a thesis.** A 27-month hold in a lender requires a view on the loan
   book, charge-off trends, deposit growth, credit quality and the student-loan refi cycle. I have done
   none of that work. "Down 55% and profitable" is a screen, which is exactly the error I just caught
   myself making on RGC and CRWV.
2. **It is making new 52-week lows today.** Counter-trend on every timeframe including the one that matters.
3. **The owner is already long 200 shares and underwater.** Adding a levered long-dated SOFI bet **doubles down
   on a losing position.** "Never average down" is written about options, but the spirit reaches this.

**Grade: A on structure, C+ on thesis.** And the DELL post-mortem from this morning says precisely this:
*do not let a well-specified structure stand in for a thesis that is not strong enough to carry it.*
Writing the ticket and declining it is the whole point of having written that sentence down.

### LONG-DATED SHORT — nothing qualifies, and the arithmetic is the reason

DELL Jan 2028 $400 put, live, as the worked example (DELL **$462.57, -8.93% today**):

- ask **$83.40 → $8,340 for ONE contract.** That is **11.2x** the $747.13 cap.
- breakeven **$318.47** — DELL must fall **another -31.1%** over 15 months **just to break even**
- **vega 1.709** — a 10-point IV drop costs **$171/contract** in P&L you never asked for
- volume **7** contracts today; OI 1,061
- IV 63.7%, delta only -0.269 for $8,340 of capital

**Long-dated puts are the worst risk/reward structure in options:** you pay for duration *and* for vega,
on a name whose IV is already inflated by the very fear that made you bearish. The premium embeds the
decline you are predicting.

And all three structural bear cases I hold are already deep into the move — **DELL -22.3% from its Sept
high, CRWV -54.9%, NBIS -39.6%.** Buying expensive duration late is the worst version of a good idea.

**Also newly relevant to any long-term DELL view: P/B is -227.80 — negative book value**, from years of
buybacks plus the EMC debt. A long-term *long* in DELL is levered to a balance sheet with no equity
cushion; a long-term *short* is fighting a $294B cap, a 0.45% dividend and a $95B backlog. Neither side
is a clean multi-quarter story.

### The one genuinely actionable long-term item: income on the shares the owner already holds

Not a new position — the **covered-call program on the 200 SOFI shares**, already calendared for Oct 28
(post-earnings). Reference pricing today, SOFI Dec 18 $17C: bid **$0.57**, OI 5,919, spread 5.1% of mark.

- 2 contracts at the bid = **$114 credit** against $2,944.64 of stock = **3.87% of notional in 64 days**,
  roughly **22% annualized**
- Over a year that is ~$235 of income against a position currently **-$287.36**, which materially changes
  the hold math without adding one dollar of directional risk

**Two honest caveats.** Delta **0.311** is slightly above the 0.20-0.30 band the Oct 28 plan specifies —
the $18 strike would be cleaner. And more importantly: **$114 is today's price with Oct 27 earnings IV
inside it (53.5%).** Written on Oct 28 after the crush, the same call pays meaningfully less — call it
**$80-90** for the pair, not $114. Quoting today's credit as if it will be there on Oct 28 would be the
same stale-denominator error as the extension screen.

### New facts recorded today

- **SOFI** new 52-week low **$13.875**, now $14.7232, **-55.0%** from its Nov 2025 high. The 200 shares
  at $16.16 avg: **-$287.36 (-8.89%)**, improved from -$306.02.
- **DELL -8.93%** to **$462.57** (low $452.42, 1.48x raw / ~2.1x time-scaled volume). Still **above** the
  withdrawn route (a) trigger of $421.89.
- **DELL goes ex-dividend $0.63 on Tue Oct 20**, payable Oct 30 — a corporate action inside any DELL
  position spanning next Tuesday, and early-assignment risk on any short call.

### Bottom line for the owner

**No long-term position recommended.** The long side has one excellent structure (SOFI Jan 2028 $15/$25,
$243, 3.11:1, zero theta) attached to a thesis I have not earned the right to pitch. The short side is
disqualified by arithmetic, not opinion. The only long-horizon action worth taking is the SOFI
covered-call program already on the calendar for Oct 28, which is income rather than a new bet.
