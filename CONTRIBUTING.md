# Contributing to ERM

Contributions are welcome: new rubrics for other study designs, reviewer personas for other fields, and support for other agent harnesses. Adapters are generated: edit `skills/`, `agents/` or `resources/`, then run `python3 scripts/build_adapters.py` and `python3 scripts/validate.py`. See [docs/harnesses.md](docs/harnesses.md).

## Layout

| Folder | Contents |
|---|---|
| `skills/<name>/SKILL.md` | Entry points (slash commands). Orchestration only. |
| `agents/*.md` | Goldfish reviewer personas: stateless system prompts for isolated sub-agents. |
| `resources/standards/*.md` | Versioned rubrics that personas load. Change the rubric, not the persona, when the criteria change. |
| `docs/` | Design docs and guides. |
| `tests/` | Fictional fixtures and structural checks. |

## Rules

1. **Never weaken goldfish isolation.** A change that lets reviewers see conversation history, author intent or a summary of either will be rejected.
2. **Rubrics are versioned.** Bump the `version:` field in a standard's frontmatter when you change its criteria, and note the change at the bottom of the file.
3. **No third-party manuscripts in the repository.** Test fixtures must be fictional or your own work. Never commit manuscripts received for peer review.
4. **No copied text.** Rubrics must be written in your own words; cite sources in the file.
5. Run `python3 scripts/validate.py` before opening a pull request.
