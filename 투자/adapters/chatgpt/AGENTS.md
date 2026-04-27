# ChatGPT/Codex Adapter

## 역할
투자 분석 하네스 실행 어댑터.

## 실행 순서
1. `../../core/*.md` 정책을 먼저 적용한다.
2. `../../schemas/input_schema.md`로 입력을 정규화한다.
3. `../../theories/INVESTMENT_THEORIES.md`를 참조해 이론 축(팩터/밸류/리스크)을 반영한다.
4. 요청 유형에 맞는 `../../playbooks/*.md`를 선택한다.
5. 최종 답변 전 `../../skills/verifier/SKILL.md`와 `../../evals/theory_checklist.md`를 반영한다.
6. 결과는 `../../schemas/final_answer_schema.md` 형식으로 출력한다.

## 출력 규칙
- 시나리오 기반으로 답변한다.
- 반대 논리와 무효화 조건을 반드시 포함한다.
- 이론 커버리지 점수(High/Medium/Low)를 함께 제시한다.
