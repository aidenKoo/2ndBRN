#!/usr/bin/env python3
"""Generate self-healing report from skill event/failure tags."""
from __future__ import annotations

import argparse
import json
import pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
EVENTS = ROOT / "logs" / "skill-events.jsonl"
REPORT = ROOT / "reports" / "self-heal-report.md"


def load_events() -> list[dict]:
    if not EVENTS.exists():
        return []
    out = []
    for line in EVENTS.read_text(encoding="utf-8").splitlines():
        if line.strip():
            out.append(json.loads(line))
    return out


def make_report(events: list[dict]) -> str:
    tag_counter = Counter()
    skill_counter = Counter()
    for ev in events:
        skill_counter[ev.get("skill_id", "unknown")] += 1
        tag = ev.get("failure_tag")
        if tag:
            tag_counter[tag] += 1

    lines = [
        "# SELF-HEAL REPORT",
        "",
        f"- total_events: {len(events)}",
        "",
        "## Top Failure Tags",
    ]
    if tag_counter:
        for tag, n in tag_counter.most_common(5):
            lines.append(f"- {tag}: {n}")
    else:
        lines.append("- none")

    lines += ["", "## Top Skills by Activity"]
    for sid, n in skill_counter.most_common(5):
        lines.append(f"- {sid}: {n}")

    lines += ["", "## Suggested Actions"]
    if tag_counter.get("test-missing", 0) > 0:
        lines.append("- bugfix-flow에 회귀 테스트 생성 단계를 강제 유지")
    if tag_counter.get("intent-miss", 0) > 0:
        lines.append("- intent-gate 질문 확장 및 acceptance criteria 강화")
    if not tag_counter:
        lines.append("- 이벤트 데이터가 부족하므로 로그 수집을 확대")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan-only", action="store_true")
    args = parser.parse_args()

    events = load_events()
    if args.scan_only:
        print(f"self_heal_scan: events={len(events)}")
        return 0

    report = make_report(events)
    REPORT.write_text(report, encoding="utf-8")
    print(f"wrote {REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
