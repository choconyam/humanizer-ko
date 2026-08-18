#!/usr/bin/env python3
"""Build the symlink-free archive used by Claude Desktop."""

from __future__ import annotations

import argparse
import stat
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parent.parent
SOURCES = {
    "humanizer-ko/SKILL.md": ROOT / "SKILL.md",
    "humanizer-ko/references/korean-editing.md": ROOT
    / "references"
    / "korean-editing.md",
    "humanizer-ko/references/domain-terminology.md": ROOT
    / "references"
    / "domain-terminology.md",
}


def build_archive(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)

    with ZipFile(output, "w") as archive:
        for archive_path, source in SOURCES.items():
            entry = ZipInfo(archive_path)
            entry.compress_type = ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(entry, source.read_bytes())

    with ZipFile(output) as archive:
        entries = archive.infolist()
        if [entry.filename for entry in entries] != list(SOURCES):
            raise SystemExit("Archive entries do not match the required skill files")

        for entry in entries:
            mode = entry.external_attr >> 16
            if not stat.S_ISREG(mode):
                raise SystemExit(f"{entry.filename} must be a regular file")
            if archive.read(entry.filename) != SOURCES[entry.filename].read_bytes():
                raise SystemExit(f"{entry.filename} does not match its source file")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Path for the generated ZIP file")
    args = parser.parse_args()

    build_archive(args.output)
    print(f"Built Claude Desktop package: {args.output}")


if __name__ == "__main__":
    main()
