# Investment Harness (모델 중립형)

이 디렉터리는 Claude/Gemini/ChatGPT에서 공통으로 참조 가능한 **투자 분석·검증 하네스 매뉴얼**을 저장한다.

## 목표
- 단일 예측 모델이 아니라 역할 분리형 분석 체계를 사용한다.
- 모든 결론에 반대 논리, 리스크, 무효화 조건을 포함한다.
- 사후평가가 가능한 형식으로 결과를 남긴다.
- 핵심 투자이론(MPT, 팩터, 밸류, 거시, 리스크관리)을 분석 루프에 강제한다.

## 시작 순서
1. `MANIFEST.yaml`에서 기본 원칙과 활성 스킬을 확인한다.
2. `core/` 정책 문서를 먼저 적용한다.
3. `theories/INVESTMENT_THEORIES.md`를 로드한다.
4. 요청 유형에 맞는 `playbooks/` 절차를 실행한다.
5. `schemas/input_schema.md`로 입력을 정규화한다.
6. 필요한 `skills/*/SKILL.md`를 호출한다.
7. `schemas/final_answer_schema.md` 형식으로 결과를 조립한다.
8. 최종 출력은 `skills/verifier/SKILL.md` 및 `evals/theory_checklist.md`로 검증한다.

## 확장 포인트
- 플레이북: `earnings_reaction`, `macro_event_response`, `portfolio_rebalance`
- 평가셋: `evals/test_cases/*`
- 사후평가: `templates/postmortem_template.md`
