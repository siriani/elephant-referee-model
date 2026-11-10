---
name: evaluation-standard
version: 1.0.0
---
# Evaluation protocol standard (models, predictors, benchmarks)

## Splits and leakage
- How the data were split is stated: random by sample, or grouped by subject, site, camera, field, farm, date or season.
- When samples are correlated (frames from the same camera, images of the same animal, plots of the same field, augmented copies), splits are grouped so correlated samples do not cross. Otherwise, leakage is likely → critical unless shown absent.
- Augmentation and preprocessing that use data statistics are fitted on training data only.

## Selection vs reporting
- Model, checkpoint, hyper-parameter and threshold selection use training/validation data only.
- Headline results are reported on a held-out test set not used for any selection. Reporting only on the selection split → critical.

## Variability
- Results report mean and spread over several seeds or folds (state how many).
- Differences smaller than the run-to-run spread are not presented as improvements.
- Confidence intervals (e.g. bootstrap over test samples) accompany headline metrics.

## Baselines
- Baselines are trained with the same data, budget and recipe, or differences are documented.
- Strong simple baselines are included (e.g. higher input resolution, tiling, a classical method, a majority or persistence baseline for forecasting).
- Ablations isolate each claimed component; components never tested alone are not credited with specific effects.

## Metrics and operating points
- Metrics measure the stated goal (e.g. counting error for a counting application, not only detection AP).
- Thresholds for precision/recall/F1 are stated and comparable across methods; threshold-free metrics are also given.
- Speed and cost claims state hardware, batch size and how they were measured.
