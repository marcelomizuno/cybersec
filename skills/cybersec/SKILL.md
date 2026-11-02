---
name: cybersec
description: Practical cybersecurity reference for authorized security work — incident response playbooks, threat hunting queries (Splunk/Sigma/KQL/ELK), detection rules, log analysis (Windows Event IDs, Linux auth, web, firewall), system hardening with verification commands, web/API pentest methodology, red team and OSINT playbooks, cloud/IAM, containers/Kubernetes/DevSecOps, mobile and APK reversing, memory/disk forensics, cryptography/PKI, GDPR/HIPAA/PCI-DSS, smart contracts, and IoT Thread/OpenThread/Matter security. Use when the user asks to investigate an incident, write a detection or hunt query, harden a system, plan or run an authorized pentest/CTF/lab, analyze logs or artifacts, or assess Thread/Matter IoT deployments.
---

# Cybersec

A curated knowledge base distilled from the [Vyber07/cyber-security](https://huggingface.co/datasets/Vyber07/cyber-security) Hugging Face dataset (Apache-2.0). It is a set of **checklists, commands and query templates**, not ground truth: adapt to the user's environment, check tool versions and syntax, and prefer authoritative sources (MITRE ATT&CK, NVD, vendor docs) for specific CVEs, malware or threat-actor facts.

## How to use

1. Pick the reference(s) matching the task from the table below and read only those. Large files (`iot-thread.md`, `red-team.md`) — `grep -n '^## '` first to find the relevant section, then read that range.
2. Use the content as a starting point; tailor queries to the user's SIEM field names, log sources and platforms.
3. Offensive techniques are for authorized engagements, CTFs, labs and defensive understanding. When scope or authorization is unclear for an action against a real target, ask before proceeding.

## References

| File | Use for |
|---|---|
| `references/incident-response.md` | IR playbooks (ransomware, phishing, etc.): detection signs, containment, eradication, recovery; SOC setup |
| `references/threat-hunting.md` | Hunt hypotheses with Splunk, Sigma, KQL and ELK queries mapped to MITRE ATT&CK |
| `references/detection-patterns.md` | Common attacks (brute force, PsExec lateral movement, SQLi, …): how they work, log evidence, detection rules, defenses |
| `references/log-analysis.md` | Key Windows Event IDs, Linux auth, web server and firewall log analysis commands |
| `references/hardening.md` | Windows/Linux/web hardening steps with verification commands |
| `references/network-security.md` | Network attacks and defenses, iptables, IDS/IPS (Snort/Suricata) |
| `references/cloud-security.md` | AWS/Azure/GCP attacks, defenses, cloud pentest, IAM auditing |
| `references/containers-devsecops.md` | Docker/Kubernetes assessment, CI/CD security pipelines, dependency and supply chain security |
| `references/web-api-pentest.md` | Web app pentest methodology, REST/GraphQL API testing, VAPT scanning workflow |
| `references/red-team.md` | Red team playbook, OSINT recon, phishing/vishing and social engineering (attack and defense) |
| `references/mobile-reversing.md` | Android/iOS app testing, Frida, APK reverse engineering |
| `references/forensics.md` | Memory acquisition and Volatility analysis, disk forensics |
| `references/cryptography.md` | Algorithms, modes, attacks, OpenSSL/GPG commands, secure implementation (AES-GCM, etc.) |
| `references/compliance.md` | GDPR, HIPAA, PCI-DSS assessment checklists |
| `references/blockchain.md` | Smart contract audit tools and common Solidity vulnerabilities |
| `references/iot-thread.md` | Thread/OpenThread/Matter: architecture, key hierarchy, commissioning attacks, border router, mesh routing, red team playbook, testing lab, forensics, defenses |
