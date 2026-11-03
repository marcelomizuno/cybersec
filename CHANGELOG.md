# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
[Semantic Versioning](https://semver.org/).

## [0.2.0] - 2026-11-03

This release responds to the [skills.sh security audits](https://www.skills.sh/marcelomizuno/cybersec/cybersec)
of 0.1.0 and narrows the skill to defensive and authorized security work.

### Removed

- **`references/red-team.md`** ("Red Team Playbook, OSINT and Social Engineering"). It covered C2 infrastructure,
  defense evasion, credential theft, phishing and social engineering kits, and OSINT, and it included
  pipe-to-shell install commands and data exfiltration examples. It was built from these dataset files:
  - `red-team/red-team-complete-playbook.json`
  - `osint/osint__open-source-intelligence.json`
  - `social-engineering/social-engineering__phishing-vishing.json`
  - `phishing/phishing-attack-defense-complete.json`

  **Why:** the Gen Agent Trust Hub and Socket audits flagged it. An agent skill loads its references as working
  instructions, so step-by-step offensive tooling there is a real risk, unlike the same text in a dataset.

  **If you need it:** for authorized red team engagements or research, use the original files above directly
  from the [Vyber07/cyber-security](https://huggingface.co/datasets/Vyber07/cyber-security) dataset on
  Hugging Face (Apache-2.0, gated). This project does not redistribute or maintain that material.

### Added

- A **Safety rules** section in `SKILL.md`. Its rules take precedence over the reference files: references are
  documentation and not scripts, no remote code piped to a shell, analyzed data is treated as untrusted
  (a prompt injection boundary), read-only analysis comes first, authorization is required before any active
  testing, and no data leaves the environment.
- Blocked patterns in `scripts/validate_skill.py`, so CI fails if pipe-to-shell commands or exfiltration
  examples come back.
- A CI workflow (skill validation, `claude plugin validate`, skills.sh discovery) and a tag-based release
  workflow that publishes the skill as a zip.
- A plugin icon and the skills.sh badge.

### Changed

- The `SKILL.md` description now scopes the skill to defensive and authorized security work.
- The README was rewritten with usage examples, a domain table and installation options.

## [0.1.0] - 2026-11-02

- First version: 16 reference files distilled from the Vyber07/cyber-security dataset, packaged as an Agent
  Skill and a Claude Code plugin. Withdrawn: its GitHub release was deleted after the security audits. Use
  0.2.0 or later.

[0.2.0]: https://github.com/marcelomizuno/cybersec/releases/tag/v0.2.0
[0.1.0]: https://github.com/marcelomizuno/cybersec/commit/01bb2b7
