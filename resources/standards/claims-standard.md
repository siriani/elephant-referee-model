---
name: claims-standard
version: 1.0.0
---
# Claims-vs-evidence standard

## Claim strength ladder
Use the weakest wording the evidence supports:

| Evidence | Allowed wording |
|---|---|
| One run, one split, one dataset | "in our experiments", "on dataset X we observed" |
| Several seeds, held-out test, CIs | "improves", "outperforms on X" |
| Several datasets or sites | "generalises across the settings tested" |
| Controlled manipulation isolating a mechanism | "because", "is caused by", "explains" |

Claims above their rung are **overstated** (major); claims with no supporting result are **unsupported** (major or critical if central); claims contradicted by the paper's own numbers are **contradicted** (critical if central).

## Consistency
- The same quantity has the same value everywhere (abstract, text, tables, figures, conclusion).
- Derived numbers are recomputed: F1 = 2PR/(P+R), deltas, percentages, ratios, totals of counts and splits.
- Words agree with numbers ("faster" means higher throughput in the table; "halves" means ≈50%).

## Interpretation
- Mechanistic explanations are labelled as hypotheses unless tested.
- Limitations named in the conclusion also appear in the abstract when they bound the main claim.
