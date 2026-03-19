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
- [ ] 각 프로젝트별 실제 도구 세부 커맨드 최적화

## Phase 3 — Evolution (진행 중)
- [x] 스킬 메타데이터 스키마 정의 (`docs/skill-metadata-schema.md`)
- [x] 실패 태깅 규칙 정의 (`docs/failure-tagging-rules.md`)
- [x] 스킬 레지스트리 초안 추가 (`skills/_registry.yaml`)
- [x] 이벤트 기반 승급/강등 스크립트 초안 추가 (`scripts/evolve_skills.py`)
- [x] self-heal 리포트 자동 생성 초안 추가 (`scripts/self_heal.py`)
- [x] failure-patterns 자동 재주입 초안 추가 (`scripts/reinject_failures.py`)
- [ ] 거버넌스 자동 전이 규칙의 완전 자동화(승인/롤백 정책 포함)
