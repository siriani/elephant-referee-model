---
name: erm-provenance
description: "Create or update a provenance record of how AI agents took part in a study or manuscript — models and versions, prompts and skills, sources retrieved, tools, number of runs, and every human intervention — and draft an AI-use disclosure. Use when the user needs to document or disclose AI assistance."
---

# erm-provenance — make the agent's part traceable

ERM_ROOT is the plugin directory, found as described in `<ERM_ROOT>/resources/standards/dispatch-standard.md` (two levels above this file, following symbolic links).

Load `<ERM_ROOT>/resources/standards/provenance-template.md` and fill it into `provenance.md` at the project root (update it if it exists; never delete earlier entries — append).

## Gather, do not invent

- Read what is verifiable: `lab_notebook.md` (the main source for runs and human interventions), `erm-reviews/` folders, `response_log.md` files, config files, git history, notebooks, `research_brief.md` decisions.
- Ask the user for what you cannot verify: which models and versions they used outside this session, which outputs they edited by hand, which candidates or results they selected and why.
- Mark anything uncertain as `unknown` rather than guessing.

## Distinguish

- **Technical replicates**: the same configured system run again on the same input.
- **Independent replicates**: the system rebuilt from the documented specification and run again.
- **Human interventions**: predefined (approval gates, planned checks) versus ad hoc (manual repair, post-hoc selection, changed search space). Ad hoc interventions must state the reason.

## Output

1. `provenance.md` completed.
2. A draft **AI-use disclosure** paragraph at the end, in plain words, suitable for a journal's methods or acknowledgements section. The user must check it against the venue's policy; say so.
