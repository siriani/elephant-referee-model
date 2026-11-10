# Agent harnesses

ERM's method lives in plain files: skills (`skills/*/SKILL.md`), goldfish personas (`agents/*.md`) and versioned standards (`resources/standards/`). Each harness gets a thin adapter generated from those files by `scripts/build_adapters.py`. The method is the same everywhere; only the way a goldfish is started differs, as set out in [`dispatch-standard.md`](../resources/standards/dispatch-standard.md).

## Support status

| Harness | Install | Skills found | Goldfish found | Full review run |
|---|---|---|---|---|
| Claude Code | `claude plugin validate` passes | yes | yes | not yet run |
| OpenCode 2.1 | installer tested | yes (8) | yes (11), checked in a live session | not yet run |
| Gemini CLI 0.38 | `gemini extensions validate` passes | yes (8) | yes (11), loaded without errors | not yet run |
| Codex (CLI and desktop) | manifests generated | untested | via generic prompt | not yet run |
| GitHub Copilot CLI | manifests and agent profiles generated | untested | untested | not yet run |
| Cursor | manifests, agents and rule generated | untested | untested | not yet run |
| Antigravity | Agent Plugins manifest generated | untested | via generic prompt | not yet run |

"Not yet run" means nobody has yet run a complete review in that harness and checked the reports. Please open an issue with what you saw, especially whether the goldfish really started without the conversation.

## Claude Code

```bash
claude plugin marketplace add siriani/elephant-referee-model
claude plugin install erm@erm
```

Commands: `/erm:erm-review <file>`, `/erm:erm-brainstorm <idea>`, and so on.

## OpenCode

```bash
git clone https://github.com/siriani/elephant-referee-model.git ~/erm
python3 ~/erm/adapters/opencode/install.py                  # all projects (~/.config/opencode)
python3 ~/erm/adapters/opencode/install.py --project .      # or only this project (.opencode/)
```

The installer links the skills back to the checkout and writes one OpenCode subagent per goldfish. It refuses to overwrite files it did not create, and `--uninstall` removes only its own files. Keep the checkout in place; after `git pull`, run the installer again. In a session, ask in plain words, for example: "Use the erm-review skill to review /abs/path/manuscript.md".

## Gemini CLI

```bash
gemini extensions install https://github.com/siriani/elephant-referee-model
```

Gemini loads the skills from `skills/`, the goldfish from `agents/`, and the routing rules from `GEMINI.md`.

## Codex

```bash
codex plugin marketplace add siriani/elephant-referee-model
codex plugin add erm@erm
```

In the desktop app, add the same marketplace from the plugin settings. Pick the ERM skill from the skill picker. Codex starts goldfish as general sub-agents using the generic prompt in `dispatch-standard.md`; reviews need a session that can start sub-agents.

## GitHub Copilot CLI

```bash
copilot plugin install siriani/elephant-referee-model
```

Goldfish profiles are in `com.github.copilot/agents/`. They are read-only, so the main agent writes each returned report to disk unchanged.

## Cursor

Install from a local checkout through Cursor's plugin settings. The plugin registers the skills, one agent per goldfish (`.cursor-plugin/agents/`) and a routing rule (`.cursor-plugin/rules/erm.mdc`).

## Antigravity

```bash
agy plugin install https://github.com/siriani/elephant-referee-model
```

## Maintainers

After changing a persona, a skill name or the version, run:

```bash
python3 scripts/build_adapters.py
python3 scripts/validate.py
```

`validate.py` fails if any generated adapter is out of date, if a frontmatter block is not valid YAML, or if a persona carries keys that Gemini CLI rejects.
