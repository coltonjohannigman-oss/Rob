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

## Active

- **SMCI | call | momentum base breakout | V?/S1/C1/RS2/R2 = 6 now, 8 (A) if volume confirms |
  ADR 5.4% | prior move +41% in 3 mo | TRIGGER: 5-min opening-range high break above $43.76
  (Friday high) with volume on pace for ≥2x the 50-day average | INVALIDATION: close back below
  $41.74 (base top); stop = entry-day low of day | CONTRACT: Oct 16 $45C (mark $2.24, spread
  0.9%, OI 11,384, delta 0.45, IV 75%) — 1 contract = $224; target $48–51 (measured move / prior
  high) ≈ 3:1 reward:risk | EVENT RISK: MU earnings Wed after close — apply the binary-event rule
  at Wednesday's close | added 2026-09-27**
  - Don't chase: skip if SMCI is already above ~$46.10 (1 ADR past the trigger) when checked.
  - Sizing blocked until the ledger is reconciled: $224 exceeds 30% of the ledger's $739.86,
    but fits 30% of the broker's $1,023.65.

  - 10/2 status (8:36 CT): $42.67, NOT triggered (ORH trigger $43.76). Base widened: closes of
    $41.02/$41.07 on 9/29-9/30 dipped under the $41.74 base top, but the $40.13 base low held and
    MU earnings + the jobs print are now behind it. Session 5 of 10. Kept.
  - 10/5 status (2:09 CT): $43.08. Probed $44.05 (above the $43.76 trigger) but volume is NOT
    there — 15.3M by 2:09 CT ≈ 0.6x pace vs the 36M average. Volume 0 = automatic pass; faded back
    under the trigger. Session 6 of 10. Kept; alert set at $43.76.
  - 10/8 status (8:41 CT): $43.36 (-3.5%). The 10/7 session cleared $43.76 and ran to $45.77
    (close $44.94) on 40.5M ≈ 1.1x — a breakout WITHOUT volume, so it never qualified. Today it gave
    the move back below the old trigger. NEW TRIGGER: 5-min ORH break above $45.77 with ≥2x volume;
    don't-chase above ~$48.20. Invalidation unchanged (close < $41.74). Contract re-quote: Oct 23 $47C
    $1.75 (delta 0.41, IV 70%, OI 1,160, spread 6.9%) or Oct 30 $47C $2.34 (OI 2,569). Session 9 of 10 —
    drops after the next session unless it triggers. Alert moved to $45.77.

- **NKE | put | EP-down / breakdown | V2/S0/C2/RS2/R0 = 6 (B) | ADR 2.9% | prior decline $46 -> $35
  in 3 mo | Q1 FY27 earnings 10/1 pm: EPS beat (0.48 vs 0.44), stock gapped -6.6% to new 52-week
  lows ($31.97) on 30M shares in the first 6 minutes (30-day avg 37.5M/day) | TRIGGER: a weak,
  low-volume bounce into the declining 10-day EMA (~$35.3-35.9) that is REJECTED, with put IV
  still under ~45% | INVALIDATION: close above the 10-day EMA on volume | CONTRACT: Oct 23 $33P or
  $34P re-checked at trigger (10/2 open: IV 34-38%, cheap; but spreads 23-37% of mark this early,
  OI ~1,000-1,600) | added 2026-10-02**
  - Why not today: counter-regime (QQQ risk-on) caps it at A only with perfect other factors, and
    structure scores 0 — at $33.10 it is ~2 ADR below the $35.00 breakdown level (chasing), gap is
    6.6% not the 10% EP standard, and ADR 2.9% is under the 4% focus-universe bar. Spreads fail too.
  - NVO lesson applies (trades.md 9/23): a trend this persistent may never bounce. The candidate
    half-size breakdown-day amendment is still the owner's call and is NOT adopted.
  - 10/5 status (2:09 CT): $33.70, range $32.76–34.12, never reached the 10-EMA bounce zone.
    Not yet. Session 2 of 10. Alert set at $35.30.
  - 10/8 status (8:41 CT): $34.03. 10-day EMA has declined to $34.99; 10/6 high $34.62 was the
    closest approach. Not yet. Session 5 of 10. Alert at $35.30 kept.

- **XP | call | EP day-2 continuation (Brazil election) | V2/S1/C1/RS2/R2 = 8 on score, but GATES
  FAIL today | ADR 3.8% (pre-gap) | prior move +30% in 3 mo ($16.60 -> $21.50, at 90-day highs) |
  CATALYST: Flavio Bolsonaro 47% vs Lula 45% in the 10/4 first round (beat polls); Brazil ADRs
  ripped 10-33% on 10/5. XP +33% on ~3.3x volume, opened $25.84, ran to $29.00 by 10:00 CT, then
  held a tight $28.14–29.00 flag for 4+ hours | WHY NOT TODAY: (1) LOD stop $25.84 is ~10% below
  = 2.6 ADR (gate is ≤1 ADR); (2) liquidity — Oct 23 $29C OI 0, spread 21% (strikes are brand-new).
  | TRIGGER (10/6+): 5-min ORH break above $29.00 with volume on pace for ≥2x, day-2 LOD within
  ~1 ADR as the stop, AND the chosen strike shows OI > 500 / spread < 15% | INVALIDATION: close
  below $27.80 (flag low) | CONTRACT: Oct 16 $29C (mark $1.18, delta 0.50, IV 63%) or Oct 23 $29C
  (mark $1.45) — re-check OI | BINARY EVENT: Brazil runoff Sun 10/25 — exit by Fri 10/23 close,
  no holding through the runoff | added 2026-10-05**
  - 10/8 status (8:41 CT): $30.18. Day-2 (10/6) opened $29.25, ABOVE the trigger, so the ORH entry
    never set up; 10/7 made $30.215 on 14.3M. Today testing that high on light volume (~260K in
    10 min). NEW TRIGGER: ORH break above $30.22 with ≥2x volume and LOD within 1 ADR. Invalidation
    unchanged ($27.80). Session 3 of 10. Alert moved to $30.22.

- **PBR | call | EP day-2 continuation (Brazil election + oil) | V1/S1/C1/RS1/R2 = 6 (B) |
  ADR 2.4% (under the 4% bar) | +14% gap to new 90-day highs ($21.99 prior) | WHY NOT TODAY: LOD
  $23.54 is 4.5% below = 1.9 ADR; volume only ~1.2x by 2 PM | TRIGGER: 5-min ORH break above
  $24.76 with ≥2x volume and day-2 LOD within 1 ADR | INVALIDATION: close below $23.54 | CONTRACT:
  Oct 23 $25C (mark $0.76, spread 10.5%, vol 340, OI 0 — new today, re-check; delta 0.47, IV 41%)
  | same 10/25 runoff rule | added 2026-10-05**
  - 10/8 status (8:41 CT): $24.41. Poked $24.77 (one cent through the trigger) in the first 5 minutes
    and faded straight back to $24.41. No hold, so no trigger (a hold above $24.76 with ≥2x volume
    would score 7 = A). Session 3 of 10. Alert at $24.76 kept.

- **PENG | call | EP day-3 pullback (FQ4 rev +68%, FY27 guide +40%) | V1/S1/C2/RS1/R2 = 7 on score,
  IV GATE FAILS | ADR 5.9% | gap 10/6–10/7 from $60.71 to $76.10 high on 15–21M (avg 2.3M) |
  10/8: opened $72.50, low $70.40, back to $74.23 | TRIGGER: pullback into $66–70 that holds,
  then a 5-min ORH reclaim on volume, AND Oct 23/30 ATM IV back under ~80% (89% today) |
  INVALIDATION: close below $64.21 (10/6 close) | CONTRACT: re-check Oct 23 $75C/$80C at trigger |
  added 2026-10-08**
  - Lesson from trade #12 (10/7, -34.9%): at 90%+ IV a single contract at 21% of the account
    cannot survive ordinary post-gap noise. Only re-enter after IV cools.
  - Theme cap: XP + PBR = 2 Brazil names, the sector maximum.

### From the first Leaders Pullback Watch run (2026-10-08, 9:42 CT) — new GAP-DAY/EXTENSION rules apply

- **SNOW | call (personal-account spread) | 5-week base | V?/S2/C1/RS1/R2 = 6 now, 8 (A) with ≥2x
  volume on the break | ADR 3.9% | prior move +77% (6m +123%), then a $316.6–349 range since early
  Sept with volume drying (0.5–0.7x), back above the rising 10/20-day EMAs | TRIGGER: 5-min ORH
  break above $349.00 (10/6 high) with ≥2x volume | INVALIDATION: close below $328 (10/7 low area /
  20-EMA) | CONTRACTS: Oct 30 350/360 call spread was $3.58 ($358 = 8%, over the 6% cap) and both
  legs OI < 300, so price a $5-wide or the Nov 20 monthly at trigger; agent account can't afford
  single-leg ($12+) | earnings late Nov, clear | added 2026-10-08**
- **CRWD | call (personal-account spread) | trend pullback to the rising 10-day EMA | V?/S1/C1/RS2/R2
  = 6 now, 8 (A) with ≥2x volume | ADR 4.7% | 9/14 cybersecurity-wide gap (+14%, 2.6x; PANW/RBRK/NET
  gapped the same day), trended $205 -> $287 (10/6), 10/7 pulled back to $264.5 = the 10-EMA on
  0.9x volume | TRIGGER: break of $276.90 (10/7 high) with ≥2x volume | INVALIDATION: close below
  the 20-EMA (~$253) | CONTRACTS: Oct 30 285/290 call spread $1.48 ($148, 29.5% of width, max gain
  $352) but legs OI 309/291 (< 500) and long-leg delta 0.36, so re-check OI or use Nov 20 at
  trigger | theme: cyber, max 2 (PANW is the alternate) | earnings Dec, clear | added 2026-10-08**
- **DOCU | call | 4-week base, tightest structure on the list | V?/S2/C1/RS1/R2 = 6, 8 with volume |
  ADR 3.7% | $63.9–74.1 range since 9/15, last 10 days $66.8–70.8, volume 0.6–0.8x | TRIGGER: break
  of $70.80 with ≥2x volume (then $74.07) | INVALIDATION: close below $66.80 | LIQUIDITY BLOCKS
  IT: Oct 30 strikes OI 11–104 with 19–37% spreads; Nov 20 70C OI 71 ($4.13, also over the agent's
  $284 cap). A spread doesn't fix OI. Watch-only unless OI builds | added 2026-10-08**

## Recently removed

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
