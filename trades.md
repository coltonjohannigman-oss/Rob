# Robbin Trade Journal

One entry per closed trade, appended at close. Open positions tracked at the bottom.
Grade the setup honestly after the fact — this is how the system learns.

Format: **Ticker contract | setup type | entry → exit | P&L | what went right / wrong**
From 2026-09-27 on, each entry also records its SETUP SCORECARD at entry
(V/S/C/RS/R = total, grade) and contract count, so `python cli.py stats` can audit quality by grade.
Trades 1-3 predate the scorecard and are ungraded in the stats.

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
