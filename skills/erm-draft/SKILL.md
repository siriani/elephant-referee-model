---
name: erm-draft
description: "Draft a scientific manuscript from a protocol, results, figures, tables and notes, one section at a time with the user's approval. Use when the user has results and wants to write or restructure a paper."
---

# erm-draft — writing the manuscript

ERM_ROOT is the plugin directory, found as described in `<ERM_ROOT>/resources/standards/dispatch-standard.md` (two levels above this file, following symbolic links).

You are the **elephant**. You know the project; the reader will not. Write for the goldfish.

## Input

`/erm-draft [protocol.md] [results folder] [--venue "<journal>"]`. Find `protocol.md`, `lab_notebook.md`, result tables, figures and analysis code in the workspace; list what you found and ask about anything missing.

Load `<ERM_ROOT>/resources/standards/manuscript-standard.md` and `claims-standard.md`.

## Procedure

1. Propose the outline (IMRaD unless the venue requires otherwise) with the single main claim of the paper in one sentence. Get it approved first — the main claim governs everything.
2. Draft section by section into `manuscript_draft.md`, pausing after each. Suggested order: Methods → Results → Discussion → Introduction → Abstract → Title.
3. **Numbers come from files, never from memory.** Every number in the text must be traceable to a results file or table; add an HTML comment after it, e.g. `<!-- src: results/table2.csv row "P2" col "mAP50" -->`, so `erm-drift` can check it.
4. **Claims are bounded.** Each claim states the evidence it rests on and its scope (dataset, conditions, split). Use the claim strength ladder in `claims-standard.md`.
5. **Report what was protocol and what changed.** Any deviation from `protocol.md` goes in Methods, with the reason. Take deviations, failed runs and exclusions from `lab_notebook.md`; a deviation the notebook records but the draft omits is a drift error.
6. **References.** Only cite works you retrieved or the user supplied. Otherwise write `[citation needed]`. Never fabricate a reference.
7. Keep a limitations paragraph that names the main threats from the protocol, not generic ones.

When done, suggest `/erm-provenance` then `/erm-review manuscript_draft.md`.
