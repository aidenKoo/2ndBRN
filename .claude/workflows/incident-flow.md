# WORKFLOW: INCIDENT

## 목적
고위험 이슈에서 피해 확산을 막고 안전하게 복구한다.

## 절차
1. governor 선호출
2. read-only 분석(초기)
3. root-cause packet 작성
4. 승인 후 최소 수정
5. validator(risk 우선) + archivist 기록

## 제한
- 승인 전 destructive operation 금지
