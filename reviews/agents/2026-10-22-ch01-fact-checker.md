# 1장 다시 만들기: fact-checker(기술 확인, 2026-10-22, PR #85)

판정 요약: 필수 3, 권장 6, 참고 7, 검증 후 확정 2, 확인한 사실 문장 약 60개. 로컬 Claude Code v2.1.302. 출처 기록은 research/ch01-sources.md "2026-10-22 1장 기술 확인"

| 발견 | 위치 | 근거 | 제안 | 확신 | 처리 |
|---|---|---|---|---|---|
| 필수: LLM, 컨텍스트 윈도 정의에 용어집 각주(용어집 문구와 다름) | background | Platform Glossary(S28), Q-106 | "이 책은"으로 정의 | 높음 | 반영 |
| 필수: "어느 권한 모드에서도 거부" 각주가 permissions 문서(문장은 permission-modes 문서) | loop | Permission modes "Deny rules block in every mode" | permission-modes 키 추가 | 높음 | 반영 |
| 필수: 기억 항목 앞 두 문장에 근거 없음 | background 기억 | Messages API "stateless" | messages-api 키 추가 | 높음 | 반영 |
| 권장: Stop 훅 연속 차단 상한 | loop | Hooks Stop | 제품 상한과 조건 | 높음 | 반영(횟수는 쓰지 않음) |
| 권장: git push 금지 규칙의 한계 | request, loop | Bash rule doesn't match | 한 문장 | 높음 | 반영 |
| 권장: .env 규칙 조건(grep -r, 기준 위치) | loop | Read and Edit | 한 문장 | 중간 | grep -r 반영, 기준 위치는 9장 |
| 권장: request 3번이 기본 권한 모드를 암시 | request | Permission modes 시작 모드 | 조건화 | 높음 | 반영 |
| 권장: API로 직접 작성 문장 각주 | agent-harness | Messages API 표 | messages-api | 중간 | 반영 |
| 권장: 엔지니어링 글 주체 표기 | 여러 곳 | S9, S12 | Anthropic의 글 | 중간 | 보류(Q-039, Q-101 작가 결정) |
| 참고: 확인 요청이 잦으면 형식 승인(근거 없음) | loop | 문서에 없음 | 이 책의 판단으로 표시 | 중간 | 반영("이 책은 … 권합니다") |
| 참고: ReAct 마지막 문장이 초록 범위 밖 | meanings | S11 | 줄임 | 중간 | 반영 |
| 참고: 세션 기록 보충, 하네스 일반 뜻 출처, 저자 표기, Codex CLI 한정, 용어집 "is the harness" | | | | | 용어집 표현은 반영, 나머지 유지 |
| 검증 후 확정: OpenAI Harness engineering 수치와 네 가지(403) | harness | S2 기록만 | 작가 브라우저 확인(Q-090) | | 유지 |
| 검증 후 확정: Codex 글의 턴 정의(403) | loop | 발췌에 없음 | 약하게 | | 턴 정의 문장 삭제 |

표 1-9 실행 확인(R8): /context, /usage 실행으로 일치, /permissions는 비대화형 실행 불가로 문서 대체. 점검 질문 4(범위): 대체로 구분, 남은 혼선 셋(git push 한계, 기본 권한 모드, 글 주체) 가운데 둘 반영. 9(출처): 필수 3건 반영, OpenAI 수치는 S2 기록 의존
