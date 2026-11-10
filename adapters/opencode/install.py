#!/usr/bin/env python3
"""Install ERM into OpenCode: skills as symbolic links, goldfish personas as OpenCode subagents.

    python3 adapters/opencode/install.py                 # into ~/.config/opencode (all projects)
    python3 adapters/opencode/install.py --project DIR   # into DIR/.opencode (one project)
    python3 adapters/opencode/install.py --uninstall     # remove what this script installed

Keep this checkout where it is: the installed skills link back to it. Run `git pull` here to update,
then re-run the installer so the subagents pick up persona changes.
"""
import argparse
import re
import sys
from pathlib import Path

ERM_ROOT = Path(__file__).resolve().parents[2]
WEB_PERSONAS = {"erm-citation-auditor", "erm-lens"}
MARK = "<!-- installed by ERM adapters/opencode/install.py -->"


def split_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').replace('\\"', '"')
    return fm, m.group(2)


def agent_file(path: Path) -> str:
    fm, body = split_frontmatter(path.read_text(encoding="utf-8"))
    web = fm["name"] in WEB_PERSONAS
    desc = fm["description"].replace('"', "'")
    return (
        "---\n"
        f'description: "{desc}"\n'
        "mode: subagent\n"
        "tools:\n"
        "  write: true\n"
        "  edit: false\n"
        "  bash: true\n"
        f"  webfetch: {'true' if web else 'false'}\n"
        "  task: false\n"
        "---\n"
        f"{MARK}\n"
        f"ERM_ROOT: {ERM_ROOT}\n"
        "Resolve every rubric and standard named below against ERM_ROOT/resources/standards/.\n"
        "Use only the files named in your task. Do not delegate.\n"
        f"{body}"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--project", type=Path, help="install into PROJECT/.opencode instead of ~/.config/opencode")
    ap.add_argument("--uninstall", action="store_true")
    ap.add_argument("--force", action="store_true", help="replace erm-* files not created by this script")
    a = ap.parse_args()

    target = (a.project.resolve() / ".opencode") if a.project else Path.home() / ".config/opencode"
    agent_dir, skill_dir = target / "agent", target / "skills"
    personas = sorted((ERM_ROOT / "agents").glob("erm-*.md"))
    skills = sorted(p for p in (ERM_ROOT / "skills").iterdir() if (p / "SKILL.md").exists())

    def ours(p: Path) -> bool:
        if p.is_symlink():
            return str(p.resolve()).startswith(str(ERM_ROOT))
        return p.is_file() and MARK in p.read_text(encoding="utf-8", errors="ignore")

    planned = [(agent_dir / p.name) for p in personas] + [(skill_dir / s.name) for s in skills]
    if a.uninstall:
        for p in list(agent_dir.glob("erm-*.md")) + list(skill_dir.glob("erm-*")):
            if ours(p):
                p.unlink()
                print("removed", p)
        return 0

    conflicts = [p for p in planned if (p.exists() or p.is_symlink()) and not ours(p)]
    if conflicts and not a.force:
        print("Refusing to overwrite files not created by ERM:\n  " + "\n  ".join(map(str, conflicts)))
        print("Move them away or re-run with --force.")
        return 1

    agent_dir.mkdir(parents=True, exist_ok=True)
    skill_dir.mkdir(parents=True, exist_ok=True)
    for p in personas:
        (agent_dir / p.name).write_text(agent_file(p), encoding="utf-8")
    for s in skills:
        link = skill_dir / s.name
        if link.is_symlink() or link.exists():
            link.unlink()
        link.symlink_to(s, target_is_directory=True)
    print(f"ERM installed into {target}")
    print(f"  {len(skills)} skills linked to {ERM_ROOT / 'skills'}")
    print(f"  {len(personas)} goldfish subagents in {agent_dir}")
    print("Start a new OpenCode session and ask, for example: 'Use the erm-review skill to review /abs/path/manuscript.md'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
