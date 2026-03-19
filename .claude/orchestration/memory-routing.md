# ORCHESTRATION: MEMORY ROUTING

## 원칙
- 내부 문서 우선, 외부 메모리 후순위
- 원문 통째 주입 금지(요약 packet으로 변환)
- 역할별 최소 컨텍스트만 전달

## 절차
1. 문제 유형별 필요 컨텍스트 정의
2. 내부 문서 검색
3. 부족 시 external-memory 조회
4. top-k 요약 + 출처 명시
5. Context Packet 생성 후 전달
