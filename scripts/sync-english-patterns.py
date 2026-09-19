#!/usr/bin/env python3
"""Rebuild the English pattern reference from an upstream release.

Usage:
  python scripts/sync-english-patterns.py            # use .upstream-version
  python scripts/sync-english-patterns.py --tag v3.0.0
  python scripts/sync-english-patterns.py --check    # exit 1 if out of date

The upstream SKILL.md is an English skill with its own workflow. This fork
keeps its Korean workflow in SKILL.md, so only the pattern material is
copied: every level-2 section except the ones listed in DROPPED_SECTIONS.
A new upstream section is kept by default and shows up in the sync PR.

Write mode also records the tag in .upstream-version, copies the upstream
LICENSE, and updates the upstream badge in README.md.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TARGETS = (
    ROOT / "references" / "english-patterns.md",
    ROOT / "skills" / "humanizer-ko" / "references" / "english-patterns.md",
)

# Upstream sections about its own workflow, voice, output, and sources.
# SKILL.md in this fork covers these for both languages.
DROPPED_SECTIONS = {
    "how to work",
    "what to do",
    "match the writer's voice",
    "add personality only when it fits",
    "how to return the result",
    "rewrite process",
    "source",
}

HEADER = """# English pattern reference

Read this reference only when editing substantial English prose. It is extracted from upstream Humanizer {tag} by `scripts/sync-english-patterns.py`. Do not edit it by hand.

The patterns below apply to English sentences only. For Korean prose, apply the K1-K10 checkpoints in `SKILL.md`; do not carry English dash, quotation mark, capitalization, or hyphen rules into Korean sentences. Isolated English product names, code, identifiers, and established technical terms inside Korean text do not require this reference.

The constraints, workflow, and output contract in `SKILL.md` apply to English text too. Upstream's own workflow and output sections are left out.
"""

BADGE = re.compile(
    r"\[!\[upstream blader/humanizer [0-9.]+\]"
    r"\(https://img\.shields\.io/badge/upstream-blader%2Fhumanizer_[0-9.]+-lightgrey\)\]"
    r"\(https://github\.com/blader/humanizer/releases/tag/v[0-9.]+\)"
)


def git_show(tag: str, path: str) -> str:
    result = subprocess.run(
        ["git", "show", f"{tag}:{path}"],
        cwd=ROOT,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        raise SystemExit(f"Could not read {path} from {tag}; fetch upstream tags first")
    return result.stdout.decode("utf-8").replace("\r\n", "\n")


def extract(skill: str, tag: str) -> str:
    skill = re.sub(r"\A---\n.*?\n---\n", "", skill, count=1, flags=re.DOTALL)
    parts = re.split(r"(?m)^(?=## )", skill)
    kept = []
    for part in parts[1:]:
        heading = part.splitlines()[0][3:].strip().lower()
        if heading not in DROPPED_SECTIONS:
            kept.append(part.rstrip("\n"))
    if not kept:
        raise SystemExit(f"No pattern sections found in {tag}:SKILL.md")
    return HEADER.format(tag=tag) + "\n" + "\n\n".join(kept) + "\n"


def badge(tag: str) -> str:
    version = tag.removeprefix("v")
    return (
        f"[![upstream blader/humanizer {version}]"
        f"(https://img.shields.io/badge/upstream-blader%2Fhumanizer_{version}-lightgrey)]"
        f"(https://github.com/blader/humanizer/releases/tag/{tag})"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--tag", help="upstream release tag, such as v3.0.0")
    parser.add_argument("--check", action="store_true", help="only report drift")
    args = parser.parse_args()

    tag = args.tag or (ROOT / ".upstream-version").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+", tag):
        raise SystemExit(f"Use a stable upstream tag such as v3.0.0: {tag}")

    reference = extract(git_show(tag, "SKILL.md"), tag)

    if args.check:
        stale = [
            str(path.relative_to(ROOT))
            for path in TARGETS
            if not path.is_file() or path.read_text(encoding="utf-8") != reference
        ]
        if stale:
            print(f"Out of date with {tag}: {', '.join(stale)}")
            print("Run python scripts/sync-english-patterns.py")
            return 1
        print(f"English pattern reference matches {tag}")
        return 0

    # Prepare every file before writing any, so a failure leaves no partial sync.
    readme_path = ROOT / "README.md"
    readme, count = BADGE.subn(badge(tag), readme_path.read_text(encoding="utf-8"))
    if count != 1:
        raise SystemExit("README.md needs exactly one upstream badge")
    license_text = git_show(tag, "LICENSE")

    for path in TARGETS:
        path.write_bytes(reference.encode("utf-8"))
    (ROOT / ".upstream-version").write_bytes(f"{tag}\n".encode("utf-8"))
    (ROOT / "LICENSE").write_bytes(license_text.encode("utf-8"))
    readme_path.write_bytes(readme.encode("utf-8"))

    print(f"English pattern reference rebuilt from {tag}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
