#!/usr/bin/env python3
"""Clone or update the cybersecurity skills library locally.

Clones the mirror (or upstream) into a local directory so the search/load
scripts have index.json and the skills/ tree to work against. HTTPS only.

Examples:
  python sync_library.py                       # clone default mirror into ./acs-library
  python sync_library.py --dest ~/acs          # custom destination
  python sync_library.py --repo https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
"""
import argparse, os, subprocess, sys

DEFAULT_REPO = "https://github.com/xlumamarathon-rog/DesignSkill.git"

def run(cmd, cwd=None):
    print("+", " ".join(cmd))
    subprocess.check_call(cmd, cwd=cwd)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=DEFAULT_REPO)
    ap.add_argument("--dest", default="acs-library")
    ap.add_argument("--depth", type=int, default=1)
    a = ap.parse_args()

    dest = os.path.expanduser(a.dest)
    if os.path.isdir(os.path.join(dest, ".git")):
        run(["git", "pull", "--ff-only"], cwd=dest)
    else:
        run(["git", "clone", "--depth", str(a.depth), a.repo, dest])
    idx = os.path.join(dest, "index.json")
    print(f"\nLibrary ready at {dest}")
    print(f"index.json present: {os.path.isfile(idx)}")
    print(f"Set ACS_ROOT={dest} for search_skills.py / load_skill.py")

if __name__ == "__main__":
    main()
