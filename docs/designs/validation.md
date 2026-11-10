# Validating ERM

Status: plan — 2026-11-09

ERM claims that zero-context goldfish find problems that a context-sharing agent misses. That claim needs evidence. This plan follows the evaluation design of Lu et al. (2026), who validated an automated reviewer against real conference decisions, and adds a planted-flaw benchmark that measures what decisions alone cannot.

## Questions

1. **Detection.** What share of known problems in a manuscript does `erm-review` find, and at what severity?
2. **Decision agreement.** How well does the readiness verdict agree with real editorial decisions, compared with agreement between human referees?
3. **Isolation effect.** Does a goldfish review find more problems than the same model reviewing with the author's context?
4. **Stability.** How much do findings vary between runs (`--runs N`)?

## Benchmarks

**A. Planted flaws.** Fictional manuscripts, like `tests/fixtures/toy_manuscript.md`, each with an answer key of planted problems by type (leakage, selection on the test split, pseudo-replication, overstated claims, arithmetic errors, invented or misattributed citations, misleading figures). Metric: recall by problem type and severity; false findings per manuscript, judged by two humans blind to the condition.

**B. Real decisions.** Openly reviewed papers with public decisions (for example OpenReview venues). Map readiness to a decision (GO → accept; GO WITH FIXES / NO-GO → reject, and a sensitivity analysis with GO WITH FIXES → accept). Report balanced accuracy, F1, AUC, false-positive rate (accepting a rejected paper) and false-negative rate, with bootstrap 95% CIs. Compare with published inter-referee agreement. Split papers published before and after the model's knowledge cutoff to estimate contamination.

**C. Isolation ablation.** For benchmark A, run the same critics (i) as goldfish and (ii) inside the drafting session, with the conversation that produced the manuscript. Metric: difference in recall; paired by manuscript.

## Protocol rules

- Fixed ERM version, rubric versions, models and settings, recorded with `erm-provenance`.
- Repeated runs (at least three per manuscript), reporting mean and spread, not best case.
- Failures and negative results reported.
- No manuscripts received for confidential peer review, ever.

## Expected limits

Real decisions are noisy labels: referees disagree with each other, so agreement with a single decision has a low ceiling. Planted flaws are easier to find than real ones. Neither benchmark measures whether the revised paper is better science; that requires expert judgement.
