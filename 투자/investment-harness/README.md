# Investment Harness

하네스 엔지니어링 관점으로 투자 아이디어를 검증하고, 가상투자 결과와 지식 아카이브를 통해 룰을 지속적으로 개선하는 프로젝트이다.

## 핵심 구조

```txt
Knowledge Archive + Virtual Portfolio + Rule Engine + Agent Layer + Decision Center
```

## 현재 정책
- 실제 투자 실행 없음
- 가상투자 전용
- 모든 전략·룰·결정은 기록 및 형상관리

## 최우선 사용 흐름
1. `strategies/draft/`에 전략 초안 생성
2. `rules/active/` 기준으로 검증
3. `decision_center/`에 사용자 승인 요청 생성
4. 승인된 전략만 `virtual_portfolio/`에서 가상운용
5. 결과는 `workspaces/meta_analyst/`와 `rules/proposals/`로 피드백

## 사용자 역할
사용자는 Investment Harness Owner로서 승인/보류/반려/수정 지시만 수행한다.
