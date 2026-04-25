# 투자전략하네스 기획서 ver0.1

## 문서 정보

- 문서명: 투자전략하네스_기획서ver0.1_20260425
- 작성일: 2026-04-25
- 상태: Draft
- 적용 범위: 투자 자동 가이드 머신 / investment-harness 초기 설계
- 현재 운용 모드: 가상투자 전용
- 실제 투자 실행: 비활성화

---

## 1. 기획 배경

본 기획서는 하네스 엔지니어링의 관점에서 투자 분석, 전략 검증, 가상투자, 룰 개선, 지식 아카이빙, 에이전트 협업 구조를 통합하기 위한 초기 설계 문서이다.

기존 투자 분석은 사람의 직관, 시장 해석, 개별 종목 판단에 강하게 의존하는 경향이 있다. 이 방식은 빠른 판단에는 유리할 수 있으나, 판단 근거가 누락되거나, 실패가 재사용 가능한 학습 데이터로 남지 않거나, 같은 오류가 반복되는 문제가 발생한다.

본 하네스의 목적은 투자 아이디어를 즉시 실행하는 것이 아니라, 투자 판단을 다음과 같은 구조로 변환하는 것이다.

```txt
투자 아이디어
→ 투자 thesis
→ 정량 signal
→ 백테스트 설계
→ 시나리오 테스트
→ 리스크 검토
→ 사용자 의사결정
→ 가상투자
→ 성과/오류 분석
→ 룰 개선
→ 버전 관리
```

즉, 본 시스템은 투자 추천기가 아니라 **투자 판단 검증기**이다.

---

## 2. 핵심 철학

### 2.1 투자 전략은 코드처럼 다룬다

투자 전략은 감각이나 의견이 아니라, 검증 가능한 입력값, 처리 규칙, 출력 결과를 가진 시스템으로 취급한다.

```txt
전략 = 코드
시장 = 런타임
수익률 = 테스트 결과
손실 = 실패 로그
룰 변경 = 리팩터링
```

따라서 전략은 다음 조건을 만족해야 한다.

1. 가설이 명확해야 한다.
2. 신호로 변환 가능해야 한다.
3. 반대 논리가 기록되어야 한다.
4. 리스크 룰을 통과해야 한다.
5. 가상투자로 검증되어야 한다.
6. 실패 시 원인이 분류되어야 한다.
7. 개선된 룰은 형상관리되어야 한다.

### 2.2 결과보다 판단 품질을 먼저 평가한다

투자에서는 좋은 판단이 나쁜 결과를 낳을 수 있고, 나쁜 판단이 좋은 결과를 낳을 수 있다. 따라서 본 하네스는 결과 수익률만이 아니라, 판단 당시의 프로세스를 별도로 평가한다.

판단은 다음 네 가지로 분류한다.

```txt
좋은 판단 / 좋은 결과
좋은 판단 / 나쁜 결과
나쁜 판단 / 좋은 결과
나쁜 판단 / 나쁜 결과
```

이 구분을 통해 운으로 얻은 수익과 재현 가능한 의사결정을 분리한다.

### 2.3 사용자는 실무자가 아니라 의사결정자다

본 하네스에서 사용자의 역할은 자료 수집자나 분석 실무자가 아니라 Investment Harness Owner이다.

사용자는 다음 판단만 수행한다.

- 승인
- 반려
- 보류
- 수정 지시
- 보수/공격 성향 선택
- 우선순위 결정
- 예외 승인

에이전트는 질문하기 전에 반드시 요약, 선택지, 추천안, 리스크, 결과를 준비해야 한다.

---

## 3. 전체 시스템 구조

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

각 레이어의 역할은 다음과 같다.

| 레이어 | 목적 |
|---|---|
| Knowledge Archive | 투자 이론, 도서, 논문, 사례, 개념 저장 및 룰 후보 추출 |
| Agent Layer | GPT, Claude, Codex 등 역할 기반 에이전트 운용 |
| Decision Center | 사용자의 승인/보류/반려 의사결정 큐 관리 |
| Rule Engine | active/proposals/versions 기반 투자 룰 형상관리 |
| Universe | 투자 후보군 관리 |
| Data Quality | 데이터 결측, 이상치, 신뢰도 검증 |
| Market Regime | 금리, 유동성, 인플레, 경기 국면 판단 |
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

## 4. 폴더 구조 설계

초기 기준 폴더 구조는 다음과 같다.

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

## 5. 핵심 롤 정의

본 하네스는 실제 인력 조직이라기보다, 에이전트 및 문서 산출물 기준의 역할 체계로 운영한다.

### 5.1 Hypothesis Designer

역할:
- 투자 아이디어 생성
- 투자 thesis 초안 작성
- 전략 YAML 초안 작성

주요 산출물:
- thesis_draft.md
- strategy_draft.yaml
- investment_thesis.md

### 5.2 Signal Engineer

역할:
- 투자 가설을 정량 신호로 변환
- factor 및 signal 후보 정의
- 데이터 필요 항목 정의

주요 산출물:
- signal_spec.md
- factor_definition.yaml

### 5.3 Backtest Engineer

역할:
- 백테스트 설계
- look-ahead bias, survivorship bias 등 편향 점검
- 성과지표 정의

주요 산출물:
- backtest_plan.md
- backtest_report.md
- bias_checklist.md

### 5.4 Portfolio Manager

역할:
- 포트폴리오 비중 설계
- 현금 비중 관리
- 섹터, 테마, 베타, 금리 민감도 노출 관리

주요 산출물:
- allocation_plan.md
- exposure_report.md

### 5.5 Scenario Simulator

역할:
- 금리 상승/하락, 경기침체, 인플레이션, 유동성 축소 등 시나리오 설계
- 전략 및 포트폴리오 충격 테스트

주요 산출물:
- scenario_report.md
- stress_test_result.md

### 5.6 Risk Manager

역할:
- 전략 승인/보류/반려 판단
- 룰 위반 탐지
- 가상투자 진입 전 리스크 검토

주요 산출물:
- risk_review.md
- approval_checklist.md

### 5.7 Paper Trading Operator

역할:
- 가상투자 실행 기록
- portfolio_status 업데이트
- trade_journal, cash_ledger 관리

주요 산출물:
- trade_journal.md
- portfolio_status.md
- decision_log.md
- cash_ledger.md

### 5.8 Knowledge Curator

역할:
- 투자 이론, 도서, 논문, 사례 아카이빙
- 핵심 원칙 추출
- 룰 후보 생성

주요 산출물:
- archive_summary.md
- rule_candidate.md
- theory_to_rule_map.md

### 5.9 Devil's Advocate

역할:
- 반대 논리 작성
- 실패 가능성 탐색
- pre-mortem 작성

주요 산출물:
- bear_case_report.md
- contradiction_log.md

### 5.10 Regime Analyst

역할:
- 현재 시장 국면 판단
- 금리, 유동성, 인플레이션, 경기 지표 해석
- 전략별 유리/불리 국면 매핑

주요 산출물:
- current_regime.md
- regime_to_strategy_map.md

### 5.11 Data Reliability Manager

역할:
- 데이터 품질 검증
- 결측치, 이상치, restatement 탐지
- 데이터 신뢰도 등급 부여

주요 산출물:
- data_validation_report.md
- missing_data_log.md
- restatement_log.md

### 5.12 Meta Analyst

역할:
- 반복 실패 패턴 분석
- 룰 개선 후보 도출
- 전략 유지/폐기 제안
- 지식 아카이브와 가상투자 결과를 연결

주요 산출물:
- meta_review.md
- rule_change_recommendation.md

---

## 6. 에이전트 운영 원칙

에이전트는 작업 중간마다 사용자를 괴롭히지 않는다. 정해진 Decision Gate에서만 사용자에게 묻는다.

### 6.1 허용되는 질문 유형

- 승인/반려
- A/B/C/D 선택
- 보수/공격 성향 선택
- 우선순위 선택
- 예외 승인
- 전략 폐기 확인

### 6.2 금지되는 질문 유형

- “무엇을 할까요?”
- “룰을 직접 정해주세요.”
- “이 종목 어떻게 볼까요?”
- “다음 단계는 뭘까요?”
- “어떤 지표를 쓸까요?”

### 6.3 사용자 질문 형식

```md
# User Decision Request

## Decision ID
DQ-XXXX

## 현재 단계
Gx Gate Name

## 요약
현재 맥락 요약

## 에이전트 결론
추천안

## 근거
1.
2.
3.

## 주요 리스크
1.
2.

## 선택지
A.
B.
C.
D.

## 추천 선택
A/B/C/D

## 사용자 응답
A / B / C / D / 보류 / 근거 추가
```

---

## 7. Decision Gate 설계

| Gate | 설명 | 사용자 결정 필요 여부 |
|---|---|---|
| G0 | 새 전략 아이디어를 실험할지 여부 | 필요 |
| G1 | 전략 초안을 신호 설계로 넘길지 여부 | 필요 |
| G2 | 신호 정의를 확정하고 백테스트로 넘길지 여부 | 필요 |
| G3 | 백테스트 결과를 시나리오 테스트로 넘길지 여부 | 필요 |
| G4 | 시나리오 테스트 후 가상투자 진입 여부 | 필요 |
| G5 | 특정 종목/전략을 가상 포트폴리오에 편입할지 여부 | 필요 |
| G6 | 주간 리뷰 후 유지/조정 여부 | 필요 |
| G7 | 룰 변경안을 active rule로 반영할지 여부 | 필요 |
| G8 | 전략 폐기 여부 | 필요 |
| G9 | 실제 투자 전환 후보 심사 | 현재 비활성화 |

---

## 8. 룰 엔진 설계

룰은 다음 상태를 가진다.

```txt
observed → candidate → proposed → tested → user_approved → active → archived
```

룰 폴더 구조는 다음과 같다.

```txt
rules/
├─ active/
│  ├─ decision_rules.yaml
│  ├─ portfolio_rules.yaml
│  ├─ scenario_rules.yaml
│  ├─ risk_rules.yaml
│  ├─ paper_trading_rules.yaml
│  ├─ user_decision_rules.yaml
│  ├─ archive_usage_rules.yaml
│  ├─ market_regime_rules.yaml
│  ├─ data_quality_rules.yaml
│  ├─ thesis_lifecycle_rules.yaml
│  ├─ retirement_rules.yaml
│  └─ override_rules.yaml
├─ proposals/
├─ versions/
└─ RULE_GOVERNANCE.md
```

### 8.1 룰 변경 원칙

1. active rule은 직접 수정하지 않는다.
2. 변경은 proposals에 먼저 작성한다.
3. 변경 사유, 근거, 검증 방법을 기록한다.
4. 승인 후 기존 active rule은 versions로 백업한다.
5. 변경 후 CHANGELOG를 작성한다.

### 8.2 룰 변경 제안서 필수 항목

- 변경 대상
- 변경 이유
- 발견 경로
- 기존 룰
- 제안 룰
- 기대 효과
- 부작용 가능성
- 검증 방법
- 지식 출처
- 하네스 데이터 근거
- 승인 여부

---

## 9. 가상투자 운영 설계

현재 시스템은 실제 투자가 아니라 가상투자만 허용한다.

### 9.1 가상투자 목적

- 전략 실험
- 의사결정 품질 평가
- 룰 위반 탐지
- 실패 패턴 수집
- 실제 투자 전환 전 검증

### 9.2 가상투자 필수 기록

- portfolio_status.md
- holdings.yaml
- trade_journal.md
- decision_log.md
- cash_ledger.md
- watchlist.md

### 9.3 가상매수 전 필수 조건

1. 투자 thesis 존재
2. signal score 기준 통과
3. valuation 과열 여부 검토
4. scenario loss 한도 통과
5. risk check 통과
6. 반대 근거 3개 이상 작성
7. pre-mortem 작성
8. kill criteria 작성
9. 사용자 승인 획득

### 9.4 Process Score와 Outcome Score

Process Score:
- thesis 명확성
- 데이터 근거
- 반대논리 검토
- 리스크 관리
- 룰 준수

Outcome Score:
- 수익률
- 벤치마크 대비 성과
- 변동성 대비 성과

---

## 10. Knowledge Archive 설계

Knowledge Archive는 투자 지식 저장소이며, 단순 학습 노트가 아니라 룰 개발을 위한 원천 데이터이다.

```txt
투자 지식 → 핵심 원칙 → 하네스 해석 → 룰 후보 → 검증 → active rule
```

### 10.1 분류

- theories
- books
- papers
- case_studies
- concepts
- extracted_rules
- mappings

### 10.2 상태

```txt
raw → summarized → interpreted → rule_candidate → tested → adopted/rejected → archived
```

### 10.3 아카이브 금지 사항

- 출처 없는 격언을 룰로 반영 금지
- 단일 성공 사례를 보편 룰로 승격 금지
- 실패 사례 무시 금지
- 검증 없는 active rule 반영 금지
- 과거 이론을 현재 시장에 무비판적으로 적용 금지

---

## 11. Market Regime 설계

투자 이론은 시장 국면에 따라 작동 여부가 달라질 수 있다. 따라서 시장 국면 판단 레이어를 둔다.

### 11.1 주요 지표

- 10년물 금리
- 기준금리
- M2 증가율
- credit spread
- financial conditions index
- CPI/PCE
- PMI
- earnings revision

### 11.2 주요 국면

- Goldilocks
- High Rate Pressure
- Recession Risk
- Liquidity Expansion
- Inflation Reacceleration

### 11.3 국면 불확실 시 기본 행동

- position size 축소
- cash buffer 증가
- scenario test 강화
- user decision gate에서 보수 옵션 기본 추천

---

## 12. Error Taxonomy 설계

손실을 단순 수익률 결과로 보지 않고 오류 유형으로 분류한다.

### 12.1 오류 유형

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

---

## 13. Strategy Zoo 설계

단일 전략에 감정적으로 몰입하지 않기 위해 여러 전략을 실험군으로 관리한다.

예시 전략군:
- quality_growth
- value_reversion
- momentum_breakout
- defensive_quality
- ai_infrastructure_theme

Strategy Scoreboard 항목:
- 전략 ID
- 상태
- 운용 기간
- 수익률
- 벤치마크 대비 성과
- MDD
- 룰 위반 횟수
- 평가

---

## 14. Thesis Lifecycle 설계

투자 thesis는 상태를 가진다.

```txt
draft → active → confirmed → weakened → broken → retired
```

### 14.1 Confirmed 조건

- 매출 성장률이 기대와 일치
- 마진 개선이 관찰됨
- 경쟁 지위 유지
- 리스크 한도 유지

### 14.2 Weakened 조건

- 핵심 지표 1회 미달
- valuation risk 증가
- management guidance 하향
- scenario risk 증가

### 14.3 Broken 조건

- thesis 관련 핵심 지표 2회 이상 훼손
- 구조적 성장 둔화 확인
- 경쟁 우위 훼손
- 회계/신뢰도 문제 발생

---

## 15. Override 설계

예외 판단은 허용하되, 기록되지 않은 예외는 금지한다.

Override 필수 기록:
- overridden_rule
- reason
- expected_benefit
- risk_acknowledgement
- review_date

Override 금지 대상:
- real_money_allowed_false
- missing_trade_journal
- missing_opposite_case
- data_quality_failed

---

## 16. 자동화 코드 설계

초기 자동화 대상은 다음과 같다.

### 16.1 Performance Tracker

역할:
- 가상 포트폴리오 수익률 계산
- 벤치마크 대비 초과수익 계산
- 판단 품질 분류

### 16.2 Rule Feedback Engine

역할:
- 반복 룰 위반 탐지
- 시나리오 실패 반복 탐지
- lucky success 탐지
- good process / bad outcome 반복 탐지
- 룰 변경 필요 여부 반환

향후 확장 대상:
- YAML rule validator
- decision queue generator
- portfolio exposure checker
- scenario simulator
- backtest harness
- report generator

---

## 17. 초기 개발 로드맵

### Phase 1. 문서 기반 하네스

목표:
- 코드 없이도 굴러가는 투자 검증 운영체계 구축

산출물:
- 운영 매뉴얼
- 룰 YAML
- 의사결정 큐
- 가상투자 템플릿
- 지식 아카이브 템플릿

### Phase 2. 반자동 하네스

목표:
- YAML 전략 파일과 보유 종목 파일을 읽어 리스크/비중/룰 위반 자동 체크

산출물:
- risk_checker.py
- portfolio_manager.py
- paper_trading_engine.py
- performance_tracker.py

### Phase 3. 시나리오/백테스트 연동

목표:
- 전략이 운이 아니라 구조적으로 유효한지 검증

산출물:
- backtest_engine.py
- scenario_simulator.py
- report_generator.py

### Phase 4. 룰 셀프 피드백 시스템

목표:
- 성과 부진이나 룰 위반 반복 시 룰 변경 후보 자동 생성

산출물:
- rule_feedback_engine.py
- meta_review_generator.py
- rule_change_proposal_generator.py

### Phase 5. 실제 투자 전환 후보 심사

현재는 비활성화한다.

실제 투자 전환 조건 예시:
- 최소 3개월 이상 가상운용
- 최소 10개 이상 의사결정 로그
- 룰 위반 0회
- 최대낙폭 허용 범위 내 유지
- 벤치마크 대비 유의미한 성과
- 메타 리뷰 통과

---

## 18. 현재 ver0.1 범위

이번 ver0.1은 다음을 포함한다.

- investment-harness 루트 구조
- 운영 매뉴얼
- 사용자 의사결정 룰
- 에이전트 레지스트리
- 의사결정 게이트 룰
- 가상투자 룰
- 포트폴리오 룰
- 시나리오 룰
- decision rules
- rule governance
- knowledge archive governance
- 가상 포트폴리오 템플릿
- trade journal 템플릿
- quality_growth_v1 전략 초안
- performance tracker 최소 코드
- rule feedback engine 최소 코드
- 기본 테스트

---

## 19. 향후 보완 필요 사항

1. GitHub PR 기반으로 scaffold 검토 및 merge
2. 누락된 active rule 파일 보강
3. Notion 운영 대시보드 생성 여부 검토
4. Google Drive 백업본 생성 여부 검토
5. Codex용 구현 프롬프트 추가
6. YAML validation 테스트 추가
7. 실제 가상투자 후보군 universe 설계
8. data_quality 룰 구체화
9. market_regime 지표 수집 방식 정의
10. knowledge_archive 초기 도서/이론 샘플 추가

---

## 20. 최종 요약

본 기획서의 핵심은 다음과 같다.

```txt
AI가 투자해주는 시스템이 아니라,
AI 에이전트들이 투자 판단의 재료를 만들고,
하네스가 검증하며,
사용자는 핵심 의사결정만 내리는 시스템.
```

본 하네스는 수익을 즉시 내는 것보다, 잘못된 투자 판단이 반복되는 경로를 차단하고, 실패를 재사용 가능한 룰 개선 데이터로 전환하는 것을 우선한다.

최종 목표는 다음과 같다.

```txt
투자 아이디어 관리
→ 투자 논리 생명주기 관리
→ 가상투자 검증
→ 실패 유형 분류
→ 지식 아카이브 연결
→ 룰 업데이트
→ 더 나은 투자 판단 체계 구축
```
