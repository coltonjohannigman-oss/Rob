# Personal Account Advisory Log

Ideas for the owner's personal Level 3 account. Robbin never executes these — the owner
places every order manually. Maintained by `/personal`; candidates are handed over by
`/trade` and `/autopilot`.

---

## Candidates

Setups Robbin's own sessions scored well but could not trade for a spread-fixable reason
(e.g. IV spiked past the buying gate). `/personal` re-checks these live and drops them after
5 sessions or on invalidation.

Format: **date | ticker | direction | score (V/S/C/RS/R = total) | why Robbin couldn't trade it | suggested structure**

All from the 2026-09-27 prep. Scores assume the trigger fires with ≥2x volume; none is live yet.
Robbin can't trade any of them because a single 2–4 week call costs more than 30% of his account.

- 2026-09-27 | PLTR | call | S2/C1/RS2/R2 (+V) | ~$190 stock | 3-day flag $188.24–194.68 at the
  all-time high, volume drying up (0.50x) | call debit spread; trigger ORH > $194.68
- 2026-09-27 | ANET | call | S2/C1/RS2/R2 (+V) | ~$207 stock | 3-week base, pivot $212.00,
  ~4% under the high, volume drying up | call debit spread; trigger ORH > $212.00
- 2026-09-27 | INTC | call | S2/C1/RS2/R2 (+V) | ~$123 stock | +34% in 3 weeks, then a 4-day flag
  $119.44–127.44; Pelosi share + call buys disclosed 8/24 | call debit spread; trigger > $127.44
- 2026-09-27 | BE | call | S1/C1/RS2/R2 (+V) | ~$289 stock | closed near the $292.72 pivot; wide
  swings (ADR 6.5%); Pelosi buys disclosed 8/24 | call debit spread; trigger > $292.72
- 2026-09-27 | DELL | call | S1/C1/RS2/R2 (+V) | ~$563 stock | volatile 530–595 range, pivot
  $595.51 | call debit spread; trigger > $595.51
- 10/2 re-check (9:20 CT): none triggered — PLTR $192.19 (< $194.68; owner holds a Nov 6 $210C
  instead), ANET $205.43 (< $212), INTC $124.57 (< $127.44), BE $289.19 (< $292.72), DELL $563 (< $595.51).
  Session 5 of 5 — all expire after today's close unless triggered.
- 10/5: all five 9/27 candidates expired (session 5 of 5 was 10/2, none triggered) — dropped.
  /trade 10/5 handed over nothing: XP/ITUB failed on open interest, which a spread does not fix.
- Watch, not a candidate: MU reports Wed after close (EPS est. $31.50). A post-earnings credit
  spread becomes possible Thursday if the reaction holds a level on volume.

## Ideas

Every idea `/personal` presents, with its outcome once the owner reports it — this is how the
advisory side's quality gets measured.

Format: **date | structure (strikes / expiries / qty) | debit or credit | max loss / max gain | grade | outcome**

- 2026-10-02 | SOFI covered call: sell 1 Nov 20 $19C against 100 sh (cost $18.10) | credit ~$0.39 ($39) |
  no added loss risk; caps shares at $19 (+$90 + $39 if called) | A (income) | pending owner
- 2026-10-02 | PLTR management: convert held Nov 6 $210C (paid $6.90) to a 210/230 call spread by
  selling 1 Nov 6 $230C at ~$3.20 | credit ~$3.20 | at-risk $690 -> ~$370; max value $20 (~$1,630 gain
  from $3.70 net) | management (earnings 11/2 pm inside expiry) | pending owner
- 2026-10-05 | status: SOFI covered call NOT placed; PLTR conversion NOT placed (no orders on ••••1866 since 10/1).
- 2026-10-05 | ACN management: 10 sh bought 10/1 @ $216.70 on the earnings gap; gap FAILED (gap-day low
  $211.04 broke 10/2; $194.78 now, 60% of the $183.37->$216 gap retraced) | sell 10 sh at ~$194.80 =
  -$219 realized (-4.9% of acct), or hard stop at $183 (gap fill, -$337 total) | management: SELL |
  pending owner
- 2026-10-05 | SOFI covered call (re-quoted): sell 1 Nov 20 $19C vs 100 sh (cost $18.10, now $16.08) |
  credit ~$0.34 ($34; bid .34/ask .35, OI 9,989, delta 0.22, 46 DTE) | no added loss risk; caps at $19
  (+$90 + $34 if called); SOFI earnings 10/27 inside expiry | A (income) | pending owner
- 2026-10-05 | PLTR management (re-quoted): sell 1 Nov 6 $230C @ ~$2.25 against held $210C (mark $5.63,
  -18.5%) | credit $2.25 -> net basis $4.65, max value $20 (max gain $1,535), BE $214.65; theta drops
  from -$17.84/day to -$6.11/day | exit if PLTR closes < $184.81 (flag low) or the $210C < ~$4.85 (-30%);
  earnings ~11/2 pm inside expiry | management: CONVERT if holding into earnings | pending owner
- 2026-10-05 | no new A+ idea: the 2% max-loss rule ($89 on a $4,458 account) rules out every scanned
  spread (e.g. NKE post-earnings bear call 35/37.5 would need a $1.61 credit to fit) | pass
