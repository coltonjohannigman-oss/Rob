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
- Watch, not a candidate: MU reports Wed after close (EPS est. $31.50). A post-earnings credit
  spread becomes possible Thursday if the reaction holds a level on volume.

## Ideas

Every idea `/personal` presents, with its outcome once the owner reports it — this is how the
advisory side's quality gets measured.

Format: **date | structure (strikes / expiries / qty) | debit or credit | max loss / max gain | grade | outcome**

(none)
