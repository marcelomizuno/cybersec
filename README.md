# cybersec

A Claude Code skill with a curated cybersecurity reference knowledge base, built from the
[Vyber07/cyber-security](https://huggingface.co/datasets/Vyber07/cyber-security) Hugging Face dataset (Apache-2.0).

Out of the original ~18 GB dataset, only the structured, practical guides were kept: incident response
playbooks, threat hunting queries, detection patterns, log analysis, hardening, web/API pentesting,
red teaming, cloud, containers, forensics, cryptography, compliance, and IoT Thread/Matter security.
Duplicates, ARVO source tarballs, synthetic scenarios (`*-realtime-scenarios`, `*-real-examples*`) and
template-generated MITRE malware entries were left out.

## Layout

```
.claude-plugin/              plugin manifest + local marketplace
skills/cybersec/             the skill (SKILL.md + references/*.md)
scripts/sources.json         mapping: reference file -> dataset source files
scripts/build_references.py  generates references/*.md from the dataset
```

## Installation

As a personal skill (symlink):

```bash
ln -s "$PWD/skills/cybersec" ~/.claude/skills/cybersec
```

Or as a plugin:

```
/plugin marketplace add marcelomizuno/cybersec
/plugin install cybersec@cybersec
```

## Rebuilding the references

The dataset is gated: accept its terms on Hugging Face and run `hf auth login` first.

```bash
hf download Vyber07/cyber-security --repo-type dataset --local-dir data/ \
    $(python3 scripts/build_references.py --list)
python3 -I scripts/build_references.py data/
```

To add or remove content, edit `scripts/sources.json`.

## License

Apache-2.0. Reference content is derived from the Vyber07/cyber-security dataset; see `NOTICE`.
