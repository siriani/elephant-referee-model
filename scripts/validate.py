#!/usr/bin/env python3
"""Structural checks for the ERM plugin. Run: python3 scripts/validate.py"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{path.relative_to(ROOT)}: missing frontmatter")
        return {}
    fields = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip()
    return fields


for manifest in [".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"]:
    try:
        json.loads((ROOT / manifest).read_text())
    except Exception as e:  # noqa: BLE001
        errors.append(f"{manifest}: invalid JSON ({e})")

skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
agents = sorted((ROOT / "agents").glob("*.md"))
standards = sorted((ROOT / "resources/standards").glob("*.md"))
agent_names = {p.stem for p in agents}
standard_files = {p.name for p in standards}

for p in skills:
    fm = frontmatter(p)
    if fm.get("name") != p.parent.name:
        errors.append(f"{p.relative_to(ROOT)}: name must equal folder '{p.parent.name}'")
    if not fm.get("description"):
        errors.append(f"{p.relative_to(ROOT)}: missing description")

for p in agents:
    fm = frontmatter(p)
    if fm.get("name") != p.stem:
        errors.append(f"{p.relative_to(ROOT)}: name must equal file stem")
    if not fm.get("description"):
        errors.append(f"{p.relative_to(ROOT)}: missing description")

for p in standards:
    fm = frontmatter(p)
    if not re.fullmatch(r"\d+\.\d+\.\d+", fm.get("version", "")):
        errors.append(f"{p.relative_to(ROOT)}: version must be semver")

# Every referenced standard and persona must exist.
for p in skills + agents:
    text = p.read_text(encoding="utf-8")
    for ref in set(re.findall(r"`([a-z0-9-]+(?:-standard|-format|-template)\.md)`", text)):
        if ref not in standard_files:
            errors.append(f"{p.relative_to(ROOT)}: references missing standard {ref}")
    for ref in set(re.findall(r"`(erm-[a-z-]+)`", text)):
        is_skill = (ROOT / "skills" / ref).is_dir()
        if ref not in agent_names and not is_skill:
            errors.append(f"{p.relative_to(ROOT)}: references unknown persona/skill {ref}")

# Isolation guard: review skills must contain the stop rule.
for name in ["erm-review", "erm-brainstorm"]:
    text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8").lower()
    if "stop" not in text or "sub-agent" not in text:
        errors.append(f"skills/{name}: missing isolation stop rule")

# Frontmatter must be valid YAML for every harness (Gemini CLI and Cursor parse it strictly).
try:
    import yaml  # type: ignore

    for p in skills + agents + standards:
        block = re.match(r"^---\n(.*?)\n---\n", p.read_text(encoding="utf-8"), re.S)
        if block:
            try:
                yaml.safe_load(block.group(1))
            except yaml.YAMLError as e:
                errors.append(f"{p.relative_to(ROOT)}: invalid YAML frontmatter ({e.__class__.__name__})")
except ImportError:
    print("note: PyYAML not installed; YAML frontmatter not checked")

# Gemini CLI loads agents/ with a strict schema: no tool list, no extra keys.
for p in agents:
    extra = set(frontmatter(p)) - {"name", "description", "model"}
    if extra:
        errors.append(f"{p.relative_to(ROOT)}: frontmatter keys {sorted(extra)} break Gemini CLI; keep name/description only")

# Generated harness adapters must be up to date.
import subprocess  # noqa: E402

r = subprocess.run([sys.executable, str(ROOT / "scripts/build_adapters.py"), "--check"], capture_output=True, text=True)
if r.returncode:
    errors.append("harness adapters out of date: run python3 scripts/build_adapters.py\n" + r.stdout.strip())

print(f"skills={len(skills)} personas={len(agents)} standards={len(standards)}")
if errors:
    print("\n".join(f"ERROR {e}" for e in errors))
    sys.exit(1)
print("OK")
