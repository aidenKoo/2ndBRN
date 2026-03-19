#!/usr/bin/env python3
"""Reinject top failure tags into docs/failure-patterns.md automatically."""
from __future__ import annotations

import json
import pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
EVENTS = ROOT / "logs" / "skill-events.jsonl"
FAIL_DOC = ROOT / "docs" / "failure-patterns.md"


def top_tags() -> list[tuple[str, int]]:
    c = Counter()
    if not EVENTS.exists():
        return []
    for line in EVENTS.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        ev = json.loads(line)
        tag = ev.get("failure_tag")
        if tag:
            c[tag] += 1
    return c.most_common(3)


def main() -> int:
    tags = top_tags()
    if not FAIL_DOC.exists():
        return 1

    base = FAIL_DOC.read_text(encoding="utf-8")
    marker = "\n## AUTO-REINJECTED TAGS\n"
    body = [marker]
    if tags:
        for tag, n in tags:
            body.append(f"- {tag}: {n} (from logs/skill-events.jsonl)")
    else:
        body.append("- none")

    # replace existing auto section
    if marker in base:
        base = base.split(marker)[0].rstrip() + "\n"
    out = base + "\n" + "\n".join(body) + "\n"
    FAIL_DOC.write_text(out, encoding="utf-8")
    print("reinject_failures: updated docs/failure-patterns.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
