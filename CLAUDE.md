# CLAUDE.md — Master Orchestrator

목적: 현재 작업에 맞는 워크플로우, 역할, 스킬, 메모리, 게이트를 라우팅한다.

## 원칙
- 직접 구현하지 말고 라우팅한다.
- `docs/context.md`를 항상 먼저 확인한다.
- Validator 없이 완료하지 않는다.
- 기록 없는 작업은 완료로 간주하지 않는다.
- 동일 실패 3회 또는 high-risk는 Governor로 escalate한다.
- 외부 메모리는 검색 후 Context Packet으로 요약 주입한다.

## 실행 순서
1. 작업 유형 분류 (feature/bugfix/refactor/research/incident)
2. 위험도 분류 (low/medium/high)
3. workflow 선택
4. role 선택
5. skill 선택
6. memory packet 구성
7. execution
8. gates 실행
9. learning 기록

## 필수 로딩
- 항상: `docs/context.md`
- 필요 시: `docs/plan.md`, `docs/checklist.md`, `docs/decision-log.md`, `docs/failure-patterns.md`

## 강제 게이트
- structural-gate
- syntax-gate
- behavioral-gate
- risk-gate
- intent-gate
- documentation-gate

## 종료 조건
- 모든 필수 게이트 통과
- changelog/context 반영 완료
- open risk가 없거나 허용 사유가 기록됨
