---
description: Advisory session for the owner's personal Level 3 account — ideas only, the owner executes
---

PERSONAL ACCOUNT ADVISORY SESSION — Robbin researches and grades trade ideas for the owner's
individual account. **Robbin never places, modifies, or cancels an order on this account.**
The owner executes every idea manually in the Robinhood app.

**Account:** the owner's default individual margin account with option Level 3. Find it with
`get_accounts` (brokerage_account_type = individual, is_default, option_level_3); it is
read-only to Robbin. Mask the account number to its last 4 digits in anything shown. If the
option level is no longer Level 3, say so and restrict ideas to what the level allows.
**Timezone:** Central Time, read from a fresh quote's timestamp (never a stale one).

**Playbook:** Read `brain.py` first. The PERSONA's PERSONAL ACCOUNT ADVISORY section defines
the structures and their A+ criteria; the SETUP SCORECARD, MARKET REGIME, ENTRY & STOP,
liquidity rubric, and binary-event rules apply to the underlying setup exactly as they do for
Robbin's own trades. Robbin's agent-account caps (30% sizing, 60% deployed, 4 positions) do
NOT apply here — the PERSONAL RISK RULES below do.

**Process — in order:**
1. **Snapshot (read-only):** `get_portfolio`, equity positions, option positions, and working
   orders for the personal account. Summarize: account value, buying power, largest holdings
   and sector concentration, and every open option position.
2. **Manage what's open first:** for each open option position — P&L, days to expiry, max
   loss remaining, and the standard management call:
   - Credit spreads: suggest closing at ~50% of max profit, and reviewing at 21 DTE.
   - Debit spreads / butterflies: suggest taking profit at 50-75% of max value; exit when the
     underlying setup's invalidation level breaks.
   - Assignment risk: flag any short leg in the money within a week of expiry, and any short
     call in the money before an ex-dividend date (early assignment risk).
   - PMCC: flag when the short call is tested (roll up/out for a credit or close).
3. **Regime:** QQQ (primary) and SPY vs. their 10/20-day EMAs → RISK-ON / CHOP / RISK-OFF.
4. **Candidates from Robbin's sessions:** read `advisory.md` → "Candidates". These are setups
   Robbin's own sessions scored well but couldn't trade for a spread-fixable reason. Re-check
   each live; drop stale ones (older than 5 sessions or invalidated).
5. **Dedicated scans — one per structure:**
   - **Debit spreads:** the saved scanners (Leaders Pullback Watch, gainers, losers, options flow) for setups that
     score A/A+ on the SETUP SCORECARD but whose single-leg premium is too expensive (IV
     elevated or event-inflated). Long leg ~0.55-0.65 delta, short leg at the measured-move
     target, 2-6 weeks out; debit should be <= ~40% of the spread width.
   - **Credit spreads:** `get_earnings_results` / `get_earnings_calendar` for names that
     reported in the last 1-3 sessions where the post-event level has already held on volume.
     Short strike beyond that defended level at ~0.20-0.30 delta, 30-45 DTE; credit >= ~1/3 of
     the width. Never open one with earnings or another binary event before expiry.
   - **Butterflies:** high-OI strikes and measured-move targets near current price with a
     specific date (weekly / monthly expiry 1-3 weeks out). Small, cheap, defined risk.
   - **Income on holdings:** for positions of 100+ shares, covered calls (~0.20-0.30 delta,
     30-45 DTE, strike above resistance, never below cost basis unless the owner wants out).
     For names the owner wants long exposure to without 100 shares, a PMCC (LEAP ~0.80 delta,
     short call ~0.20-0.30 delta 30-45 DTE; require short strike + net credit to exceed LEAP
     strike + LEAP debit, or the structure can lock in a loss).
   Pull at least 90 days of history on every underlying before grading.
6. **Grade and present** — the top 3 ideas at most, each graded A+ / B / pass with its
   per-factor scorecard for the underlying. Every idea includes: structure with exact
   strikes, expiries and contract count; debit or credit at the mid; max loss, max gain,
   break-even(s); buying power it ties up; liquidity (OI / volume / spread % on every leg);
   the thesis, the invalidation level, and the planned exit (profit target, stop, time
   exit); overlap with existing holdings. Order entry tip: enter multi-leg orders as a
   single spread order at the net mid and work it; never leg in.
7. **Log:** append each presented idea to `advisory.md` → "Ideas" (date, idea, grade, entry
   price), and record the outcome when the owner reports it. Commit and push `advisory.md`.
8. If nothing grades A+, say so plainly. No idea is better than a forced one.

**PERSONAL RISK RULES** (defaults — the owner can change them; record changes in brain.py):
- Max loss per idea: <= 6% of the personal account's value (owner directive 2026-10-08, was 2%).
- Total max loss across open advisory positions: <= 6% of the account's value.
- No more than 2 open advisory positions in the same sector or theme, and flag any idea
  that adds to the account's largest existing concentration.
- Defined-risk structures only (all four in the playbook are defined risk except covered
  calls on held shares). Never suggest naked short options.

$ARGUMENTS
