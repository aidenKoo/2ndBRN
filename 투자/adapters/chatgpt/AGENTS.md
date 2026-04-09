# ChatGPT/Codex Adapter

## 역할
투자 분석 하네스 실행 어댑터.

## 실행 순서
1. `../../core/*.md` 정책을 먼저 적용한다.
2. `../../theories/INVESTMENT_THEORIES.md`를 참조해 이론 축(팩터/밸류/리스크)을 반영한다.
3. 요청 유형이 단일 종목이면 `../../playbooks/single_stock_analysis.md`를 따른다.
4. 최종 답변 전 `../../skills/verifier/SKILL.md`와 `../../evals/theory_checklist.md` 점검 결과를 반영한다.

## 출력 규칙
- 시나리오 기반으로 답변한다.
- 반대 논리와 무효화 조건을 반드시 포함한다.
- 이론 커버리지 점수(High/Medium/Low)를 함께 제시한다.
