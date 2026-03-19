#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

TODAY_UTC="$(date -u +%Y-%m-%d)"
FAIL=0

pass() { echo "[PASS] $1"; }
warn() { echo "[WARN] $1"; }
fail() { echo "[FAIL] $1"; FAIL=1; }

run_structural_gate() {
  echo "== structural-gate =="
  local required=(
    "CLAUDE.md"
    "SYSTEM-MANIFEST.md"
    "USER-GUIDE.md"
    "docs/context.md"
    "docs/plan.md"
    "docs/checklist.md"
    "docs/changelog.md"
    ".claude/roles/validator.md"
    ".claude/gates/intent-gate.md"
    ".claude/gates/risk-gate.md"
    "scripts/harness.sh"
    "templates/context-packet.md"
    "scripts/markdown_guard.py"
  )

  local missing=0
  for f in "${required[@]}"; do
    if [[ ! -f "$f" ]]; then
      fail "missing required file: $f"
      missing=1
    fi
  done

  if [[ $missing -eq 0 ]]; then
    pass "required structure exists"
  fi
}

run_syntax_gate() {
  echo "== syntax-gate =="

  local sh_files=(scripts/*.sh)
  if [[ ${#sh_files[@]} -gt 0 ]]; then
    bash -n scripts/*.sh && pass "bash -n scripts/*.sh"
  fi

  python3 scripts/markdown_guard.py && pass "python3 scripts/markdown_guard.py"

  if command -v shellcheck >/dev/null 2>&1; then
    shellcheck scripts/*.sh && pass "shellcheck scripts/*.sh"
  else
    warn "shellcheck not installed; optional"
  fi
}

run_behavioral_gate() {
  echo "== behavioral-gate =="
  bash scripts/harness.sh check >/dev/null
  bash scripts/harness.sh packet >/dev/null
  bash scripts/harness.sh report >/dev/null
  pass "harness check/packet/report"
}

run_risk_gate() {
  echo "== risk-gate =="
  if rg -n --glob "!scripts/gate_runner.sh" --glob "!docs/changelog.md" "rm -rf /|curl\s+.*\|\s*sh|chmod\s+777" scripts .claude docs >/dev/null; then
    fail "risky command pattern found"
  else
    pass "no risky command patterns"
  fi
}

run_intent_gate() {
  echo "== intent-gate =="
  if rg -n "Operationalization|Evolution" docs/plan.md docs/checklist.md >/dev/null; then
    pass "plan/checklist include next execution intent"
  else
    fail "plan/checklist missing execution intent markers"
  fi
}

run_documentation_gate() {
  echo "== documentation-gate =="
  if rg -n "## ${TODAY_UTC}" docs/changelog.md >/dev/null; then
    pass "changelog updated for today (${TODAY_UTC})"
  else
    warn "changelog has no section for today (${TODAY_UTC})"
  fi

  if [[ -f reports/latest-report.md ]]; then
    pass "latest report exists"
  else
    fail "reports/latest-report.md missing"
  fi
}

main() {
  run_structural_gate
  run_syntax_gate
  run_behavioral_gate
  run_risk_gate
  run_intent_gate
  run_documentation_gate

  if [[ $FAIL -ne 0 ]]; then
    echo "Gate runner failed"
    exit 1
  fi

  echo "All required gates passed"
}

main "$@"
