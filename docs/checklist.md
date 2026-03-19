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
- [x] 프로젝트 도구 게이트 브릿지 추가 (`scripts/project_tool_gates.py`)
- [x] type 게이트 기본 검증 추가 (`scripts/registry_typecheck.py`)
- [x] 프로젝트 스택 자동 감지 기반 커맨드 확장

## Evolution
- [x] Skill 메타데이터 필드 정의
- [x] 실패 패턴 태깅 규칙 정의
- [x] 스킬 레지스트리 초안 추가
- [x] 이벤트 기반 스킬 전이 스크립트 추가
- [x] self-heal 리포트 자동 생성 추가
- [x] failure-patterns 자동 재주입 초안 추가
- [x] 거버넌스 전이 제안/승인/백업/감사 자동화 초안
- [ ] 도메인별 승인 정책 세분화
