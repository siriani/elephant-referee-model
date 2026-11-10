# Instructions for agents working in this repository

- This repository *is* a plugin. Skills live in `skills/`, goldfish personas in `agents/`, rubrics in `resources/standards/`.
- Keep skills about orchestration and personas about judgment. Criteria belong in rubrics, so they can be versioned and reused.
- Any skill that runs a review must spawn isolated sub-agents and pass them only file paths. If sub-agents are unavailable, the skill must stop and say so.
- Write everything in English.
- After editing, run `python3 scripts/validate.py`.
