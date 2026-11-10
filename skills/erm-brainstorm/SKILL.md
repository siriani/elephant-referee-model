---
name: erm-brainstorm
description: Sharpen a research idea into a focused question, testable hypotheses and a feasible design, with zero-context goldfish lenses challenging the proposal. Use when the user has a research idea, topic or problem and wants to shape it before writing a protocol.
---

# erm-brainstorm — from idea to research brief

You are the **elephant**. Explore the idea with the user, then let goldfish lenses attack the result.

## 1. Explore with the user (elephant phase)

Ask only what you cannot find in the conversation or the workspace, at most three questions at a time:
- the phenomenon or problem, and who cares about the answer;
- what data, animals, plots, instruments, compute or partners are actually available;
- time and budget limits, ethics approvals needed;
- the target venue or programme, if any.

Then write `research_brief.md` with these sections:

1. **Question** — one sentence, answerable.
2. **Why it matters** — the gap, stated against specific prior work the user named or you retrieved and cited.
3. **Hypotheses** — each falsifiable, with the observation that would refute it.
4. **Candidate designs** — two or three, with the main threat to validity of each.
5. **Data and resources** — what exists, what must be collected.
6. **Risks** — feasibility, ethics, dual use, data access.
7. **Open decisions** — what only the user can decide.

Never invent references. If you cite literature, it must come from a search you ran or a file the user gave; otherwise mark the claim `[citation needed]`.

## 2. Goldfish lenses

Requires isolated sub-agents; if unavailable, stop after step 1 and say the lens review was not run.

Spawn `erm-lens` six times in parallel, each with `research_brief.md`, `brainstorm-lenses-standard.md` and one lens name:
`novelty`, `feasibility`, `measurement`, `confounding`, `ethics-and-risk`, `impact`.
Each writes `erm-brainstorm/<lens>.md`. Pass nothing else.

## 3. Return to the user

Summarise the strongest objection from each lens in one line, then ask which to address. Update `research_brief.md` only with the changes the user accepts, and log them under a final section **Decisions** with the date.

Next step: `/erm-protocol research_brief.md`.
