#!/usr/bin/env python3
"""Minimal markdown quality checks without external dependencies."""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

SKIP_DIRS = {".git", ".github"}


def iter_markdown_files() -> list[pathlib.Path]:
    files = []
    for p in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        files.append(p)
    return files


def check_file(path: pathlib.Path) -> list[str]:
    errs: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # rule 1: no trailing whitespace
    for idx, line in enumerate(lines, 1):
        if line.endswith(" ") or line.endswith("\t"):
            errs.append(f"{path}:{idx}: trailing whitespace")

    # rule 2: first non-empty line must be h1
    for line in lines:
        if not line.strip():
            continue
        if not line.startswith("# "):
            errs.append(f"{path}:1: first non-empty line should be H1")
        break

    # rule 3: avoid TODO placeholders in reports (except checklist/plan)
    if "reports" in path.parts and re.search(r"\bTODO\b", text):
        errs.append(f"{path}: report contains TODO")

    return errs


def main() -> int:
    errors: list[str] = []
    for md in iter_markdown_files():
        errors.extend(check_file(md))

    if errors:
        print("markdown_guard: FAIL")
        for e in errors:
            print(e)
        return 1

    print("markdown_guard: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
