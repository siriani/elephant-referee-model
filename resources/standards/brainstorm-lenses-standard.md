---
name: brainstorm-lenses-standard
version: 1.1.0
---
# Brainstorm lenses

| Lens | Attack the brief by asking |
|---|---|
| **novelty** | Has this been answered already or is it a minor variant? What is the closest existing work the brief seems unaware of? **Search** (see below) before answering. |
| **feasibility** | Can it be done with the stated data, time, money, animals, plots, compute and permits? What is the first thing likely to fail? |
| **measurement** | Do the planned measurements actually capture the construct? Are they valid, reliable and at the right resolution and unit? |
| **confounding** | What else could produce the expected result? Which design choice would rule it out? Where could leakage or selection bias enter? |
| **ethics-and-risk** | Animal welfare, human subjects, data protection, dual use, environmental cost, harm from a wrong answer. |
| **impact** | If the hypothesis is confirmed, who changes what decision? If refuted, is that still worth knowing? |

## Novelty search (novelty lens only)

The novelty lens is the only lens allowed to search. It builds its own queries from the brief's question, hypotheses and design, without using the brief's "Closest prior work" list as a starting point.

1. Run at least three queries in OpenAlex (`https://api.openalex.org/works?search=...`) or Semantic Scholar, varying terms for the population, the intervention or method, and the outcome.
2. Read the abstracts of the most similar results. For each work judged close, give DOI, year and one line on what it already answers.
3. Rate overlap: **answered** (the question has been answered in the same setting), **variant** (same question, different species, site, data or method), or **open**.
4. Report works the brief did not list. Cite only works retrieved in this search; never cite from memory.
5. List the queries and the date, so the search can be repeated.
