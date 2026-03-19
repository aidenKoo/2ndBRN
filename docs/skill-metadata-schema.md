# SKILL METADATA SCHEMA

## 목적
스킬 진화(승급/강등)를 정량적으로 관리하기 위한 공통 스키마를 정의한다.

## 필드
- `id`: `domain/name` 형식의 고유 식별자
- `status`: `draft | verify | trusted | restricted | deprecated`
- `confidence`: 0.0 ~ 1.0
- `usage_count`: 누적 사용 횟수
- `success_rate`: 최근 윈도우 기준 성공률
- `failure_tags`: 실패 패턴 태그 목록

## 운영 규칙
- 최근 10회 중 8회 PASS + 회귀 없음 -> `trusted`
- 최근 5회 중 3회 FAIL -> `verify`
- 동일 failure tag 2회 반복 -> `restricted`
