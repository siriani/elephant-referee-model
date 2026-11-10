---
name: erm-notebook
description: "Keep a dated, append-only lab notebook of experiments, analysis runs, failures and decisions, recording what was run, with which code and data, what came out and how it deviates from the protocol. Use after running an experiment or analysis, when a result comes in, or when a design decision is made."
---

# erm-notebook — write it down while it happens

ERM_ROOT is the plugin directory, found as described in `<ERM_ROOT>/resources/standards/dispatch-standard.md` (two levels above this file, following symbolic links).

You are the **elephant**. The notebook is the memory the goldfish will never have, and the record that `erm-draft`, `erm-drift` and `erm-provenance` read later.

Load `<ERM_ROOT>/resources/standards/lab-notebook-template.md`. Append to `lab_notebook.md` at the project root; create it if it does not exist.

## When to write an entry

- after any experiment, data collection or analysis run, including failed and repeated ones;
- when a result arrives that changes the plan;
- when the user makes a decision about design, data, exclusions or analysis;
- when an agent (you included) takes an action on the user's behalf.

## How

1. Fill the fields from what you can verify: the command you ran, `git rev-parse HEAD`, file paths and hashes, the output files. Ask the user only for what you cannot see (instrument settings, field conditions, who decided).
2. Copy result values **from the output file**, never from memory, and name the file.
3. Compare with `protocol.md` if it exists. Any difference is a deviation; record it and its reason.
4. Mark who acted: human, or agent with or without human approval. This is what `erm-provenance` will report as a human intervention.
5. Never edit or delete a past entry. A correction is a new entry that points to the old one.

Show the new entry to the user in one block after appending it.
