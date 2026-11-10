# Elephant-Referee Model (ERM)

**Write research with an elephant. Referee it with a goldfish.**

ERM is an open-source plugin for AI agent harnesses (Claude Code first) that structures scientific work — from research question to submission-ready manuscript — around one rule about *who sees what*:

| Role | What it sees | What it does |
|---|---|---|
| **Elephant** | The whole project: your conversation, notes, data, code, prior decisions | Brainstorms, drafts protocols and manuscripts, resolves findings |
| **Goldfish** | Only the document under review and the files it cites | Referees the document cold, like an anonymous reviewer who was never in the room |
| **You** | Everything | Make the scientific calls, accept or reject findings, sign the work |

A goldfish that has been told what the elephant meant is no longer a goldfish. ERM therefore runs every review in fresh, isolated sub-agents. If the harness cannot create them, the review stops instead of pretending.

> ERM is inspired by Google's [Elephant-Goldfish Model](https://github.com/google/elephant-goldfish-model) (EGM) and adapts its pattern from software design to scientific research. It is an independent project, not affiliated with or endorsed by Google. See [NOTICE](NOTICE).

## Why

An author who drafted a paper with an AI agent has a shared blind spot with that agent: both know what the text *means*, so neither notices what it fails to *say*. Reviewers notice — months later, after submission. ERM moves that cold read to before submission, and makes the agent's own contribution traceable.

## Skills

| Skill | Purpose | Output |
|---|---|---|
| `erm-brainstorm` | Sharpen a research question and hypotheses; goldfish lenses challenge the idea | `research_brief.md` |
| `erm-protocol` | Turn the brief into a study protocol, section by section, pausing for your feedback | `protocol.md` |
| `erm-draft` | Draft a manuscript from the protocol, results and notes, section by section | `manuscript_draft.md` |
| `erm-review` | Referee a protocol or manuscript with zero-context goldfish across five stages | `erm-reviews/<doc>/*.md` |
| `erm-resolve` | Work through review findings with you; revise the document | Revised document + `response_log.md` |
| `erm-drift` | Check that the manuscript still says what the results, tables and code show | `drift_report.md` |
| `erm-provenance` | Record how AI took part: models, prompts, sources, human interventions, runs | `provenance.md` |

Each skill works on its own. The full sequence is optional.

## Review stages

`erm-review` runs five goldfish stages, each with its own versioned rubric in [`resources/standards/`](resources/standards/):

1. **Scope** — does the work fit the field and the target venue? Is the contribution stated against the state of the art?
2. **Comprehension** — can a reader with no context restate question → method → finding? If not, the document is sent back before critique.
3. **Critique** (parallel) — methods & statistics, evaluation protocol, claims-vs-evidence, reproducibility.
4. **Synthesis** — findings are merged, deduplicated and ranked by severity.
5. **Readiness** — go / no-go: could an independent group reproduce this, and is everything a journal will ask for present?

## Typical workflow

```text
/erm:erm-brainstorm Does early heat stress alter broiler gait scores detectable by video?
/erm:erm-protocol
/erm:erm-draft          # after you have results
/erm:erm-review manuscript_draft.md
/erm:erm-resolve
/erm:erm-drift
/erm:erm-provenance
```

## Install (Claude Code)

```bash
claude plugin marketplace add siriani/elephant-referee-model
claude plugin install erm@erm
```

Start a new session after installing. Install the whole plugin: skills load the reviewer personas and rubrics at runtime.

Other harnesses: the skills are plain Markdown and the personas are standard sub-agent definitions, so ports to Codex, Antigravity or others are welcome. See [CONTRIBUTING](CONTRIBUTING.md).

## Rules ERM enforces

- **Isolation.** Goldfish receive the document path and cited files only — never the conversation, a summary of it, or the author's intent.
- **The human decides.** Findings are evidence to weigh, not verdicts. ERM never edits your document on a finding you have not accepted.
- **Provenance.** AI contributions are recorded so you can disclose them accurately.
- **Confidentiality.** Do **not** use ERM on manuscripts you received for confidential peer review unless the journal's policy explicitly allows AI tools. Many publishers prohibit uploading submissions to generative AI services.

## Limits

A goldfish review does not replace experiments, statistics done properly, domain expertise or human peer review. Goldfish can miss problems, misread a method or share the biases of the underlying model; using a different model for reviewers than for the elephant reduces — but does not remove — shared blind spots.

## License and citation

Apache License 2.0. If ERM helps your work, please cite it using [CITATION.cff](CITATION.cff).
