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

## C3-9. fact-checker 2차 확인(2026-10-20, 흐름 재점검 PR #37, 예제 파일 대조와 문서 재확인)
- Tools reference(https://code.claude.com/docs/en/tools-reference), 확인 2026-10-20: Read는 파일 읽기, Grep은 파일 내용 패턴 검색, Glob은 이름 패턴으로 파일 찾기, Edit는 지정 부분 편집, Write는 파일 생성 또는 덮어쓰기. macOS, Linux, WSL에서는 Glob과 Grep이 기본 도구 집합에 없고, 하위 에이전트가 tools에 적고 Bash를 빼면 그 하위 에이전트에서만 쓸 수 있음
- Hooks reference(https://code.claude.com/docs/en/hooks), 확인 2026-10-20: matcher "Edit|Write"는 두 도구 이름과 정확히 일치(Bash나 NotebookEdit로 한 수정에는 실행 안 됨). PostToolUse 종료 코드 2는 stderr를 Claude에 보이고 도구는 이미 실행됨. 뒷부분 미열람
- How Claude remembers your project(https://code.claude.com/docs/en/memory), 확인 2026-10-20: 각 세션은 새 컨텍스트 창으로 시작, CLAUDE.md는 매 대화 시작에 로드되며 강제 설정이 아닌 컨텍스트
- Configure permissions(https://code.claude.com/docs/en/permissions), 확인 2026-10-20: 이름만 쓴 규칙은 도구를 컨텍스트에서 제거, Edit 규칙은 내장 편집 도구 전체에 적용, Bash 규칙은 명령 문자열 기준이라 우회 가능(샌드박스 병행, 9장)
- Create custom subagents(https://code.claude.com/docs/en/sub-agents), 확인 2026-10-20: 정의 위치 .claude/agents/, tools 생략 시 모든 도구 상속
- Commands(https://code.claude.com/docs/en/commands), 확인 2026-10-20: /hooks는 훅 설정 보기, /permissions는 승인 규칙 설정
- 예제 파일 대조: check.py는 폴더별 실행 건수 > 0이고 실패 0이면 종료 0(건수 0은 실패, 건수 감소는 감지하지 않음. 그래서 본문은 "다른 시험이 통과하는 상태에서 한 건을 지우면"). tasks.example.json 확인 방법은 작업 1 결정 기록 D-012, 작업 2~4 check.py, 작업 5 사람 승인
- 미확인: /hooks 목록의 matcher 표시, /context의 하위 에이전트 항목(실습 4 실행 때 RUNLOG.md에 기록)

## C3-10. fact-checker 3차 확인(2026-10-21, 외부 검토 반영 PR, 브랜치 ch03-external-review)
- Hooks reference(https://code.claude.com/docs/en/hooks), 확인 2026-10-21, 작성 Anthropic(게시일 표기 없음): 종료 코드 2 표에서 PostToolUse는 "Can block? No", "Shows stderr to Claude; the tool already ran". 막으려면 PreToolUse. 본문 95행 마지막 문장과 일치
- How the agent loop works(https://code.claude.com/docs/en/agent-sdk/agent-loop), 확인 2026-10-21, 작성 Anthropic(게시일 표기 없음): 상한이 없으면 범위가 분명한 작업에는 괜찮지만 열린 요청에서는 오래 실행될 수 있음. "Setting a budget is a good default for production agents." max_turns와 max_budget_usd의 기본값은 No limit. 상한 도달 시 subtype error_max_turns, error_max_budget_usd. ch01 91행, ch03 48행과 일치
- CLI reference(https://code.claude.com/docs/en/cli-reference), 확인 2026-10-21, 작성 Anthropic(게시일 표기 없음): --max-turns와 --max-budget-usd는 print mode(-p) 전용이고 기본값은 제한 없음. 대화형 세션 설정으로는 확인하지 못함. C3 "확인하지 못한 것"의 첫째 항목(대화형 CLI 대응 설정)은 이 확인으로 해소
- 예제 파일 대조: CLAUDE.example.md 작업 순서 15행이 본문 105행 인용과 같음(32줄 유지). settings.example.json에 상한 키 없음(allow 6, ask 1, deny 9, PostToolUse Edit|Write). examples/ 전체에서 max_turns, max_budget, 상한, 예산 검색 0건
- 내부 링크: ch07.html#criteria, ch01.html#loop, ch09.html#cost, ch02.html#tbl-2-4, practice.html#lab-1, lab-3, lab-4, lab-6 모두 존재
- 미확인: RUNLOG.md에 python check.py 종료 코드 0 실행 기록 없음(실습 6 실행 때 기록할 것). /hooks 목록의 matcher 표시, /context의 하위 에이전트 항목은 계속 미확인

## C3-11. 3장 정비(이슈 #66 3단계, PR #88, 2026-10-22) 새 문장의 근거
- 자료 키: agent-loop(C3-1), hooks(C3-2), sub-agents(C3-3), permissions(C3-4), commands(C3-5), memory(C3-6), cli-reference(C3-10), permission-modes(1장 기록). 옛 표기 (Anthropic, 2026b)는 문서 셋(hooks-guide, hooks, sub-agents)을 묶었으므로 문서마다 키 하나로 나눔(BOOK_STANDARD 8절)
- Configure permissions(https://code.claude.com/docs/en/permissions), 확인 2026-10-22(실무자 역할 검토자 WebFetch): Edit 규칙은 내장 편집 도구와 Claude Code가 알아보는 파일 명령에 적용되고, Bash로 실행한 프로그램이 파일을 직접 여는 경우에는 적용되지 않음(OS 수준 차단은 샌드박스). ./path는 현재 디렉터리 기준. Bash(git push *)는 git -C . push처럼 다르게 쓴 명령과 일치하지 않음. 본문 files 절 "금지 규칙이 막는 범위에는 한계" 문단
- Hooks reference(https://code.claude.com/docs/en/hooks), 확인 2026-10-22(같음): 훅 명령은 현재 디렉터리에서 실행되며, 프로젝트 기준 경로는 $CLAUDE_PROJECT_DIR로 지정. 종료 코드 2면 stderr를 Claude에 보여 줌(PostToolUse는 막지 못함, 막는 것은 PreToolUse). 본문 훅 문단과 실습 파일 settings.example.json의 cd "$CLAUDE_PROJECT_DIR"
- unittest 결과 출력: Python 표준 라이브러리 unittest의 TextTestRunner 기본 스트림은 sys.stderr(실행 확인: examples/expense-app에서 python -m unittest discover tests -q 2>/dev/null 출력 없음, 2026-10-22 작성 에이전트). fact-checker 재확인 대상
- CLI reference(C3-10): --max-turns, --max-budget-usd는 -p 전용. 본문은 "명령 줄 상한 옵션은 -p 실행 전용"까지만 쓰고, 대화형 세션의 상한 설정 유무는 쓰지 않음
- Permission modes(permission-modes): 기본 모드(default)는 허용 목록에 없는 도구 사용 전에 확인을 요청함. 본문은 "권한 모드가 사람에게 묻는 기본 모드라면"으로 조건을 밝힘(Q-116과 같은 처리)
