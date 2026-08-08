#!/usr/bin/env python3
"""Search the Anthropic-Cybersecurity-Skills library.

Searches index.json (name + description + domain) and, when --deep is used,
the YAML frontmatter of each SKILL.md (subdomain, tags, and framework
technique IDs: mitre_attack, nist_csf, atlas_techniques, d3fend_techniques,
nist_ai_rmf, mitre_f3).

Examples:
  python search_skills.py phishing
  python search_skills.py --subdomain cloud-security
  python search_skills.py --technique T1566.001 --deep
  python search_skills.py --framework mitre_f3 --deep
  python search_skills.py ransomware --limit 20 --json
"""
import argparse, json, os, re, sys

ROOT = os.environ.get("ACS_ROOT", os.getcwd())

def load_index(root):
    p = os.path.join(root, "index.json")
    if not os.path.isfile(p):
        sys.exit(f"index.json not found at {p} (set ACS_ROOT or run --sync first)")
    return json.load(open(p, encoding="utf-8"))["skills"]

def read_frontmatter(skill_path):
    md = os.path.join(ROOT, skill_path, "SKILL.md")
    if not os.path.isfile(md):
        return ""
    txt = open(md, encoding="utf-8", errors="ignore").read()
    m = re.match(r"^---\n(.*?)\n---", txt, re.S)
    return m.group(1) if m else ""

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="?", default="", help="keyword matched against name + description")
    ap.add_argument("--subdomain", help="filter by subdomain (requires reading frontmatter)")
    ap.add_argument("--technique", help="framework technique ID, e.g. T1566.001, RS.AN-03, AML.T0052 (implies --deep)")
    ap.add_argument("--framework", help="only skills that carry this framework key: mitre_attack|nist_csf|atlas_techniques|d3fend_techniques|nist_ai_rmf|mitre_f3 (implies --deep)")
    ap.add_argument("--deep", action="store_true", help="read every SKILL.md frontmatter (slower, needed for subdomain/technique/framework)")
    ap.add_argument("--limit", type=int, default=40)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    deep = a.deep or bool(a.subdomain or a.technique or a.framework)
    skills = load_index(ROOT)
    q = a.query.lower()
    out = []
    for s in skills:
        hay = (s["name"] + " " + s.get("description", "")).lower()
        if q and q not in hay:
            continue
        fm = read_frontmatter(s["path"]) if deep else ""
        if a.subdomain and f"subdomain: {a.subdomain}" not in fm:
            continue
        if a.technique and a.technique not in fm:
            continue
        if a.framework and not re.search(rf"^{re.escape(a.framework)}\s*:", fm, re.M):
            continue
        out.append(s)
        if len(out) >= a.limit:
            break

    if a.json:
        print(json.dumps(out, indent=2))
    else:
        print(f"{len(out)} match(es){' (showing limit)' if len(out)>=a.limit else ''}\n")
        for s in out:
            desc = s.get("description", "")
            print(f"• {s['name']}")
            print(f"    {desc[:160]}{'…' if len(desc)>160 else ''}")
            print(f"    path: {s['path']}\n")

if __name__ == "__main__":
    main()
