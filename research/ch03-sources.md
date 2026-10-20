# Chapter 3 개정 출처(2026-10-20, researcher 조사, 메인 세션 저장)

기존 기록은 research/ch03-10-sources.md. 이 파일은 3장 개정(ch03-write)에서 새로 확인한 것입니다. 원문은 영어이고 인용은 짧게 줄였습니다. Claude Code 문서는 게시일 표기가 없어 확인일만 적습니다.

## C3-1. How the agent loop works (Agent SDK)
- URL: https://code.claude.com/docs/en/agent-sdk/agent-loop, 확인 2026-10-20
- "Without limits, the loop runs until Claude finishes on its own, which is fine for well-scoped tasks but can run long on open-ended prompts"
- 옵션: max_turns(도구 사용 왕복 수), max_budget_usd(추정 비용). 기본값은 둘 다 제한 없음. 상한에 걸리면 결과 subtype이 error_max_turns, error_max_budget_usd
- 쓸 수 있는 문장: 상한이 없으면 열린 요청에서 루프가 오래 실행될 수 있다(지금 원고와 일치). Agent SDK의 옵션이며 대화형 CLI 설정으로 쓰지 않음
- 확신: 높음

## C3-2. Hooks reference
- URL: https://code.claude.com/docs/en/hooks, 확인 2026-10-20
- 종료 코드 2 표: PostToolUse "Can block? No", "Shows stderr to Claude; the tool already ran". PreToolUse는 "Blocks the tool call"
- 쓸 수 있는 문장: PostToolUse 훅이 종료 코드 2로 끝나면 오류 출력이 모델에 전달되지만 이미 실행된 도구를 막지 못함. 막으려면 PreToolUse
- 확신: 높음("되돌리지 못함"은 해석이므로 "막지 못함"으로 씀)

## C3-3. Create custom subagents
- URL: https://code.claude.com/docs/en/sub-agents, 확인 2026-10-20
- name, description 필수, tools 선택. "Inherits every tool available to subagents if omitted." tools는 허용 목록
- 위임: "Claude uses each subagent's description to decide when to delegate tasks." 요청 문장, description, 현재 컨텍스트로 자동 위임하고, 이름을 불러 명시 호출할 수 있음
- 쓸 수 있는 문장: 도구 줄을 생략하면 모든 도구를 물려받으므로, 검토 에이전트는 도구 줄로 읽기 도구만 지정함
- 확신: 높음

## C3-4. Configure permissions
- URL: https://code.claude.com/docs/en/permissions, 확인 2026-10-20
- "Rules are evaluated in order: deny, then ask, then allow."
- "A bare tool name like Bash removes the tool from Claude's context entirely"
- Bash(git push *)는 git push로 시작하는 명령을 거부. 다른 형태의 push는 일치하지 않을 수 있어 규칙만으로는 보안 경계가 아님(샌드박스와 함께, Chapter 9)
- 경로 규칙은 gitignore 방식, ./로 시작하는 경로는 현재 디렉터리 기준
- 쓸 수 있는 문장: 괄호 앞은 도구 이름, 괄호 안은 대상(경로나 명령), *는 아무 문자열
- 확신: 높음

## C3-5. Commands
- URL: https://code.claude.com/docs/en/commands, 확인 2026-10-20
- /permissions: 허용, 확인, 금지 규칙을 범위별로 보고 고치는 대화 상자
- /context: 현재 컨텍스트 사용량을 격자로 보여 줌
- /hooks: "View hook configurations."
- 확신: 높음

## C3-6. How Claude remembers your project (CLAUDE.md)
- URL: https://code.claude.com/docs/en/memory, 확인 2026-10-20
- "Claude treats them as context, not enforced configuration. To block an action regardless of what Claude decides, use a PreToolUse hook instead."
- "there's no guarantee of strict compliance"
- 쓸 수 있는 문장: 규칙 문서의 중단 규칙은 지시이며 강제가 아님
- 확신: 높음

## C3-7. 장의 주장 근거
- Young, Effective harnesses for long-running agents(Anthropic, 2025-11-26) https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents: 높은 수준의 프롬프트만으로는 제품 수준의 웹 앱을 만들지 못하고, 진행 파일과 git 이력이 새 컨텍스트 창에서 상태를 파악하게 함(요약 수준 확인, 확신 중간)
- "요청 문장이 아니라 하네스 항목이 동작을 정한다"를 직접 말하는 1차 출처 문장은 찾지 못함. 장의 주장은 작가의 주장(BOOK_SPEC)이며 C3-1, C3-4, C3-6이 보조 근거
- OpenAI Harness engineering 본문은 403으로 열지 못함(기존 research/ch01-sources.md 참고)

## 확인하지 못한 것
- Hooks reference 뒷부분, sub-agents 뒷부분 일부
- max_turns, max_budget_usd에 대응하는 대화형 CLI 설정

## C3-8. fact-checker 재확인(2026-10-20, ch03 개정 diff)
- Configure permissions: 평가 순서 deny, ask, allow. ./path는 현재 디렉터리 기준. Bash(git push *)는 git push로 시작하는 명령을 거부하고 git -C . push는 일치하지 않음. 도구 이름만 쓴 규칙은 컨텍스트에서 도구를 없앰
- Hooks reference: PostToolUse 종료 코드 2는 막지 못하고 stderr를 보임. PreToolUse 종료 코드 2는 호출을 막음. "Edit|Write" matcher는 정확한 이름 목록. /hooks는 읽기 전용 목록이고 출처를 표시하며 선택하면 전체 명령과 정의 위치를 보여 줌(matcher가 목록에 보이는지는 미확인)
- Create custom subagents: tools 생략 시 모든 도구 상속, tools는 허용 목록
- Commands: /hooks "View hook configurations". /context는 격자와 최적화 제안. 하위 에이전트 항목 표시는 문서에서 찾지 못함(미확인)
- How Claude remembers your project: "context, not enforced configuration", "no guarantee of strict compliance"
- How the agent loop works: max_turns, max_budget_usd 기본값 제한 없음(SDK 옵션)
- 예제 파일 대조: settings.example.json(deny 9, ask 1, allow 6, PostToolUse Edit|Write), CLAUDE.example.md(작업 순서에 reviewer 요청, 수정 범위, 중단 규칙), reviewer.example.md(tools: Read, Grep, Glob), tasks.example.json(작업 5 사람 승인), acceptance/test_cr07.py(5건, 4와 5는 구현 전 통과), RUNLOG.md(실패 3건, exit 1)
- 미확인: /context 화면의 하위 에이전트 항목, /hooks 목록의 matcher 표시. 실습 4 실행 때 화면을 보고 RUNLOG.md에 남길 것
