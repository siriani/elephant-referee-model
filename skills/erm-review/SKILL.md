---
name: erm-review
description: Referee a research protocol or manuscript with zero-context goldfish sub-agents across five stages (scope, comprehension, critique, synthesis, readiness). Use when the user asks to review, referee, stress-test or pre-submission-check a scientific document.
---

# erm-review — goldfish refereeing

You are the **elephant**: you hold the project context. In this skill your job is to *orchestrate* reviewers who do **not** have that context. You do not review the document yourself.

## Input

`/erm-review <path-to-document> [--venue "<journal or conference>"] [--type protocol|manuscript]`

- If no path is given, ask for one. Do not guess.
- If `--type` is missing, infer it from the document (a protocol has no results) and state your inference.
- Resolve the plugin root as two directories above this file. Rubrics are in `<root>/resources/standards/`.

## Preconditions — stop if any fails

1. **Sub-agents.** You must be able to spawn isolated sub-agents (in Claude Code, the Task/Agent tool with the `erm:*` agent types). If you cannot, stop and say: "ERM review needs isolated sub-agents; this session cannot create them, so no review was run." Never simulate a goldfish in your own context.
2. **Confidentiality.** If the user indicates the document is a manuscript they received to review for a journal, stop and remind them that many publishers forbid uploading submissions to AI tools. Continue only if they confirm the venue's policy allows it.
3. **Self-contained input.** List the files the document cites locally (supplementary files, tables, code, data dictionaries). These, and only these, are passed to goldfish.

## The isolation contract

Every goldfish prompt contains **only**:
- the path to the document,
- the paths of locally cited files,
- the path to its rubric,
- the venue name, if given,
- the output path for its report.

Never include: conversation history, a summary of the project, what the author intended, what you think the weak points are, earlier review results (except where a stage below says so), or encouragement to be lenient or harsh.

## Stages

Create the output folder `erm-reviews/<document-stem>/<YYYY-MM-DD-HHMM>/`.

**Stage 1 — Scope.** Spawn `erm-scope` with `scope-standard.md`. Output `01-scope.md`.

**Stage 2 — Comprehension (gate).** Spawn `erm-comprehension` with `comprehension-standard.md`. Output `02-comprehension.md`. Then compare its restatement of question, design, main result and conclusion against the document yourself.
- If the restatement is materially wrong or the reviewer reports it could not restate one of them, **stop the pipeline**. Tell the user the document failed comprehension, show the mismatch, and recommend revising before critique. Critiquing a text that cannot be understood wastes reviewers.

**Stage 3 — Critique (parallel).** Spawn these in parallel, each with its rubric:

| Persona | Rubric | Output | When |
|---|---|---|---|
| `erm-methods-critic` | `methods-standard.md` | `03a-methods.md` | always |
| `erm-evaluation-critic` | `evaluation-standard.md` | `03b-evaluation.md` | if the work trains, tunes, compares or benchmarks models or predictors |
| `erm-claims-auditor` | `claims-standard.md` | `03c-claims.md` | manuscripts only |
| `erm-reproducibility-auditor` | `reproducibility-standard.md` | `03d-reproducibility.md` | always |

**Stage 4 — Synthesis.** Spawn `erm-synthesizer` with `finding-format.md`, giving it the paths of the stage 1–3 reports and the document. Output `04-synthesis.md`. This is the only goldfish allowed to read other reviewers' reports.

**Stage 5 — Readiness.** Spawn `erm-readiness` with `readiness-standard.md` (plus the venue name). Output `05-readiness.md` with a GO / NO-GO verdict.

## Hand-off to the human

Reply with:
1. The verdict line from readiness and the comprehension result.
2. The count of findings by severity from the synthesis.
3. The top three findings, one line each, with their IDs.
4. The path to the review folder.
5. The next step: `/erm-resolve <review-folder>`.

Do not edit the document. Do not defend the document against findings. Do not drop findings you disagree with — you may add a note under each saying what project context the goldfish lacked, clearly labelled as the elephant's view.
