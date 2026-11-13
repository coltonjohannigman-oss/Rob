# Robbin Trade Pipeline

Setups in formation — B grades and not-yet-triggered A setups. Checked at the start of every
session BEFORE scanning for new names. A triggered entry is re-scored live and trades only if
it now grades A or A+. Drop entries after 10 sessions or on invalidation. Every trigger gets a
Robinhood price alert.

Format: **Ticker | direction | setup | score (V/S/C/RS/R = total) | ADR | prior move | trigger (range high/low + volume) | invalidation | candidate contract | added**

---

## Weekly prep — 2026-09-27 (Sun), for the week of Sep 28 – Oct 2

- **Regime: RISK-ON** — QQQ 744.50 > 10-EMA 732.28 > 20-EMA 725.13 (both rising); SPY 771.35 >
  rising 20-EMA 765.83, ~0.8% under its 8/13 high. Caveats: leadership is narrow (IWM 281.97 is
  below declining 10/20-EMAs), and the 10-yr Treasury touched 5.23% (highest since 2007).
- **Event calendar:** Tue 9/29 CCL (am); Wed 9/30 GDP 3rd est (8:30 ET), **MU earnings after the
  close** (drives every AI-hardware name, SMCI included); Thu 10/1 NKE (pm), ACN (am);
  **Fri 10/2 September jobs report (8:30 ET)** → Thursday is the final session before a macro
  print: no new entries unless exceptional AND at the reduced size (15%). Government funding is
  settled through Dec 11 (no shutdown risk). Trump–Xi summit (9/23–25) ended with no trade deal.
- **Official trades (Tip Ranks, STOCK Act — lag up to 45 days, not a signal on its own):** Rep.
  Pelosi bought BE and INTC shares + calls Jul 23–28 (disclosed 8/24); both are now leaders.
  No congressional SMCI trades disclosed. Rep. Cisneros small PLTR buy 7/16.
- **Focus universe (RS leaders, ADR ≥ ~4%):** DELL, AMD, CRWD, INTC, SMCI, BE, NET, PLTR, HOOD,
  ANET, NVDA (ADR 2.4% — below standard), MU (earnings 9/30), ALAB, NBIS, LITE, CLS.
  Laggards / put-watch (counter-regime, A max): APP, ORCL, OKLO, SMR, UEC, MP.
- **Budget constraint:** only SMCI (and GME) among the leaders has options Robbin can afford
  under the 30% cap; everything else is a personal-account spread candidate (advisory.md).

## Persona review — 2026-11-10 (no market session run; nothing below was re-scored live)

- The drawdown brake that every entry below cites ("A+ only, 15% = $142") was switched on by a
  stats bug and no longer exists. `python cli.py stats` now prints **DRAWDOWN LADDER: level 1**
  (2 straight losses: XPEV, PENG) → every trade capped at 20%, at most 2 open positions, **A and
  A+ both trade**. Level 1 is 35% after the owner's 11/10 raise of the ceiling to 50%, so on
  the $904.56 broker cash that is ~$317 per trade → price ceiling roughly $63 for stocks,
  $127 for ETFs.
- Regime at the 11/9 close: still RISK-OFF by the EMAs (QQQ $679.35 under a declining 10-EMA
  $684.3 and 20-EMA $699.1; SPY $752.69 under $753.3 / $759.0). Rally attempt: low $647.05 on
  11/5, so 11/6 = day 1, 11/9 = day 2 (+3.5%, but on lower volume than 11/6). A follow-through
  day is possible from day 4 (11/11) — see PERSONA: MARKET REGIME → TURNS.
- Next session: re-score NU and PBR under the post-gap-flag amendment (PBR's flag already broke
  on 11/2 and the move is 5 sessions old, so check DON'T CHASE and the PBR/NU earnings dates
  before anything), rebuild the focus list under the price ceiling with the ETF sleeve, and
  drop CCI / TENB unless they re-base.

## Pass audit

One line per candidate that scored 7+ but was blocked by a gate, and per pipeline entry that aged
out. Outcome is filled in 10 sessions later. Tally by gate every 20 lines (PERSONA: PASS AUDIT).

Format: **date | ticker | dir | score | blocking gate | price that day | outcome (date, price, verdict)**

- 10/26 | PBR | put | 8 | extension limit; low ADR read as "A+ only"; brake | $22.50 | 11/9 $18.35 (-18%), never bounced to the EMA — MISSED
- 10/26 | NU | put | 8 | -20% flush / IV day 1, then extension limit; brake | $12.59 | 11/9 $12.36, low $11.21 on 11/5 — NEUTRAL
- 10/27 | XYL | put | 8 | extension limit; low ADR; chain liquidity | $92.86 | 11/9 $99.26 (+7%; +13% from the 10/28 close) — GATE RIGHT
- 10/27 | BA | put | 9 | extension limit; DON'T CHASE; price | $168.18 | 11/9 $172.38, range $165-179 — GATE RIGHT
- 10/23 | CCI | call | 5-6 | counter-regime; brake | $85.97 | broke the $91.45 trigger 11/4, 11/9 $87.83 — GATE RIGHT
- 10/29 | TENB | call | 7-8 | gap-day rule; extension limit; regime | $51.78 | 11/9 $43.67 (-16%) — GATE RIGHT
- 10/23 | GMAB | call | 6 | counter-regime; brake; gap-day rule | $43.79 | 10/28 $57.29 (+31%), 11/9 $55.80 — MISSED (B grade; a 2-session flag in RISK-OFF)
- 11/11 | ZETA | call | 9 | DON'T CHASE (>1 ADR past $35.35); extension ~2 ADR over the 10-EMA; price over the level-2 cap | $37.90 | (fill in by 11/25)
- 11/11 | REZI | call | 7 | options liquidity: Dec 18 $22.5C OI 2, $20C OI 22; also 3 ADR above its low of day | $22.16 | (fill in by 11/25)
- 11/13 | EEM | put | 7 | DON'T CHASE (1.5 ADR through $61.67); Dec 18 $60P spread 28% | $60.38 | (fill in by 11/30)
- 11/13 | SLV | put | 7 | extension limit (2.7 ADR under the 10-EMA) after the 11/10 stop-out | $44.41 | (fill in by 11/30)
- Tally so far (7): extension limit blocked 5 → 1 missed, 1 neutral, 3 right. Counter-regime blocked 3 → 1 missed, 2 right.

## Active

### Session 2026-11-13 (Fri, 9:27 AM CT) — regime CHOP under test (the 11/11 follow-through confirmed at the close: QQQ +2.3% on 44.9M vs 38.8M; today QQQ $675 (-1.9%) is back under its 10-EMA $684.8 and 20-EMA $695.4, SPY $750 under $754.6 / $758.2; rally low $647.05 intact), ladder LEVEL 2 → cap 25% = $221, ONE position, ceiling ~$44 stocks / ~$88 ETFs

- Breadth: IWM $275.1 under its 10/20-EMAs ($279.4 / $279.1); RSP $219.7 on its 10-EMA, above its 20-EMA ($218.4), so the selling is
  concentrated in semis/AI (SMH -4.7%, AMD -9.5%, NVDA -3.9%). VIX 20.7 (17.7 on 11/11). **NVDA reports Tue 11/17 after the
  close**: Tuesday is the final session before a binary event for the whole tape (reduced size only).
- **No trade. Closest: EWZ put (A+ on score once it triggers; $32.13 is 2.3% above the $31.40 trigger).** No-trade sessions: 3.
- **EWZ | PUT | post-gap flag (Brazil runoff 10/25) | V?/S2/C2/RS2/R1 = 7 + volume (A+ at V2) | ADR 2.4%, ADX 41 | 1 month -25%;
  12-session flag $31.50–32.92 since 10/30 on fading volume (27–29M vs a 63M 20-day average) | TRIGGER: break of $31.40 (the
  90-day low) by the ORL rules with volume above the prior day's pace and ≥1.2x average | INVALIDATION: close above $32.92 (flag
  high) | CONTRACT: Dec 18 $33P $1.93/2.04, Δ -0.55, IV 39%, OI 24,993 (1 = ~$199) or $32P $1.32/1.36, Δ -0.45, OI 48,185 |
  alert < $31.40 set | day 4 of 10**
- **XLE | PUT | breakdown, failed-bounce watch | V?/S1/C1/RS1/R1 = 4 + volume (B) | ADR 2.4%, ADX 26 | fell $70.15 → $60.43 in 7
  sessions (11/4 on 2x volume), then a 5-session bounce on fading volume (24–26M vs 37M) into the 20-EMA: today's high
  $64.96 vs the 20-EMA $64.99, now $64.56 | TRIGGER: break of the prior day's low ($63.42 for today) on ≥1.5x volume |
  INVALIDATION: close above $65.30 | CONTRACT: Dec 18 $64P $1.62/1.66, Δ -0.42, IV 25%, OI 24,477 | alert < $63.42 set | day 4 of 10**
- **ZETA | call | post-gap flag, session 3 | V?/S2/C2/RS2/R1 = 7 + volume | $37.19 (-0.2% on a -2% tape); flag $36.00–38.80 above the
  $35.35 gap-day high on fading volume (9.3M → 5.1M); ~1.2 ADR over the 10-EMA, so the extension gate now passes | TRIGGER:
  break of $38.80 on above-pace volume | INVALIDATION: close below $35.35 | still over the $221 cap at Δ0.55+ (IV ~60%), so
  it is in advisory.md as a call-spread candidate | alerts > $38.80 and < $36.00 | day 3 of 10**
- **NFLX | PUT | B, volume fails | broke $62.90 on 11/12 (low $62.55, close $62.69) on 31.6M = 0.68x average, so no volume; today
  $62.47–63.95, now $62.89 | same trigger with ≥1.5x volume; real level $61.39 | Dec 18 $64P still over the cap | day 4 of 10**
- **ONON | PUT | watch | closed $33.07 on 11/12, under the $33.86 gap-day low, on day 2 (the flush, banned) and on average volume;
  back to $33.80 today | TRIGGER: from Monday (3 post-gap sessions done), a break of $32.87 on ≥1.5x volume | INVALIDATION:
  close above $35.58 | alert < $32.87 set | day 4 of 10**
- **EEM | PUT | trend pullback (mirror) | V1/S2/C1/RS2/R1 = 7 (A on score, GATES FAIL) | ADR 1.5%, ADX 30 | 4-session quiet rally
  $58.00 → $62.43 into the declining 20-EMA ($62.0); broke the prior day's low by gapping down 11/12; today $60.38 (-1.2%) |
  GATES: 1.5 ADR through the $61.67 trigger (DON'T CHASE); Dec 18 $60P quoted $1.78/2.36, a 28% spread | TRIGGER: a 1–3
  session bounce toward $61 (10-EMA $61.1) that fails, then a break of the prior day's low, with the spread back under 15% |
  INVALIDATION: close above $62.45 | TSM/Samsung/Hynix weight makes NVDA 11/17 a binary event for it | alert > $61.00 set |
  added 2026-11-13**
- **VFC | call | post-earnings flag at the 10-EMA | V?/S2/C2/RS2/R1 = 7 + volume | ADR 3.9%, ADX 52 | +35% in 3 months; 7-session
  flag $20.02–21.24 on fading volume; $20.13, 10-EMA $19.93 | TRIGGER: reclaim of the prior day's high ($20.87) on ≥1.2x
  average volume, or a break of $21.24 | INVALIDATION: close below $19.60 | CONTRACT: Dec 18 $20C fails both tests today (OI
  232, spread 19%) — check Nov 27 / Jan at the trigger; no liquid strike = pass | alert > $20.90 set | added 2026-11-13**
- Passed 11/13: KD (post-earnings flag $16.0–17.39, a clean chart; Dec 18 $16C/$17C OI ~205 and spreads 26–34% — fails both
  liquidity tests, which a spread does not fix), CPRI (same flag shape, thinner chain), BRZE (pinned at $46.6, ADR 1.1%: a
  deal), SLV ($44.41, a new closing-basis low; 2.7 ADR under its 10-EMA), KWEB (2.7 ADR under), ARKK (put over the cap),
  today's semis/AI/miner flush (IREN, APLD, IONQ, ASTS, WULF: day-1 drops inside violent 2-day bounces, 80–100% IV, stop
  anchors wider than 1 ADR). Gainers: MOD +26%, LFTO +24%, STN +14% are day-1 gaps over the ceiling or with no chain.
  Leaders over the ceiling (ULTA, ACN, PTC, HAS, KOD, SWKS, EXEL): no workup.

### Session 2026-11-11 (Wed, 10:43 AM CT) — regime CHOP (QQQ $692 above its 10-EMA $682.6, under the 20-EMA $696.8; SPY $759 above both), rally attempt DAY 4, ladder LEVEL 2 → cap 25% = $221, ONE position, ceiling ~$44 stocks / ~$88 ETFs

- **SLV closed 11/10: stop filled $2.25 at 9:04 AM CT, -$20.09 (-8.2%). Ledger booked, journal #13.** Losing streak 3 →
  ladder level 2 (relaxes to level 1 on 11/17 with no new loss, or on the next winner).
- **Possible follow-through day today:** QQQ +2.6%, SMH +6%, on day 4 of the attempt off the 11/5 low ($647.05). Volume
  through the first 90 minutes ran ~0.9x yesterday's pace, so it is NOT confirmed — judge at the close (needs volume above
  11/10). Either way calls score R1. VIX 17.7. PPI Fri 11/13 → Thursday entries at reduced size only.
- **ZETA | call | EP day 2 (Q3 EPS $0.38 vs $0.23, 11/9 pm) | V2/S2/C2/RS2/R1 = 9 (A+ on score, GATES FAIL) | ADR 5.8% |
  6-week base $29.4–35.75; gap day 11/10 $31.34–35.35 on 2x volume; today $37.9, new 90-day high | GATES: more than 1 ADR
  through the $35.35 trigger (DON'T CHASE), ~2 ADR over the 10-EMA (~$33.3), and a ~0.50Δ 5-week call is over the $221
  cap | TRIGGER: a 3–10 day flag above $35.35–35.75 that breaks out, or a pullback to the rising 10-EMA that reclaims the
  prior day's high | INVALIDATION: close below $35.35 | added 2026-11-11**
- **NFLX | PUT | failed bounce | V?/S1/C1/RS2/R1 = 5 + volume (B) | $63.63; poked $62.92 on 11/10 on light volume and
  closed $63.26; under the 10-EMA $64.14 | TRIGGER: break of $62.90 on ≥1.5x volume; real level $61.39 | INVALIDATION:
  close above $65.41 (20-EMA) | CONTRACT: Dec 18 $64P (OI 5,323, $2.70) — over the level-2 cap by $49 | day 2 of 10**
- **XLE | PUT | breakdown, bounce in progress | $63.12 (+1.5%); 11/10 low $60.43; declining 10-EMA $64.26, 20-EMA $65.24 |
  TRIGGER: a weak bounce into $64.2–65.2 that fails, then a break of the bounce low on ≥1.5x volume | INVALIDATION: close
  above $65.3 | day 2 of 10**
- **EWZ | PUT | post-gap flag | not triggered | $32.41 | TRIGGER: break of $31.40 on ≥1.5x volume | INVALIDATION: close
  above $33.60 | day 2 of 10**
- **ONON | PUT | EP-down day 2 | watch | $34.20; gap day 11/10 $33.86–35.58 on 25M shares | TRIGGER: 3+ sessions inside the
  gap-day range, then a break of $33.86 | INVALIDATION: close above $35.58 | day 2 of 10**
- Semis off the lows today (SMCI +11%, AMKR +12%, ASX +7.5%, GFS +6%, VIAV +9%, IREN +9%): all still under declining
  20/50-EMAs with no base — a thrust, not a setup. If the follow-through confirms, their first tight pullbacks are the
  next call funnel. SLV: back to $47.0, under its 10-EMA $47.29; no setup.
- **Re-check 11:39 AM CT (same day): nothing triggered.** ZETA $38.05 (alert < $36.00 set), NFLX $64.04 (alert < $62.90
  set), XLE $62.94 (alert > $64.20 set), EWZ $32.42, ONON $34.29. QQQ $694.5 (+2.9%), SPY $761.2; QQQ volume still
  ~0.9x yesterday's pace on patchy intraday data — follow-through unconfirmed until the close. No-trade sessions: 2.
- Dropped: KSS (earnings 11/24 inside any hold), NU (aged out day 10; earnings 11/12), PBR (post-earnings, $18.07, nothing).

### Session 2026-11-02 (Mon, 10:51 AM CST) — regime RISK-OFF (SPY $760 / QQQ $694 both under declining 10/20-EMAs), DRAWDOWN BRAKE ON (A+ only, 15% = $142). Midterm election 11/3 is a binary event, so today counts as the final session before it.

- **NU (day 6): not yet, but it is the closest affordable put.** $11.90 (+2.5%, bouncing off the $11.48 low). It is ~2.6 ADR under
  the 10-EMA (~$13.0), so the EXTENSION LIMIT still blocks it. Nov 20 $12P: mark $0.59, Δ −0.50, IV 52%, OI 23k, spread 7%, so
  2 contracts = $118, which fits the cap. Nov 20 $11.5P: $0.35, Δ −0.35, OI 5.6k. TRIGGER: the bounce runs toward $12.5–13
  (which brings the extension under 2 ADR), stalls on fading volume, then the bounce low breaks on ≥1.5x volume. Earnings
  are 11/12 pm, so any hold must exit before then. Day 6 of 10.
- **PBR (day 6): not yet.** $21.36 (−3.1%), a new low with no bounce, ~3 ADR under the 10-EMA ($23.3). Earnings are 11/10. Day 6 of 10.
- **BA (day 4): it reached the bounce zone (the $176 alert fired), but there's no rejection yet.** $177.2 at the high of day, right at the declining
  10-EMA (~$178.5), on light volume (~2.3M in 80 min). Robbin can't afford a single put (~$4+), so it moved to advisory.md
  as a put debit spread candidate. Keep it here as a watch only. Day 4 of 10.
- **CCI (day 7) / TENB (day 3): calls are now counter-regime (R0), so A+ is impossible.** CCI $87.1, flag intact
  (invalidation $83.26). TENB $49.4, holding the $48.7 invalidation.

### Session 2026-10-29 (Thu, 9:10 AM CT) — regime CHOP (QQQ under both EMAs, SPY on them), DRAWDOWN BRAKE ON (A+ only, 15% = $142)

- **NU (day 4): not yet.** Yesterday it broke the bounce low to $11.96 on 1.1x volume. It is now $12.10, ~3.4 ADR
  under the 10-EMA ($13.74), so the EXTENSION LIMIT still blocks it. Same trigger. Day 4 of 10.
- **PBR (day 4): not yet.** $22.27, ~2.6 ADR under the 10-EMA ($23.98). It hasn't reached the $23–23.8 bounce zone. Day 4 of 10.
- **CCI (day 5): flag intact, not triggered.** $88.26. Yesterday's low of $83.72 held above the $83.26 invalidation.
  Trigger unchanged: a break of $91.45 on ≥2x volume (alert set). It is a call in CHOP (R1), so it can reach A at most and
  can't trade under the brake. Day 5 of 10.
- **XYL (day 3): not yet.** $89.0, ~4.4 ADR under the 10-EMA ($100.9). It kept falling (yesterday's close was $88.23). A new
  alert at $96 marks a bounce toward the declining EMA. Day 3 of 10.
- **BA (day 3): not yet.** $170.1, bouncing +1.8% from yesterday's $165.01 low and ~2.5 ADR under the 10-EMA ($182.1).
  A new alert at $176 marks the bounce zone. A ~0.40Δ Nov put is still likely over the $142 brake cap. Day 3 of 10.
- **TENB | call | EP (earnings reaction, verify catalyst) | V?/S1/C2/RS2/R1 = 7–8 (A at best, GATES FAIL) | ADR 5.6% |
  +39% in 1 month, +50% in 3 months | +5% gap to $51.14, a new high over $50.21 | GATES: a day-1 gap (GAP-DAY RULE), and
  ~2.4 ADR over the 10-EMA ($44.18; EXTENSION LIMIT) | TRIGGER: a day-2+ pullback that holds today's low or the 10-EMA,
  then a reclaim of the prior day's high on ≥2x volume, or a 3–10 day flag break | INVALIDATION: close below $48.7
  (yesterday's close) | CONTRACT: Nov 20/Nov 28, ~0.45Δ, check OI/spread at the trigger | added 2026-10-29**

### Session 2026-10-27 (Tue, 9:20 AM CT) — regime RISK-OFF, DRAWDOWN BRAKE ON (A+ only, 15% size)

- **NU (day 2 of the bounce): not yet triggered.** Today's range is $12.50–13.00, and the price is $12.68.
  The bounce tagged the bottom of the $12.8–13.4 resistance zone (the $12.80 alert fired). Put IV has
  cooled to **54%** (Nov 20 $12P: mark $0.375, OI 19,623, spread 8%, Δ −0.31), so the IV gate now passes.
  It is still blocked by the EXTENSION LIMIT: ~5 ADR under the 10-EMA (~$14.6). The trigger is
  unchanged: the bounce stalls, then today's or the next bounce low breaks on ≥1.5x volume. The
  extension must also be under ~2 ADR, so it needs a higher bounce or a few sessions for the EMA to
  come down. Use the Nov 20 $12.5P (closer to Δ0.40) at the trigger. Day 2 of 10.
- **PBR: not yet.** Range $22.46–22.97, so it hasn't reached the $23–23.8 bounce zone. Day 2 of 10.
- **GMAB (day 3): flag forming.** Range $43.99–44.53, an inside day under Monday's $45.45 high, on
  light volume (0.96M by 9:20 CT). The trigger is a break of $45.45 on ≥2x volume, but the calls are
  counter-regime, so it can't trade while the brake is on. Day 3 of 10.
- **CCI: not yet.** Range $85.71–87.27, holding the $85 flag floor, on light volume. Day 3 of 10.
- **XYL | PUT | EP-down (Q3 EPS $1.44 vs $1.45 est, 10/27 am) | V2/S1/C2/RS1/R2 = 8 (A on score, GATES
  FAIL) | ADR 2.2% (under the 4% bar) | gapped −9% to a new 52-week low of $97.38 (it fell from a $127
  90-day high, bounced to $108, and is now breaking down). 1.4M shares in 50 min vs. a 2.07M daily
  average | GATES: ~3.4 ADR under the 10-EMA ($106.1), low ADR | TRIGGER: a weak bounce toward
  $102–104 that fails, then a break of the bounce low on ≥1.5x volume | INVALIDATION: close above
  $106 (the 10-EMA) | watch name, trades only at A+ | added 2026-10-27**
- **BA | PUT | EP-down / breakdown (Q3 EPS −$0.34 vs −$0.20 est, 10/27 am) | V2/S1/C2/RS2/R2 = 9 (A+ on
  score, GATES FAIL) | ADR ~1.9% (under the 4% bar) | Prior decline from $240 (8/5) to $184. Then a
  4-week $182.4–193 base, which broke today on the gap to a new 52-week low of $176.67, on 7.2M shares
  by 9:37 CT (already above the 6.3M daily average) | GATES: ~3 ADR under the 10-EMA (~$188.6), and
  ~1.4 ADR past the $182.4 breakdown level (DON'T CHASE) | TRIGGER: a weak bounce back toward
  $182–184 (the old base low, now resistance) that fails, then a break of the bounce low on ≥1.5x
  volume, with the 10-EMA within ~2 ADR | INVALIDATION: close back above $184 | CONTRACT: ~0.40Δ
  put 3–4 weeks out (Nov 20). Check the cost: a ~$180 strike may be $5+ (>$500), which is over the
  15% brake cap, so it may be unaffordable | added 2026-10-27 (autopilot cycle 1)**

### Session 2026-10-26 (Mon, 9:53 AM CT) — regime RISK-OFF (bouncing), DRAWDOWN BRAKE ON (A+ only, 15% size)

- **GMAB (day 2): the gap held, but the pullback never came, so it is not triggered.** Opened $44.79,
  above Friday's $44.34 high, and printed a new 52-week high at $45.45. Volume is running well above
  pace (2.84M in 23 min vs. a 4.6M daily average). The GAP-DAY trigger needs a pullback that holds
  $39.6–42 or the 10-EMA, so today's gap-and-go is not the entry. It also can't trade while the regime
  is RISK-OFF and the brake is on. Keep it. The next valid trigger is a 3–10 day flag, then a break of
  its high. Day 2 of 10.
- **CCI (day 2): not yet.** At $88.70, holding above the $85 flag floor but below the $91.45 day-1 high,
  on light volume (1.9M by 9:53 CT). Day 2 of 10.
- **NU | PUT | EP-down (Brazil runoff result, 10/25) | V2/S1/C2/RS1/R2 = 8 (A on score, but GATES
  FAIL) | ADR ~3% | the 10/5 gap-up base ($15.2–16.2) failed in one session: opened $11.65 (−23%)
  on 166M shares in 23 min (2.5x the daily average) and is bouncing to $12.03 | GATES: a −20%+ flush
  (put rules ban buying it), ~7 ADR under the 10-EMA (~$15.1, EXTENSION LIMIT), put IV is surely
  >70% (GAP-DAY rule) | TRIGGER: first weak bounce on fading volume toward $12.8–13.4 (the 9/28–10/2
  base, now resistance), which stalls and then breaks the bounce's low on ≥1.5x volume, with put IV
  cooled under ~70% | INVALIDATION: close above $13.50 | CONTRACT: ~0.40-delta put, 3–4 weeks out
  (≈ Nov 20 $12P), with OI >500 and spread <15% checked at trigger. Note the $11.20 52-week low
  just below. | added 2026-10-26**
- **PBR | PUT | EP-down (same catalyst) | V2/S1/C2/RS1/R2 = 8 (A on score, GATES FAIL) | ADR ~2%
  (under the 4% bar) | opened $21.50 (−18%) from a fresh 52-week high ($26.39 on 10/23); 43M shares
  in 23 min (2.4x the average); range $21.38–22.41 | GATES: ~8+ ADR under the 10-EMA, IV spiked,
  low ADR | TRIGGER: same bounce-fail pattern toward $23–23.8 (the 10/5 gap open area), then a break
  of the bounce low on volume | INVALIDATION: close above $24 | watch name, trades only at A+ |
  added 2026-10-26**

### Session 2026-10-23 (Fri, 1:48 PM CT) — regime RISK-OFF, DRAWDOWN BRAKE ON (A+ only, 15% size)

- **GMAB | call (counter-regime) | EP day-1 gap to new 90-day highs | V2/S1/C1/RS2/R0 = 6 (B) |
  ADR 3.6% | prior move +43% in 3 mo, 4-week rising base $36–40 | +9% to ~$43.6 on 1.8x relvol by
  1:48 CT | TRIGGER (day 2+, GAP-DAY RULE): pullback that holds today's low (~$41.5–42 area,
  re-check at the open) or the rising 10-EMA, then a 5-min ORH reclaim of the prior day's high on
  ≥2x volume — AND the regime back to at least CHOP (counter-regime calls cannot reach A+ while the
  brake is on) | INVALIDATION: close below the gap-day low | CONTRACT: Nov 20 $45C, check OI > 500 /
  spread < 15% at trigger (catalyst not yet verified) | added 2026-10-23**
- **CCI | call (counter-regime) | EP day-1 gap | V2/S1/C2?/RS1/R0 = 5–6 (B) | ADR 3.2% (under the
  4% bar) | +10.2% to ~$86.9, through the $83.26 90-day high on 2x relvol | TRIGGER: day-2+ flag
  that holds ~$85 and breaks today's high on ≥2x volume, regime ≥ CHOP | INVALIDATION: close below
  $83.26 | added 2026-10-23. Low ADR, so it's a watch name; it trades only if it gets to A+.**

## Recently removed

- **Removed 11/2:** XYL's chain fails liquidity: the Nov 20 $95P has a $1.30/$2.95 spread (78% of mark), and the $92.5P has OI of 12.
  A spread doesn't fix that, so it's dropped (it bounced to $96.8 and the alert fired). **Passed 11/2 (losers scan):** DRUG −61%,
  OFRM −38%, PGEN −25% (flushes, small caps), MRVL −7.8% ($181, a second leg down after 10/29, but the puts are unaffordable),
  LITE −13% ($730), KRYS −14% ($285), and the rest are small, illiquid caps. Leaders Pullback (PTC, ANF, COP, ELF, KOD,
  DOCU, FRO, APA, BOX…): calls are counter-regime in RISK-OFF.

- **Removed 10/29:** GMAB gapped another +28% on 10/28 to $57.29 (8x volume). It is ~4 ADR over the 10-EMA, and earnings on
  11/5 fall inside any hold. The old flag thesis is gone, so it needs a fresh base after earnings.
- **Passed 10/29 (losers scan):** NOW −24%, FTNT −21%, IOVA −32% are −20%+ flushes, which the put rules ban. GOOGL −12% is
  ~7 ADR under its 10-EMA (EXTENSION LIMIT). SFM −19% is ~7 ADR under. MRVL −12.7% ($219) is within ~1.8 ADR of its 10-EMA,
  but it is a leader in a +37% 3-month uptrend (RS 0 for puts) and its puts are ~$1,500, far over the cap. ALNY −15%
  ($198) is ~4 ADR under and too expensive. Gainers (ADT +34%, GKOS +26%, CROX +23%, CVNA +17%…) are all day-1 gaps,
  so they're watch-only. Leaders Pullback Watch (PTC, ANF, ELF, DOCU, WIX, GTLB, RBLX, BOX, ZETA): these are calls in
  CHOP with no fresh catalyst, so they max out at A (8) and can't trade under the brake. RBLX reports tonight, and ELF/PTC
  report 11/4. Smart Money Flow (AURA, FTNT, NOW, SFM, GOOGL, SRCE): nothing actionable.

- **Passed 10/27:** INOD −23.6% (a −20%+ flush, which the put rules ban), CTAS −6.7% (an earnings
  reversal off a fresh 52-week high: no puts against a stock making new highs; ADR 1.7%), UNF −14% ($240,
  thin chain, ADR 2.7%), HSBC −6.1% / WELL −5.5% (ADR 1.2–2.0%), MRNA −5.4% (a pullback inside
  a +230% 3-month uptrend, above the rising 50-EMA, with earnings 11/5), refiners VLO/MPC/PSX −4–6% (low
  relvol; MPC/PSX are leaders pulling back, not breakdowns). Gainers: SOFI +11% (1.4x relvol at 50
  min, a day-1 gap), CLS +10%, NBIS +8%, BE +8%: all day-1 gaps or counter-regime calls. Leaders
  Pullback Watch (19: MSFT, PLTR, CRM, TEAM, SHOP, GTLB, ZETA, IOVA…): calls are counter-regime and
  capped at A, so none can trade under the brake. Smart Money Flow (AURA, INSM, DBD, FFIN, THG): nothing actionable.

- **Aged out / invalidated 2026-10-23 (stale since 10/8, 11+ sessions):** SMCI ($32.87, far below
  the $41.74 invalidation), NKE ($37.40, back above the 10-EMA, so the put thesis is dead), XP and
  PBR (Brazil runoff 10/25 binary exit date reached), PENG ($54.98, below the $64.21 invalidation),
  SNOW ($321.8, below $328), CRWD (aged out; +6.7% today at $253.9 but never cleared $276.90),
  DOCU ($84.8, broke out through $74 with no entry while unmonitored. Its options chain was too
  thin to trade anyway).
- **Passed 10/26:** XP −51% / STNE −30% / PAGS −27% / AFYA −27% / ITUB −24% (Brazil runoff flush,
  all past −20%, so the put rules ban them; ITUB/STNE/PAGS chains are thin anyway), MELI −10.8% ($1,615,
  unaffordable), FICO −7.8% ($752, unaffordable), RDDT −5.3% / CRCL −6.7% (0.5–0.7x relvol, so volume
  fails). Gainers: SGRY +46% (12x relvol, fresh gap: day-1 watch only, 74% IV, small cap), XNCR +24%, RRC
  +15% (nat-gas gap). All are day-1 gaps (GAP-DAY RULE), and calls are counter-regime under the
  brake. Leaders Pullback (17 names: MSFT, PLTR, CRM, TEAM, SHOP, ZETA…): calls, so counter-regime
  and capped at A.
- **Passed 10/23 (losers scan, RISK-OFF puts):** LKQ -21.5% / CORT -19.7% (−20% flushes: the put
  rules ban these), BE -11% (IV 93% > 70% gap-day gate; ~2.9 ADR under its 10-EMA), CRDO -8.7%
  (new lows, but ~2.7 ADR under the 10-EMA: EXTENSION LIMIT), T -7.1% / TMUS -6.6% (ADR 2.1–2.4%,
  4 ADR under the 10-EMA), TNGX/FLG/WGS (small caps, liquidity). Leaders Pullback Watch (PLTR, CRM,
  MSFT, ULTA, MPC/PSX, ZETA…): calls are counter-regime, which caps them at A, and A cannot trade
  while the brake is on.

- **Passed 10/8 (Leaders Pullback Watch):** ANF (good base, but options OI 1–73), MSFT/NTNX/DT (ADR
  2.1–2.9%), LITE ($1,080, unaffordable), NET (earnings 10/29 inside the hold), MRNA (+303% in 3 mo,
  earnings 11/5), SMTC (loose: 24% 10-day range), ELF/RNG/ERO (earnings 11/2–11/4; ERO also a 22%
  pullback below its 10-EMA), PANW/RBRK (same cyber theme as CRWD; CRWD is the cleaner pullback).

- **Passed 10/8:** PCRX (+44%, pinned at $36.27–36.33 on 2.2M shares in 10 min, so a cash deal is
  likely; merger-arb pattern), HELE (+21% on the FQ2 beat/raise but faded from $31.94 to $29.2 in
  10 min, avg volume 0.38M, options thin), WOLF ($1.5B Dept. of War loan commitment is a real
  catalyst, but the Oct 23 $35–38C have OI 6–88 and spreads 40–70% of mark: liquidity fails on
  both tests, which a spread does not fix; fading from $35.93 ORH), ARGX (-10.8% at $828:
  unaffordable), AAOI/COHR (-4% pullbacks inside uptrends: no puts against leaders).

- **Passed 10/5:** PTC (+33%, 21x volume; pinned in a $192.4–196 range all day: Autodesk deal
  pattern, merger arb), RXO (pinned $28–29: same pattern), PCVX (opened $87, faded to $72:
  failed gap), NVAX (+20% intraday from noon, unexplained, LOD 22% below = chase), ITUB/NU/STNE/
  PAGS (ITUB Oct 16 $10C OI 10 / spread 33%; PAGS LOD 2 ADR below; STNE fading; NU in a downtrend).

- **SYNA (10/2)** — +14.6% gap on 3x volume is an AMENDED ALL-CASH TAKEOVER by ON Semi at $123/sh.
  Price pinned at ~$121.6: merger arb, no upside to a call. Permanent pass.

(none)
