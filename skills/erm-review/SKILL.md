---
name: erm-review
description: "Referee a research protocol or manuscript with zero-context goldfish sub-agents across five stages (scope, comprehension, critique, synthesis, readiness). Use when the user asks to review, referee, stress-test or pre-submission-check a scientific document."
---

# erm-review — goldfish refereeing

You are the **elephant**: you hold the project context. In this skill your job is to *orchestrate* reviewers who do **not** have that context. You do not review the document yourself.

## Input

`/erm-review <path-to-document> [--venue "<journal or conference>"] [--venue-pack <file>] [--type protocol|manuscript] [--runs N]`

- If no path is given, ask for one. Do not guess.
- If `--type` is missing, infer it from the document (a protocol has no results) and state your inference.
- `--runs N` (default 1, recommended 3 before submission): how many independent instances of each stage 3 critic to run. Agent output is stochastic; one run can miss a problem or invent one. Several runs let the synthesizer report how consistently each finding appears.
- `--venue-pack <file>`: a filled copy of `venue-pack-template.md` with the venue's own reviewer questions, required statements and AI policy. If `--venue` is given without a pack, say that scope and readiness will use general criteria only, and point the user to the template.
- Resolve ERM_ROOT and start every goldfish as described in `dispatch-standard.md`. Rubrics are in `<ERM_ROOT>/resources/standards/`.

## Preconditions — stop if any fails

1. **Sub-agents.** You must be able to start isolated sub-agents, in the way `dispatch-standard.md` gives for your harness. If you cannot, stop and say: "ERM review needs isolated sub-agents; this session cannot create them, so no review was run." Never simulate a goldfish in your own context.
2. **Confidentiality.** If the user indicates the document is a manuscript they received to review for a journal, stop and remind them that many publishers forbid uploading submissions to AI tools. Continue only if they confirm the venue's policy allows it.
3. **Self-contained input.** List the files the document cites locally (supplementary files, tables, code, data dictionaries) and its figure files (images, or the PDF if figures are embedded). These, and only these, are passed to goldfish.

## The isolation contract

Every goldfish prompt contains **only**:
- the path to the document,
- the paths of locally cited files,
- the path to its rubric,
- the venue name and the venue pack path, if given,
- the output path for its report.

Never include: conversation history, a summary of the project, what the author intended, what you think the weak points are, earlier review results (except where a stage below says so), or encouragement to be lenient or harsh.

## Stages

Create the output folder `erm-reviews/<document-stem>/<YYYY-MM-DD-HHMM>/`.

**Stage 1 — Scope.** Spawn `erm-scope` with `scope-standard.md` and the venue pack, if any. Output `01-scope.md`.

**Stage 2 — Comprehension (gate).** Spawn `erm-comprehension` with `comprehension-standard.md`. Output `02-comprehension.md`. Then compare its restatement of question, design, main result and conclusion against the document yourself.
- If the restatement is materially wrong or the reviewer reports it could not restate one of them, **stop the pipeline**. Tell the user the document failed comprehension, show the mismatch, and recommend revising before critique. Critiquing a text that cannot be understood wastes reviewers.

**Stage 3 — Critique (parallel).** Spawn these in parallel, each with its rubric:

| Persona | Rubric | Output | When |
|---|---|---|---|
| `erm-methods-critic` | `methods-standard.md` | `03a-methods.md` | always |
| `erm-evaluation-critic` | `evaluation-standard.md` | `03b-evaluation.md` | if the work trains, tunes, compares or benchmarks models or predictors |
| `erm-claims-auditor` | `claims-standard.md` | `03c-claims.md` | manuscripts only |
| `erm-reproducibility-auditor` | `reproducibility-standard.md` | `03d-reproducibility.md` | always |
| `erm-citation-auditor` | `citation-standard.md` | `03e-citations.md` | if the document has a reference list or citations |
| `erm-figures-critic` | `figures-standard.md` | `03f-figures.md` | if the document has figures and their files can be passed |

With `--runs N` and N > 1, spawn N independent instances of each critic. Give every instance the identical prompt; never tell an instance about the others. Name outputs `03a-methods.r1.md`, `03a-methods.r2.md`, … Skip a critic only when its "When" condition fails, and say so in the hand-off.

**Stage 4 — Synthesis.** Spawn `erm-synthesizer` with `finding-format.md`, giving it the paths of the stage 1–3 reports, the document and the number of runs N. Output `04-synthesis.md`. This is the only goldfish allowed to read other reviewers' reports.

**Stage 5 — Readiness.** Spawn `erm-readiness` with `readiness-standard.md`, the path of `04-synthesis.md`, and the venue name and pack, if given. Output `05-readiness.md` with a GO / NO-GO verdict.

## Hand-off to the human

Reply with:
1. The verdict line from readiness and the comprehension result.
2. The count of findings by severity from the synthesis and, if N > 1, how many findings were raised in every run versus in one run only.
3. The top three findings, one line each, with their IDs.
   Remind the user that a GO is not a prediction of acceptance: automated reviewers tend to pass work that human referees reject.
4. The path to the review folder.
5. The next step: `/erm-resolve <review-folder>`.

Do not edit the document. Do not defend the document against findings. Do not drop findings you disagree with — you may add a note under each saying what project context the goldfish lacked, clearly labelled as the elephant's view.
