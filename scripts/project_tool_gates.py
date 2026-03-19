#!/usr/bin/env python3
"""Run project tool gates from config/tool-gates.json.

This is a bridge for real repo commands (lint/type/test/security).
If commands are empty, it reports WARN and continues.
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CFG = ROOT / "config" / "tool-gates.json"


def run_cmd(cmd: str) -> int:
    print(f"[RUN] {cmd}")
    return subprocess.call(cmd, cwd=ROOT, shell=True)


def main() -> int:
    if not CFG.exists():
        print("[WARN] config/tool-gates.json missing")
        return 0

    cfg = json.loads(CFG.read_text(encoding="utf-8"))
    fail = 0

    for gate in ["lint", "type", "test", "security"]:
        cmds = cfg.get(gate, [])
        if not cmds:
            print(f"[WARN] {gate} gate command list is empty")
            continue

        print(f"== tool-gate:{gate} ==")
        for cmd in cmds:
            rc = run_cmd(cmd)
            if rc != 0:
                print(f"[FAIL] {gate}: {cmd} (exit={rc})")
                fail = 1
            else:
                print(f"[PASS] {gate}: {cmd}")

    return fail


if __name__ == "__main__":
    raise SystemExit(main())
