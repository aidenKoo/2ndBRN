# Input Schema

## 목적
하네스 실행 시 필요한 입력 필드를 표준화한다.

## Required
```json
{
  "request_id": "uuid",
  "user_goal": "string",
  "asset": {"ticker": "string", "asset_type": "stock|etf"},
  "position": {
    "has_position": true,
    "avg_price": 0,
    "weight": 0,
    "holding_period": "intraday|swing|position"
  },
  "risk_profile": "low|medium|high",
  "market_timestamp": "ISO-8601",
  "evidence": []
}
```

## Optional
- `constraints.max_confidence_without_official_source`
- `constraints.must_include_counterargument`
- `watchlist_context`
