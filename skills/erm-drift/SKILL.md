---
name: erm-drift
description: Check that a manuscript still matches its results, tables, figures, code and protocol — numbers, claims, methods and deviations. Use before submission, after re-running analyses, or after revising a paper.
---

# erm-drift — does the text still say what the data show?

## Input

`/erm-drift <manuscript> [--results <folder>] [--protocol protocol.md] [--code <folder>]`. Locate missing inputs in the workspace and list what you will compare.

## Checks

Run as a goldfish if sub-agents are available: spawn `erm-claims-auditor` with the manuscript, the listed files and `drift-standard.md`. Otherwise run the checks yourself and say so in the report header (a self-check is weaker than a goldfish check).

1. **Numbers.** Every number with a `<!-- src: ... -->` tag is compared with its source. Numbers without a source tag are listed.
2. **Internal consistency.** Abstract, results, tables, figures and conclusion report the same values; derived values (F1, deltas, percentages, totals) are recomputed with code, not by eye.
3. **Methods vs code.** Hyper-parameters, splits, seeds, thresholds and preprocessing stated in the text match configuration files and scripts.
4. **Protocol vs paper.** Primary outcome and analysis match `protocol.md`; every deviation is disclosed.
5. **Words vs numbers.** Qualitative statements ("faster", "halves", "highest", "significant") agree with the values.

## Output

`drift_report.md`: a table with `location | statement | source | expected | found | status (ok / mismatch / unverifiable)`, then a short list of mismatches ordered by severity. Do not edit the manuscript; offer `/erm-resolve`-style fixes for the user to approve.
