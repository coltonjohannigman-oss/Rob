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
day one — but he buys *shares* with a 2-3% stop, not 9-DTE calls at 102% IV where decay alone
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
