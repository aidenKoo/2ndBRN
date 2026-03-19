#!/usr/bin/env python3
"""Update skills/_registry.yaml from usage events.

Event format (JSONL):
  {"skill_id":"common/write-spec","ok":true,"failure_tag":null}
"""
from __future__ import annotations

import json
import pathlib
from dataclasses import dataclass, field

ROOT = pathlib.Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "skills" / "_registry.yaml"
EVENTS = ROOT / "logs" / "skill-events.jsonl"


@dataclass
class SkillRow:
    skill_id: str
    status: str
    confidence: float
    usage_count: int
    success_rate: float
    failure_tags: list[str] = field(default_factory=list)


def parse_registry(text: str) -> tuple[str, list[SkillRow]]:
    lines = text.splitlines()
    updated_at = "1970-01-01"
    skills: list[SkillRow] = []
    cur: dict[str, object] | None = None

    for line in lines:
        s = line.strip()
        if s.startswith("updated_at:"):
            updated_at = s.split(":", 1)[1].strip()
        elif s.startswith("- id:"):
            if cur:
                skills.append(
                    SkillRow(
                        skill_id=str(cur.get("id", "")),
                        status=str(cur.get("status", "verify")),
                        confidence=float(cur.get("confidence", 0.5)),
                        usage_count=int(cur.get("usage_count", 0)),
                        success_rate=float(cur.get("success_rate", 0.0)),
                        failure_tags=list(cur.get("failure_tags", [])),
                    )
                )
            cur = {"id": s.split(":", 1)[1].strip(), "failure_tags": []}
        elif cur is not None and s.startswith("status:"):
            cur["status"] = s.split(":", 1)[1].strip()
        elif cur is not None and s.startswith("confidence:"):
            cur["confidence"] = float(s.split(":", 1)[1].strip())
        elif cur is not None and s.startswith("usage_count:"):
            cur["usage_count"] = int(s.split(":", 1)[1].strip())
        elif cur is not None and s.startswith("success_rate:"):
            cur["success_rate"] = float(s.split(":", 1)[1].strip())
        elif cur is not None and s.startswith("failure_tags:"):
            if s.endswith("[]"):
                cur["failure_tags"] = []
        elif cur is not None and s.startswith("-") and "id:" not in s:
            tag = s[1:].strip()
            if tag:
                cur.setdefault("failure_tags", []).append(tag)

    if cur:
        skills.append(
            SkillRow(
                skill_id=str(cur.get("id", "")),
                status=str(cur.get("status", "verify")),
                confidence=float(cur.get("confidence", 0.5)),
                usage_count=int(cur.get("usage_count", 0)),
                success_rate=float(cur.get("success_rate", 0.0)),
                failure_tags=list(cur.get("failure_tags", [])),
            )
        )

    return updated_at, skills


def load_events() -> list[dict]:
    if not EVENTS.exists():
        return []
    rows = []
    for line in EVENTS.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rows.append(json.loads(line))
    return rows


def apply_events(skills: list[SkillRow], events: list[dict]) -> list[SkillRow]:
    by_id = {s.skill_id: s for s in skills}
    event_window = {s.skill_id: [] for s in skills}

    for ev in events:
        sid = ev.get("skill_id")
        if sid not in by_id:
            continue
        sk = by_id[sid]
        ok = bool(ev.get("ok", False))
        sk.usage_count += 1

        # moving average on full history
        prev_successes = round(sk.success_rate * max(sk.usage_count - 1, 0))
        successes = prev_successes + (1 if ok else 0)
        sk.success_rate = successes / max(sk.usage_count, 1)

        tag = ev.get("failure_tag")
        if tag and tag not in sk.failure_tags:
            sk.failure_tags.append(str(tag))

        event_window[sid].append(ok)
        if len(event_window[sid]) > 10:
            event_window[sid] = event_window[sid][-10:]

    # transitions
    for sid, sk in by_id.items():
        wins = event_window[sid]
        if not wins:
            continue
        last10 = wins[-10:]
        last5 = wins[-5:]
        pass10 = sum(1 for x in last10 if x)
        fail5 = sum(1 for x in last5 if not x)

        if len(last10) >= 10 and pass10 >= 8:
            sk.status = "trusted"
            sk.confidence = min(0.95, sk.confidence + 0.05)
        elif len(last5) >= 5 and fail5 >= 3:
            sk.status = "verify"
            sk.confidence = max(0.40, sk.confidence - 0.05)

    return list(by_id.values())


def dump_registry(updated_at: str, skills: list[SkillRow]) -> str:
    out = []
    out.append("version: 1")
    out.append(f"updated_at: {updated_at}")
    out.append("skills:")
    for s in skills:
        out.append(f"  - id: {s.skill_id}")
        out.append(f"    status: {s.status}")
        out.append(f"    confidence: {s.confidence:.2f}")
        out.append(f"    usage_count: {s.usage_count}")
        out.append(f"    success_rate: {s.success_rate:.2f}")
        if s.failure_tags:
            out.append("    failure_tags:")
            for t in s.failure_tags:
                out.append(f"      - {t}")
        else:
            out.append("    failure_tags: []")
    return "\n".join(out) + "\n"


def main() -> int:
    if not REGISTRY.exists():
        print("registry missing")
        return 1

    text = REGISTRY.read_text(encoding="utf-8")
    _updated_at, skills = parse_registry(text)
    events = load_events()

    if not events:
        print("no events; registry unchanged")
        return 0

    updated_skills = apply_events(skills, events)
    new_text = dump_registry(updated_at="2026-03-19", skills=updated_skills)
    REGISTRY.write_text(new_text, encoding="utf-8")
    print(f"updated {len(updated_skills)} skills from {len(events)} events")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
