# FAILURE PATTERNS

## FP-001 요구 누락형 PASS
- 증상: 테스트는 통과했지만 사용자 의도 일부 미충족
- 원인: Intent Gate 질문 불충분
- 조치: Intent Gate에 누락/확장 체크 항목 추가

## FP-002 회귀형 버그 재발
- 증상: 유사 버그 반복
- 원인: 회귀 테스트 미추가
- 조치: bugfix-flow에서 regression test를 완료조건으로 강제


## AUTO-REINJECTED TAGS

- test-missing: 1 (from logs/skill-events.jsonl)
