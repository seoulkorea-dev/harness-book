# 5장 기술 감수(fact-checker, 2026-10-23, PR #94)

## 총평
- 범위 src/chapters/ch05.html 전체, 사실 문장 약 70개. 1차 출처: Claude Code 문서 7쪽(memory, commands, context-window, sub-agents, how-claude-code-works, skills, agent-sdk/agent-loop), Anthropic 엔지니어링 글. examples/expense-app/, 실습 2, 3, 5, docs/example-facts.md 대조
- 대부분 일치. 필수 3: 자동 요약 문장의 각주가 SDK 문서, 표 5-6 설명의 "넷째 행"이 다섯째 행, "작업 중에 새로 필요해진 자료는 담기지 않습니다"가 "같은 글에 따르면" 아래에 있으나 글에 없음
- OpenAI 글은 403, research 기록으로 판정(Q-030)
- 일치: /clear, /compact, /context [all], Memory files, 압축 뒤 재읽기, CLAUDE.md 작성 기준 네 가지, @경로, 추가 시점 네 가지, 강제 여부와 PreToolUse 훅, AGENTS.md v2.1.277, 컨텍스트 엔지니어링 글 문구, 예제 사실(32줄 6절, deny 6경로, 훅, reviewer 읽기 전용, 실습 5 요청 문장), 앵커 11개

## 발견
| # | 발견 | 위치 | 제안 | 확신 | 등급 |
|---|---|---|---|---|---|
| 1 | 자동 요약 각주가 agent-loop(SDK 주체) | resource 3문단 | how-cc-works 키, "오래된 도구 출력을 먼저 지우고, 필요하면 대화를 자동으로 요약" | 높음 | 필수 |
| 2 | 표 5-6 "넷째 행"은 다섯째 행 | fail 첫 문단 | "마지막 행", 행과 종류 대응을 밝힘 | 높음 | 필수 |
| 3 | 미리 제공의 단점이 글에 없음 | retrieval 2문단 | 이 책의 정리로 밝힘 | 높음 | 필수 |
| 4 | context-window 각주가 Skill 설명, 시스템 프롬프트, 도구 정의를 받치지 못함 | kinds | how-cc-works, skills 키, Skill에 "기본 설정에서" 조건 | 중간 | 권고 |
| 5 | 하위 에이전트 포크 예외, CLAUDE.md 읽음 누락, "모두 담습니다" 지나침 | retrieval 끝 문단 | 조건과 "또는 파일 위치" | 높음 | 권고 |
| 6 | 버전 주석에 v2.1.281 조건 누락 | version-note | Bedrock, 텔레메트리 끈 세션 | 높음 | 권고 |
| 7 | "Codex는 AGENTS.md를 읽습니다" 각주 없음 | rule-doc | ch10 링크로 받침 또는 PR 기록 | 중간 | 권고 |
| 8 | /context 문장 각주 없음 | resource | commands 각주 | 높음 | 권고 |
| 9 | "지키는 비율이 낮아진다" 단정 | rule-doc 둘째 li | "낮아질 수 있다" | 높음 | 권고 |
| 10 | "가장 작은 정보 묶음"에서 high-signal 누락 | retrieval 2문단 끝 | "신호가 강한" | 높음 | 권고 |
| 11 | "권한 설정은 강제를 맡습니다" 한계 | example | "도구 호출의 강제"로 좁힘, 9장에서 확정 | 중간 | 검증 후 확정 |
| 12 | OpenAI 글 원문 403 | kinds 사례 | 유지, Q-030 | 중간 | 검증 후 확정 |
| 13, 14 | 예제 사실, 1,000~2,000 토큰 | 표 5-4, 5-5, 5-7 | 변경 없음 | 높음 | 참고(일치) |

## research 기록
research/ch05-sources.md C5-8로 반영.

## 결론
필수 3, 권고 7, 검증 후 확정 2, 참고 2.
