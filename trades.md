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

## Open positions

### SOFI $18.5C Jul 17 — Catalyst swing (NFP) — OPENED 2026-06-29
- **Entry:** $0.74 x1 (order 6a427819)
- **Stop:** $0.85 stop-market GTC (order 6a456baf — raised from $0.55 → $0.74 → $0.85 as gain grew)
- **Take-profit target:** $1.10–1.35 (+50–80%), manual
- **Thesis:** Fintech momentum into NFP Jul 2 (7:30 AM CT); break-even $19.24 at expiry.
- **Lesson logged 2026-07-01:** peaked +45% ($1.075) intraday, faded to +28% while sell/hold decision was pending — decision latency costs real money. Stop raised to lock ~+15% floor.

### GRND $15C Jul 17 — Episodic pivot base breakout — OPENED 2026-07-01
- **Entry:** $1.05 x1 (order 6a45274e; original $0.95 limit missed, re-priced once to mid)
- **Stop:** $0.75 stop-market GTC (order 6a4527e4)
- **Take-profit target:** $1.37–1.89 (+30–80%); trail if squeeze extends
- **Thesis:** 2-week base $13–15, broke out on 1.7–1.9x relative volume; 25.5M low float. Thesis-exit if closes below $15.
- **Rule note:** entered with ~20% spread (rule says <15%) and 0.69 delta (rule 0.35–0.55) — justified by OI 1,560 when all OTM strikes were illiquid; formalized as exception rubric in PERSONA 2026-07-01.
