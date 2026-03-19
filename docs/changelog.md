# CHANGELOG

## 2026-03-19
- VCHS vNext 초기 문서 아키텍처 생성
- 역할/워크플로우/게이트/스킬/메모리 문서 추가
- 워크플로우·역할·게이트를 실행 지향 형식으로 상세화
- 거버넌스 전이 규칙과 Context Packet 스펙 강화
- 실행 지원 파일 추가: `scripts/harness.sh`, `templates/context-packet.md`, `docs/runbook.md`
- 호환성 보강: `roles/escalation.md`, `skills/common/write-spec.md`, `skills/common/write-test.md`, `skills/infra/deploy-safety.md`, `reports/latest-report.md`
- 게이트 자동화 추가: `scripts/gate_runner.sh`, `.github/workflows/gates.yml`
- 품질 검사 강화: `scripts/markdown_guard.py`로 의존성 없는 Markdown 검증 추가
- 진화 레이어 보강: `docs/skill-metadata-schema.md`, `docs/failure-tagging-rules.md`, `skills/_registry.yaml` 추가
- 이벤트 기반 스킬 진화 초안 추가: `logs/skill-events.jsonl`, `scripts/evolve_skills.py`, `harness evolve` 명령
- 운영/진화 자동화 확장: `scripts/self_heal.py`, `scripts/project_tool_gates.py`, `config/tool-gates.json`, `harness heal/tools` 명령
- 추가 자동화: `scripts/registry_typecheck.py`(type gate), `scripts/reinject_failures.py`(failure-patterns 자동 재주입)
- 거버넌스 자동화 확장: `scripts/governance_autopilot.py`, `harness govern`, 승인/백업/감사 로그 루프 추가
