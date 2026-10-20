# ch01 fact-checker (2026-10-20, v1.0 보강)

범위: 주장 줄, 확인 방법(표 1-9), 원칙과 점검 질문, CR 이름 문장, 그림 1-2 캡션. 확인 문서: Claude Code Docs의 Commands, Debug your configuration, Manage costs effectively, Agent SDK의 How the agent loop works(2026-10-20 확인). 연구 기록은 research/ch01-sources.md의 S20~S22에 추가함.

| 발견 | 위치 | 근거 | 제안 | 확신 | 심각도 |
|---|---|---|---|---|---|
| 내용은 일치하나 확인 방법 절에 발표 주체와 참고 자료 링크가 없음 | 확인 방법 절, 표 1-9 | ch05의 /context, ch09의 /usage는 참고 자료로 링크함 | 주체를 밝히고 Commands 문서 항목 추가 | 중간 | 권장 |
| /context가 시스템 프롬프트, 도구, 메모리 파일 등을 범주별로 보여 줌. 전체화면 모드에서는 분류를 접고 /context all로 펼침 | 표 1-9 1행 | Debug your configuration, Commands | 수정 불필요(버전 주석 선택) | 높음 | 참고 |
| /permissions는 allow, ask, deny 규칙을 범위별로 보여 줌 | 표 1-9 2행 | Commands | 수정 불필요 | 높음 | 참고 |
| 종료 사유는 Agent SDK 결과(subtype), 토큰 사용량은 /usage. 한 칸에 묶어 /usage가 종료 사유도 보여 주는 것처럼 읽힐 수 있음 | 표 1-9 3행 | How the agent loop works(Handle the result), Costs(/usage) | 명령별로 짝지어 적기 | 중간 | 권장 |
| /usage Session은 API 사용자용, 금액은 정가 기준 추정치. 표는 토큰만 말해 충돌 없음 | 확인 방법 절 | Costs, Commands | 수정 불필요 | 높음 | 참고 |
| 원칙은 이 책의 권고. 하네스만 바꾼 정량 비교의 1차 출처는 찾지 못함 | 원칙 문장 | research/ch01-sources.md "근거가 부족한 곳" | 효과를 수치로 보증하지 않는 지금 문장 유지 | 중간 | 참고(미확인) |
| 주장 줄은 이 책의 정의이며 Glossary와 방향이 같음 | 주장 줄 | research S6, D-055 | 수정 불필요 | 중간 | 참고 |
| CR 이름 표기가 ch03, CLAUDE.md와 일치 | 결합형 문장 | ch03 20행 | 수정 불필요 | 높음 | 참고 |
| 루프 다섯 단계는 문서 표기와 달라 "이 책이 정리"가 맞음. 캡션에는 링크 없음 | 그림 1-2 캡션 | How the agent loop works | 캡션 링크 추가 여부는 작가 확인(D-104 표기 변경) | 중간 | 권장 |
| Codex 쪽 근거(Unrolling the Codex agent loop)는 403으로 확인 못 함 | 그림 1-2 캡션과 루프 절 | research S3 | 작가가 원문 확인 | 낮음 | 참고(미확인) |

필수 0, 권장 3, 참고 3, 확인한 사실 문장 10개
