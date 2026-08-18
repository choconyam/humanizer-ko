#!/usr/bin/env python3
"""Check the Korean localization and its upstream provenance."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")
NOTICE = (ROOT / "NOTICE.md").read_text(encoding="utf-8")
GUIDE_NAMES = ("korean-editing.md", "domain-terminology.md")
TRACKED_VERSION = (ROOT / ".upstream-version").read_text(encoding="utf-8").strip()


def fail(message: str) -> None:
    raise SystemExit(message)


if not re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+", TRACKED_VERSION):
    fail(".upstream-version must contain one stable upstream tag such as v2.11.1")

tag_check = subprocess.run(
    ["git", "cat-file", "-e", f"{TRACKED_VERSION}^{{commit}}"],
    cwd=ROOT,
    capture_output=True,
    text=True,
    check=False,
)
if tag_check.returncode:
    fail(f"Fetch the tracked upstream tag before validating: {TRACKED_VERSION}")

guide_texts: list[str] = []
for guide_name in GUIDE_NAMES:
    guide = ROOT / "references" / guide_name
    plugin_guide = ROOT / "skills" / "humanizer" / "references" / guide_name
    if not guide.is_file() or not plugin_guide.is_file():
        fail(f"Add {guide_name} to the root skill and plugin package")

    guide_text = guide.read_text(encoding="utf-8")
    if guide_text != plugin_guide.read_text(encoding="utf-8"):
        fail(f"Keep both copies of {guide_name} byte-for-byte identical")

    if not re.search(r"[가-힣]", guide_text):
        fail(f"{guide_name} must contain real Korean examples")

    if f"](references/{guide_name})" not in SKILL:
        fail(f"Link {guide_name} from SKILL.md")

    guide_texts.append(guide_text)

if "blader/humanizer" not in NOTICE or "Copyright (c) 2025 Siqi Chen" not in NOTICE:
    fail("NOTICE.md must preserve the upstream project and copyright attribution")

if ".upstream-version" not in README:
    fail("README.md must identify .upstream-version as the source of truth")

license_at_tag = subprocess.run(
    ["git", "show", f"{TRACKED_VERSION}:LICENSE"],
    cwd=ROOT,
    capture_output=True,
    text=True,
    check=False,
)
if license_at_tag.returncode:
    fail(f"Could not read LICENSE from {TRACKED_VERSION}")

current_license = (ROOT / "LICENSE").read_text(encoding="utf-8").replace("\r\n", "\n")
if current_license != license_at_tag.stdout.replace("\r\n", "\n"):
    fail("Keep LICENSE identical to the tracked upstream release")

public_text = "\n".join((SKILL, README, NOTICE, *guide_texts))
if re.search(r"(?i)[a-z]:\\users\\", public_text):
    fail("Remove personal Windows paths before publishing")

print(f"Korean localization based on {TRACKED_VERSION} is valid")
