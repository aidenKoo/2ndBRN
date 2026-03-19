# PLAN

## Phase 1 — Foundation (완료)
- 문서 구조/역할/게이트/스킬 골격 구축

## Phase 2 — Operationalization (진행 중)
- [x] CLI 명령 기본 골격 추가 (`scripts/harness.sh`)
- [x] Context Packet 템플릿 추가 (`templates/context-packet.md`)
- [x] Gate Runner 추가 (`scripts/gate_runner.sh`)
- [x] CI Gate Workflow 추가 (`.github/workflows/gates.yml`)
- [x] 내장 Markdown 품질 검사 추가 (`scripts/markdown_guard.py`)
- [ ] syntax/behavioral/risk 게이트를 프로젝트별 실제 도구로 확장

## Phase 3 — Evolution (진행 중)
- [x] 스킬 메타데이터 스키마 정의 (`docs/skill-metadata-schema.md`)
- [x] 실패 태깅 규칙 정의 (`docs/failure-tagging-rules.md`)
- [x] 스킬 레지스트리 초안 추가 (`skills/_registry.yaml`)
- [ ] 자동 승급/강등 정책 적용 스크립트 구현
- [ ] failure-patterns 기반 self-healing 루프 자동화
