#!/usr/bin/env python3
"""Apply governance transitions with approval + rollback safety.

- Always writes proposal report.
- Applies only when .governance/approve.txt contains APPROVED.
- Creates backup skills/_registry.backup.yaml before apply.
"""
from __future__ import annotations

import pathlib
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
REG = ROOT / "skills" / "_registry.yaml"
BACKUP = ROOT / "skills" / "_registry.backup.yaml"
APPROVAL = ROOT / ".governance" / "approve.txt"
REPORT = ROOT / "reports" / "governance-proposal.md"
AUDIT = ROOT / "logs" / "governance-actions.jsonl"


def parse_registry(text: str):
    rows = []
    cur = None
    for raw in text.splitlines():
        s = raw.strip()
        if s.startswith("- id:"):
            if cur:
                rows.append(cur)
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
            t = s[1:].strip()
            if t:
                cur["failure_tags"].append(t)
    if cur:
        rows.append(cur)
    return rows


def proposal(rows):
    changes = []
    for r in rows:
        old = r.get("status", "verify")
        new = old
        sr = float(r.get("success_rate", 0.0))
        tags = r.get("failure_tags", [])
        if sr >= 0.8 and len(tags) == 0:
            new = "trusted"
        elif sr < 0.4 or len(tags) >= 2:
            new = "restricted"
        elif sr < 0.6:
            new = "verify"

        if new != old:
            changes.append((r["id"], old, new))
            r["status"] = new
    return changes


def dump(rows):
    out = ["version: 1", f"updated_at: {datetime.now(timezone.utc).date()}", "skills:"]
    for r in rows:
        out.append(f"  - id: {r['id']}")
        out.append(f"    status: {r['status']}")
        out.append(f"    confidence: {float(r.get('confidence', 0.5)):.2f}")
        out.append(f"    usage_count: {int(r.get('usage_count', 0))}")
        out.append(f"    success_rate: {float(r.get('success_rate', 0.0)):.2f}")
        tags = r.get("failure_tags", [])
        if tags:
            out.append("    failure_tags:")
            for t in tags:
                out.append(f"      - {t}")
        else:
            out.append("    failure_tags: []")
    return "\n".join(out) + "\n"


def main() -> int:
    if not REG.exists():
        print("missing registry")
        return 1

    rows = parse_registry(REG.read_text(encoding="utf-8"))
    changes = proposal(rows)

    lines = ["# GOVERNANCE PROPOSAL", "", f"- proposed_changes: {len(changes)}", "", "## Changes"]
    if changes:
        for sid, old, new in changes:
            lines.append(f"- {sid}: {old} -> {new}")
    else:
        lines.append("- none")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    approved = APPROVAL.exists() and APPROVAL.read_text(encoding="utf-8").strip() == "APPROVED"
    if not approved:
        print("governance_autopilot: proposal only (approval missing)")
        return 0

    BACKUP.write_text(REG.read_text(encoding="utf-8"), encoding="utf-8")
    REG.write_text(dump(rows), encoding="utf-8")

    stamp = datetime.now(timezone.utc).isoformat()
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT.open("a", encoding="utf-8") as f:
        f.write(f'{{"ts":"{stamp}","applied":{len(changes)},"backup":"{BACKUP.name}"}}\n')

    print(f"governance_autopilot: applied {len(changes)} changes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
