---
description: Review the trade journal for repeated mistakes and propose persona improvements
---

Review trading performance and propose evidence-based improvements to the agent persona.

**Process:**
1. Read `journal.md` in full.
2. If there are fewer than ~5 closed trades, say so and stop — there isn't enough
   data to draw conclusions yet. Do not propose changes off a tiny sample.
3. Look for **repeated** patterns across multiple entries — the same mistake (or the
   same winning behavior) showing up 3+ times. Ignore one-off results; a single loss
   is noise, not a lesson.
4. Summarize the patterns you found, with the specific journal dates as evidence.
5. For each genuine pattern, propose a concrete, specific edit to the `PERSONA` in
   `brain.py` — quote the exact wording you'd add or change.
6. **Wait for the user's explicit approval before editing `brain.py`.** Do not change
   the persona unilaterally.
7. Once approved, make the edit, commit with a message that references the journal
   evidence, and push.

**Guardrails:**
- Never over-fit to the most recent trade. The market is noisy; one outcome rarely
  justifies a rule change.
- Prefer removing or tightening a rule that repeatedly fails over adding complexity.
- Keep the persona readable — don't let it bloat into contradictory micro-rules.
- Every persona change is a git commit, so it's auditable and reversible.

$ARGUMENTS
