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
- [ ] 프로젝트별 lint/type/test/security 도구 연동

## Evolution
- [ ] Skill 메타데이터 필드 정의
- [ ] 실패 패턴 자동 태깅 규칙 정의
- [ ] 거버넌스 자동 전이 규칙 검증
