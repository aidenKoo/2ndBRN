# WORKFLOW: REFACTOR

## 목적
동작은 보존하고 유지보수성을 높인다.

## 절차
1. planner: 비기능 목표 정의(복잡도, 가독성, 결합도)
2. architect: 변경 단위/리스크 설계
3. builder: 작은 단위 리팩터링
4. validator: regression-heavy 검증
5. archivist: decision-log + changelog 반영

## 완료 기준
- 동작 동일성 + 회귀 테스트 통과
