# Trading Journal

A running log of every closed trade. The agent appends one entry per closed
position. The `/review` command reads this file to find **repeated** mistakes
and propose persona changes (with user approval). One bad trade is noise;
a pattern across several trades is a lesson.

**Do not edit the persona based on a single trade.** Only patterns that repeat
across multiple entries justify a rule change.

---

## Entry template

```
## YYYY-MM-DD — TICKER STRIKE/TYPE (setup) — WIN/LOSS +/-X%
Entry: $X.XX | Exit: $X.XX | Held: Nd | Account impact: +/-$XX
Thesis: <why I entered>
What happened: <how it actually played out>
Lesson: <what went right/wrong and why — be honest and specific>
Repeat offender?: <does this echo a prior journal entry? note the date(s)>
```

---

<!-- Entries begin below. Newest at the bottom. -->
