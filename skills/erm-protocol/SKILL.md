---
name: erm-protocol
description: Turn a research brief or notes into a complete study protocol (pre-registration style), drafting section by section and pausing for the user's feedback. Use when the user wants to plan a study, write a protocol, a pre-registration or the methods plan of a grant.
---

# erm-protocol — drafting the study protocol

You are the **elephant**. Use everything you know about the project. The protocol must be clear enough that a goldfish — and later an independent group — could run the study without you.

## Input

`/erm-protocol [research_brief.md or notes]`. If nothing is given, look for `research_brief.md`; if absent, ask.

Load `<root>/resources/standards/protocol-standard.md` (plugin root = two levels above this file). Its sections are the outline.

## Procedure

1. Show the outline with one line per section stating what you will write. Ask for corrections.
2. Draft **one section at a time** into `protocol.md`. After each section, stop and ask: accept, change, or skip. Do not draft ahead.
3. Wherever a decision is the user's (sample size target, primary outcome, exclusion rules, stopping rules), propose options with their trade-offs and wait. Do not choose silently.
4. Mark every assumption you made as `> ASSUMPTION:` inline, so reviewers and the user can see it.
5. Fix the analysis plan *before* data are seen: primary outcome, primary analysis, how the test/hold-out set is protected, how many runs or seeds, what counts as success.

When done, offer `/erm-review protocol.md --type protocol`.
