# 투자전략하네스 기획서 ver0.1

## 문서 정보

- 문서명: 투자전략하네스_기획서ver0.1_20260425
- 작성일: 2026-04-25
- 상태: Draft / Planning Baseline
- 적용 범위: 투자 자동 가이드 머신 / investment-harness 초기 설계
- 현재 운용 모드: 가상투자 전용
- 실제 투자 실행: 비활성화
- 주요 저장 위치: `투자/investment-harness/`

---

# 0. Executive Summary

본 기획서는 하네스 엔지니어링의 관점에서 투자 분석, 투자 전략 검증, 가상투자 운영, 룰 형상관리, 지식 아카이빙, AI 에이전트 협업, 사용자 의사결정 자동화를 통합하기 위한 설계 문서이다.

핵심 아이디어는 다음과 같다.

```txt
투자 판단을 의견이 아니라 테스트 가능한 시스템으로 취급한다.
```

본 하네스는 사용자가 매번 모든 분석을 직접 수행하는 구조가 아니다. GPT, Claude, Codex 등 에이전트가 역할별로 분석·정리·검증·기록을 수행하고, 사용자는 정해진 의사결정 게이트에서 승인/보류/반려/수정 지시만 내리는 구조를 목표로 한다.

최종 지향점은 다음과 같다.

```txt
투자 아이디어
→ 투자 논리 작성
→ 신호화
→ 검증
→ 가상운용
→ 실패/성공 패턴 수집
→ 룰 업데이트
→ 버전 관리
→ 판단 품질 개선
```

즉, 본 프로젝트는 투자 추천기가 아니라 **투자 판단 품질을 개선하는 하네스**이다.

---

# 1. 기획 배경

## 1.1 문제의식

일반적인 투자 의사결정은 다음 문제를 가진다.

1. 투자 아이디어가 즉흥적으로 발생함.
2. 진입 당시의 근거가 명확히 기록되지 않음.
3. 반대 논리가 충분히 검토되지 않음.
4. 실패 이후 원인이 체계적으로 분류되지 않음.
5. 같은 판단 오류가 반복됨.
6. 좋은 결과와 좋은 판단을 혼동함.
7. 투자 이론을 공부하더라도 실제 룰로 연결되지 않음.
8. 시장 국면 변화에 따라 어떤 이론이 유효한지 판단하기 어려움.
9. AI에게 물어본 결과가 일회성 답변으로 흩어짐.
10. 전략, 룰, 가상투자, 피드백, 지식 아카이브가 분리되어 있음.

본 하네스는 이러한 문제를 해결하기 위해 투자 판단을 다음 구조로 정규화한다.

```txt
가설 → 정량 신호 → 검증 → 리스크 판단 → 가상투자 → 리뷰 → 룰 개선
```

## 1.2 하네스 엔지니어링 관점

소프트웨어 개발에서 하네스는 시스템을 직접 운영하기 전에 입력, 실행, 결과, 검증, 회귀 테스트를 관리하는 구조다. 이를 투자에 적용하면 다음과 같이 대응된다.

| 소프트웨어 하네스 | 투자 하네스 |
|---|---|
| 코드 | 투자 전략 |
| 테스트 케이스 | 시장 시나리오 |
| 런타임 | 실제 시장 환경 |
| 로그 | 매매/판단 기록 |
| 실패 테스트 | 손실/오류 사례 |
| 리그레션 테스트 | 과거 전략 대비 성과 비교 |
| CI/CD 승인 | 사용자 의사결정 게이트 |
| 버전 관리 | 룰/전략 형상관리 |

따라서 투자 전략은 감각적 판단이 아니라 **테스트 가능한 코드형 자산**으로 관리한다.

---

# 2. 핵심 철학

## 2.1 전략은 코드처럼 다룬다

```txt
전략 = 코드
시장 = 런타임
수익률 = 테스트 결과
손실 = 실패 로그
룰 변경 = 리팩터링
```

전략이 실행되기 전에는 반드시 다음 조건을 만족해야 한다.

1. 가설이 명확해야 한다.
2. 가설을 측정 가능한 신호로 변환해야 한다.
3. 반대 논리가 기록되어야 한다.
4. 시나리오 테스트가 가능해야 한다.
5. 리스크 룰을 통과해야 한다.
6. 가상투자로 검증되어야 한다.
7. 실패 시 오류 유형을 분류해야 한다.
8. 개선 룰은 버전 관리되어야 한다.

## 2.2 좋은 결과보다 좋은 프로세스를 우선한다

투자에서는 다음 네 가지 조합이 모두 가능하다.

```txt
좋은 판단 / 좋은 결과
좋은 판단 / 나쁜 결과
나쁜 판단 / 좋은 결과
나쁜 판단 / 나쁜 결과
```

본 하네스는 특히 `나쁜 판단 / 좋은 결과`를 경계한다. 이는 운으로 얻은 성공이며, 반복하면 장기적으로 시스템을 훼손할 가능성이 높다.

따라서 모든 가상투자 판단에는 다음 점수를 분리한다.

- Process Score
- Outcome Score

Process Score는 판단의 질을 평가하고, Outcome Score는 결과를 평가한다.

## 2.3 사용자는 실무자가 아니라 의사결정자다

사용자는 매번 자료를 수집하거나 직접 분석 기준을 만들지 않는다. 사용자는 Investment Harness Owner로서 다음 의사결정만 수행한다.

- 승인
- 반려
- 보류
- 수정 지시
- 더 보수적으로
- 더 공격적으로
- 근거 추가 요청
- 대안 비교 요청

에이전트는 반드시 다음 형식으로 질문해야 한다.

```txt
현재 추천은 B입니다.

A. 공격적으로 진행
B. 보수적으로 진행
C. 보류
D. 반려

선택해주세요.
```

## 2.4 질문을 줄이고 선택지를 명확히 한다

본 하네스의 운영 원칙은 다음과 같다.

```txt
질문은 줄이고,
선택지는 명확하게,
추천안은 반드시 제시하고,
결정은 기록한다.
```

에이전트가 사용자에게 해서는 안 되는 질문:

- “어떻게 할까요?”
- “어떤 기준을 쓸까요?”
- “이 종목 어떻게 볼까요?”
- “다음 단계는 뭘까요?”

대신 에이전트는 다음처럼 물어야 한다.

```txt
세 가지 설계안을 만들었습니다.
A. Quality Growth 중심
B. Momentum + Growth 중심
C. Valuation Guardrail 중심

추천은 A입니다.
이유는 신호화와 가상투자 검증이 가장 쉽기 때문입니다.
```

---

# 3. 전체 시스템 구조

본 하네스는 다음 레이어로 구성된다.

```txt
Investment Harness
├─ Knowledge Archive
├─ Agent Layer
├─ Decision Center
├─ Rule Engine
├─ Universe
├─ Data Quality
├─ Market Regime
├─ Thesis Lifecycle
├─ Strategy Lab
├─ Strategy Zoo
├─ Risk & Scenario Lab
├─ Virtual Portfolio
├─ Error Taxonomy
├─ Override Log
├─ Workspaces
├─ Reports
├─ Source Code
└─ Tests
```

| 레이어 | 목적 |
|---|---|
| Knowledge Archive | 투자 이론, 도서, 논문, 사례, 개념 저장 및 룰 후보 추출 |
| Agent Layer | GPT, Claude, Codex 등 역할 기반 에이전트 운용 |
| Decision Center | 사용자의 승인/보류/반려 의사결정 큐 관리 |
| Rule Engine | active/proposals/versions 기반 투자 룰 형상관리 |
| Universe | 투자 후보군 관리 |
| Data Quality | 데이터 결측, 이상치, 신뢰도 검증 |
| Market Regime | 금리, 유동성, 인플레이션, 경기 국면 판단 |
| Thesis Lifecycle | 투자 논리의 active/weakened/broken 상태 관리 |
| Strategy Lab | 전략 YAML, 신호 정의, 백테스트 설계 |
| Strategy Zoo | 여러 전략을 실험군으로 관리 |
| Risk & Scenario Lab | 금리, 침체, 유동성, 멀티플 축소 등 충격 검증 |
| Virtual Portfolio | 가상투자 현황, 매매 일지, 현금 장부 관리 |
| Error Taxonomy | 실패 유형 분류 및 룰 개선 연결 |
| Override Log | 예외 판단 기록 |
| Workspaces | 롤별 진행사항 및 피드백 산출물 |
| Reports | 주간/월간/전략/메타 리뷰 |
| Source Code | 자동화 코드 |
| Tests | 룰 및 코드 검증 테스트 |

---

# 4. 초기 폴더 구조

```txt
investment-harness/
├─ README.md
├─ HARNESS_OPERATING_MANUAL.md
├─ 투자전략하네스_기획서ver0.1_20260425.md
│
├─ agents/
│  ├─ agent_registry.yaml
│  ├─ agent_task_rules.yaml
│  ├─ agent_handoff_rules.yaml
│  ├─ agent_question_rules.yaml
│  ├─ agent_decision_gate_rules.yaml
│  └─ prompts/
│
├─ decision_center/
│  ├─ pending_decisions.md
│  ├─ decision_queue.yaml
│  ├─ decision_log.md
│  ├─ decision_templates.md
│  └─ escalation_rules.yaml
│
├─ rules/
│  ├─ active/
│  ├─ versions/
│  ├─ proposals/
│  └─ RULE_GOVERNANCE.md
│
├─ knowledge_archive/
├─ universe/
├─ data_quality/
├─ market_regime/
├─ thesis/
├─ strategies/
├─ strategy_zoo/
├─ virtual_portfolio/
├─ error_taxonomy/
├─ overrides/
├─ workspaces/
├─ reports/
├─ src/
└─ tests/
```

---

# 5. 롤 기반 운영 체계

본 하네스는 사람 조직이라기보다, 에이전트와 산출물 중심의 역할 체계이다.

## 5.1 핵심 롤 요약

| 롤 | 핵심 질문 | 주요 산출물 |
|---|---|---|
| Hypothesis Designer | 무엇을 베팅할 것인가? | thesis_draft.md, strategy_draft.yaml |
| Signal Engineer | 가설을 어떻게 수치화할 것인가? | signal_spec.md, factor_definition.yaml |
| Backtest Engineer | 과거에 작동했는가? | backtest_plan.md, bias_checklist.md |
| Portfolio Manager | 포트폴리오 전체 노출은 안전한가? | allocation_plan.md, exposure_report.md |
| Scenario Simulator | 특정 충격에서 살아남는가? | scenario_report.md |
| Risk Manager | 승인/보류/반려 중 무엇인가? | risk_review.md, approval_checklist.md |
| Paper Trading Operator | 가상운용 기록이 정확한가? | trade_journal.md, portfolio_status.md |
| Knowledge Curator | 지식을 룰 후보로 바꿀 수 있는가? | archive_summary.md, rule_candidate.md |
| Devil's Advocate | 이 전략이 틀릴 이유는 무엇인가? | bear_case_report.md, contradiction_log.md |
| Regime Analyst | 현재 국면에서 어떤 이론이 맞는가? | current_regime.md |
| Data Reliability Manager | 데이터는 믿을 만한가? | data_validation_report.md |
| Meta Analyst | 반복되는 오류는 무엇인가? | meta_review.md, rule_change_recommendation.md |

## 5.2 롤 간 핸드오프 원칙

각 롤은 다음 롤로 넘기기 전에 산출물을 남긴다.

```txt
Hypothesis Designer
→ Signal Engineer
→ Backtest Engineer
→ Scenario Simulator
→ Risk Manager
→ Paper Trading Operator
→ Meta Analyst
→ Rule Proposal
```

Knowledge Curator와 Devil's Advocate는 독립적으로 개입한다.

```txt
Knowledge Curator → Meta Analyst → Rule Proposal
Devil's Advocate → Risk Manager → Decision Center
```

---

# 6. 전략 파이프라인 설계

전략은 다음 상태를 가진다.

```txt
idea
→ draft
→ signal_designed
→ backtest_ready
→ backtested
→ scenario_checked
→ risk_reviewed
→ user_approved_for_paper
→ paper_running
→ paper_passed
→ retired
```

## 6.1 전략 입력 단계

전략 아이디어는 반드시 다음 항목을 포함해야 한다.

- 전략명
- 핵심 가설
- 대상 유니버스
- 왜 지금 검토하는지
- 기대 수익 원천
- 주요 리스크
- 반대 논리
- 검증 방법

예시:

```txt
전략명: Quality Growth v1
핵심 가설: 성장성과 수익성이 동시에 개선되는 기업은 장기적으로 시장 대비 우수한 성과를 낼 가능성이 높다.
대상: 미국 대형주
수익 원천: 매출 성장, 영업 레버리지, 질적 프리미엄 유지
리스크: 고밸류에이션, 금리 상승, 성장 둔화
```

## 6.2 전략 YAML 기준

전략은 YAML로 표현한다.

```yaml
strategy_id: quality_growth_v1
status: draft
description: 성장성과 수익성이 함께 개선되는 기업 선별 전략
universe:
  market: US
  min_market_cap: 10000000000
rebalance:
  frequency: monthly
signals:
  growth:
    revenue_growth_yoy:
      weight: 0.30
      direction: higher_is_better
  profitability:
    gross_margin:
      weight: 0.20
      direction: higher_is_better
    operating_margin:
      weight: 0.20
      direction: higher_is_better
  valuation:
    psr:
      weight: 0.20
      direction: lower_is_better
  risk:
    beta:
      weight: 0.10
      direction: lower_is_better
approval_rules:
  require_backtest: true
  require_scenario_test: true
  require_risk_check: true
```

## 6.3 전략 승격 조건

전략은 다음 조건을 만족해야 다음 단계로 이동한다.

| 이동 | 조건 |
|---|---|
| idea → draft | 사용자 G0 승인 |
| draft → signal_designed | thesis와 signal 후보 작성 |
| signal_designed → backtest_ready | 사용자 G2 승인 |
| backtest_ready → backtested | 백테스트 설계 및 편향 체크 완료 |
| backtested → scenario_checked | 사용자 G3 승인 |
| scenario_checked → risk_reviewed | 시나리오 테스트 결과 기록 |
| risk_reviewed → paper_running | 사용자 G4 승인 |
| paper_running → paper_passed | 최소 관찰기간 및 리뷰 통과 |
| paper_running → retired | 폐기 조건 충족 및 사용자 승인 |

---

# 7. 전략 유형별 초기 실험군

## 7.1 Quality Growth 전략

핵심 가설:

```txt
성장성과 수익성이 동시에 개선되는 기업은 단순 성장주보다 더 높은 생존성과 복리 성과를 가질 수 있다.
```

주요 신호:
- 매출 성장률
- 매출총이익률
- 영업이익률
- FCF margin
- PSR/PER/EV/EBITDA
- 베타
- 금리 민감도

반대 논리:
- 이미 높은 밸류에이션이 반영되어 있을 수 있음
- 금리 상승기에 멀티플 압축 가능
- 성장 둔화 시 고평가 리스크 급증

적용 룰:
- valuation guardrail
- rate sensitivity check
- margin durability check
- downside scenario pass

## 7.2 Defensive Quality 전략

핵심 가설:

```txt
재무 안정성과 수익성이 높고 변동성이 낮은 기업은 경기 둔화 국면에서 상대적으로 방어력이 높다.
```

주요 신호:
- 낮은 부채비율
- 높은 이자보상배율
- 안정적 FCF
- 낮은 주가 변동성
- 낮은 실적 변동성

활용 국면:
- recession risk
- high rate pressure
- liquidity tightening

## 7.3 Momentum Breakout 전략

핵심 가설:

```txt
가격 추세와 이익 추정치 상향이 동시에 발생하는 종목은 단기~중기 초과성과 가능성이 있다.
```

주요 신호:
- 3개월/6개월 상대수익률
- 신고가 돌파
- 거래량 증가
- EPS revision
- 매출 가이던스 상향

주의점:
- 추세 붕괴 시 빠른 손절/퇴출 룰 필요
- valuation guardrail이 약하면 버블 추격 위험 존재

## 7.4 Value Reversion 전략

핵심 가설:

```txt
내재가치 대비 과도하게 할인된 기업은 평균회귀 가능성이 있다.
```

주요 신호:
- 낮은 PER/PBR/EV/EBITDA
- 높은 FCF yield
- 개선되는 마진
- 부정적 뉴스 피크아웃

주의점:
- value trap 방지 필요
- thesis broken과 price undervaluation을 구분해야 함

## 7.5 AI Infrastructure Theme 전략

핵심 가설:

```txt
AI 인프라 확산은 반도체, 클라우드, 전력, 네트워크, 데이터센터 관련 기업의 구조적 수요를 만들 수 있다.
```

주요 세부 테마:
- GPU/반도체
- 클라우드 인프라
- 데이터센터 전력
- 네트워크 장비
- 냉각/전력 효율
- AI 소프트웨어 플랫폼

반대 논리:
- 과잉투자 가능성
- 수익화 지연
- 공급망 병목
- capex 부담
- 특정 기업 쏠림

필수 룰:
- theme concentration cap
- valuation guardrail
- capex efficiency check
- revenue durability check

---

# 8. 포트폴리오 매니저 룰

포트폴리오 매니저는 좋은 종목을 많이 담는 역할이 아니라, 전체 포트폴리오가 한 방향으로 과도하게 쏠리지 않도록 관리하는 역할이다.

## 8.1 주요 제약

```yaml
constraints:
  max_single_asset_weight: 0.10
  max_sector_weight: 0.35
  max_theme_weight: 0.45
  max_portfolio_beta: 1.20
  max_interest_rate_sensitivity: 1.30
```

## 8.2 현금 비중 관리

현금은 실패가 아니라 선택지 보유로 본다.

현금 비중 확대 조건:
- 시나리오 실패 2회 이상
- 시장 국면 불확실
- data quality failure
- 전략 간 상관관계 급증
- 가상 포트폴리오 MDD 경고

## 8.3 포지션 사이징

포지션 크기는 확신도 기반으로 결정한다.

| Confidence Score | 허용 상태 |
|---:|---|
| 20~25 | 최대 비중 허용 |
| 15~19 | 정상 비중 |
| 10~14 | 절반 비중 또는 watch |
| 10 미만 | watch only |

---

# 9. 시나리오 시뮬레이터 설계

전략은 기본 시나리오에서만 좋아 보여서는 안 된다. 본 하네스는 다음 충격을 기본 검증 세트로 둔다.

## 9.1 기본 시나리오

| 시나리오 | 설명 | 주요 충격 |
|---|---|---|
| rate_up | 금리 상승 | 성장주 멀티플 압축 |
| rate_down | 금리 하락 | 성장주 멀티플 확장 가능 |
| recession | 경기침체 | 매출 성장률, 마진 하락 |
| inflation_reacceleration | 인플레 재가속 | 비용 상승, 멀티플 하락 |
| liquidity_tightening | 유동성 축소 | 고밸류 자산 압박 |
| multiple_compression | 밸류에이션 정상화 | PSR/PER 하락 |

## 9.2 통과 기준

```yaml
pass_rules:
  max_loss_under_single_scenario: -0.20
  max_loss_under_any_two_scenarios: -0.30
  minimum_survival_score: 65
```

## 9.3 시나리오 실패 시 조치

| 실패 유형 | 조치 |
|---|---|
| 단일 시나리오 경미 실패 | position size 축소 |
| 복수 시나리오 실패 | 가상편입 보류 |
| rate_up 실패 | 금리 민감도 룰 강화 |
| recession 실패 | defensive quality 필터 추가 |
| multiple compression 실패 | valuation guardrail 강화 |

---

# 10. 가상투자 운영 설계

## 10.1 현재 원칙

```yaml
paper_trading:
  mode: virtual_only
  real_money_allowed: false
```

가상투자는 실제 투자 전 단계가 아니라 실험 환경이다.

## 10.2 가상투자 문서

```txt
virtual_portfolio/current/
├─ portfolio_status.md
├─ holdings.yaml
├─ cash_ledger.md
├─ trade_journal.md
├─ decision_log.md
└─ watchlist.md
```

## 10.3 trade_journal 필수 항목

- Trade ID
- 날짜
- 구분
- 종목
- 전략 ID
- 실행 가격
- 목표 비중
- 실행 사유
- 반대 근거 3개
- Pre-mortem
- Kill Criteria
- Process Score
- Outcome Score
- 사후 평가 예정일

## 10.4 가상투자 상태

종목 상태는 다음과 같다.

```txt
universe
→ watch
→ candidate
→ risk_reviewed
→ user_approved_virtual_buy
→ virtual_hold
→ trim_candidate
→ virtual_sell
→ archived
```

---

# 11. Thesis Lifecycle 설계

투자 thesis는 단순 설명문이 아니라 생명주기를 가진다.

```txt
draft → active → confirmed → weakened → broken → retired
```

## 11.1 Thesis 문서 필수 항목

- 핵심 주장
- 수익 원천
- 정량 확인 지표
- 반대 논리
- thesis가 맞다면 관찰될 신호
- thesis가 틀렸다면 먼저 나타날 경고 신호
- kill criteria
- 관련 전략 ID
- 관련 종목

## 11.2 Thesis Broken 조건

- 핵심 성장률 2개 분기 연속 훼손
- 마진 개선 thesis 실패
- 경쟁 우위 훼손
- 회계 신뢰도 문제
- 시장 국면 변화로 핵심 가정 무효화
- 더 나은 대체 전략 확인

---

# 12. Devil's Advocate 설계

Devil's Advocate는 투자 판단의 균형을 잡는 역할이다.

## 12.1 Bear Case Report 구성

```md
# Bear Case Report

## 대상

## Bull Thesis 요약

## 가장 강한 반대 논리
1.
2.
3.

## 이 반대 논리가 맞다면 먼저 나타날 신호
1.
2.
3.

## 현재 위험도
Low / Medium / High / Critical

## 결론
가상편입 가능 / watch only / 반려 / size cap 필요
```

## 12.2 강제 적용 조건

Devil's Advocate 검토는 다음 경우 필수다.

- 고밸류에이션 종목
- 테마 집중 전략
- 비중 확대
- 기존 thesis upgrade
- 시나리오 테스트 일부 실패
- 사용자가 “더 공격적으로” 선택한 경우

---

# 13. Knowledge Archive 설계

Knowledge Archive는 단순 독서 기록이 아니라 룰 개발 공급망이다.

```txt
도서/이론/논문/사례
→ 핵심 원칙 추출
→ 하네스 해석
→ 룰 후보 작성
→ 검증
→ active rule 반영 또는 반려
```

## 13.1 아카이브 구조

```txt
knowledge_archive/
├─ theories/
│  ├─ value_investing/
│  ├─ growth_investing/
│  ├─ factor_investing/
│  ├─ macro_investing/
│  ├─ behavioral_finance/
│  ├─ portfolio_theory/
│  └─ risk_management/
├─ books/
├─ papers/
├─ case_studies/
│  ├─ success_cases/
│  ├─ failure_cases/
│  └─ regime_cases/
├─ concepts/
├─ extracted_rules/
└─ mappings/
```

## 13.2 우선 아카이빙 대상

### 도서
- The Intelligent Investor
- Common Stocks and Uncommon Profits
- One Up on Wall Street
- Security Analysis
- Quality Investing
- Expected Returns
- Adaptive Markets

### 이론
- Margin of Safety
- Quality Factor
- Momentum
- Value Factor
- Low Volatility
- Behavioral Finance
- Market Regime
- Credit Cycle
- Liquidity Cycle

### 사례
- Dotcom Bubble
- Peloton Growth Reversal
- WeWork Valuation Failure
- SVB Duration Risk
- Amazon Operating Leverage
- Nvidia AI Cycle

## 13.3 이론 → 룰 변환 예시

### 안전마진

```txt
이론: 예측 오류를 견디기 위해 가격 또는 리스크 완충 필요
룰: valuation guardrail, downside scenario 필수
```

### 확증편향

```txt
이론: 사람은 자신이 믿고 싶은 정보만 수집함
룰: 가상매수 전 반대 근거 3개 필수
```

### 성장 지속성

```txt
이론: 일시적 성장과 구조적 성장을 구분해야 함
룰: growth durability check 필수
```

---

# 14. Market Regime 설계

## 14.1 주요 국면

| 국면 | 특징 | 유리한 전략 | 주의 전략 |
|---|---|---|---|
| Goldilocks | 성장 안정, 인플레 둔화, 유동성 양호 | Quality Growth, Momentum | Deep Defensive |
| High Rate Pressure | 금리 상승, 유동성 긴축 | Defensive Quality, Value | High PSR Growth |
| Recession Risk | 경기 둔화, credit spread 확대 | Defensive Quality, Cash | Cyclical Growth |
| Liquidity Expansion | 유동성 증가, 위험선호 회복 | Growth, Momentum | Excess Cash |
| Inflation Reacceleration | 비용 상승, 금리 재상승 | Pricing Power, Commodity-sensitive | Low Margin Growth |

## 14.2 국면 판단 지표

- 10년물 금리
- 기준금리
- 장단기 금리차
- credit spread
- M2 증가율
- financial conditions index
- CPI/PCE
- PMI
- earnings revision

## 14.3 국면 불확실 시 기본값

```txt
더 보수적으로
```

구체적 조치:
- position size 축소
- 현금 비중 증가
- scenario test 강화
- 고밸류 전략 보류
- Decision Gate에서 보수 선택지 추천

---

# 15. Data Quality 설계

데이터가 틀리면 하네스 전체가 틀린다. 따라서 데이터 신뢰도는 별도 레이어로 관리한다.

## 15.1 검증 대상

- 가격 데이터
- 재무제표 데이터
- factor data
- benchmark data
- 섹터/테마 분류
- 금리/매크로 데이터

## 15.2 데이터 품질 실패 시 조치

| 문제 | 조치 |
|---|---|
| 가격 결측 | 해당 기간 수익률 계산 보류 |
| 비정상 수익률 | manual review |
| 재무 데이터 결측 | signal unreliable 표시 |
| restatement 발생 | 과거 signal 재계산 |
| benchmark 오류 | 성과 비교 보류 |

## 15.3 데이터 품질 룰

```yaml
if_data_quality_failed:
  action:
    - mark_signal_unreliable
    - block_strategy_approval
    - require_manual_review
```

---

# 16. Error Taxonomy 설계

실패는 단순 손실이 아니라 학습 데이터다.

## 16.1 오류 대분류

분석 오류:
- 시장 규모 과대평가
- 성장률 지속성 오판
- 마진 구조 오판
- 경쟁 우위 과대평가
- 밸류에이션 정당화 오류

실행 오류:
- 너무 빠른 진입
- 너무 큰 비중
- 리밸런싱 지연
- 청산 조건 무시

심리 오류:
- 확증편향
- 손실회피
- 최근성 편향
- 스토리 과몰입
- 결과 편향

데이터 오류:
- 잘못된 지표 사용
- 결측치 처리 실패
- 회계 변경 미반영
- 생존자 편향

체계 오류:
- 룰 부재
- 룰 위반 미탐지
- 피드백 미반영

## 16.2 오류 → 룰 매핑

| 오류 | 연결 룰 |
|---|---|
| 고평가 정당화 오류 | valuation_guardrail |
| 성장률 지속성 오판 | growth_durability_check |
| 확증편향 | opposite_case_required |
| 너무 큰 비중 | position_size_mapping |
| 손절/청산 지연 | kill_criteria_required |
| 데이터 오류 | data_quality_blocker |

---

# 17. Decision Center 설계

Decision Center는 사용자가 판단해야 할 사항만 모아두는 곳이다.

## 17.1 Decision Queue 항목

- decision_id
- gate
- title
- requested_by
- priority
- status
- options
- default_recommendation
- created_at

## 17.2 Decision 상태

```txt
drafted
→ pending_user_decision
→ approved
→ rejected
→ held
→ executed
→ logged
```

## 17.3 기본 원칙

- 사용자에게 한 번에 하나의 의사결정만 요청한다.
- 모든 질문은 A/B/C/D 선택지로 압축한다.
- 기본 추천안을 반드시 제시한다.
- 사용자가 답하지 않으면 실행하지 않고 보류한다.
- 실제 투자 전환은 현재 정책상 비활성화한다.

---

# 18. Agent Layer 설계

## 18.1 모델별 역할 권장

| 모델 | 권장 역할 |
|---|---|
| GPT | 구조화, 룰 설계, 수치화, 코드 초안, 의사결정 템플릿 |
| Claude | 긴 문서 요약, 도서/이론 아카이빙, 반대 논리, 메타 분석 |
| Codex | 파일 생성, 코드 구현, 테스트 작성, 리팩터링 |

## 18.2 에이전트 자율성 레벨

```txt
L0 manual_only
L1 draft_allowed
L2 analysis_allowed
L3 file_update_allowed
L4 rule_proposal_allowed
L5 active_rule_update_allowed
L6 real_money_action_allowed
```

현재 정책:

```txt
L6 disabled
active rule update requires user approval
virtual buy requires user approval
strategy retirement requires user approval
```

## 18.3 Codex 작업 원칙

Codex는 다음 작업을 수행한다.

1. 폴더 구조 생성
2. Markdown/YAML 템플릿 생성
3. Python validator 작성
4. 테스트 작성
5. CHANGELOG 기록

Codex가 해서는 안 되는 작업:

- 실제 브로커 API 연동
- 실제 투자 실행 코드 작성
- 사용자 승인 없는 active rule 수정
- 사용자 승인 없는 전략 승격

---

# 19. Rule Governance 설계

## 19.1 룰 버전 규칙

```txt
vMAJOR.MINOR.PATCH_YYYY-MM-DD
```

예시:

```txt
v0.1.0_2026-04-25
v0.1.1_2026-04-28
v0.2.0_2026-05-10
v1.0.0_2026-06-01
```

변경 기준:

| 변경 | 의미 |
|---|---|
| PATCH | 문구 수정, 기준값 소폭 조정 |
| MINOR | 새 룰 추가, 검증 항목 추가 |
| MAJOR | 승인 구조 또는 전략 파이프라인 변경 |

## 19.2 룰 변경 흐름

```txt
피드백 발생
→ rule_change_xxxx.md 작성
→ 검토
→ 테스트
→ 사용자 승인
→ active 룰 변경
→ 기존 룰 versions 저장
→ CHANGELOG 작성
```

## 19.3 룰 변경 트리거

- 백테스트 실패 패턴 반복
- 시나리오 손실 과다
- 룰 위반 반복
- 가상투자 결과와 기대의 괴리
- 나쁜 판단/좋은 결과 반복
- 좋은 판단/나쁜 결과 반복
- Knowledge Archive에서 강한 룰 후보 도출

---

# 20. Review 설계

## 20.1 Weekly Review

목적:
- 가상 포트폴리오 상태 점검
- 룰 위반 확인
- 다음 주 액션 결정

필수 항목:
- 주간 수익률
- 벤치마크 수익률
- 초과수익률
- 주요 변동
- 룰 위반 여부
- 가장 잘 작동한 판단
- 가장 취약했던 판단
- 룰 변경 필요성

## 20.2 Monthly Review

목적:
- 전략별 성과 평가
- 종목별 기여도 분석
- 반복 오류 패턴 확인
- 룰 개선 후보 도출

필수 항목:
- 월간 수익률
- MDD
- 승률
- 회전율
- 전략별 기여도
- 오류 유형
- 룰 변경 후보

## 20.3 Meta Review

목적:
- 가상투자 결과와 지식 아카이브를 결합해 룰 개선 후보를 만든다.

핵심 질문:
- 어떤 판단이 반복적으로 실패했는가?
- 어떤 성공이 운에 가까웠는가?
- 어떤 이론이 현재 하네스 룰과 연결될 수 있는가?
- 어떤 룰을 강화/완화해야 하는가?

---

# 21. Override 설계

예외는 허용하되, 기록되지 않은 예외는 금지한다.

## 21.1 Override 필수 항목

- overridden_rule
- reason
- expected_benefit
- risk_acknowledgement
- review_date
- approving_decision_id

## 21.2 Override 불가 항목

- real_money_allowed_false
- missing_trade_journal
- missing_opposite_case
- data_quality_failed
- user_approval_missing

---

# 22. 자동화 코드 설계

## 22.1 초기 구현 대상

- performance_tracker.py
- rule_feedback_engine.py
- risk_checker.py
- portfolio_manager.py
- scenario_simulator.py
- paper_trading_engine.py

## 22.2 Performance Tracker

역할:
- 포트폴리오 수익률 계산
- 벤치마크 대비 초과수익 계산
- Process/Outcome 기반 판단 분류

## 22.3 Rule Feedback Engine

역할:
- 반복 룰 위반 탐지
- 시나리오 실패 반복 탐지
- lucky success 감지
- rule_change_proposal 필요 여부 반환

## 22.4 향후 테스트 항목

- YAML 문법 검증
- active rule 필수 필드 검증
- decision queue 필수 옵션 검증
- 가상매수 전 trade_journal 존재 여부 검증
- real_money_allowed false 강제 검증
- scenario pass rule 검증

---

# 23. 단계별 개발 로드맵

## Phase 1. 문서 기반 하네스

목표:
- 코드 없이도 운영 가능한 투자 검증 체계 구축

산출물:
- 운영 매뉴얼
- 기획서
- 룰 YAML
- 가상투자 템플릿
- 의사결정 큐
- 지식 아카이브 템플릿

## Phase 2. 반자동 하네스

목표:
- YAML 전략과 보유 종목 파일을 읽어 룰 위반 자동 검출

산출물:
- risk_checker.py
- portfolio_manager.py
- paper_trading_engine.py
- performance_tracker.py

## Phase 3. 시나리오/백테스트 연동

목표:
- 전략이 운이 아니라 구조적으로 유효한지 검증

산출물:
- scenario_simulator.py
- backtest_engine.py
- report_generator.py

## Phase 4. 룰 셀프 피드백 시스템

목표:
- 반복 실패와 룰 위반에서 자동으로 룰 변경 후보 생성

산출물:
- rule_feedback_engine.py
- meta_review_generator.py
- rule_change_proposal_generator.py

## Phase 5. 운영 대시보드

목표:
- Notion 또는 Drive에서 사용자가 의사결정만 쉽게 볼 수 있도록 구성

산출물:
- Decision Center Dashboard
- Strategy Scoreboard
- Virtual Portfolio Dashboard
- Rule Proposal Board

## Phase 6. 실제 투자 전환 후보 심사

현재 비활성화.

실제 투자 전환 후보 조건:
- 최소 3개월 이상 가상운용
- 최소 10개 이상 decision log
- 룰 위반 0회
- MDD 허용 범위
- 벤치마크 대비 유의미한 성과
- Meta Review 통과
- 사용자 별도 승인

---

# 24. ver0.1 현재 반영 범위

현재 PR에는 다음 초기 파일이 포함된다.

- README.md
- HARNESS_OPERATING_MANUAL.md
- 투자전략하네스_기획서ver0.1_20260425.md
- agents/agent_registry.yaml
- agents/agent_decision_gate_rules.yaml
- rules/active/user_decision_rules.yaml
- rules/active/paper_trading_rules.yaml
- rules/active/decision_rules.yaml
- rules/active/portfolio_rules.yaml
- rules/active/scenario_rules.yaml
- rules/RULE_GOVERNANCE.md
- decision_center/pending_decisions.md
- decision_center/decision_queue.yaml
- virtual_portfolio/current/portfolio_status.md
- virtual_portfolio/current/holdings.yaml
- virtual_portfolio/current/trade_journal.md
- strategies/draft/quality_growth_v1.yaml
- knowledge_archive/README.md
- knowledge_archive/archive_governance.md
- src/performance_tracker.py
- src/rule_feedback_engine.py
- tests/test_performance_tracker.py

---

# 25. 향후 보완 필요 사항

1. 누락된 active rule 파일 추가
   - archive_usage_rules.yaml
   - market_regime_rules.yaml
   - data_quality_rules.yaml
   - thesis_lifecycle_rules.yaml
   - retirement_rules.yaml
   - override_rules.yaml

2. workspaces 템플릿 추가
   - progress.md
   - feedback.md
   - output_template.md

3. decision_center 보강
   - decision_log.md
   - escalation_rules.yaml
   - decision_templates.md

4. 가상투자 파일 보강
   - cash_ledger.md
   - watchlist.md
   - weekly_review.md
   - monthly_review.md

5. Knowledge Archive 샘플 추가
   - margin_of_safety.md
   - confirmation_bias.md
   - quality_factor.md
   - growth_durability.md

6. Strategy Zoo 보강
   - strategy_scoreboard.md
   - quality_growth/
   - defensive_quality/
   - ai_infrastructure_theme/

7. 자동화 코드 보강
   - YAML validator
   - decision queue generator
   - portfolio exposure checker
   - scenario simulator
   - report generator

---

# 26. 최종 요약

본 하네스의 핵심은 다음과 같다.

```txt
AI가 투자해주는 시스템이 아니라,
AI 에이전트들이 투자 판단의 재료를 만들고,
하네스가 검증하며,
사용자는 핵심 의사결정만 내리는 시스템.
```

투자전략하네스는 수익을 즉시 내는 시스템이 아니다. 더 중요한 목적은 다음이다.

```txt
잘못된 투자 판단이 반복되는 경로를 차단하고,
실패를 재사용 가능한 룰 개선 데이터로 전환하며,
투자 이론과 실제 가상운용 결과를 연결해
시간이 지날수록 판단 품질이 개선되는 구조를 만드는 것.
```

최종 운영 사이클은 다음과 같다.

```txt
투자 아이디어 관리
→ 투자 논리 생명주기 관리
→ 전략 신호화
→ 시나리오/리스크 검증
→ 가상투자
→ 실패 유형 분류
→ 지식 아카이브 연결
→ 룰 변경 제안
→ 사용자 승인
→ 룰 버전 업데이트
→ 다음 전략에 반영
```

이 구조가 완성되면 사용자는 매번 시장을 해석하는 사람이 아니라, 하네스가 만든 분석과 선택지를 보고 핵심 의사결정만 내리는 투자 시스템 오너가 된다.
