---
name: finding-format
version: 1.0.0
---
# Finding format and severity scale

Every ERM reviewer writes findings in this format:

```markdown
### <ID> [<severity>] <short title>
- **Type:** wrong | missing | unclear
- **Location:** §4.1, Table 2, Eq. (6), line 214 …
- **Evidence:** "<at most one short quoted phrase>" or a description of what is absent
- **Why it matters:** the consequence for the conclusions or for reproduction
- **Smallest fix:** the minimal change that would resolve it
- **Needs new data or analysis:** yes | no
```

Reviewer-level IDs use the reviewer prefix (SC-, CO-, ME-, EV-, CL-, RE-, RD-). The synthesizer renumbers as F-01, F-02…

## Severity

| Severity | Meaning |
|---|---|
| **critical** | The main conclusion may not hold, or the result cannot be interpreted as reported (e.g. results only on the selection split, leakage, wrong unit of analysis). |
| **major** | A conclusion is overstated, a key comparison is unfair or unspecified, or reproduction would be blocked. Fixable, often with extra analysis. |
| **minor** | Clarity, presentation, missing detail that does not change conclusions. |
| **note** | Suggestion or strength worth keeping. |

Severity reflects consequence, not effort to fix.
