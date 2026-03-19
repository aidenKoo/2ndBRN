# DECISION LOG

## 2026-03-19 — Router Slim + Distributed Rules
- 결정: CLAUDE.md를 라우터 전용으로 유지하고 세부 규칙은 하위 문서로 분리
- 이유: 지시 충돌 감소, 컨텍스트 오염 방지
- 대안: 단일 대형 매뉴얼(기각)

## 2026-03-19 — Gate-first Verification
- 결정: lint/test 나열이 아닌 다단 게이트(의도·리스크·문서 포함) 채택
- 이유: 기술적 통과와 요구 충족의 간극 축소
- 재검토 조건: 프로젝트 규모 증가로 게이트 병목이 발생할 때
