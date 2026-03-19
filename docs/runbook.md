# RUNBOOK

## 목적
VCHS 문서 하니스를 실제 실행 루프로 연결하기 위한 운영 절차.

## 기본 명령
- `bash scripts/harness.sh check`
- `bash scripts/harness.sh report`
- `bash scripts/harness.sh packet`
- `bash scripts/gate_runner.sh`

## 운영 순서
1. planner 단계에서 `docs/plan.md` 업데이트
2. 구현 후 `check`로 필수 구조 점검
3. `gate_runner`로 구조/문법/행동/리스크/의도/문서 게이트 실행
4. `report`로 최신 리포트 갱신
5. 외부 자료 사용 시 `packet` 템플릿으로 요약 주입

## CI 연동
- `.github/workflows/gates.yml`에서 PR/Push 시 `scripts/gate_runner.sh` 자동 실행
