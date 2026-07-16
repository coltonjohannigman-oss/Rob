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

### 4. WULF $18P Jul 31 — Breakdown/Downtrend (bearish #2) — CLOSED 2026-07-16 ✅ +$47 (+42.7%)
- **Entry:** $1.10 x1, 2026-07-14 (owner in-app fill, order 6a569290; agent's $1.05 limit
  cancelled unfilled — the nickel for certainty was worth it, echoing GRND).
- **Exit:** $1.57 — user-confirmed TP limit a hair above mid (order 6a591131), filled 12:55 PM
  CT on day 3 of downside follow-through. Inside the puts-specific 30-50% band bias.
- **Thesis:** Broken momentum leader: −26% over 7 sessions, $427.6M Q1 net loss, sold off even
  on the good-news Anthropic-lease headlines, weak bounce rejected at declining 10d EMA 7/9,
  then a ~1.7x-volume break of the 3-month $19-20 shelf on 7/14 — with CLSK/BMNR ripping the
  same day (relative weakness, not sector drag). WULF fell $19.59 → $17.9 by exit.
- **Right:** First put trade under the BEARISH SETUPS section and it played to script. Volume
  gate + chart gate did their jobs; day-1 entry on the shelf break was correct even though the
  breakdown took 2 days to confirm. Stop ratchets $0.80 → $1.05 → $1.30 meant the winner could
  never round-trip. Sold into strength, not into the bounce.
- **Wrong / lessons:** (1) Cancelling the stop at 8:36 AM CT before Robinhood's 9:45 AM ET
  stop-market window left the position naked to a rejection — saved by a stop-LIMIT guard;
  mechanic now in PERSONA. (2) The TP limit occupied the single order slot for ~40 minutes
  unprotected (accepted single-contract tradeoff). (3) Entry day stall (7/14-7/15 flat) burned
  2 days of theta before the move — the time-stop discipline was 6 days from firing; puts need
  the move to start fast.

## Open positions

(none — 100% cash)
