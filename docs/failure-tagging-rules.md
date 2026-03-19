# FAILURE TAGGING RULES

## 목적
실패 로그를 일관된 태그로 분류해 스킬/규칙 개선에 재사용한다.

## 기본 태그
- `intent-miss`: 요구사항 불일치
- `context-missing`: 필요 컨텍스트 누락
- `test-missing`: 회귀/테스트 누락
- `risk-unsafe`: 위험 명령/보안 이슈
- `scope-drift`: 범위 확장으로 인한 실패

## 작성 규칙
- 실패 1건당 최소 1개, 최대 3개 태그
- 태그는 `docs/failure-patterns.md`와 `skills/_registry.yaml` 모두에 반영
