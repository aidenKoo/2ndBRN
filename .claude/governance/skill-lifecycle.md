# GOVERNANCE: SKILL LIFECYCLE

## 상태
- draft: 초안
- verify: 검증 필요
- trusted: 반복 성공
- restricted: 조건부 사용
- deprecated: 사용 중지

## 전이 규칙(권장)
- 최근 10회 8회 이상 PASS + 회귀 없음 -> trusted
- 최근 5회 3회 이상 FAIL -> verify 강등
- 동일 실패 패턴 2회 반복 -> restricted
