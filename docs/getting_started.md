# Getting started

## 1. Install (Claude Code)

```bash
claude plugin marketplace add siriani/elephant-referee-model
claude plugin install erm@erm
```

Open a new session in your project folder.

## 2. Try a review on the fixture

The repository ships a short fictional manuscript with deliberate problems:

```text
/erm:erm-review tests/fixtures/toy_manuscript.md --type manuscript
```

You should get a folder under `erm-reviews/toy_manuscript/` with five stage reports. The fixture's planted problems are listed in `tests/fixtures/README.md`; compare.

## 3. Use it on your own work

- Starting from an idea: `/erm:erm-brainstorm <your idea>`
- Have a plan: `/erm:erm-protocol`
- Have results: `/erm:erm-draft`
- Have a draft: `/erm:erm-review <file>` → `/erm:erm-resolve` → `/erm:erm-drift`
- Before submission: `/erm:erm-provenance`

## Tips

- Keep cited files (tables, supplementary material, configs) next to the document so goldfish can read them.
- Tag numbers with `<!-- src: file … -->` while drafting; drift checks become mechanical.
- If a goldfish misunderstood something, ask first whether the text should have said it.
