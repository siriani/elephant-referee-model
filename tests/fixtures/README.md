# Fixtures

All fixtures are fictional. Never add real manuscripts — especially not manuscripts received for peer review.

## toy_manuscript.md — planted problems

Use this answer key to check that a review run is working, not to score reviewer quality.

| # | Problem | Expected reviewer | Expected severity |
|---|---|---|---|
| 1 | Random split over frames from the same houses and flocks → near-duplicate leakage | evaluation | critical |
| 2 | Checkpoint selected on the **test** set | evaluation | critical |
| 3 | Single run, no seeds or uncertainty | evaluation / methods | major |
| 4 | Unfair baseline: ResNet-50 trained 20 epochs with defaults vs 50 for FlockNet | evaluation | major |
| 5 | F1 for FlockNet inconsistent: 2·0.88·0.92/(0.88+0.92) = 0.90, not 0.91 | claims | minor |
| 6 | Mechanism ("TAH is responsible") with no ablation | claims / evaluation | major |
| 7 | Generalisation to "commercial broiler production" from four houses, two flocks | claims / scope | major |
| 8 | "Replace manual gait scoring" with no agreement study against observers | claims | major |
| 9 | Single annotator, no inter-observer agreement | methods | major |
| 10 | Frame-level labels treated as independent; bird or house is the real unit | methods | major |
| 11 | "First in commercial houses" unsupported by cited literature (no references at all) | scope | major |
| 12 | FPS hardware not stated; "twice as fast" is 58 vs 31 (≈1.9×) | claims / evaluation | minor |
| 13 | No data, code or ethics statements | reproducibility / readiness | major |
| 14 | TAH defined only by acronym expansion; class balance not reported | comprehension | minor |
