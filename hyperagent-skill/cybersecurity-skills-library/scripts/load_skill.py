#!/usr/bin/env python3
"""Load one skill's full content for execution.

Prints the SKILL.md body and lists reference/script/asset files so an agent can
follow the complete practitioner workflow. Accepts a skill name or a path.

Examples:
  python load_skill.py analyzing-email-headers-for-phishing-investigation
  python load_skill.py skills/abusing-dpapi-for-credential-access --refs
"""
import argparse, os, sys

ROOT = os.environ.get("ACS_ROOT", os.getcwd())

def resolve(name):
    if os.path.isdir(os.path.join(ROOT, name)):
        return os.path.join(ROOT, name)
    cand = os.path.join(ROOT, "skills", name)
    if os.path.isdir(cand):
        return cand
    sys.exit(f"skill not found: {name}")

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("skill", help="skill name or path")
    ap.add_argument("--refs", action="store_true", help="also print reference files inline")
    a = ap.parse_args()

    d = resolve(a.skill)
    md = os.path.join(d, "SKILL.md")
    if not os.path.isfile(md):
        sys.exit(f"SKILL.md missing in {d}")
    print(open(md, encoding="utf-8", errors="ignore").read())

    extras = []
    for sub in ("references", "scripts", "assets"):
        subd = os.path.join(d, sub)
        if os.path.isdir(subd):
            for f in sorted(os.listdir(subd)):
                extras.append(os.path.join(sub, f))
    if extras:
        print("\n--- Supporting files ---")
        for e in extras:
            print(f"  {e}")
    if a.refs:
        rd = os.path.join(d, "references")
        if os.path.isdir(rd):
            for f in sorted(os.listdir(rd)):
                print(f"\n===== references/{f} =====")
                print(open(os.path.join(rd, f), encoding="utf-8", errors="ignore").read())

if __name__ == "__main__":
    main()
