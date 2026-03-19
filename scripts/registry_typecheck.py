#!/usr/bin/env python3
"""Type-check-like validation for skill registry and gate config."""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
REG = ROOT / "skills" / "_registry.yaml"
CFG = ROOT / "config" / "tool-gates.json"

ID_RE = re.compile(r"^[a-z0-9-]+/[a-z0-9-]+$")
STATUS = {"draft", "verify", "trusted", "restricted", "deprecated"}


def parse_registry() -> list[dict]:
    if not REG.exists():
        raise SystemExit("missing skills/_registry.yaml")

    skills = []
    cur = None
    for raw in REG.read_text(encoding="utf-8").splitlines():
        s = raw.strip()
        if s.startswith("- id:"):
            if cur:
                skills.append(cur)
            cur = {"id": s.split(":", 1)[1].strip(), "failure_tags": []}
        elif cur is not None and s.startswith("status:"):
            cur["status"] = s.split(":", 1)[1].strip()
        elif cur is not None and s.startswith("confidence:"):
            cur["confidence"] = float(s.split(":", 1)[1].strip())
        elif cur is not None and s.startswith("usage_count:"):
            cur["usage_count"] = int(s.split(":", 1)[1].strip())
        elif cur is not None and s.startswith("success_rate:"):
            cur["success_rate"] = float(s.split(":", 1)[1].strip())
        elif cur is not None and s.startswith("-") and "id:" not in s:
            tag = s[1:].strip()
            if tag:
                cur["failure_tags"].append(tag)

    if cur:
        skills.append(cur)

    return skills


def main() -> int:
    skills = parse_registry()
    errs = []

    if not CFG.exists():
        errs.append("config/tool-gates.json missing")
    else:
        cfg = json.loads(CFG.read_text(encoding="utf-8"))
        for k in ["lint", "type", "test", "security"]:
            if k not in cfg:
                errs.append(f"tool-gates missing key: {k}")

    for s in skills:
        sid = s.get("id", "")
        if not ID_RE.match(sid):
            errs.append(f"invalid skill id: {sid}")
        if s.get("status") not in STATUS:
            errs.append(f"invalid status: {sid}:{s.get('status')}")
        conf = s.get("confidence", -1.0)
        if conf < 0 or conf > 1:
            errs.append(f"invalid confidence: {sid}:{conf}")
        sr = s.get("success_rate", -1.0)
        if sr < 0 or sr > 1:
            errs.append(f"invalid success_rate: {sid}:{sr}")

    if errs:
        print("registry_typecheck: FAIL")
        for e in errs:
            print(f"- {e}")
        return 1

    print("registry_typecheck: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
