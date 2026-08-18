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
GUIDE = ROOT / "references" / "korean-editing.md"
PLUGIN_GUIDE = ROOT / "skills" / "humanizer" / "references" / "korean-editing.md"
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

if not GUIDE.is_file() or not PLUGIN_GUIDE.is_file():
    fail("Add the Korean editing guide to the root skill and plugin package")

guide_text = GUIDE.read_text(encoding="utf-8")
if guide_text != PLUGIN_GUIDE.read_text(encoding="utf-8"):
    fail("Keep both Korean editing guide copies byte-for-byte identical")

if not re.search(r"[가-힣]", guide_text):
    fail("The Korean editing guide must contain real Korean examples")

if "](references/korean-editing.md)" not in SKILL:
    fail("Link the Korean editing guide from SKILL.md")

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

public_text = "\n".join((SKILL, README, NOTICE, guide_text))
if re.search(r"(?i)[a-z]:\\users\\", public_text):
    fail("Remove personal Windows paths before publishing")

print(f"Korean localization based on {TRACKED_VERSION} is valid")
