# ERM architecture

Status: v0.1.0 — 2026-11-09

## Problem

When a researcher drafts a protocol or paper together with an AI agent, the agent and the author share the same context. Both know what the text is supposed to mean, so neither sees what it fails to say: undefined terms, unreported splits, unstated assumptions, claims stronger than the evidence. Those gaps surface only at peer review, months later. Asking the same agent to "review" its own draft does not help, because it reviews with the same context.

## Approach

Separate *writing* from *refereeing* by memory:

- **Elephant** — the main session. It holds the whole project and drafts.
- **Goldfish** — fresh sub-agents that receive only the document, the files it cites and a rubric. They referee cold.
- **Human** — decides on every finding and signs the work.

The pattern comes from Google's Elephant-Goldfish Model for software design. ERM adapts it to research: the documents are research briefs, protocols and manuscripts; the reviewers are scientific referees; and the rubrics encode research-specific failure modes (pseudo-replication, leakage, selection on the reporting split, overstated claims, missing provenance of AI involvement).

The research requirements follow Feng et al., "Agentic AI systems for scientific discovery", *Nature Reviews Methods Primers* 6, 81 (2026), [doi:10.1038/s43586-026-00534-y](https://doi.org/10.1038/s43586-026-00534-y). From it come the critic roles in a multi-agent workflow, human checkpoints at consequential decisions, explicit documentation of human intervention, provenance linking results to agent decisions, and hallucination as a primary failure mode.

## Layers

| Layer | Folder | Responsibility | Changes when |
|---|---|---|---|
| Skills | `skills/` | Orchestration: inputs, preconditions, stages, hand-off | The workflow changes |
| Personas | `agents/` | Judgment stance of each goldfish | A reviewer role changes |
| Standards | `resources/standards/` | Versioned criteria and formats | The criteria change |

Skills never contain criteria; personas reference standards by file name. This lets a rubric be revised (and versioned) without touching prompts, and lets a lab add a field-specific rubric without forking the plugin.

## Lifecycle

```text
idea ──erm-brainstorm──▶ research_brief.md
        (6 goldfish lenses)
      ──erm-protocol──▶ protocol.md ──erm-review (protocol)──▶ revise
      ... study runs ...
      ──erm-draft──▶ manuscript_draft.md
      ──erm-provenance──▶ provenance.md
      ──erm-review──▶ erm-reviews/<doc>/<ts>/01..05
      ──erm-resolve──▶ revised manuscript + response_log.md
      ──erm-drift──▶ drift_report.md ──▶ human approval ──▶ submission
```

## Review pipeline

1. **Scope** (`erm-scope`) — fit and positioning.
2. **Comprehension** (`erm-comprehension`) — gate. Failing stops the pipeline.
3. **Critique**, in parallel — `erm-methods-critic`, `erm-evaluation-critic` (model-based work only), `erm-claims-auditor` (manuscripts), `erm-reproducibility-auditor`.
4. **Synthesis** (`erm-synthesizer`) — the only goldfish that reads other reports; merges, deduplicates, ranks.
5. **Readiness** (`erm-readiness`) — GO / GO WITH FIXES / NO-GO.

## Invariants

1. Goldfish receive file paths only. No conversation, summary, intent or hint.
2. If isolated sub-agents are unavailable, review skills stop. No simulated goldfish.
3. Skills never edit a document on a finding the human has not accepted.
4. Numbers in drafts carry source tags so drift can be checked mechanically.
5. References are never fabricated; unknown citations are marked `[citation needed]`.
6. ERM warns against use on manuscripts received for confidential peer review.

## Non-goals

- Replacing peer review, statistics consultation or experiments.
- Benchmarking reviewer quality. (A separate study could do this with fictional manuscripts containing planted flaws.)
- Laboratory automation.

## Open questions

- Model diversity: should goldfish default to a different model family than the elephant, where the harness allows it?
- Field packs: rubric sets for animal science, field trials, remote sensing, clinical studies.
- Ports to other harnesses (Codex, Antigravity, Gemini CLI).
