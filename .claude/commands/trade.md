---
description: Run an options trading session for the Agentic Robinhood account
---

Run an options trading session using the Robinhood MCP tools.

**Account:** Agentic account `452369101` (the only agentic-allowed, options-enabled account).
**Budget:** Check the agent ledger first — run `python cli.py balance b7763d77` to see allocated/remaining.

**Persona & rules:** Read `brain.py` and follow the `PERSONA` block exactly — it is the single
source of truth for strategy, setups (Qullamaggie episodic pivot / momentum / short squeeze),
stop losses, profit-taking, pricing discipline, and scanning criteria. Do not improvise around it.

**Process:**
1. Read the `PERSONA` in `brain.py`.
2. Check current positions and buying power on account `452369101`.
3. Scan the market per the persona's 5-factor criteria (technicals, fundamentals, news/catalysts,
   smart money, political commentary) and the three proven setups.
4. If a trade qualifies, run `review_option_order` and present the full details — strike, expiry,
   delta, cost, liquidity, the setup it matches, and the thesis.
5. **Wait for my explicit confirmation before placing any order.** (Confirmation stays ON until I
   say otherwise.)
6. If nothing qualifies, say so plainly — cash is a position.

$ARGUMENTS
