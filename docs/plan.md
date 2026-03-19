# PLAN

## Phase 1 — Foundation (완료)
- 문서 구조/역할/게이트/스킬 골격 구축

## Phase 2 — Operationalization (진행 중)
- [x] CLI 명령 기본 골격 추가 (`scripts/harness.sh`)
- [x] Context Packet 템플릿 추가 (`templates/context-packet.md`)
- [x] Gate Runner 추가 (`scripts/gate_runner.sh`)
- [x] CI Gate Workflow 추가 (`.github/workflows/gates.yml`)
- [x] 내장 Markdown 품질 검사 추가 (`scripts/markdown_guard.py`)
- [x] 프로젝트 도구 게이트 브릿지 추가 (`scripts/project_tool_gates.py`, `config/tool-gates.json`)
- [x] type 게이트 기본 검증 추가 (`scripts/registry_typecheck.py`)
- [x] 프로젝트 스택 자동 감지 기반 도구 커맨드 확장 (`scripts/project_tool_gates.py`)

## Phase 3 — Evolution (진행 중)
- [x] 스킬 메타데이터 스키마 정의 (`docs/skill-metadata-schema.md`)
- [x] 실패 태깅 규칙 정의 (`docs/failure-tagging-rules.md`)
- [x] 스킬 레지스트리 초안 추가 (`skills/_registry.yaml`)
- [x] 이벤트 기반 승급/강등 스크립트 초안 추가 (`scripts/evolve_skills.py`)
- [x] self-heal 리포트 자동 생성 초안 추가 (`scripts/self_heal.py`)
- [x] failure-patterns 자동 재주입 초안 추가 (`scripts/reinject_failures.py`)
- [x] 거버넌스 전이 제안/승인/백업/감사 자동화 초안 (`scripts/governance_autopilot.py`)
- [ ] 도메인별 승인 정책(인간 승인자, SLA, 롤백 임계값) 세분화
