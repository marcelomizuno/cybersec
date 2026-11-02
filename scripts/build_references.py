#!/usr/bin/env python3
"""Build skills/cybersec/references/*.md from a local copy of the
Vyber07/cyber-security Hugging Face dataset.

Usage:
    hf download Vyber07/cyber-security --repo-type dataset \
        --local-dir data/ $(python3 scripts/build_references.py --list)
    python3 -I scripts/build_references.py data/
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SOURCES = json.loads((REPO / "scripts" / "sources.json").read_text())
OUT = REPO / "skills" / "cybersec" / "references"
SKIP_KEYS = {"id", "category", "metadata", "Metadata", "note", "Input", "input", "Score", "Sentiment"}


def humanize(key: str) -> str:
    return key.replace("_", " ").replace("-", " ").strip().capitalize()


def render_value(value, depth: int) -> list[str]:
    """Render arbitrary JSON as Markdown."""
    lines: list[str] = []
    if isinstance(value, dict):
        for k, v in value.items():
            if k in SKIP_KEYS:
                continue
            if isinstance(v, str) and "\n" not in v and len(v) < 300:
                lines.append(f"- **{humanize(k) if not k[:1].isdigit() else k}**: {v}")
            elif isinstance(v, str):
                lang = "yaml" if v.lstrip().startswith("title:") else ""
                lines += ["", f"**{humanize(k)}**", "", f"```{lang}", v.rstrip(), "```", ""]
            else:
                lines += ["", "#" * min(depth, 6) + " " + humanize(k), ""]
                lines += render_value(v, depth + 1)
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, (dict, list)):
                lines += render_value(item, depth)
            else:
                lines.append(f"- {item}")
        lines.append("")
    else:
        lines.append(str(value))
    return lines


def demote_headings(md: str, min_level: int) -> str:
    """Shift Markdown headings so the document nests under our section heading."""
    out, in_code = [], False
    for line in md.splitlines():
        if line.lstrip().startswith("```"):
            in_code = not in_code
        if not in_code and line.startswith("#"):
            hashes = len(line) - len(line.lstrip("#"))
            line = "#" * min(hashes + min_level - 1, 6) + line[hashes:]
        out.append(line)
    return "\n".join(out)


def render_record(rec, level: int) -> str:
    """Render one record (conversation, instruction/output, or structured)."""
    if isinstance(rec, dict) and "conversations" in rec:
        turns = rec["conversations"]
        parts = []
        for t in turns:
            if t.get("from") == "human":
                parts.append(f"{'#' * level} {t['value'].strip()}\n")
            elif t.get("from") == "gpt":
                parts.append(demote_headings(t["value"].strip(), level + 1) + "\n")
        return "\n".join(parts)
    if isinstance(rec, dict) and ("Output" in rec or "output" in rec):
        q = (rec.get("Instruction") or rec.get("instruction") or "").strip()
        a = (rec.get("Output") or rec.get("output") or "").strip()
        return f"{'#' * level} {q}\n\n{demote_headings(a, level + 1)}\n"
    if isinstance(rec, dict):
        title = next((rec[k] for k in ("incident_type", "hunt_name", "attack_pattern", "system", "log_type", "name") if k in rec), None)
        body = {k: v for k, v in rec.items() if rec.get(k) != title}
        head = f"{'#' * level} {title}\n" if title else ""
        return head + "\n".join(render_value(body, level + 1)) + "\n"
    return "\n".join(render_value(rec, level)) + "\n"


# Anthropic's skill authoring guide recommends a table of contents for
# reference files longer than 100 lines, so partial reads still show scope.
TOC_MIN_LINES = 100


def table_of_contents(md: str) -> str:
    """List the level-2 headings (outside code blocks) as a contents section."""
    items, in_code = [], False
    for line in md.splitlines():
        if line.lstrip().startswith("```"):
            in_code = not in_code
        elif not in_code and line.startswith("## "):
            items.append(f"- {line[3:].strip()}")
    return "## Contents\n\n" + "\n".join(items) + "\n"


def build(data_dir: Path) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for fname, spec in SOURCES.items():
        if fname.startswith("_"):
            continue
        chunks = [f"# {spec['title']}\n",
                  "> Source: [Vyber07/cyber-security](https://huggingface.co/datasets/Vyber07/cyber-security) on Hugging Face (Apache-2.0). "
                  "Community-curated reference; verify commands and versions before use.\n"]
        for src in spec["sources"]:
            data = json.loads((data_dir / src).read_text())
            records = data if isinstance(data, list) else [data]
            for rec in records:
                chunks.append(render_record(rec, 2))
        text = "\n".join(chunks[2:])
        while "\n\n\n" in text:
            text = text.replace("\n\n\n", "\n\n")
        if text.count("\n") > TOC_MIN_LINES:
            text = table_of_contents(text) + "\n" + text
        text = "\n".join(chunks[:2]) + "\n" + text
        (OUT / fname).write_text(text.strip() + "\n")
        print(f"{fname}: {len(text) // 1024} KB")


if __name__ == "__main__":
    if sys.argv[1:] == ["--list"]:
        print(" ".join(s for k, v in SOURCES.items() if not k.startswith("_") for s in v["sources"]))
    elif len(sys.argv) == 2:
        build(Path(sys.argv[1]))
    else:
        sys.exit(__doc__)
