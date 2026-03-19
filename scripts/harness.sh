#!/usr/bin/env bash
set -euo pipefail

CMD="${1:-check}"

required_files=(
  "CLAUDE.md"
  "docs/context.md"
  "docs/plan.md"
  "docs/checklist.md"
  "docs/changelog.md"
  ".claude/roles/validator.md"
  ".claude/gates/intent-gate.md"
  ".claude/gates/risk-gate.md"
)

check_docs() {
  local missing=0
  for f in "${required_files[@]}"; do
    if [[ ! -f "$f" ]]; then
      echo "[FAIL] missing: $f"
      missing=1
    else
      echo "[OK] $f"
    fi
  done
  return $missing
}

write_report() {
  local ts
  ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  cat > reports/latest-report.md <<REPORT
# LATEST REPORT

- generated_at: $ts
- check: documentation harness baseline
- next: run gate tools (lint/test/security) in CI pipeline
REPORT
  echo "[OK] reports/latest-report.md updated"
}

render_packet() {
  cp templates/context-packet.md reports/context-packet.latest.md
  echo "[OK] reports/context-packet.latest.md created from template"
}

case "$CMD" in
  check) check_docs ;;
  report) write_report ;;
  packet) render_packet ;;
  *)
    echo "Usage: $0 {check|report|packet}"
    exit 2
    ;;
esac
