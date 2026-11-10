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

Before writing, **search the literature for the closest existing work**. Query OpenAlex (`https://api.openalex.org/works?search=<keywords>&per-page=25`) or Semantic Scholar with two or three formulations of the question, and read the abstracts of the most similar results. Keep a list of what you searched and when. If the idea has already been answered, say so to the user now: it is cheaper to learn it here than from a reviewer.

Then write `research_brief.md` with these sections:

1. **Question** — one sentence, answerable.
2. **Why it matters** — the gap, stated against specific prior work the user named or you retrieved and cited.
3. **Closest prior work** — the three to five most similar studies you found, each with DOI and one line on how this project differs. Add the search queries and date.
4. **Hypotheses** — each falsifiable, with the observation that would refute it.
5. **Candidate designs** — two or three, with the main threat to validity of each.
6. **Data and resources** — what exists, what must be collected.
7. **Risks** — feasibility, ethics, dual use, data access.
8. **Open decisions** — what only the user can decide.

Never invent references. If you cite literature, it must come from a search you ran or a file the user gave; otherwise mark the claim `[citation needed]`.

## 2. Goldfish lenses

Requires isolated sub-agents; if unavailable, stop after step 1 and say the lens review was not run.

Spawn `erm-lens` six times in parallel, each with `research_brief.md`, `brainstorm-lenses-standard.md` and one lens name:
`novelty`, `feasibility`, `measurement`, `confounding`, `ethics-and-risk`, `impact`.
Each writes `erm-brainstorm/<lens>.md`. Pass nothing else. The `novelty` lens runs its own literature search from the brief alone; do not pass it your search results, so that it can find what you missed.

## 3. Return to the user

Summarise the strongest objection from each lens in one line, then ask which to address. Update `research_brief.md` only with the changes the user accepts, and log them under a final section **Decisions** with the date.

Next step: `/erm-protocol research_brief.md`.
