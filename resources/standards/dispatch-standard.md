---
name: dispatch-standard
version: 1.0.0
---
# Dispatch standard: how the elephant starts a goldfish

ERM runs in several agent harnesses. The method is the same in all of them; only the way a sub-agent is started differs.

## 1. Find ERM_ROOT

ERM_ROOT is the directory two levels above the `SKILL.md` you were invoked from, **after following symbolic links** (use `realpath` or equivalent). It must contain `agents/` and `resources/standards/`. If it does not, ask the user for the path of their ERM checkout. Never use a different ERM copy or version than the one whose skill you are running.

Every path you pass to a goldfish is **absolute**.

## 2. Start a fresh sub-agent

| Harness | How |
|---|---|
| Claude Code | Agent/Task tool with `subagent_type` `erm:<persona>` |
| OpenCode (after `adapters/opencode/install.py`) | `task` tool with `subagent_type` `<persona>`; omit `task_id` so a new session is created |
| Cursor | Task with the registered `<persona>` agent type |
| GitHub Copilot CLI | the `<persona>` custom agent of the `erm` plugin |
| Codex, Gemini CLI, Antigravity and any other harness | spawn a new general-purpose sub-agent with the generic prompt below |

Rules for every harness:
- One new sub-agent per reviewer and per run. Never resume, reuse or message an earlier reviewer.
- Never run the review in your own context and call it a goldfish. If no isolated sub-agent can be started, stop as the skill says.
- Wait for every reviewer of a stage before starting the next stage.

## 3. The generic goldfish prompt

Send exactly this, filled in, and nothing else:

```text
You are an ERM goldfish reviewer.
Read ERM_ROOT/agents/<persona>.md and follow it as your role. Ignore its YAML frontmatter.
ERM_ROOT: <absolute path>
Document: <absolute path>
Cited files: <absolute paths, or "none">
Rubric: ERM_ROOT/resources/standards/<rubric>.md
Finding format: ERM_ROOT/resources/standards/finding-format.md
Venue: <name, or "none">     Venue pack: <absolute path, or "none">
Other inputs required by your role: <absolute paths, or "none">
Write your report to: <absolute path>
```

Do not add the conversation, a summary of the project, the author's intent, your own opinion of the document, or any instruction to be lenient or harsh.

## 4. If the sub-agent cannot write files

Some harnesses start reviewers read-only. The reviewer then returns its full report as its reply, and you write it **verbatim** to the output path. Do not edit, shorten or soften it.
