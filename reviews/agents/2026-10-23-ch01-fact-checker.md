# Chapter 1 기술 감수 보고 (fact-checker, 브랜치 ch01-playbook-trial, PR #103)

확인일: 2026-10-23. 범위는 src/chapters/ch01.html 전체이고, 기준은 플레이북 7장, 8장, 25장 22~26항, BOOK_SPEC 4절, 5절, 7절입니다. 원고와 파일은 고치지 않았습니다. claude 명령은 저장소 밖 빈 임시 폴더(/tmp/ccx)에서 실행했고, 로컬 Claude Code는 v2.1.302입니다.

- 호출 방식: 이 세션이 저장소 밖(홈 폴더)에서 시작해 .claude/agents/가 등록되지 않아, 범용 에이전트(model: sonnet)가 .claude/agents/fact-checker.md를 읽고 그 정의대로 수행함.
- 이 파일은 하위 에이전트의 최종 보고를 작성 세션이 저장한 것임.

요약
- 필수 2건: 거부된 도구 호출 뒤 모델의 행동을 단정한 문장, 표 1-2의 "거쳐서만".
- 권장 10건: 규칙 문서 이름, 인용 누락, 캡션 표기 등.
- 나머지 요청 항목은 모두 1차 문서로 일치를 확인했습니다.
- OpenAI 글 두 편은 이번에도 HTTP 403이라 미확인으로 두었고 문장 변경을 제안하지 않습니다.
- 인용 키 17종은 모두 research/bibliography.json에 있습니다.

## 판정 표

| # | 심각도 | 위치 | 사실 문장(앞부분) | 판정 | 근거(주소, 확인 위치, 확인 날짜) | 제안 |
|---|---|---|---|---|---|---|
| 1 | 필수 | 에이전트 루프 절, 거부 문단 | "모델은 그 메시지를 읽고 다른 방법을 찾거나, 진행할 수 없다고 보고합니다" | 불일치(단정) | https://code.claude.com/docs/en/agent-sdk/agent-loop, Tool permissions 절: "Claude receives a rejection message as the tool result and typically attempts a different approach or reports that it couldn't proceed", 2026-10-23. 이전 원고의 "대개"를 뺀 것. 원문은 일반적 경향(플레이북 7.2) | "모델은 대개 그 메시지를 읽고 …"로 되돌림 |
| 2 | 필수 | 표 1-2, 외부 실행 환경 행 기능적 제약 | "하네스가 실행한 도구를 거쳐서만 변경됨" | 범위 초과 | 대상에 사용자, 네트워크, 기타 외부 서비스가 들어가 에이전트와 무관하게 바뀜. Anthropic 서버가 실행하는 도구도 있음(how-tool-use-works, Server-executed tools). 2026-10-23 | "에이전트가 일으키는 변경은 하네스가 실행한 도구를 거침"으로 주어를 좁힘. 그림 1-1 캡션의 "모든 실행은 하네스를 거침"도 맞춤 |
| 3 | 권장 | 한 요청 절, 표 1-9 | "규칙 문서는 … Claude Code에서는 CLAUDE.md, Codex에서는 AGENTS.md" | 일치(불완전) | Codex: https://learn.chatgpt.com/docs/agent-configuration/agents-md "Codex reads AGENTS.md files before doing any work". Claude Code: https://code.claude.com/docs/en/memory, 작업 위치와 상위에 CLAUDE.md가 없으면 AGENTS.md를 읽음(v2.1.277 이상, 둘 다 있으면 CLAUDE.md만). 2026-10-23 | 대응은 맞음. AGENTS.md만 있는 저장소의 동작을 한 줄 더할지 작가 결정 |
| 4 | 권장 | 모델만으로 할 수 없는 일, 실행 항목 | "웹 검색처럼 Anthropic 서버가 실행하는 도구도 있습니다" | 일치(인용 없음) | how-tool-use-works, Server-executed tools 절(web_search, web_fetch, code_execution, tool_search), 2026-10-23 | 문장 끝에 tool-use-how 인용 |
| 5 | 권장 | 그림 1-1 캡션, 표 1-1 실행 행 | "모델과 외부 실행 환경 사이의 모든 실행은 하네스를 거침" | 일치(범위 좁힘 필요) | 4와 같은 문서. 서버 실행 도구는 Anthropic 서버가 실행 | 조건을 붙이거나 예외를 캡션 밖에 |
| 6 | 일치 | 기억 항목 | "Anthropic의 메시지 API는 상태를 저장하지 않아 …" | 일치 | https://platform.claude.com/docs/en/build-with-claude/working-with-messages "The Messages API is stateless …", 주체 Anthropic도 맞음 | 변경 없음 |
| 7 | 일치 | 기억 항목에서 도구 사용 절차 문장 삭제 | (삭제된 문장) | 일치(범위 변경 없음) | 남은 근거(messages-api)가 더 일반적인 문장. 같은 인용은 앞 문단에 남음 | 변경 없음 |
| 8 | 권장 | 기억 항목 | "채팅에서 앞의 대화를 기억하는 것처럼 보이는 것은 …" | 일치(범위 넓음) | messages-api 문서는 API 수준만 말함. 채팅 제품 전체의 기억 방식은 확인되지 않음 | "API를 직접 쓰는 프로그램에서는"처럼 범위를 밝힘 |
| 9 | 일치 | API 문서, 도구 실패 반환 | 모델과 프로그램의 역할 구분, 오류 내용 반환 | 일치 | how-tool-use-works "The model never runs anything on its own …", handle-tool-calls is_error(S27) | 변경 없음 |
| 10 | 일치 | 다섯 구성 요소, 역할 | "실행 장치의 컨텍스트 관리가 규칙 문서를 모델의 입력에 포함합니다" | 일치 | glossary CLAUDE.md 항목 "loaded at the start of every session …", how-claude-code-works, Codex agents-md "concatenates them into the prompt" | 변경 없음 |
| 11 | 권장 | 다섯 구성 요소, 검증 | "자동 검사로 정하고, 실행 장치가 정해진 시점에 그 검사를 실행합니다" | 일치(조건부) | hooks: Stop, exit 2. 훅 형태의 검사에 한함. CI와 사람의 검토는 루프 밖. Hook handler는 command 외에 HTTP, MCP tool, prompt, subagent도 가능 | 조건을 붙임. 훅 정의 "명령"도 느슨히 |
| 12 | 일치 | 다섯 구성 요소, 도구, 권한, 기록 | "권한 설정에 적고, 실행 장치의 권한 확인이 …" | 일치 | permissions "Permission rules are enforced by Claude Code, not by the model" | 변경 없음 |
| 13 | 일치 | 표 1-3 컨텍스트 구성, 판단과 응답 | | 일치 | how-claude-code-works "When context fills up", agent-loop | 변경 없음 |
| 14 | 일치 | 표 1-3 권한 확인 | "명령 문장으로 판정해 다르게 작성한 명령은 거부하지 못함" | 일치 | permissions, What a Bash rule doesn't match | 변경 없음 |
| 15 | 권장 | 표 1-3 도구 실행 | "… 격리 환경으로만 제한" | 일치(단정 "만") | permissions: OS 수준 차단은 sandbox, PreToolUse 훅도 대안(명령 문장만 봄) | "격리 환경이 아니면 막지 못함"처럼 |
| 16 | 일치 | 표 1-3 완료 기준 확인, 최종 응답 | | 일치 | hooks Exit code 절, agent-loop "Without limits …" | 변경 없음 |
| 17 | 일치 | 표 1-2 모델, 실행 장치, 설정 행 | | 일치 | 6, 9, BOOK_SPEC 4절 | 변경 없음 |
| 18 | 일치 | 표 1-6 | | 일치(책의 정의) | | 19 참조 |
| 19 | 권장 | 표 1-6 컨텍스트 행 | 제어 주체 "팀" | 내부 불일치 | 본문은 시스템 프롬프트를 "제품이 미리 포함"한다고 씀. glossary System prompt 항목 | "제품과 팀"처럼 주체를 나눔. 하네스 행도 실행 장치는 제품 |
| 20 | 일치 | 표 1-8 | 일곱 행 | 일치 | how-claude-code-works "Put persistent rules in CLAUDE.md …", agent-loop compaction | 변경 없음 |
| 21 | 권장 | 에이전트 루프 절 첫 문단과 완료 기준 문단 | "실행 루프를 정리하면 다음 다섯 단계" / "다섯 단계에 더한 정리" | 일치(설명 불완전) | agent-loop 단계: Receive prompt, Evaluate and respond, Execute tools, Repeat, Return result. 권한 확인은 별도 단계가 아님 | 권한 확인을 별도 단계로 나눈 것도 정리라고 밝힘 |
| 22 | 일치 | 턴, 상한, 종료 사유 | | 일치 | agent-loop Turns and budget, Handle the result, 용어집 Turn | 변경 없음 |
| 23 | 일치 | Stop 훅 연속 차단 | | 일치 | hooks stop_hook_active, 8회 연속 상한 | 변경 없음 |
| 24 | 일치 | 권한 모드 | "금지 규칙에 맞은 호출은 어느 권한 모드에서도 거부" | 일치 | permission-modes "Deny rules block in every mode …" | 변경 없음 |
| 25 | 일치 | 한 요청 절 3번 | | 일치 | permission-modes(-p, SDK는 v2.1.302 이상 Manual) | 변경 없음 |
| 26 | 일치 | 금지 규칙의 한계 | cat, sed, grep -r, 스크립트 | 일치 | permissions Read and Edit 절 | 변경 없음 |
| 27 | 일치 | 세션 기록 | | 일치 | how-claude-code-works, Work with sessions(JSONL) | 변경 없음 |
| 28 | 일치 | API로 루프를 직접 작성 | | 일치 | messages-api 상단 표 | 변경 없음 |
| 29 | 권장 | 외부 실행 환경 문단 | "도구는 … 기본 도구와 MCP로 연결한 도구로 나뉩니다" | 일치(분류 불완전) | agent-loop Tool execution: custom tool handlers도 있음 | "대표적으로"로 완화하거나 사용자 정의 도구를 더함 |
| 30 | 일치 | Claude Code 용어집 하네스 | | 일치 | glossary, Agentic harness | 변경 없음 |
| 31 | 일치 | Hashimoto 글 | | 일치 | mitchellh.com Step 5, 2026-02-05 | 변경 없음 |
| 32 | 참고 | Codex 글, 하네스 엔지니어링 글의 수치 | | 미확인 | openai.com 두 글 HTTP 403(2026-10-23) | 문장 변경 없음, Q-040, Q-090 유지 |
| 33 | 참고 | ReAct | | 일치(초록 범위) | S11 | 변경 없음 |
| 34 | 참고 | "Claude Code의 컨텍스트 엔지니어링 글" | | 일치(주체 표기는 작가 확정) | BOOK_SPEC 7절, Q-039, Q-101 | 지적하지 않음 |
| 35 | 권장 | 표 1-9 캡션 | "… Claude Code의 명령으로, … Agent SDK의 실행 결과로 확인함" | 표기 위반 | BOOK_SPEC 7절: 캡션에는 제품명을 쓰지 않음 | 일반 용어로 |
| 36 | 일치 | 표 1-9 /context | | 일치(조건) | 실행 출력. 규칙 문서(Memory files) 줄은 파일이 있을 때만 | 변경 없음 |
| 37 | 일치 | 표 1-9 /permissions | | 일치(문서) | 비대화형 실행 불가, commands 문서 | 변경 없음 |
| 38 | 일치 | 표 1-9 /usage | | 일치 | costs 문서, 구독 계정 실행 출력 | 변경 없음 |
| 39 | 일치 | 표 1-9 종료 사유 | | 일치 | agent-loop Handle the result | 변경 없음 |
| 40 | 참고 | 73차례 검수 | | 미확인(작가 경험 수치) | Q-064 | 변경 없음 |
| 41 | 참고 | 하네스의 일반 뜻 | | 미확인(일반 상식) | | 변경 없음 |
| 42 | 참고 | 검증 항목 | "작업한 모델의 완료 보고만으로는 충분하지 않아 …" | 일치(인용 없음) | S12, S13 | long-running-harness 인용 검토 |

## research/ 추가 기록 문안
research/ch01-sources.md 끝의 "2026-10-23 ch01 기술 감수" 절로 옮김(S39~S43, 재확인, 실행 기록, 열람 실패).

## 실행 출력 원문(발췌)
```
$ claude --version
2.1.302 (Claude Code)

$ claude -p "/context"
## Context Usage
**Model:** claude-opus-5-5
**Tokens:** 31.4k / 1m (3%)
### Estimated usage by category
| Category | Tokens | Percentage |
| System prompt | 2.7k | 0.3% |
| System tools | 22k | 2.2% |
| MCP tools | 627 | 0.1% |
| MCP server instructions | 1.4k | 0.1% |
| MCP tools (deferred) | 74.2k | 7.4% |
| System tools (deferred) | 20.2k | 2.0% |
| Skills | 4.7k | 0.5% |
| Messages | 10 | 0.0% |
| Free space | 935.6k | 93.6% |
| Autocompact buffer | 33k | 3.3% |

$ claude -p "/context all"
(같은 구성, Tokens 33.2k / 1m)

$ claude -p "/permissions"
/permissions isn't available in this environment.

$ claude -p "/usage"
You are currently using your subscription to power your Claude Code usage
Current session: 86% used · resets Oct 23, 6:50pm (Asia/Seoul)
Current week (all models): 38% used · resets Oct 29, 4am (Asia/Seoul)
```

## 장별 점검 질문 10개(플레이북 20.4)
| # | 질문 | 짧은 답 |
|---|---|---|
| 1 | 개념 | 대체로 예. 규칙 문서 이름은 3에서 보충 여지 |
| 2 | 분류 | 예. 표 1-6 컨텍스트 제어 주체(19), 도구 분류(29) |
| 3 | 논리 | 예. 1은 근거보다 단정이 강함. 완료 보고 문장 인용 없음(42) |
| 4 | 범위 | 대체로 예. 2, 8 |
| 5 | 절차 | 예. 권한 확인 단계는 재구성(21) |
| 6 | 책임 | 예. 검증 실행 범위는 훅에 한함(11) |
| 7 | 검증 | 예. Codex 두 글 미확인(32) |
| 8 | 일관성 | 대체로 예. 2, 5, 19, 35 |
| 9 | 출처 | 예. 누락 인용 4, 42. 미확인 수치 32, 40 |
| 10 | 편집 한계 | 예. 작가 확인 Q-040, Q-090, Q-064, Q-039, Q-101, 3 |

필수 2, 권장 10, 참고 5, 확인한 사실 문장 약 110개
