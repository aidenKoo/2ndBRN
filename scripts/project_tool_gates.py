#!/usr/bin/env python3
"""Run project tool gates from config + auto-detected project stack commands."""
from __future__ import annotations

import json
import pathlib
import shutil
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
CFG = ROOT / "config" / "tool-gates.json"


def run_cmd(cmd: str) -> int:
    print(f"[RUN] {cmd}")
    return subprocess.call(cmd, cwd=ROOT, shell=True)


def load_cfg() -> dict[str, list[str]]:
    base = {"lint": [], "type": [], "test": [], "security": []}
    if CFG.exists():
        data = json.loads(CFG.read_text(encoding="utf-8"))
        for k in base:
            base[k] = list(data.get(k, []))
    return base


def detect_auto_cmds() -> dict[str, list[str]]:
    auto = {"lint": [], "type": [], "test": [], "security": []}

    if (ROOT / "pyproject.toml").exists():
        if shutil.which("ruff"):
            auto["lint"].append("ruff check .")
        if shutil.which("mypy"):
            auto["type"].append("mypy .")
        if shutil.which("pytest"):
            auto["test"].append("pytest -q")

    if (ROOT / "package.json").exists() and shutil.which("npm"):
        auto["lint"].append("npm run -s lint --if-present")
        auto["test"].append("npm run -s test --if-present")

    # generic security check if rg exists
    if shutil.which("rg"):
        auto["security"].append("rg -n \"(SECRET|PASSWORD|API_KEY)=\" . || true")

    return auto


def dedup(items: list[str]) -> list[str]:
    seen = set()
    out = []
    for i in items:
        if i in seen:
            continue
        seen.add(i)
        out.append(i)
    return out


def main() -> int:
    cfg = load_cfg()
    auto = detect_auto_cmds()
    fail = 0

    for gate in ["lint", "type", "test", "security"]:
        cmds = dedup(cfg.get(gate, []) + auto.get(gate, []))
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
