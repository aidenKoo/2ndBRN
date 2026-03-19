# WORKFLOW: BUGFIX

## 목적
재현 가능한 버그를 원인 기반으로 수정하고 재발을 차단한다.

## 절차
1. planner: 증상/범위 정의
2. debug skill: 재현 절차·가설 정리
3. builder: 수정 + 회귀 테스트 추가
4. validator: 게이트 + 재현 케이스 재검증
5. archivist: failure-patterns 업데이트

## 완료 기준
- 원인/해결/재발방지 항목이 모두 기록됨
