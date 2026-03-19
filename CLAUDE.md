# CLAUDE.md — Master Orchestrator

목적: 현재 작업에 맞는 워크플로우·역할·스킬·메모리·검증 게이트를 라우팅한다.

## 절대 규칙
- 직접 구현 세부를 여기 적지 않는다(라우팅 전용).
- 항상 `docs/context.md`를 먼저 읽는다.
- Validator 없는 완료는 금지한다.
- 기록 없는 변경은 완료로 간주하지 않는다.
- 동일 실패 3회 또는 high-risk는 Governor로 escalate한다.

## 작업 분류
- feature: 신규 기능/요건 구현
- bugfix: 결함 수정/원인 재현
- refactor: 동작 보존 구조 개선
- research: 조사/비교/의사결정
- incident: 장애/보안/데이터 위험

## 실행 순서
1. 작업 유형 분류
2. 위험도 분류(low/medium/high)
3. workflow 선택
4. role 선택
5. skill 선택
6. memory packet 구성
7. execution
8. gates 실행
9. learning 기록

## 메모리 로딩
- 항상: `docs/context.md`
- 조건부: `docs/plan.md`, `docs/checklist.md`, `docs/decision-log.md`, `docs/failure-patterns.md`, `docs/open-risks.md`
- 외부 메모리: 검색 → 요약(Context Packet) → 주입

## 필수 게이트
- structural-gate
- syntax-gate
- behavioral-gate
- risk-gate
- intent-gate
- regression-gate
- documentation-gate

## 종료 조건
- 필수 게이트 통과
- changelog/context/checklist 반영
- open risk 해소 또는 허용 사유 기록
