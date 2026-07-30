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

## Open positions

### Robbin — agentic account (452369101)

(none — 100% cash. Ledger $739.86 vs broker buying power $839.40; $99.54 unreconciled as of 2026-07-30.)

### Owner's personal account (439441866) — advisory positions, logged retroactively 2026-07-30

Both entries below were RECOMMENDED BY A PRIOR AGENT SESSION on 2026-07-29 and executed by the
owner in-app. Neither was logged at the time. The next session opened blind and had to
reverse-engineer them from raw contract IDs, then wrongly told the owner they were self-directed.
Logging advisory flags is now a PERSONA requirement because of this.

#### PSN $35P/$30P Aug 21 x3 — bear put debit spread (EP-down) — OPEN, −83%
- **Entry:** $0.88 net debit x3 = **$264**, 2026-07-29 11:13 AM ET (order 6a6a189a)
- **As advised:** "Level-3 idea — grade B+", net debit ~$1.00, max risk $100/spread, 4:1 payoff,
  break-even $34.00. Owner filled better ($0.88) but sized 3 spreads vs the 1 implied.
- **Thesis as given:** PSN $38.14 (−38%) after Q2 miss + guidance cut — "textbook Qullamaggie
  episodic-pivot-down, continued downside is the base case." Debit spread chosen to neutralize
  IV blown out to 74–83%.
- **Current:** PSN $42.20 (bounced off the $36.26 low), spread ~$0.25 → $75. **−$219.**
- **Why it was wrong — two hard gates skipped, not weighed:**
  1. **LIQUIDITY (fatal):** persona requires OI > 500. $35P OI 450, $30P OI 151 — *every* strike
     in the chain fails. This is an automatic reject before any thesis. It is also why the
     position is now near-unexitable: the $30P has printed a $0.00 bid.
  2. **TIMING:** bought ON the −38% panic day. Persona bars puts after a −20% flush with IV
     blown out and prefers the first weak bounce into the declining 10/20-day EMA. A debit
     spread fixes expensive premium; it does not fix buying the flush.
- **Grade: D.** B+ was far too generous. Correct action was a pass on liquidity alone.

#### F $16C Aug 21 x3 — post-earnings continuation — OPEN, −71%
- **Entry:** $0.45 x3 = **$135**, 2026-07-29 11:07 AM ET (order 6a6a1721)
- **As advised:** "a real, qualifying trade... clears every hard gate — grade B", sized 1
  contract (~$69) at ~$0.69. Owner took 3 at a better price.
- **Thesis as given:** Q2 beat +24% w/ raised FY guidance, elite liquidity (OI ~9,900, 2.9%
  spread), cheap IV 37%, no pending binary event.
- **Current:** F $14.72, mark $0.13 → $39. **−$91.50.** The earnings gap has fully round-tripped
  ($14.96 pre-print close → $14.72), so the thesis is objectively invalidated — a thesis-stop exit.
- **Why it was wrong:** the write-up named the disqualifier itself — "a slow mega-cap recovering
  INTO resistance, not an explosive breakout to new highs" — and recommended it anyway as "the
  only knock." Setup quality is not one gate among many; it IS the trade. Liquidity and IV are
  necessary, not sufficient.
- **Grade: D+.** The analysis was honest; the conclusion ignored it.

#### SOFI — 100 shares @ $18.10 + short $20C Aug 14 — covered call — OPEN
- Shares $1,588.50 (−$221.50). Short call collected $90, now $3.50 → **+$86.50 (96% captured)**.
- Roll to the $18C Sep 18 for ~$0.51–0.56 net credit was advised 2026-07-30; owner working it.
- The covered call absorbed 39% of the share drawdown — this leg did its job.
