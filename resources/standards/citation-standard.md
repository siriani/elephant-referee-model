---
name: citation-standard
version: 1.0.0
---
# Citation standard

Inaccurate and invented citations are among the most frequent failures of AI-written papers (Lu et al., *Nature*, 2026). Check each item and report it with the finding format.

| Check | Severity if it fails |
|---|---|
| **Exists.** The work can be found by DOI, or by title + first author + year in OpenAlex or Crossref. | major (critical if the main claim rests on it) |
| **Described correctly.** Authors, year, title, venue, volume and pages match the record. | minor |
| **Not retracted.** The record carries no retraction or expression of concern. | major |
| **Supports the sentence.** The cited work actually reports what the sentence attributes to it, at the same strength (not "shows" when it "suggests"). | major |
| **Right kind of source.** A primary study for empirical claims; a review only for summary statements. Preprints are labelled as such. | minor |
| **Complete list.** Every in-text citation is in the list, and every listed item is cited. | minor |
| **No placeholders.** No `[citation needed]`, `[ref]`, `??` or empty brackets remain. | major in a manuscript, note in a protocol |
| **Novelty claims.** Claims of "first" or "novel" cite the closest prior work. | major |

Report what you searched for each reference you could not find. Absence of evidence is reported as **not found**, never as **fabricated**.
