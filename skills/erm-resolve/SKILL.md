---
name: erm-resolve
description: Work through ERM review findings with the user, one decision at a time, revise the document for accepted findings and keep a response log. Use after erm-review, or when the user wants to address reviewer comments.
---

# erm-resolve — deciding on findings

You are the **elephant** again: you now bring back the project context the goldfish lacked. The user decides.

## Input

`/erm-resolve <review-folder>`; if omitted, use the most recent folder under `erm-reviews/`. Read `04-synthesis.md` and the document it reviewed.

## Procedure

1. Present findings in severity order (critical → major → minor), in batches of at most five.
2. For each finding give: ID, one-line restatement, your assessment with the project context (is it valid, partly valid, a misunderstanding caused by missing text?), and a proposed action.
3. The user chooses: **accept**, **accept with changes**, **reject** (with reason), or **defer**.
4. A finding the goldfish got "wrong" because context was missing is usually a **text** problem: the document should have said it. Default to clarifying the text rather than rejecting.
5. Apply only accepted changes to the document. Do not change anything else.
6. Append each decision to `<review-folder>/response_log.md`:

```markdown
### F-07 (major) — Test split never reported
Decision: accepted
Action: Added Table 3 with test-split metrics; abstract updated.
Location: manuscript_draft.md §4.1, Table 3
```

7. The response log is reusable as a point-by-point response to journal reviewers.

When all critical and major findings are decided, suggest `/erm-drift` and, if the changes were large, a fresh `/erm-review`.
