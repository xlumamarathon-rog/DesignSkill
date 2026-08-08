# DesignSkill — Cybersecurity Skills Library (mirror + router)

A **full mirror** of the [Anthropic Cybersecurity Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
library — **817 production-grade, agentskills.io-format cybersecurity skills** across 29
subdomains, each mapped to up to six industry frameworks — **plus a Hyperagent router
skill** for discovering and loading them.

> ⚠️ **Community project — not affiliated with Anthropic PBC.** Apache-2.0 licensed.
> Skills authored by mukul975 and contributors; this repo preserves their license and
> attribution (see [`NOTICE`](NOTICE)).
>
> 🔐 **Authorized, lawful use only.** Includes offensive/dual-use techniques (red-team
> C2, phishing simulation, credential access, exploitation). Use only for authorized
> testing, research, defense, and education.

## What's inside
| Path | Contents |
|------|----------|
| `skills/` | 817 skills, each `SKILL.md` (YAML frontmatter + workflow) with `references/`, `scripts/`, `assets/` |
| `index.json` | Searchable catalog: name, description, domain, path for all 817 skills |
| `mappings/` | MITRE ATT&CK Navigator layer, NIST CSF / OWASP crosswalks |
| `docs/` | MITRE F3 mapping schema |
| `tools/` | Frontmatter validators + JSON schema |
| `hyperagent-skill/cybersecurity-skills-library/` | Router skill: `SKILL.md` + `scripts/` (sync, search, load) |

## Frameworks
MITRE ATT&CK v19.1 · NIST CSF 2.0 · MITRE ATLAS 2026.07 · MITRE D3FEND v1.4.0 ·
NIST AI RMF 1.0 · MITRE F3 (Fight Fraud) v1.1.

## Quick start (router skill)
```bash
export ACS_ROOT="$(pwd)"                       # this repo root (has index.json + skills/)
# search
python hyperagent-skill/cybersecurity-skills-library/scripts/search_skills.py "beacon config"
python hyperagent-skill/cybersecurity-skills-library/scripts/search_skills.py --subdomain cloud-security
python hyperagent-skill/cybersecurity-skills-library/scripts/search_skills.py --technique T1566.001
# load a full workflow
python hyperagent-skill/cybersecurity-skills-library/scripts/load_skill.py analyzing-email-headers-for-phishing-investigation --refs
```
Each skill costs ~30 tokens to scan (frontmatter) and 500–2,000 to fully load —
progressive disclosure lets an agent search all 817 in one pass, then load only what it needs.

## Subdomains (817 skills)
cloud-security (66) · threat-hunting (58) · threat-intelligence (52) · network-security (43) ·
web-application-security (42) · digital-forensics (41) · malware-analysis (39) ·
identity-access-management (37) · soc-operations (35) · red-teaming (33) · container-security (33) ·
security-operations (28) · ot-ics-security (28) · api-security (28) · incident-response (26) ·
vulnerability-management (25) · penetration-testing (21) · devsecops (18) ·
zero-trust-architecture (17) · endpoint-security (17) · cryptography (16) · phishing-defense (15) ·
ai-security (14) · ransomware-defense (13) · mobile-security (13) · compliance-governance (9) ·
supply-chain-security (8) · and more.

## License & attribution
Apache-2.0 — see [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE). Upstream:
https://github.com/mukul975/Anthropic-Cybersecurity-Skills

*Note: the upstream `assets/banner.png` image is omitted from this mirror (binary asset).*
