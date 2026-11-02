#!/usr/bin/env python3
"""Validate the cybersec skill against Anthropic's skill authoring rules.

Checks:
- SKILL.md frontmatter: `name` and `description` constraints
- SKILL.md body under 500 lines
- every reference linked from SKILL.md exists, and every reference file is linked
- reference files: balanced code fences, a Contents section when over 100 lines
- plugin.json / marketplace.json parse and agree on the plugin name
- optional: --tag vX.Y.Z must match plugin.json version

Exits non-zero with one line per problem.
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILL_DIR = REPO / "skills" / "cybersec"

# Limits from https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
NAME_MAX = 64
DESCRIPTION_MAX = 1024
BODY_MAX_LINES = 500
TOC_MIN_LINES = 100
RESERVED_WORDS = ("anthropic", "claude")

errors: list[str] = []


def error(msg: str) -> None:
    errors.append(msg)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not match:
        error("SKILL.md: missing YAML frontmatter delimited by '---'")
        return {}, text
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields, match.group(2)


def check_skill_md() -> set[str]:
    path = SKILL_DIR / "SKILL.md"
    if not path.exists():
        error(f"{path.relative_to(REPO)} not found")
        return set()
    fields, body = parse_frontmatter(path.read_text())

    name = fields.get("name", "")
    if not name:
        error("SKILL.md: `name` is required")
    elif len(name) > NAME_MAX or not re.fullmatch(r"[a-z0-9-]+", name):
        error(f"SKILL.md: `name` must be <= {NAME_MAX} chars of lowercase letters, digits and hyphens")
    elif any(w in name for w in RESERVED_WORDS):
        error(f"SKILL.md: `name` must not contain reserved words {RESERVED_WORDS}")
    if name and name != SKILL_DIR.name:
        error(f"SKILL.md: `name` ({name}) must match its directory ({SKILL_DIR.name})")

    desc = fields.get("description", "")
    if not desc:
        error("SKILL.md: `description` is required")
    elif len(desc) > DESCRIPTION_MAX:
        error(f"SKILL.md: `description` is {len(desc)} chars (max {DESCRIPTION_MAX})")
    if re.search(r"<[^>]+>", name + desc):
        error("SKILL.md: `name`/`description` must not contain XML tags")

    if body.count("\n") > BODY_MAX_LINES:
        error(f"SKILL.md: body exceeds {BODY_MAX_LINES} lines")

    links = set(re.findall(r"\]\((references/[^)]+\.md)\)", body))
    for link in sorted(links):
        if not (SKILL_DIR / link).exists():
            error(f"SKILL.md links to missing file {link}")
    return links


def check_references(linked: set[str]) -> None:
    ref_dir = SKILL_DIR / "references"
    for path in sorted(ref_dir.glob("*.md")):
        rel = f"references/{path.name}"
        text = path.read_text()
        if rel not in linked:
            error(f"{rel} is not linked from SKILL.md")
        fences = sum(1 for line in text.splitlines() if line.lstrip().startswith("```"))
        if fences % 2:
            error(f"{rel}: unbalanced ``` code fences")
        if text.count("\n") > TOC_MIN_LINES and "\n## Contents\n" not in text:
            error(f"{rel}: over {TOC_MIN_LINES} lines without a '## Contents' section")


def check_manifests(tag: str | None) -> None:
    try:
        plugin = json.loads((REPO / ".claude-plugin" / "plugin.json").read_text())
        market = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text())
    except (OSError, json.JSONDecodeError) as exc:
        error(f"plugin manifests: {exc}")
        return
    names = [p.get("name") for p in market.get("plugins", [])]
    if plugin.get("name") not in names:
        error(f"marketplace.json does not list plugin {plugin.get('name')!r}")
    if tag:
        version = tag.removeprefix("v")
        if plugin.get("version") != version:
            error(f"tag {tag} does not match plugin.json version {plugin.get('version')}")


def main() -> None:
    tag = None
    if len(sys.argv) == 3 and sys.argv[1] == "--tag":
        tag = sys.argv[2]
    elif len(sys.argv) != 1:
        sys.exit("usage: validate_skill.py [--tag vX.Y.Z]")
    check_references(check_skill_md())
    check_manifests(tag)
    if errors:
        print("\n".join(f"ERROR: {e}" for e in errors))
        sys.exit(1)
    print("Skill validation passed")


if __name__ == "__main__":
    main()
