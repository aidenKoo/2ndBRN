# CHECKLIST

## Foundation
- [x] Master Router 작성
- [x] Role/Workflow/Gate 문서 작성
- [x] Skill/Memory/Report 기본 템플릿 작성

## Operationalization
- [x] CLI 진입점 문서화 (`docs/runbook.md`)
- [x] Harness 스크립트 추가 (`scripts/harness.sh`)
- [x] Context Packet 템플릿 추가
- [x] Gate Runner 추가 (`scripts/gate_runner.sh`)
- [x] CI 게이트 워크플로우 추가 (`.github/workflows/gates.yml`)
- [x] Markdown 품질 검사 추가 (`scripts/markdown_guard.py`)
- [ ] 프로젝트별 lint/type/test/security 도구 연동

## Evolution
- [x] Skill 메타데이터 필드 정의
- [x] 실패 패턴 태깅 규칙 정의
- [x] 스킬 레지스트리 초안 추가
- [ ] 거버넌스 자동 전이 규칙 검증/자동화
