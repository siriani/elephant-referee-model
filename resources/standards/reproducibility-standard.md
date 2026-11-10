---
name: reproducibility-standard
version: 1.0.0
---
# Reproducibility standard

## Data
- Origin: who collected the data, where, when, how; licence and access route.
- Exact version or snapshot; the identifiers of each split are released or described precisely.
- Ethics approval or permits, where applicable.

## Computation
- Code, configuration and trained artefacts are available, or restrictions are explained.
- Software versions and environment (e.g. lock file, container) are given.
- Hardware is stated where it affects results or speed.
- Randomness: seeds and number of runs are reported.

## AI agents and language models in the workflow
If agents or LLMs produced, selected or analysed results, or drafted text:
- models and versions, access dates, and settings that matter;
- prompts, skills or profiles used (or a description where they cannot be shared);
- tools the agent could call, with versions — treat them like instruments;
- number of runs, and whether results are technical replicates (same system re-run) or independent replicates (system rebuilt from the description);
- every human intervention, distinguishing predefined checkpoints from ad hoc repairs, post-hoc selection or changes to the search space, with reasons;
- negative or failed runs, not only the best trajectory.

## Severity guide
Data or splits impossible to reconstruct → major (critical if the main result depends on an unusual split). Undisclosed post-hoc selection of agent outputs → critical.

Source note: the AI-agent items are the author's formulation informed by Feng et al., Nat. Rev. Methods Primers 6, 81 (2026).
