# Investment Harness Operating Manual

## 목적
투자 아이디어를 즉시 실행하지 않고, 문서화·검증·가상투자·피드백을 통해 투자 판단 품질을 개선하는 하네스이다.

## 현재 모드
- Paper Trading Only
- Real Money Action: Disabled

## 핵심 원칙
1. 투자 판단은 반드시 기록한다.
2. 모든 전략은 룰을 통과해야 한다.
3. 모든 가상매수는 반대논리와 pre-mortem을 포함한다.
4. 결과보다 판단 품질을 먼저 평가한다.
5. 룰은 버전 관리한다.
6. 이론은 검증 없이 active rule이 될 수 없다.
7. 사용자는 실무자가 아니라 의사결정자다.
8. 에이전트는 질문 전에 선택지와 추천안을 준비한다.
9. 실제 투자는 현재 비활성화한다.
10. 가상투자는 실험으로 취급한다.

## 기본 워크플로우
Idea → Thesis Draft → Signal Design → Backtest Plan → Scenario Test → Risk Review → User Decision → Paper Trading → Weekly Review → Meta Review → Rule Proposal → User Decision → Rule Version Update

## 사용자 응답 형식
- A
- B
- C
- D
- 승인
- 반려
- 보류
- 더 보수적으로
- 더 공격적으로
- 근거 추가

## 폴더 레이어
- agents: GPT/Claude/Codex 역할 및 핸드오프 규칙
- decision_center: 사용자 의사결정 큐와 로그
- rules: active/proposals/versions 기반 룰 엔진
- knowledge_archive: 도서·이론·논문·사례 저장소
- universe: 투자 후보군 관리
- data_quality: 데이터 신뢰도 검증
- market_regime: 시장 국면 판단
- thesis: 투자 논리 생명주기 관리
- strategies: 전략 YAML
- strategy_zoo: 전략 실험장
- virtual_portfolio: 가상투자 기록
- error_taxonomy: 실패 유형 분류
- overrides: 예외 판단 기록
- workspaces: 롤별 산출물
- src/tests: 자동화 코드와 테스트
