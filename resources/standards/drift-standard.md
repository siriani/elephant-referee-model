---
name: drift-standard
version: 1.1.0
---
# Drift standard

Compare the manuscript with its sources and report each check as ok / mismatch / unverifiable.

1. **Tagged numbers**: values with `<!-- src: … -->` equal the source value after stated rounding.
2. **Untagged numbers**: listed for the author to tag or verify.
3. **Recomputed values**: derived metrics, deltas, percentages and totals recomputed in code.
4. **Methods vs configuration**: splits, seeds, epochs, input sizes, thresholds, hyper-parameters match config files and scripts.
5. **Protocol vs manuscript**: primary outcome and analysis match; every deviation, discarded run and exclusion in `lab_notebook.md` is disclosed.
6. **Qualitative statements**: comparative words agree with the numbers.
