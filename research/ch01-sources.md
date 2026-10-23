# Chapter 1 사실 확인 기록

확인일: 2026-10-04. 원문을 직접 열어 확인한 내용만 적습니다. 문장은 원문 번역이 아니라 요약입니다.

## S1. Anthropic, Effective context engineering for AI agents

- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- 게시일: 2025-09-29(페이지 표기 "Published Sep 29, 2025"), 수정 2026-01-06(메타데이터)
- 작성: Anthropic Applied AI 팀
- 1장에서 사용한 내용
  - 컨텍스트: 모델이 응답을 생성할 때 포함되는 토큰의 집합
  - 프롬프트 엔지니어링: 최적의 결과를 위해 LLM 지시문을 작성하고 구성하는 방법
  - 컨텍스트 엔지니어링: 추론 중 최적의 토큰(정보) 집합을 선별하고 유지하는 전략의 묶음, 프롬프트 밖의 정보 포함
  - Anthropic은 컨텍스트 엔지니어링을 프롬프트 엔지니어링이 자연스럽게 발전한 단계로 봄
  - 프롬프트 작성은 한 번의 작업이고, 컨텍스트 선별은 모델에 무엇을 넘길지 정할 때마다 반복됨
  - 컨텍스트는 한정된 자원. 토큰이 늘수록 정보를 정확히 찾아내는 능력이 떨어지는 현상(context rot)을 언급
  - 에이전트의 정의: LLM이 반복 루프 안에서 스스로 도구를 사용하는 것

## S2. OpenAI, Harness engineering: leveraging Codex in an agent-first world

- URL: https://openai.com/index/harness-engineering/
- 게시일: 2026-02-11, 작성자 Ryan Lopopolo
- 1장에서 사용한 내용
  - 5개월 동안 사람이 직접 작성한 코드 없이 내부 베타 제품을 개발(애플리케이션, 테스트, CI 설정, 문서 모두 Codex가 작성)
  - 약 100만 줄, 약 1,500개 풀 리퀘스트, 처음 엔지니어 3명에서 7명으로 늘어남(OpenAI 발표 수치)
  - 엔지니어의 주된 일이 코드 작성에서 환경 설계, 의도 명시, 피드백 루프 구축으로 이동
  - 초기 진행이 느렸던 이유를 Codex의 능력이 아니라 환경이 충분히 정의되지 않았기 때문이라고 설명
  - 실패하면 "어떤 능력이 누락되었는가"를 묻고, 그 능력을 에이전트가 읽을 수 있고 강제되는 형태로 추가
  - 큰 AGENTS.md 하나는 실패, 약 100줄의 짧은 AGENTS.md가 세부 문서의 위치를 안내하는 방식으로 전환
  - 에이전트가 실행 중 접근할 수 없는 지식(문서 도구, 채팅, 사람의 머릿속)은 에이전트에게 없는 것과 마찬가지라고 설명
  - 문서 구조는 전용 lint와 CI로 기계적으로 검사
  - 사람은 작업 우선순위를 정하고, 사용자 의견을 수용 기준으로 옮기고, 결과를 검증

## 작가 경험(지난 책)

- 출처: NEW_BOOK_PLAYBOOK.md 0장(검수 누적 73차, 반복 실수의 lint 규칙화, 결정 기록, 작성과 검수 역할 분리)

---

# 2026-10-19 재확인과 추가 조사(1장 재작성 계획, researcher)

확인일: 2026-10-19. OpenAI 글 두 편(S3, S4)은 원문 열람이 막혀(HTTP 403) 이번에 1차 확인하지 못했다. 작가가 브라우저로 직접 확인해야 한다.

## S1, S2 재확인
- S1: 바뀐 점 없음. 저자 Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, Jeremy Hadfield(Applied AI 팀). 상세는 S9.
- S2: 이번 재확인 불가(403). 게시일 2026-02-11, Ryan Lopopolo, "5개월, 직접 작성한 코드 없음, 약 100만 줄"은 검색 결과 요약으로만 확인. 나머지는 2026-10-04 기록을 유지한다. 2차 요약 사이트(ZenML, theneuron 등)는 수치가 달라 쓰지 않는다.

## S3. OpenAI, Unrolling the Codex agent loop
- URL: https://openai.com/index/unrolling-the-codex-agent-loop/
- 게시일: 2026-01-23(검색 결과 표기, 페이지 직접 확인 못 함), 확인일: 2026-10-19
- 작성: Michael Bolin
- 확인 수준: 원문 열람 실패(403). 아래는 단서이며 1차 확인이 아니다. 원문 확인 전에는 본문에 새로 쓰지 않는다.
  - Codex 하네스가 모든 Codex 경험(CLI, Cloud, VS Code 확장)에 공통인 에이전트 루프와 실행 로직을 제공
  - 한 턴에 수백 번 도구 호출, 컨텍스트 윈도 소진 가능, 컨텍스트 윈도 관리는 에이전트의 책임
  - 미확인: 턴의 정의 원문 표현

## S4. OpenAI, Harness engineering: leveraging Codex in an agent-first world
- URL: https://openai.com/index/harness-engineering/
- 게시일: 2026-02-11, 확인일: 2026-10-19(열람 실패, S2 기록 유지)
- 작성: Ryan Lopopolo
- 실패 표용(2026-10-04 기록 기준): 큰 AGENTS.md 하나는 실패, 약 100줄 안내 문서와 세부 문서로 전환

## S5. Anthropic, How the agent loop works(Agent SDK)
- URL: https://code.claude.com/docs/en/agent-sdk/agent-loop
- 게시일: 표기 없음, 확인일: 2026-10-19
- 작성: Anthropic
- 이 장에서 사용할 내용
  - 루프 단계(페이지 표기): Receive prompt → Evaluate and respond → Execute tools → Repeat → Return result. "권한 확인"은 별도 단계가 아니라 도구 실행 단계에서 허용 규칙, 권한 모드, 훅이 정한다. 원고의 다섯 단계는 이 책의 정리임을 밝히거나 문서 표기에 맞춘다.
  - 턴: 도구 호출이 포함된 모델 출력 → 도구 실행 → 결과 환류의 한 왕복. 도구 호출 없는 응답이면 루프 종료.
  - 상한: max_turns/maxTurns(도구 사용 턴만 셈, 기본 제한 없음), max_budget_usd/maxBudgetUsd(기본 제한 없음, 하위 에이전트 지출 합산, 응답 하나분 초과 가능)
  - 종료 사유(ResultMessage subtype): success, error_max_turns, error_max_budget_usd, error_during_execution, error_max_structured_output_retries
  - "Setting a budget is a good default for production agents"
  - 거부된 도구 호출은 거부 메시지가 도구 결과로 모델에 돌아가고, 모델은 다른 방법을 찾거나 진행 불가를 보고. PreToolUse 훅이 거부해도 같음
  - 결과에 최종 텍스트, usage, total_cost_usd, num_turns, session_id
  - 컨텍스트는 턴 사이에 누적, 한도 근처에서 자동 압축. 초반 지시가 보존되지 않을 수 있어 지속 규칙은 CLAUDE.md에 두라고 안내
  - Claude Code가 쓰는 것과 같은 실행 루프를 SDK로 제공

## S6. Anthropic, Glossary(Claude Code Docs)
- URL: https://code.claude.com/docs/en/glossary
- 게시일: 표기 없음, 확인일: 2026-10-19
- 작성: Anthropic
- 이 장에서 사용할 내용
  - Agentic harness: 언어 모델을 코딩 에이전트로 만드는 도구, 컨텍스트 관리, 실행 환경. "Claude Code is the harness; Claude is the model inside it." 파일 접근, 셸 실행, 권한 게이트, 메모리 로딩, 루프를 제공. 기존 인용과 일치
  - Permission rule: deny → ask → allow 순서, 먼저 맞는 규칙 적용. Hook: 정해진 수명주기 지점에서 결정적으로 실행
  - Turn: 사용자 메시지부터 응답 종료까지(사이에 도구 호출 여러 번). S5의 턴(도구 왕복 한 번)과 다르다. 본문에서 턴을 쓰면 어느 문서 기준인지 밝힌다

## S7. Anthropic, How Claude Code works
- URL: https://code.claude.com/docs/en/how-claude-code-works
- 게시일: 표기 없음, 확인일: 2026-10-19
- 작성: Anthropic
- 이 장에서 사용할 내용
  - "Claude Code is the layer around the model that provides the tools and manages the context the model sees. This surrounding layer is what the term agentic harness refers to."
  - 루프 3단계: gather context, take action, verify results
  - 대화는 ~/.claude/projects/ 아래 JSONL로 저장, 새 세션은 이전 기록 없이 시작하므로 지속 지시는 CLAUDE.md에
  - /context로 컨텍스트 사용량 확인. 체크포인트는 파일 변경만 되돌리고 원격 변경은 못 되돌림

## S8. Anthropic, Tool use / How tool use works / Handle tool calls / Bash tool(Claude Platform Docs)
- URL: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview , .../how-tool-use-works , .../handle-tool-calls , .../bash-tool
- 게시일: 표기 없음, 확인일: 2026-10-19
- 작성: Anthropic
- 이 장에서 사용할 내용
  - 클라이언트 도구는 호출한 애플리케이션이 실행하고 tool_result로 돌려줌. "The model never runs anything on its own."
  - 애플리케이션이 stop_reason이 tool_use인 동안 루프를 구동
  - 실패 시 tool_result에 오류 메시지와 is_error: true
  - bash 도구: "The API is stateless. Nothing about your shell session travels between requests"(셸 세션에 대한 문장)
  - 대화를 이어 가려면 호출한 쪽이 이전 메시지를 다시 보냄(how-tool-use-works). 대화 상태 일반에 대한 "stateless" 문장은 찾지 못함(미확인 3)

## S9. Anthropic, Effective context engineering for AI agents
- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- 게시일: 2025-09-29, 확인일: 2026-10-19
- 작성: Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, Jeremy Hadfield
- 이 장에서 사용할 내용: 정의 세 가지(S1과 같음), context rot, 맺음의 "even as models improve ... will remain central"(컨텍스트를 precious, finite resource로 다루는 일)

## S10. Anthropic, Building effective agents
- URL: https://www.anthropic.com/research/building-effective-agents
- 게시일: 2024-12-19, 확인일: 2026-10-19
- 작성: Erik Schluntz, Barry Zhang(상단 byline은 직접 재확인 필요)
- 이 장에서 사용할 내용: 워크플로는 predefined code paths로 조율, 에이전트는 LLM이 프로세스와 도구 사용을 스스로 지휘. 참고 자료 날짜를 "2024년 12월 19일"로 구체화 가능

## S11. Yao 외, ReAct
- URL: https://arxiv.org/abs/2210.03629 , https://iclr.cc/virtual/2023/poster/11003
- 게시일: arXiv v1 2022-10-06(v3 2023-03-10, ICLR camera ready), 확인일: 2026-10-19
- 작성: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- 이 장에서 사용할 내용: 2022년 공개, ICLR 2023. 추론과 행동을 번갈아 수행

## S12. Anthropic, Effective harnesses for long-running agents
- URL: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- 게시일: 2025-11-26, 확인일: 2026-10-19
- 작성: Justin Young
- 이 장에서 사용할 내용
  - 에이전트는 세션 단위로 일하고 새 세션은 이전 기억이 없음. 압축만으로는 부족
  - 출처가 설명한 실패: ① 한 번에 전체를 만들려다 컨텍스트가 바닥나 반쯤 만든 기능을 문서 없이 남김 ② 나중 세션이 진행 흔적만 보고 끝났다고 선언 ③ 기능을 너무 일찍 완료로 표시(명시하지 않으면 종단 간 테스트 생략)
  - 장치: 초기화 에이전트(init.sh, 진행 기록, 첫 커밋), 한 기능씩 진행하는 코딩 에이전트, 기능 목록 JSON(passes 필드만 수정), 진행 파일, git 커밋, 세션 시작 루틴

## S13. Anthropic, Harness design for long-running application development
- URL: https://www.anthropic.com/engineering/harness-design-long-running-apps
- 게시일: 2026-03-24(페이지 안내 기준), 확인일: 2026-10-19
- 작성: Prithvi Rajasekaran
- 이 장에서 사용할 내용(반대 의견, 실패 표)
  - 하네스의 각 구성 요소는 "모델이 혼자 못 하는 일"에 대한 가정이고, 모델이 발전하면 그 가정이 quickly go stale할 수 있어 새 모델마다 다시 시험. 스프린트 구조는 뺐지만 계획 에이전트와 평가 에이전트는 남김
  - "the space of interesting harness combinations doesn't shrink as models improve." 하네스가 사라진다가 아니라 필요한 조합이 바뀐다는 취지
  - 실패: 컨텍스트가 차면 일관성 저하, context anxiety(서둘러 마무리), 자기 결과를 후하게 평가, QA 에이전트가 문제를 찾고도 승인하거나 얕게 시험

## S14. Anthropic, How we built Claude Code auto mode
- URL: https://www.anthropic.com/engineering/claude-code-auto-mode
- 게시일: 2026-03-25(페이지 안내 기준), 확인일: 2026-10-19
- 작성: John Hughes
- 이 장에서 사용할 내용(권한)
  - 사용자가 권한 확인의 93%를 승인(approval fatigue)
  - 내부 사고 기록의 과잉 행동: 범위 확대(원격 브랜치 일괄 삭제), 자격 증명 탐색, 추정한 매개변수로 삭제 시도, 외부 서비스로 공유, 안전 확인 우회

## S15. Anthropic, Debug your configuration(Claude Code Docs)
- URL: https://code.claude.com/docs/en/debug-your-config
- 게시일: 표기 없음, 확인일: 2026-10-19
- 작성: Anthropic
- 이 장에서 사용할 내용(확인 방법)
  - /context: 컨텍스트를 차지하는 항목을 범주별로(시스템 프롬프트, 도구, MCP 도구, 하위 에이전트와 출처, 메모리 파일, 스킬, 대화). CLAUDE.md가 로드됐는지 먼저 확인하라고 안내
  - /memory, /skills, /hooks, /mcp, /permissions, /doctor, /debug, /status(활성 설정 출처)
  - 설정 병합: 관리형이 먼저, 나머지는 local > project > user
  - 훅이 안 불리면 /hooks로 확인, claude --debug로 이벤트, matcher, 종료 코드와 출력 확인
  - claude --safe-mode: CLAUDE.md, 스킬, 플러그인, 훅, MCP 등을 끄고 시작
  - CLAUDE.md는 지침이고 권한과 훅은 모델의 결정과 무관하게 강제. 반드시 막을 일은 후자로
  - Bash(rm *) 거부 규칙은 문자열 일치라 /bin/rm, find -delete를 막지 못함. PreToolUse 훅이나 샌드박스 권장

## S16. Anthropic, Commands(Claude Code Docs)
- URL: https://code.claude.com/docs/en/commands
- 게시일: 표기 없음, 확인일: 2026-10-19
- 작성: Anthropic
- 이 장에서 사용할 내용
  - /context [all], /permissions(allow, ask, deny 규칙 관리), /hooks(읽기 전용), /memory, /status, /doctor, /debug, /usage(= /cost), /resume, /rewind, /compact
  - /agents는 현재 안내만 출력(대화형 관리 화면은 v2.1.197 이전). 하위 에이전트 목록은 /context의 하위 에이전트 항목으로 확인

## S17. Anthropic, Hooks reference(Claude Code Docs)
- URL: https://code.claude.com/docs/en/hooks
- 게시일: 표기 없음, 확인일: 2026-10-19(앞 200,000자까지 읽음)
- 작성: Anthropic
- 이 장에서 사용할 내용
  - 종료 코드: 0 성공, 2 차단 오류(이유는 stderr), 그 외 비차단. 정책 강제는 exit 2
  - PreToolUse + exit 2: 도구 호출 차단, stderr가 도구 오류로 전달
  - Stop + exit 2: 멈추지 못하게 하고 계속. stderr가 계속해야 하는 이유로 전달
  - stop_hook_active: 이미 stop 훅 때문에 계속 중이면 true. 연속 차단 상한 8회(도구 호출 시 초기화), CLAUDE_CODE_STOP_HOOK_BLOCK_CAP
  - PostToolUse + exit 2: 이미 실행된 뒤라 차단 불가, stderr만 전달
  - /hooks는 훅 출처(user, project, local, plugin, session)와 명령을 보여 줌
  - 참고(이 저장소 시험): 2026-10-19 작동 시험에서 Stop 훅의 exit 2가 "Hook script appears to be missing"으로 분류되어 막지 못한 사례(reviews/agents/2026-10-19-harness-test.md, F-13)

## S18. Anthropic, Configure permissions / Settings files and precedence(Claude Code Docs)
- URL: https://code.claude.com/docs/en/permissions , https://code.claude.com/docs/en/settings
- 게시일: 표기 없음, 확인일: 2026-10-19
- 작성: Anthropic
- 이 장에서 사용할 내용
  - 평가 순서 deny → ask → allow, 먼저 맞는 규칙. 어느 범위의 deny든 allow보다 먼저
  - "Permission rules are enforced by Claude Code, not by the model." 프롬프트나 CLAUDE.md는 허용 여부를 바꾸지 못함
  - /permissions: 규칙과 규칙이 나온 settings.json 파일
  - 우선순위: 관리형 > 명령줄 --settings > .claude/settings.local.json > .claude/settings.json > ~/.claude/settings.json. 목록 키(permissions.allow 등)는 합쳐짐
  - 권한 모드: default, acceptEdits, plan, auto, dontAsk, bypassPermissions. v2.1.283 이상에서 대화형 터미널과 VS Code의 시작 모드는 auto

## S19. Anthropic, Manage sessions(Claude Code Docs)
- URL: https://code.claude.com/docs/en/sessions
- 게시일: 표기 없음, 확인일: 2026-10-19
- 작성: Anthropic
- 이 장에서 사용할 내용
  - 대화 기록: ~/.claude/projects/<project>/<session-id>.jsonl. 형식은 내부용이라 파싱하지 말고 /export나 claude -p --output-format json 사용
  - 보존 기본 30일(cleanupPeriodDays)

## 미확인
1. S3 원문(턴 정의, 수백 번 도구 호출, 공통 루프 문장, 게시일): 403. 작가 직접 확인 필요
2. S4 이번 재확인(약 1,500 PR, 3명→7명, AGENTS.md 실패): 403. 2026-10-04 기록에만 의존
3. "API가 요청 사이 대화 상태를 유지하지 않는다"는 일반 문장: bash-tool 페이지의 셸 세션 문장만 확인
4. Building effective agents 상단 byline
5. 훅 문서 마지막 약 73,000자 미열람(결론 영향 없음)
6. 하위 에이전트 목록 전용 명령: 현행 문서에 없음. /context로 확인
7. "모델이 좋아지면 하네스는 필요 없다"를 직접 반박한 문장: 없음. S13이 "필요한 조합이 바뀐다"로 간접 답

## 근거가 부족한 곳
- "같은 모델로도 결과가 달라지는 원인은 모델 바깥의 설계"를 같은 모델에서 하네스만 바꾼 정량 비교로 뒷받침하는 1차 출처는 확인하지 못했다. 주장은 "팀이 바꿀 수 있는 것은 모델 바깥"으로 좁히는 편이 근거에 맞다.
- 이 책의 정의(실행 장치 + 설정)는 Anthropic 용어집 정의와 같은 문장이 아니다. 출처의 정의와 이 책의 정의를 구분해 쓴다(D-055).
- 실패 표의 층 분류는 출처가 직접 한 분류가 아니라 출처 설명을 근거로 한 제안이다(확신 중간).
- 참고 자료 표기: "Glossary, How Claude Code works"는 두 항목으로 나누고, "How the agent loop works"는 Agent SDK 문서로 표기한다.

# 2026-10-20 v1.0 보강 확인(fact-checker)

확인일: 2026-10-20. 원문을 직접 열어 확인한 내용만 적는다. 문장은 요약이다.

## S20. Anthropic, Commands(Claude Code Docs)
- URL: https://code.claude.com/docs/en/commands
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic
- 1장 확인 방법 절(표 1-9)에서 사용한 내용
  - /context: 컨텍스트 사용량을 보여 줌. 전체화면 모드에서는 항목별 분류를 접고 `/context all`로 펼침
  - /permissions: allow, ask, deny 규칙을 관리하는 대화 창, 범위별로 규칙을 보여 줌. 별칭 /allowed-tools
  - /usage: 세션 비용, 요금제 사용량 한도, 활동 통계. /cost, /stats는 별칭

## S21. Anthropic, Debug your configuration(Claude Code Docs)
- URL: https://code.claude.com/docs/en/debug-your-config
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic
- 사용한 내용
  - /context 분류 범주: 시스템 프롬프트, 시스템 도구, MCP 도구, 하위 에이전트, 메모리 파일, 스킬, 대화 메시지. 하위 폴더의 CLAUDE.md는 시작 때 읽히지 않아 분류에 나타나지 않음
  - CLAUDE.md는 지침, 권한과 훅은 강제

## S22. Anthropic, Manage costs effectively(Claude Code Docs)
- URL: https://code.claude.com/docs/en/costs
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic
- 사용한 내용
  - /usage의 Session 블록은 현재 세션의 토큰 사용량을 보여 주며 API 사용자용. 구독 사용자는 같은 화면에서 요금제 사용량을 봄
  - 금액은 토큰 수에 정가를 곱한 추정치. 실제 청구는 Claude Console의 Usage 페이지 기준

## S5 재확인(Agent SDK, How the agent loop works), 2026-10-20
- ResultMessage subtype: success, error_max_turns, error_max_budget_usd, error_during_execution 등
- 모든 subtype에 total_cost_usd, usage, num_turns, session_id 포함
- max_turns, max_budget_usd 기본값은 제한 없음. 운영 환경에 예산 설정을 권함. 변경 없음

# 2026-10-20 ch01-flow 사실 확인(fact-checker)
확인일: 2026-10-20. 원문을 직접 열어 확인한 내용만 적는다.

## S23. Anthropic, Agent SDK overview(Claude Code Docs)
- URL: https://code.claude.com/docs/en/agent-sdk/overview
- 게시일: 표기 없음, 확인일: 2026-10-20, 작성: Anthropic
- 사용한 내용: Agent SDK는 Claude Code를 구동하는 것과 같은 도구, 에이전트 루프, 컨텍스트 관리를 Python과 TypeScript로 프로그램에서 쓰게 하는 라이브러리(1장 "Agent SDK" 풀이)

## S5 재확인(Agent SDK, How the agent loop works), 2026-10-20
- 루프 문장: "Without limits, the loop runs until Claude finishes on its own"(조건은 상한 없음, Stop 훅과 무관)
- 거부된 도구 호출: 거부 메시지가 도구 결과로 돌아가고 Claude는 "typically" 다른 방법을 찾거나 진행 불가를 보고
- 루프 5단계 원문 표기는 Receive prompt, Evaluate and respond, Execute tools, Repeat, Return result(권한 확인 단계는 이 책의 정리)
- 상한 강제 동작(하위 에이전트 포함)은 Claude Code v2.1.217 이상

## S17 재확인(Hooks reference), 2026-10-20(앞 200,000자)
- Stop: 응답을 마칠 때 발동, decision "block"(reason 필수) 또는 exit 2로 종료를 막고 계속. 연속 차단 상한 8회, stop_hook_active
- PreToolUse permissionDecision 값: allow, deny, ask, defer

## S24. Anthropic, How tool use works(Claude Platform Docs)
- URL: https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works
- 게시일: 표기 없음, 확인일: 2026-10-20, 작성: Anthropic
- 사용한 내용: "The model never runs anything on its own." 클라이언트 도구는 호출한 애플리케이션이 실행해 tool_result로 돌려줌. 도구 결과를 보낼 때 원래 메시지, 어시스턴트 응답, tool_result를 담은 새 요청을 보냄(1장 "기억" 항목). 대화 상태 일반의 "stateless" 문장은 없음(S8 미확인 3 유지)

## S25. Anthropic, API overview(Claude Platform Docs)
- URL: https://platform.claude.com/docs/en/api/overview
- 확인일: 2026-10-20
- 사용한 내용: Claude API는 Claude 모델에 프로그램으로 접근하게 하는 REST API(1장 "API" 풀이)

## S9 재확인(Effective context engineering), 2026-10-20
- 게시 2025-09-29, 저자 Anthropic Applied AI 팀. 에이전트 정의, "natural progression", "treating context as a precious, finite resource will remain central". 발표 주체는 Anthropic(본문의 "Claude Code" 표기는 Q-039)

## 미확인
- S3(OpenAI Unrolling the Codex agent loop): 2026-10-20 접근 불가(DNS). Codex 턴 정의 원문 미확인 유지

# 2026-10-22 ch01 각주 대조(fact-checker, 1장 정비 PR #69)

확인일: 2026-10-22. 원문을 직접 열어 확인한 내용만 적는다. S8, S24의 인용 "executes"는 현행 문구 "runs"로 정정함.

## S26. Anthropic, How tool use works(Claude Platform Docs) 재확인
- URL: https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works
- 확인일: 2026-10-22, 작성: Anthropic
- 사용한 내용: "The model never runs anything on its own. It emits a structured request, your code (or Anthropic's servers) runs the operation". 4단계: 원래 메시지, 어시스턴트 응답, tool_result를 담은 새 요청. 대화 상태 일반의 stateless 문장은 없음(미확인 3 유지, 본문 "기억" 항목은 도구 사용 절차로 한정)

## S27. Anthropic, Handle tool calls(Claude Platform Docs)
- URL: https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls
- 확인일: 2026-10-22, 작성: Anthropic
- 사용한 내용: "Handling errors with is_error": 도구 실행 오류 시 content에 오류 메시지와 "is_error": true(각주 3)

## S28. Anthropic, Glossary(Claude Platform Docs)
- URL: https://platform.claude.com/docs/en/about-claude/glossary
- 확인일: 2026-10-22, 작성: Anthropic
- 사용한 내용: Tokens: 언어 모델의 가장 작은 개별 단위로 단어, 부분 단어, 문자, 바이트에 대응할 수 있고, 텍스트는 토큰열로 부호화되어 모델이 처리함(각주 1, 본문 "모델이 텍스트를 나누어 처리하는 단위"). Context window: 모델이 되돌아보고 참고할 수 있는 텍스트의 양

## S5, S6, S17, S20 재확인(2026-10-22)
- S6 Glossary(Claude Code Docs): Agentic harness 문구 변경 없음. Turn: 사용자 메시지부터 Claude 응답 종료까지(본문 Codex 문단에 반영)
- S5 Agent SDK(https://code.claude.com/docs/en/agent-sdk/agent-loop): 턴은 도구 호출 왕복 한 번("Each full cycle is one turn"), max_turns와 max_budget_usd 기본 No limit, "Setting a budget is a good default for production agents", 종료 사유 success, error_max_turns, error_max_budget_usd, error_during_execution, 결과에 비용, 사용량, 세션 ID, 거부된 호출은 거부 메시지가 도구 결과로 돌아감
- S17 Hooks reference(앞 100,000자): Stop "When Claude finishes responding", 종료 코드 2 "Prevents Claude from stopping", decision "block"과 reason. Stop 절 본문과 연속 차단 상한은 미확인
- S20 Commands: /context [all], /permissions, /usage(/cost, /stats 별칭)

## S9, S10, S11, S12 재확인(2026-10-22)
- S9: 저자 Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, Jeremy Hadfield, 2025-09-29. 에이전트 정의, "natural progression", context rot, "treating context as a precious, finite resource will remain central"
- S10: December 19, 2024, workflows "predefined code paths", agents "dynamically direct their own processes and tool usage". 상단 byline 성 표기는 직접 확인 못 함(감사 문구 "Erik S. and Barry Zhang")
- S11: arXiv 2210.03629 v1 2022-10-06, ICLR 2023 포스터. 초록은 문맥 내 예시 한두 개 프롬프팅, HotpotQA, Fever, ALFWorld, WebShop(표 1-2 "논문이 평가한 과제")
- S12: Justin Young, 2025-11-26. 하네스를 따로 정의하지 않고 반복 세션을 돌리는 주변 체계의 뜻으로 사용, Claude Agent SDK를 "a powerful, general-purpose agent harness adept at coding"으로 부름(본문을 "주변 체계라는 뜻으로 하네스라는 말을 사용"으로 고침)

## 열람 실패(2026-10-22)
- OpenAI, Unrolling the Codex agent loop: HTTP 403. 검색 결과 요약으로만: Michael Bolin, 2026-01-23, 하네스가 Codex 제품(CLI, Cloud, VS Code 확장)에 공통인 루프 제공. 턴 정의, 수백 번의 도구 호출, 컨텍스트 소진은 미확인(Q-040, Q-090)
- OpenAI, Harness engineering: HTTP 403. 검색 결과 요약으로만: Ryan Lopopolo, 2026-02-11, 약 5개월, 약 100만 줄. 약 1,500개 풀 리퀘스트는 미확인(Q-090)

# 2026-10-22 ch01 기술 감수(fact-checker, 1장 완성본 PR #81)
확인일: 2026-10-22. 원문을 직접 열어 확인한 내용만 적는다.

## S29. Anthropic, Run Claude Code programmatically / CLI reference(Claude Code Docs)
- URL: https://code.claude.com/docs/en/headless , https://code.claude.com/docs/en/cli-reference
- 사용한 내용: claude -p는 "Agent SDK via the CLI". --max-turns(print 모드, 한도 도달 시 오류 종료, 기본 제한 없음), --max-budget-usd(추정 지출, 초과 가능). --output-format json은 result, 세션 ID, total_cost_usd. CLI JSON의 subtype은 미확인(본문은 Agent SDK 결과 메시지로 한정)

## S30. Anthropic, Hooks reference, Stop 절
- URL: https://code.claude.com/docs/en/hooks , 확인일 2026-10-22(앞 200,000자)
- 사용한 내용: Stop은 메인 에이전트가 응답을 마칠 때 실행, 사용자 중단에는 실행 안 됨, 종료 코드 2 또는 decision block, 연속 8회 차단 뒤 종료, 0과 2 외 종료 코드는 비차단

## S31. Anthropic, Manage costs effectively 재확인
- URL: https://code.claude.com/docs/en/costs
- 사용한 내용: /usage Session 블록은 API 사용자용, 금액은 정가 기준 로컬 추정(청구는 Console), 구독 사용자는 요금제 사용량(표 1-9)

## S32. Anthropic, Commands / Debug your configuration 재확인
- /context [all](전체 화면에서 all로 펼침), /permissions(allow, ask, deny, 별칭 /allowed-tools), /usage(별칭 /cost, /stats), 하위 폴더 CLAUDE.md는 시작 때 로드되지 않음

## S33. Glossary(Platform Docs, Claude Code Docs) 재확인
- Platform: Tokens, Context window("amount of text … look back on and reference"), 다음 토큰 예측은 Pretraining 항목. Claude Code: Turn, Session, Agentic harness

## 열람 재시도(2026-10-22)
- OpenAI 두 글 HTTP 403. 검색 발췌: Bolin 2026-01-23 "core agent loop and execution logic that underlies all Codex experiences". Lopopolo 2026-02-11 5개월, 직접 작성 코드 0줄, 약 100만 줄. 1,500 PR, 턴 정의, 수백 번 호출은 미확인(Q-040, Q-090)

# 2026-10-22 ch01 인용 링크 감수(fact-checker, 1장 수정 PR #82)
확인일: 2026-10-22. 원문을 직접 열어 확인한 내용만 적는다. 인용 변경은 이슈 #66 08:39, 08:42로 취소되어, 아래 "→" 가운데 표 1-4 칸만 반영하고 본문 문장(7, 8, 10, 40, 95행)은 PR #81 그대로 둠(Q-106, 다음 인용 지시 때 반영).
- S28 정정, Glossary(Claude Platform Docs) https://platform.claude.com/docs/en/about-claude/glossary : LLM 항목은 "많은 매개변수를 가진 AI 언어 모델, 방대한 텍스트로 학습, 다양한 작업 수행". 다음 단어 예측은 Pretraining 항목("pretrained to predict the next word, given the previous context"). Context window 항목은 "모델이 되돌아보고 참고할 수 있는 텍스트의 양, 학습 코퍼스와 다른 작업 기억". Tokens 항목은 "언어 모델의 가장 작은 단위(단어, 부분 단어, 문자, 바이트)". → 본문 7행은 LLM, 컨텍스트 윈도 정의를 "이 책에서"로 밝히고(용어표 정의 유지), 용어집에는 토큰과 사전 학습의 다음 단어 예측만 귀속(Q-106)
- S27 재확인, Handle tool calls https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls : 실행 오류는 content에 오류 메시지와 "is_error": true를 "돌려줄 수 있다"(is_error는 선택). → 10행 가능형
- S26 재확인, How tool use works https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works : 도구 실행 위치 세 가지(사용자 정의, Anthropic 스키마는 클라이언트 실행, 서버 도구). 대화 상태 일반의 stateless 문장은 없음 → 8행 "이 설명을 바탕으로 이 책은 … 정리"
- S5 재확인, How the agent loop works https://code.claude.com/docs/en/agent-sdk/agent-loop : 턴 = 도구 호출 왕복 한 번, max_turns와 max_budget_usd 기본 제한 없음, 결과 subtype(success, error_max_turns, error_max_budget_usd, error_during_execution, error_max_structured_output_retries), 거부 뒤 "typically attempts a different approach or reports that it couldn't proceed", 사용자 정의 도구가 기본 도구, MCP와 나란히 있음 → 95행 "대개", 표 1-4 외부 실행 환경 칸
- S17/S30 재확인, Hooks reference https://code.claude.com/docs/en/hooks (앞 100,000자): Stop은 응답을 마칠 때 실행, 종료 코드 2나 decision "block"은 멈추지 못하게 하고 대화를 계속. 연속 차단 상한은 이번 열람 범위에서 다시 확인하지 못함(S30 유지)
- S6 재확인, Glossary(Claude Code Docs) https://code.claude.com/docs/en/glossary : Agentic harness "The tools, context management, and execution environment that turn a language model into a capable coding agent. Claude Code is the harness; Claude is the model inside it." Turn 문장 일치. 기본 권한 모드는 버전에 따라 다름 → 40행 "Claude Code 용어집은"
- 열람 실패: https://openai.com/index/unrolling-the-codex-agent-loop/ HTTP 403(턴 정의, 수백 번 도구 호출 미확인, Q-040, Q-090 유지), https://openai.com/index/harness-engineering/ 이번에 열지 않음(약 1,500 PR 미확인)

# 2026-10-22 1장 다시 만들기 사전 확인(fact-checker, 이슈 #66 18:20)
확인일: 2026-10-22. 원문을 직접 열어 확인한 내용만 적는다.

## S34. Mitchell Hashimoto, My AI Adoption Journey
- URL: https://mitchellh.com/writing/my-ai-adoption-journey , 게시일 2026-02-05
- "Step 5: Engineer the Harness" 절: 에이전트가 실수할 때마다 같은 실수를 되풀이하지 않도록 해결책을 설계하는 일을 "harness engineering"이라 부른다고 씀("I don't know if there is a broad industry-accepted term for this yet, but I've grown to calling this 'harness engineering.'"). OpenAI 글(2026-02-11)보다 앞선 1차 사용 예 → 하네스 엔지니어링 절 "먼저 Mitchell Hashimoto의 글은"

## S2/S4 재시도(OpenAI, Harness engineering)
- https://openai.com/index/harness-engineering/ HTTP 403(2026-10-22) 열람 실패. 5개월, 직접 작성 코드 0줄, 약 100만 줄은 검색 요약과 InfoQ(2차)로만 일치. 약 1,500 PR은 2026-10-04 S2 기록 유지. 이 글이 이름이 알려진 계기라는 1차 근거는 찾지 못함 → 첫머리는 "제목으로 쓰였습니다"(Q-108)

## S18 재확인, Configure permissions
- URL: https://code.claude.com/docs/en/permissions
- 평가 순서 deny, ask, allow, 첫 일치 적용, deny가 거부한 호출은 거부로 유지. 권한 모드는 "control how it approves tool calls"(default, acceptEdits, plan, auto, dontAsk, bypassPermissions) → 루프 절 권한 모드 정의(Q-110)
- Read and Edit 절: Read(./.env) 예시. Read와 Edit 금지 규칙은 내장 파일 도구, Claude Code가 인식하는 Bash 파일 명령(cat, head, tail, sed, tee), 리다이렉션 대상에 적용, 파일을 지정하지 않고 읽는 명령(grep -r)이나 스크립트가 직접 파일을 여는 경우는 적용되지 않음, OS 수준 차단은 샌드박스 → 루프 절 금지 규칙 문단, 한 요청 절의 .env 예

## S7 재확인, How Claude Code works
- URL: https://code.claude.com/docs/en/how-claude-code-works
- Work with sessions: 작업하는 동안 각 메시지, 도구 사용, 결과를 ~/.claude/projects/ 아래 파일에 기록 → 루프 절 세션 기록 문장
- When context fills up: 한도에 가까워지면 오래된 도구 출력을 먼저 지우고 필요하면 대화를 요약, 초반의 세부 지시는 사라질 수 있음 → 표 1-1 이전 대화 행, background 표 소개 문단, 표 1-8 긴 작업 행

## S17 재확인, Hooks reference(Stop)
- stop_hook_active는 이미 Stop 훅 때문에 계속하는 중이면 true("Check this value ... to avoid blocking on a condition that will never resolve") → 루프 절 Stop 훅 문장. 연속 8회 뒤 다음 차단 무시(제품 안전장치, 본문에는 쓰지 않음)

## S5 재확인, How the agent loop works
- 거부 메시지가 도구 결과로 돌아가고 "typically" 다른 방법 시도나 진행 불가 보고, max_turns와 max_budget_usd 기본 No limit, 결과 subtype 5종 → 문장 유지

## S36. Codex 소개 문구
- https://github.com/openai/codex : "Codex CLI is a coding agent from OpenAI that runs locally on your computer."(CLI 한정). 제품 전체를 정의한 1차 문구는 미확인 → 본문은 "OpenAI의 Codex"를 코딩 에이전트 제품의 예로만 씀

# 2026-10-22 1장 기술 확인(fact-checker, 1장 다시 만들기 PR #85)
확인일: 2026-10-22. 원문을 직접 열어 확인한 내용만 적는다. 로컬 Claude Code v2.1.302.

## S37. Anthropic, Using the Messages API(Claude Platform Docs)
- URL: https://platform.claude.com/docs/en/build-with-claude/working-with-messages
- "Multiple conversational turns": "The Messages API is stateless, which means that you always send the full conversational history to the API" → background "기억" 항목(미확인 3 해소). 상단 표: Messages API "Best for: Custom agent loops and fine-grained control" → agent-harness "모델의 API로 루프를 직접 작성해 하네스를 만들면"

## S38. Anthropic, Permission modes(Claude Code Docs)
- URL: https://code.claude.com/docs/en/permission-modes
- "Available modes": "Deny rules block in every mode, including bypassPermissions" → loop 권한 모드 문단. "Which mode a session starts in": v2.1.283 이상 대화형 터미널은 auto로 시작, claude -p와 Agent SDK는 v2.1.302 이상에서 모드를 정하지 않으면 Manual이고 승인이 필요한 호출은 거부 → request 3번은 "사람의 확인이 필요한 동작이면"으로 조건화

## S18 재확인(Configure permissions)
- "What a Bash rule doesn't match": Bash(git push *)는 git -C . push …, git -c … push …, git 'push' …을 막지 못함, 규칙은 보안 경계가 아님(대안: 샌드박스, PreToolUse 훅) → loop 금지 규칙 문단. Read 금지 규칙은 grep -r처럼 파일을 지정하지 않는 명령에는 적용되지 않음

## S17 재확인(Hooks reference, Stop)
- stop_hook_active, 연속 8회 차단 뒤 다음 차단 무시(도구 호출 때 초기화, CLAUDE_CODE_STOP_HOOK_BLOCK_CAP), 사용자 중단 때는 실행되지 않음 → loop Stop 훅 문장("연이어 여러 번", 횟수는 쓰지 않음)

## S10 재확인(Building effective agents)
- workflows "predefined code paths", agents "dynamically direct their own processes and tool usage", prompt chaining 예 "Generating Marketing copy, then translating it into a different language" → meanings 워크플로 예. 저자 줄 "Erik S. and Barry Zhang"(성 표기 직접 확인 못 함)

## 실행 기록(R8, 표 1-9), v2.1.302
- /context: claude -p "/context" 실행(Git Bash는 MSYS_NO_PATHCONV=1). System prompt, System tools, MCP tools, Memory files, Skills, Messages, Free space, Autocompact buffer가 항목별 토큰 수로 보임 → 표 1-9 일치
- /usage: 실행 확인. 구독 계정은 요금제 사용량 표시. Manage costs 문서: 금액은 로컬 정가 계산 추정, 청구는 Console → 표 1-9 일치
- /permissions: 비대화형에서 실행 불가("isn't available in this environment"), 문서로 대체(대화 상자가 모든 권한 규칙과 출처 settings.json을 나열)

## 재시도 실패
- OpenAI Harness engineering, Unrolling the Codex agent loop: HTTP 403. 1,500 PR과 네 가지 내용은 2026-10-04 기록(S2)에만 근거(Q-090). Codex 글의 턴 정의 문장은 미확인이라 본문에서 뺌(수백 번 도구 호출과 컨텍스트 소진은 검색 결과의 openai.com 발췌로 일치)
- ReAct: 초록 범위만 확인(S11) → "모델 바깥의 코드가 맡았다" 문장을 빼고 "루프의 원형에 해당"으로 줄임

# 2026-10-23 ch01 기술 감수(fact-checker, 1장 플레이북 시범 PR #103)
확인일: 2026-10-23. 원문을 직접 열어 확인한 내용만 적는다. 로컬 Claude Code v2.1.302. 보고 전문은 reviews/agents/2026-10-23-ch01-fact-checker.md

## S39. Anthropic, Using the Messages API(Claude Platform Docs) 재확인
- URL: https://platform.claude.com/docs/en/build-with-claude/working-with-messages
- 사용한 내용: "The Messages API is stateless, which means that you always send the full conversational history to the API"(background 기억 항목, 범위를 API를 사용하는 프로그램으로 한정). 문서 첫 문장 "Anthropic offers two ways to build with Claude"(주체 표기 Anthropic). 상단 표 Messages API "Best for: Custom agent loops and fine-grained control"

## S40. Anthropic, How tool use works 재확인
- URL: https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works
- 사용한 내용: "The model never runs anything on its own. It emits a structured request, your code (or Anthropic's servers) runs the operation". Server-executed tools 절: web_search, web_fetch, code_execution, tool_search는 Anthropic이 실행(background 실행 항목, 인용 추가)

## S41. Anthropic, How the agent loop works 재확인
- URL: https://code.claude.com/docs/en/agent-sdk/agent-loop
- 사용한 내용: 거부된 도구 호출은 "Claude receives a rejection message as the tool result and typically attempts a different approach or reports that it couldn't proceed"("대개" 유지). 단계 표기는 Receive prompt, Evaluate and respond, Execute tools, Repeat, Return result(권한 확인을 별도 단계로 나눈 것과 완료 기준 확인은 이 책의 정리). 턴, 상한, 기본값, 종료 사유 subtype은 S5와 같음

## S42. Anthropic, How Claude remembers your project / Glossary(Claude Code Docs)
- URL: https://code.claude.com/docs/en/memory , https://code.claude.com/docs/en/glossary
- 사용한 내용: CLAUDE.md는 세션 시작 때 읽히고 시스템 프롬프트 뒤 사용자 메시지로 전달됨. 작업 위치와 상위에 CLAUDE.md가 없으면 AGENTS.md를 프로젝트 지침으로 읽음(v2.1.277 이상, Q-145). Hook handler는 shell command, HTTP endpoint, MCP tool, LLM prompt, subagent(Q-146)

## S43. OpenAI, AGENTS.md 안내
- URL: https://learn.chatgpt.com/docs/agent-configuration/agents-md (https://developers.openai.com/codex/guides/agents-md 에서 308 리디렉션)
- 사용한 내용: "Codex reads AGENTS.md files before doing any work"(규칙 문서 설명의 "Codex에서는 AGENTS.md")

## S17, S18, S20, S22, S34, S38 재확인(2026-10-23)
- S17 Hooks: Stop은 "When Claude finishes responding", exit 2는 "Prevents Claude from stopping", stop_hook_active, 8회 연속 계속 상한 뒤 다음 차단 무시(도구 호출 시 초기화)
- S18 Permissions: What a Bash rule doesn't match(git -C . push 등), Read and Edit 절(cat, head, tail, sed, tee 적용, grep -r과 스크립트 미적용), OS 수준 차단은 sandbox
- S20/S32 Commands: /context [all], /permissions(별칭 /allowed-tools), /usage
- S22/S31 Costs: Session block은 API 사용자용, 금액은 list price 로컬 계산 추정, 구독자는 plan usage
- S34 Hashimoto: Step 5 "I've grown to calling this 'harness engineering.'", 2026-02-05
- S38 Permission modes: "Deny rules block in every mode, including bypassPermissions"

## 실행 기록(표 1-9), v2.1.302, 2026-10-23, 저장소 밖 빈 임시 폴더
- claude -p "/context": System prompt, System tools, MCP tools, Skills, Messages, Free space, Autocompact buffer가 항목별 토큰 수로 나옴. 규칙 문서가 없는 폴더라 Memory files 항목 없음(파일이 있을 때만 나옴)
- claude -p "/context all": 비전체화면에서는 같은 구성. all의 효과는 commands 문서로 확인
- claude -p "/permissions": "/permissions isn't available in this environment." commands 문서로 대체
- claude -p "/usage": 구독 계정, 요금제 사용률(Current session, Current week) 표시

## 열람 실패(2026-10-23)
- https://openai.com/index/unrolling-the-codex-agent-loop/ , https://openai.com/index/harness-engineering/ : HTTP 403. Q-040, Q-090 유지
