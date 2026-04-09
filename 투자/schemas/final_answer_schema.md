# Final Answer Schema

## 목적
모델/플랫폼이 달라도 동일한 최종 출력 구조를 보장한다.

```json
{
  "summary": "한 줄 판단",
  "bull_points": ["..."],
  "bear_points": ["..."],
  "action_plan": {
    "primary_action": "분할 익절|관망|분할 매수|비중 축소",
    "position_sizing": "비중/단계",
    "execution_note": "유동성/슬리피지 대응"
  },
  "risk_controls": {
    "invalidators": ["..."],
    "stop_or_exit_rule": "...",
    "reentry_rule": "..."
  },
  "checkpoints": ["실적", "CPI", "FOMC"],
  "confidence": 0.0,
  "theory_coverage": "High|Medium|Low"
}
```

## Validation Rule
- `bull_points`/`bear_points` 최소 2개 이상
- `invalidators` 최소 1개 이상
- `theory_coverage`가 `Low`이면 재작성
