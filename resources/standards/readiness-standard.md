---
name: readiness-standard
version: 1.1.0
---
# Readiness standard

## Calibration
Automated reviewers are lenient. In Lu et al. (*Nature*, 2026), an ensemble AI reviewer accepted 45–52% of papers that human referees rejected, against 17% for humans. ERM therefore applies these rules:
- Any **critical** finding in the synthesis means **NO-GO**, whatever the checklist says.
- Any **major** finding that needs new data or analysis means **NO-GO**; other major findings mean at best **GO WITH FIXES**.
- If a required item cannot be checked (file missing, figure not provided, reference unverifiable), mark it **absent**, not present.
- When in doubt between two verdicts, choose the stricter one.

## Required — manuscript
- [ ] Main claim stated in abstract and supported by a held-out or otherwise valid result
- [ ] Methods sufficient to repeat the study (design, data, analysis, software)
- [ ] Uncertainty reported for headline results
- [ ] All numbers consistent across abstract, text, tables and figures
- [ ] Limitations that bound the main claim are stated
- [ ] Data and code availability statement
- [ ] AI-use disclosure, if AI tools contributed to results or text
- [ ] Ethics, permits and conflicts of interest statements, where applicable
- [ ] Every reference is real, correctly described, not retracted and supports the sentence that cites it (see `03e-citations.md`)
- [ ] Figures report uncertainty and do not misrepresent results (see `03f-figures.md`)

## Required — protocol
- [ ] Question, hypotheses and primary outcome defined
- [ ] Design, sampling unit and sample size justified
- [ ] Analysis plan fixed, including how the test/hold-out set is protected
- [ ] Success and stopping criteria defined
- [ ] Data management and ethics addressed

## Recommended
- [ ] Figures readable without the text
- [ ] Notation consistent and defined once
- [ ] Venue formatting and length limits met (if venue given)
- [ ] Every required statement and reviewer question in the venue pack addressed (if a pack is given)
- [ ] Supplementary material referenced from the main text
