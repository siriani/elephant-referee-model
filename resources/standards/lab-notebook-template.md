---
name: lab-notebook-template
version: 1.0.0
---
# Lab notebook

One entry per experiment, analysis run or decision, newest last. Never edit or delete a past entry; correct it with a new entry that refers to it.

```markdown
## <YYYY-MM-DD HH:MM> — <short title>
- **Kind:** experiment | analysis | data collection | decision | failure
- **Who:** <human name> | <agent and model> (with human approval: yes/no)
- **Protocol step:** <section of protocol.md, or "not in protocol">
- **What was run:** <command, script, notebook cell, instrument setting>
- **Code and config:** <git commit or file hash>; <config file path>
- **Inputs:** <data files, versions, sample IDs>
- **Outputs:** <result files, figures, tables — paths>
- **Result in one line:** <the number or observation, with its source file>
- **Deviation from protocol:** none | <what changed and why>
- **Discarded or repeated runs:** none | <which, and why>
- **Next:** <what this result changes in the plan>
```

Failures and negative results are recorded with the same care as successes: they are evidence too.
