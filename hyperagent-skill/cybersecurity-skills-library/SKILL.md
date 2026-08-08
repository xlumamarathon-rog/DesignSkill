# Cybersecurity Skills Library (Router / Loader)

A router over the **Anthropic Cybersecurity Skills** library — 817 production-grade,
agentskills.io-format cybersecurity skills across 29 subdomains, each mapped to up to
six industry frameworks (MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, MITRE D3FEND,
NIST AI RMF, MITRE F3 "Fight Fraud"). This skill does not replace those skills; it
teaches an agent how to **discover the right one, load it progressively, and follow
its practitioner workflow.**

> ⚠️ **Authorized, lawful use only.** The library includes offensive and dual-use
> techniques (red-team C2, phishing simulation, credential access, exploitation).
> Use only for authorized penetration testing, security research, defense, and
> education with explicit permission. Refuse and stop if a request lacks authorization.
>
> This is a mirror of a community project (mukul975/Anthropic-Cybersecurity-Skills),
> Apache-2.0 licensed, **not affiliated with Anthropic PBC.**

## When to Use
- The user asks for a security investigation, playbook, or "how would an analyst do X"
  in DFIR, malware analysis, threat hunting, cloud/container security, red/purple team,
  IAM, AppSec/API security, incident response, AI/LLM security, fraud, or compliance.
- You need a MITRE ATT&CK / D3FEND / ATLAS / NIST CSF / NIST AI RMF / MITRE F3 mapped
  procedure rather than a generic checklist.
- You want to enumerate coverage for a specific technique ID (e.g. T1566.001, AML.T0052).

## Why a router instead of 817 skills
Each skill is tiny to scan (~30 tokens of frontmatter) and cheap to fully load
(500–2,000 tokens). Progressive disclosure lets you search all 817 in one pass, then
load only the one you need — never pull the whole library into context.

## Architecture of the library
```
index.json                     # {name, description, domain, path} for all 817 skills — search this first
skills/<skill-name>/SKILL.md   # YAML frontmatter + structured Markdown workflow
skills/<skill-name>/references/*.md   # standards, CVEs, deep procedure
skills/<skill-name>/scripts/*.py|ps1  # real helper scripts
skills/<skill-name>/assets/*          # templates, checklists
docs/mitre-f3-mapping.md       # F3 frontmatter schema
mappings/                      # ATT&CK Navigator layer, NIST CSF / OWASP crosswalks
tools/validate-*.py            # frontmatter validators + JSON schema
```

### SKILL.md frontmatter fields
`name` (kebab-case, matches dir), `description` (what + when, keyword-rich),
`domain`, `subdomain`, `tags`, `version`, `author`, `license`, and framework maps:
`mitre_attack` (T-IDs), `nist_csf` (e.g. RS.AN-03), `atlas_techniques` (AML.*),
`d3fend_techniques`, `nist_ai_rmf`, `mitre_f3` (structured block, F-IDs + reused T-IDs).
Body sections: When to Use · Prerequisites · Workflow · Key Concepts · Tools & Systems ·
Common Scenarios · Output Format.

## Workflow (how to use this skill)
1. **Sync** the library locally (first run only):
   `python scripts/sync_library.py --dest acs-library` then export `ACS_ROOT=acs-library`.
2. **Search** for candidates — fast (index) or deep (frontmatter):
   - Keyword: `python scripts/search_skills.py "beacon config"`
   - By subdomain: `python scripts/search_skills.py --subdomain cloud-security`
   - By technique: `python scripts/search_skills.py --technique T1566.001`
   - By framework presence: `python scripts/search_skills.py --framework mitre_f3`
3. **Load** the chosen skill's full workflow:
   `python scripts/load_skill.py <skill-name> --refs`
4. **Execute** the workflow's numbered steps with real commands, honoring prerequisites
   and the authorized-use guardrail. Use its `scripts/` and `references/` as provided.
5. **Report** in the skill's Output Format, citing the framework technique IDs it maps to.

## Subdomains (817 skills)
cloud-security (66) · threat-hunting (58) · threat-intelligence (52) · network-security (43) ·
web-application-security (42) · digital-forensics (41) · malware-analysis (39) ·
identity-access-management (37) · soc-operations (35) · red-teaming (33) ·
container-security (33) · security-operations (28) · ot-ics-security (28) · api-security (28) ·
incident-response (26) · vulnerability-management (25) · penetration-testing (21) ·
devsecops (18) · zero-trust-architecture (17) · endpoint-security (17) · cryptography (16) ·
phishing-defense (15) · ai-security (14) · ransomware-defense (13) · mobile-security (13) ·
compliance-governance (9) · supply-chain-security (8) · plus deception, hardware/firmware,
wireless, blockchain, privacy, purple-team and more.

## Framework coverage
MITRE ATT&CK v19.1 · NIST CSF 2.0 · MITRE ATLAS 2026.07 · MITRE D3FEND v1.4.0 ·
NIST AI RMF 1.0 · MITRE F3 v1.1. See `mappings/` and `docs/mitre-f3-mapping.md`.

## Helper scripts
- `scripts/sync_library.py` — clone/update the library over HTTPS.
- `scripts/search_skills.py` — search index + frontmatter by keyword, subdomain, technique, or framework.
- `scripts/load_skill.py` — print a skill's full SKILL.md and (optionally) its references.

All scripts read `ACS_ROOT` (defaults to CWD) to locate `index.json` and `skills/`.

## Attribution & license
Skills authored by the mukul975/Anthropic-Cybersecurity-Skills community, Apache-2.0.
This router preserves that license and attribution (see `NOTICE`).
