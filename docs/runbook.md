# RUNBOOK

## 목적
VCHS 문서 하니스를 실제 실행 루프로 연결하기 위한 운영 절차.

## 기본 명령
- `bash scripts/harness.sh check`
- `bash scripts/harness.sh report`
- `bash scripts/harness.sh packet`
- `bash scripts/harness.sh evolve`
- `bash scripts/harness.sh heal`
- `bash scripts/harness.sh tools`
- `bash scripts/harness.sh govern`
- `bash scripts/gate_runner.sh`

## 운영 순서
1. planner 단계에서 `docs/plan.md` 업데이트
2. 구현 후 `check`로 필수 구조 점검
3. `evolve`로 skill registry를 이벤트 로그 기준 갱신
4. `heal`로 self-heal report 생성 + failure-patterns 자동 재주입
5. `tools`로 프로젝트 lint/type/test/security 게이트 실행(자동 감지 포함)
6. `govern`으로 상태 전이 제안/적용(approval 파일 기반)
7. `gate_runner`로 구조/문법/행동/리스크/의도/문서 게이트 실행
8. `report`로 최신 리포트 갱신
9. 외부 자료 사용 시 `packet` 템플릿으로 요약 주입

## 거버넌스 승인/롤백
- 승인 파일: `.governance/approve.txt`에 `APPROVED` 입력 시 적용
- 적용 전 백업: `skills/_registry.backup.yaml`
- 제안 리포트: `reports/governance-proposal.md`
- 감사 로그: `logs/governance-actions.jsonl`
