# 6장 사실 점검(fact-checker, 2026-10-24, 커밋 59a5a53)

결론: 필수 0, 권고 6, 참고 5 (확인한 사실 문장 52개, 인용 13곳). 1차 문서와 실행 출력으로 불일치나 낡음은 찾지 못했습니다. 고칠 곳은 근거를 넘어선 단정, 예외 누락, 인용 위치입니다. 확인 기준은 2026-10-24 현행 페이지와 브랜치 ch06-playbook의 HEAD 59a5a53입니다. 원고는 고치지 않았습니다.

**주의:** 점검 중에 HEAD가 59a5a53("JSON 코드 상자를 원본 두 줄 그대로")으로 바뀌었습니다. 이 보고는 바뀐 뒤 판입니다. 이전 판 코드 상자는 작업 3의 완료 기준이 원본보다 짧아(괄호 부분 "(project_code 시험 추가, 기존 시험 통과)" 없음) 필수였지만, 지금은 해소되었습니다. 이 확인이 research에 없으므로 기록 문안 S-C6-18에 넣었습니다.

## 확인한 항목별 판정 요약
- **장기 실행 글(항목 1)**: 일치. 글은 Justin Young, 2025-11-26, 실험 대상은 Opus 4.5가 Claude Agent SDK 위에서 도는 구성입니다. 확인한 내용은 다음과 같습니다.
  - 실패 양상 두 가지는 한 번에 많이 하려다 구현 도중 컨텍스트가 소진되는 것과, 뒤의 인스턴스가 진행을 보고 완료를 선언하는 것입니다.
  - 기능 목록은 "over 200 features"이고 모두 처음에 "failing"입니다.
  - 한 번에 기능 하나만 맡깁니다.
  - "This incremental approach turned out to be critical…" 문장이 있습니다.
  - JSON은 Markdown보다 "less likely to inappropriately change or overwrite"라는 이유로 택했고, passes 필드만 수정하라고 지시했습니다.
  - "Claude Code"는 글의 감사의 말에만 나옵니다.
- **글의 주체 표기**: BOOK_SPEC 7절 문구("Claude Code의 … 글은"처럼 글을 주어로)에는 맞습니다. 그러나 글의 하네스는 Claude Agent SDK이고 Claude Code를 하네스로 지목하지 않습니다. 5장 점검(Anthropic의 컨텍스트 엔지니어링 글 = 유지)과 같은 쟁점이고 Q-039, Q-101(작가 결정 대기)에 올라 있어 권고(행 1)로 둡니다.
- **인용 13곳**: 모두 바로 앞 주장을 뒷받침합니다. 근거 범위를 넘는 단정은 행 2, 3에 올렸습니다.
- **Claude Code 제품 동작(항목 2)**: 일치 (행 3, 4, 6, 8은 보완).
  - 용어집은 팀원이 각자 컨텍스트 윈도를 갖고 직접 대화할 수 있으며, 에이전트 팀은 "experimental and disabled by default"라고 씁니다.
  - 비용 문서는 에이전트 팀 토큰 사용량이 "roughly proportional to team size"라고 씁니다. 에이전트 팀이 기본 비활성이라는 것도 비용 문서에 있고, "하위 에이전트의 요청도 사용량을 씀"도 같은 문서에 있습니다.
  - sub-agents 문서는 비포크는 대화 기록을 보지 않고 CLAUDE.md는 읽는다고 씁니다. 포크 모드는 v2.1.302부터, 대화형 터미널은 v2.1.232부터 기본 켜짐입니다. "Claude can start a fork on its own while fork mode is on, as it is by default"라는 문장과, 포크의 도구 호출은 주 대화에 남지 않고 최종 결과만 돌아온다는 문장도 있습니다.
  - Agent SDK 문서: 예산 상한에 하위 에이전트 지출이 합산됩니다. v2.1.217 이상에서는 상한 도달 시 새 하위 에이전트 생성이 `Budget limit reached`로 실패합니다. 응답 도착 뒤 비교하므로 "그 응답 비용 + 실행 중이던 하위 에이전트 지출"만큼 넘을 수 있습니다. 하위 에이전트는 최종 응답만 돌려주어 "main agent's context grows by a summary"입니다.
  - CLI reference: `--max-budget-usd`는 "print mode only"이고, 하위 에이전트 지출이 합산되며 추정치입니다. 이 장 원고의 "대화형 세션에는 상한이 없다"는 이 옵션에 한해 맞습니다.
- **git(항목 3)**: 실행으로 확인했습니다. 추적하지 않는 tasks.json에서 `git diff HEAD -- tasks.json`은 종료 코드 0에 출력이 없습니다. `git diff`, `git diff --cached`도 같습니다. 세 명령의 차이는 아래 실행 기록 1에 있습니다. 원고 112, 113행(작성 시점 번호) 설명과 일치합니다.
- **예제(항목 4)**: 일치.
  - 표 6-4 다섯 행은 `reference/tasks.example.json`과 코드로 대조해 필드마다 같습니다.
  - 코드 상자 두 줄은 원본 3, 4번째 줄과 글자까지 같습니다(`==` 비교 True, True).
  - D-012는 DECISIONS.md에 있습니다.
  - 기준 상태에서 수용 시험 1, 2, 3 실패, 4, 5 통과, tests 3건 실패 0, project_code 시험 0건, 종료 코드 1을 실행으로 확인했습니다.
  - `check.py`가 시험 이름에 "project_code"가 들어 있는지만 센다는 원고 설명도 코드와 일치합니다.

## 판정표
| 번호 | 등급 | 위치(절, 문장 첫머리) | 원고 문장 | 확인 결과와 1차 출처 | 고칠 문안(원문 → 바꿀 문장) |
|---|---|---|---|---|---|
| 1 | 권고(R3, 작가 결정 Q-039, Q-101 대기) | 작업 단위 분할, "이 방식을 뒷받침하는 공개 사례로…" | "이 방식을 뒷받침하는 공개 사례로 Claude Code의 장기 실행 글이 있습니다." | 글(https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents, 2026-10-24 확인)은 Anthropic 소속 저자의 글이고, 실험은 Claude Agent SDK 위의 Opus 4.5입니다. BOOK_SPEC 7절 형식에는 맞지만 하네스를 Claude Code로 지목하는 문장은 글에 없습니다. 다만 agent-loop 문서가 SDK를 "Claude Code's agent loop를 내장하는 것"으로 설명하므로 연결은 가능합니다 | 작가 결정 전에는 유지. 권장안: `이 방식을 뒷받침하는 공개 사례로 Claude Code의 장기 실행 글이 있습니다.` → `이 방식을 뒷받침하는 공개 사례로 Anthropic의 장기 실행 에이전트 글이 있습니다.` |
| 2 | 권고(R4, R13) | 예제, "파일 형식은 변경을 막는 장치가 아니고…" | "권한 규칙(Permission Rule)도 파일 단위로 적용되어 tasks.json 안에서 통과 값만 수정하도록 강제하지 못합니다" + permissions 인용 | permissions 문서(https://code.claude.com/docs/en/permissions, 2026-10-24)는 Read, Edit 규칙을 gitignore 식 경로 패턴으로 적는다고 씁니다. "파일 안 항목 단위 규칙이 없다"는 직접 서술은 문서에 없고, 이번 확인(키워드 검색)에서 그런 규칙도 찾지 못했습니다(부재 확인은 전체 정독이 아님). 인용은 "경로 패턴 적용"까지만 뒷받침합니다 | `권한 규칙(Permission Rule)도 파일 단위로 적용되어 tasks.json 안에서 통과 값만 수정하도록 강제하지 못합니다<sup class="cite" data-ref="permissions"></sup>` → `권한 규칙(Permission Rule)은 Read와 Edit에 경로 패턴을 적어 적용하므로, tasks.json 안에서 통과 값만 수정하도록 제한하는 용도로는 쓰기 어렵습니다<sup class="cite" data-ref="permissions"></sup>` |
| 3 | 권고(R4, 인용 위치) | 여러 에이전트에 나눠 맡기기, "하위 에이전트의 작업이 끝나면…" 둘째 문장 | "그래서 주 대화의 컨텍스트에는 하위 작업의 전체 기록 대신 요약이 더해지고<sup agent-loop>, 맡긴 요청도 도구 입력으로 대화 기록에 남습니다." | 요약 부분은 agent-loop(https://code.claude.com/docs/en/agent-sdk/agent-loop, "Keep context efficient": grows by a summary, not by the subtask's transcript)로 일치. "맡긴 요청이 도구 입력으로 남는다"는 직접 서술이 없습니다. agent-loop의 "What consumes context" 표에 대화 기록에 tool inputs가 쌓인다는 말이 있고 tools-reference에 Agent가 도구라는 설명이 있어 추론은 되지만, 인용은 문장 가운데 있어 두 번째 절을 뒷받침하는 것처럼 읽힙니다(플레이북 7.4 위반) | `그래서 주 대화의 컨텍스트에는 하위 작업의 전체 기록 대신 요약이 더해지고<sup class="cite" data-ref="agent-loop"></sup>, 맡긴 요청도 도구 입력으로 대화 기록에 남습니다.` → `그래서 주 대화의 컨텍스트에는 하위 작업의 전체 기록 대신 요약이 더해집니다<sup class="cite" data-ref="agent-loop"></sup>. 하위 에이전트를 부르는 것도 도구 호출이므로, 맡긴 요청은 그 도구 입력으로 대화 기록에 남습니다.` (둘째 문장은 인용 없는 추론으로 둠) |
| 4 | 권고(R4, R1; 반복 주의: 금액은 추정치) | 같은 절, 비용 문단 끝 | "비용 상한은 SDK 옵션이나 비대화형 실행(claude -p의 --max-budget-usd)에서 지정하며, 대화형 세션에는 이 상한이 없습니다." | 무인용입니다. cli-reference(https://code.claude.com/docs/en/cli-reference, `--max-budget-usd` 행, 2026-10-24)에 "print mode only", 클라이언트 추정치라 청구와 다를 수 있다는 문장이 있어 내용은 일치합니다. 3장은 이미 같은 사실에 cli-reference를 인용하고 있습니다. 상한이 추정 지출 기준이라는 점이 6장에는 빠져 있습니다 | `비용 상한은 SDK 옵션이나 비대화형 실행(claude -p의 --max-budget-usd)에서 지정하며, 대화형 세션에는 이 상한이 없습니다.` → `비용 상한은 SDK 옵션이나 비대화형 실행(claude -p의 --max-budget-usd)에서 지정하며, 이 명령 줄 옵션은 -p 실행에서만 쓸 수 있어 대화형 세션에는 이 상한이 없습니다. 상한과 비교하는 금액은 Claude Code가 계산한 추정치라 실제 청구와 다를 수 있습니다<sup class="cite" data-ref="cli-reference"></sup>.` (키 cli-reference는 bibliography에 있음) |
| 5 | 권고(인용 위치) | 같은 절, 에이전트 팀 문단 | "Claude Code의 비용 문서는 … 안내하고<sup costs>, 용어집은 … 설명합니다<sup cc-glossary>." | 두 사실은 모두 해당 문서와 일치합니다(비용 문서의 "roughly proportional to team size", 용어집의 "experimental and disabled by default"). 첫 인용이 문장 가운데(쉼표 앞)에 있어 7.4와 다릅니다 | `Claude Code의 비용 문서는 에이전트 팀에서 토큰 사용량이 팀 크기에 거의 비례한다고 안내하고<sup class="cite" data-ref="costs"></sup>, 용어집은 에이전트 팀을 기본으로 꺼져 있는 실험 기능으로 설명합니다<sup class="cite" data-ref="cc-glossary"></sup>.` → `Claude Code의 비용 문서는 에이전트 팀에서 토큰 사용량이 팀 크기에 거의 비례한다고 안내합니다<sup class="cite" data-ref="costs"></sup>. 용어집은 에이전트 팀을 기본으로 꺼져 있는 실험 기능으로 설명합니다<sup class="cite" data-ref="cc-glossary"></sup>.` |
| 6 | 권고(R2, 예외 누락) | 같은 절, 포크 문단 첫 문장 | "…프로젝트의 규칙 문서(CLAUDE.md)는 읽지만 주 대화의 기록은 보지 않습니다." | sub-agents 문서(https://code.claude.com/docs/en/sub-agents, 2026-10-24): 정의 파일로 만든 하위 에이전트는 CLAUDE.md를 읽지만 frontmatter에서 `omitClaudeMd: true`로 끌 수 있습니다. 내장 Explore, Plan은 읽지 않습니다. 원고는 "정의 파일로 만든" 한정이라 틀리지는 않지만, 끄는 설정이 빠져 있습니다. 규칙 문서에 의존하는 이 장 흐름에서 실무적으로 중요합니다 | `프로젝트의 규칙 문서(CLAUDE.md)는 읽지만 주 대화의 기록은 보지 않습니다.` → `프로젝트의 규칙 문서(CLAUDE.md)는 읽지만(정의 파일에서 omitClaudeMd를 true로 하면 읽지 않습니다) 주 대화의 기록은 보지 않습니다.` |
| 7 | 참고(7.1 시점 표기) | 같은 문단 | "Claude Code v2.1.302부터(대화형 터미널은 v2.1.232부터) 포크 모드가 기본으로 켜져 있어" | 버전은 문서와 일치합니다("Fork mode is on by default from Claude Code v2.1.302, and in an interactive terminal session from v2.1.232"). 껐을 때는 `CLAUDE_CODE_FORK_SUBAGENT=0` 또는 `permissions.deny`의 `Agent(fork)`입니다. 바뀌는 정보인데 확인 시점이 문장에 없습니다 | `Claude Code v2.1.302부터(대화형 터미널은 v2.1.232부터) 포크 모드가 기본으로 켜져 있어` → `2026년 10월 확인 기준으로 Claude Code v2.1.302부터(대화형 터미널은 v2.1.232부터) 포크 모드가 기본으로 켜져 있어` |
| 8 | 참고(R16, 근거 일부 미확인) | 예제, 같은 문단 | "도구 호출의 내용을 검사하는 훅(Hook)으로 강제할 수도 있지만" | hooks 문서(https://code.claude.com/docs/en/hooks)는 PreToolUse 훅이 종료 코드 2 또는 permissionDecision deny로 도구 호출을 막을 수 있다고 씁니다. 같은 문서에서 시간 초과나 종료 코드 1은 기본적으로 차단하지 않는다고 하므로 "강제"는 조건부입니다. Edit의 tool_input 필드(old_string 등)는 이번에 읽은 범위(약 10만 자 중 앞부분)에서 확인하지 못했습니다(미확인). 인용이 없습니다 | `도구 호출의 내용을 검사하는 훅(Hook)으로 강제할 수도 있지만` → `도구 호출을 검사해 차단하는 훅(Hook)을 쓸 수도 있지만<sup class="cite" data-ref="hooks"></sup>` (인용 위치는 문장 끝으로 옮겨야 하므로 작가가 문장을 다시 나눠야 함. Edit 입력 필드는 쓰지 않음) |
| 9 | 참고(R7) | 예제, 검증 가능성 기준 | "프로젝트 코드 조회 방식은 연동 규격이 없어 인사팀과 합의해야 하므로…" | `examples/expense-app/DECISIONS.md`의 D-012는 "CR 조건부 수용. 프로젝트 코드는 인사 시스템 일 1회 갱신 자료(data/projects.csv) 사용", 근거는 "운영 위원회 결정, 실시간 연동 규격 없음"입니다. 인사팀과 합의했다는 서술은 `docs/example-facts.md` 표(작업 1 완료 기준)에서 왔고 D-012 원문에는 "인사팀"이 없습니다. 표 6-4와 원본 JSON은 일치하므로 오류는 아닙니다 | 변경 필요 없음. 작가가 D-012 원문에 맞출지 결정 |
| 10 | 참고(실무 주의점, R3 빠진 주의) | 같은 절, 비용 문단 | (해당 문장 없음) | 구독 요금제(Pro, Max, Team, Enterprise)에서는 달러 상한이 아니라 좌석의 5시간, 주간 사용 한도에 하위 에이전트 요청도 합산됩니다(costs 문서 "Claude for Teams and Enterprise" 절, sub-agents 문서 "count toward the same usage limits"). 이 장은 API 비용 상한 위주입니다 | 필요하면 비용 문단에 `구독 요금제에서는 하위 에이전트의 요청도 같은 사용 한도에 합산됩니다.` 한 문장 추가 (선택) |
| 11 | 참고(research 기록) | research/ch06-sources.md | S-C6-9의 "표 6-4와 본문 JSON(작업 2, 3)과 글자 일치" | 59a5a53 이전 판에서는 코드 상자 작업 3의 완료 기준이 원본보다 짧았습니다(S-C6-9 기록은 그 시점에는 틀림). 지금 판은 원본 두 줄 그대로입니다 | 아래 S-C6-18로 기록 갱신 |

일치로 확인한 나머지 사실은 표에 올리지 않았습니다. 기록 문안(아래)에 근거를 남겼습니다.

## 실행 기록(원문 요약)
**1. git 동작 (git 2.43.0, Linux, 임시 저장소 /tmp/claude-0/-home-user-harness-book/4fa31d71-64a2-5605-bad4-d31a3ffd2331/scratchpad/ch06fc/r, commit 1개 있음)**
```
--- untracked tasks.json
$ git diff HEAD -- tasks.json   -> (출력 없음) exit=0
$ git diff -- tasks.json        -> (출력 없음) exit=0
$ git diff --cached -- tasks.json -> (출력 없음) exit=0
$ git status --short            -> ?? tasks.json
--- git add 뒤(아직 commit 전)
git diff HEAD -- tasks.json     -> new file mode 100644 (출력됨)
git diff -- tasks.json          -> (출력 없음)
git diff --cached -- tasks.json -> new file mode 100644 (출력됨)
--- commit 뒤 {"a":1} -> {"a":2} 수정, 스테이징 안 함
git diff -> -{"a":1} +{"a":2} / git diff --cached -> (없음) / git diff HEAD -> -{"a":1} +{"a":2}
--- {"a":2} 스테이징 뒤 작업 파일을 {"a":3}으로 다시 수정
git diff -> -2 +3 (스테이징 안 한 변경만)
git diff --cached -> -1 +2 (스테이징한 변경만)
git diff HEAD -> -1 +3 (마지막 commit과 지금 파일)
```
원고 설명과 모두 일치합니다. "스테이징하지 않은 새 파일은 어느 쪽에도 나오지 않는다"는 추적하지 않는 파일에 한한 설명이고, `git add`만 한 새 파일은 `git diff --cached`와 `git diff HEAD`에 나옵니다. 원고 문장(추적하지 않는 파일)은 정확합니다.

**2. 기준 상태(examples/expense-app, python3.13, 2026-10-24)**: `python3 -B check.py`
```
Ran 3 tests ... OK
tests: 실행 3건, 실패 0건, 건너뜀 0건, project_code 시험 0건
FAIL: test_1_form_offers_project_codes / test_2_unknown_code_rejected_with_reason / test_3_list_shows_project_code
Ran 5 tests ... FAILED (failures=3)
acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)
exit=1
```
실패는 test_1, 2, 3뿐이므로 test_4, 5는 통과입니다(부록 실습 1 기준 상태와 같음).

**3. 예제 대조(Python 비교, 2026-10-24)**
```
표 6-4 5행 vs tasks.example.json: 작업/완료 기준/확인 방법 필드 모두 True
코드 상자 2줄 vs tasks.example.json 3, 4번째 줄: True True (줄 수 2)
```
`reference/CLAUDE.example.md` 13행: "작업 5의 '통과' 값은 변경하지 않는다"(원고의 "규칙 문서의 작업 5 규칙"과 일치). 앵커 존재: ch02#tool-scope, ch03#example, ch03#check, ch04#example, ch05#retrieval, ch07#criteria, ch08#handover, practice#lab-1, #lab-5.

## research/ch06-sources.md에 덧붙일 기록 문안
```
## 2026-10-24 fact-checker 재확인(브랜치 ch06-playbook, HEAD 59a5a53)
- S-C6-15 Young(2025) 재확인(https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents, 확인 2026-10-24): 저자 Justin Young, 2025-11-26. "Opus 4.5 running on the Claude Agent SDK". 실패 두 가지(너무 많이 하려다 구현 도중 컨텍스트 소진, 뒤의 인스턴스가 완료 선언), "over 200 features"와 모두 "failing", 한 번에 기능 하나, "This incremental approach turned out to be critical…", JSON이 Markdown보다 덮어쓰기 가능성이 낮다는 선택 이유, passes 필드만 수정. "Claude Code"는 감사의 말에만 있음. 표기는 Q-039, Q-101 대기.
- S-C6-16 sub-agents(https://code.claude.com/docs/en/sub-agents, 확인 2026-10-24): 비포크는 대화 기록을 보지 않음, 내장 Explore와 Plan 외 정의 파일 하위 에이전트는 CLAUDE.md를 읽고 frontmatter omitClaudeMd로 끌 수 있음. "Claude can start a fork on its own while fork mode is on, as it is by default", "Fork mode is on by default from Claude Code v2.1.302, and in an interactive terminal session from v2.1.232", 끄기는 CLAUDE_CODE_FORK_SUBAGENT=0 또는 permissions.deny의 Agent(fork), 포크의 도구 호출은 주 대화에 남지 않고 최종 결과만 돌아옴. 하위 에이전트 요청은 같은 사용 한도에 합산.
- S-C6-17 agent-loop, costs, glossary, cli-reference, permissions, hooks 재확인(확인 2026-10-24): agent-loop는 예산 상한에 하위 에이전트 지출 합산, v2.1.217 이상 새 하위 에이전트 생성이 `Budget limit reached`로 실패, Budget headroom, "grows by a summary". costs는 "roughly proportional to team size", "disabled by default", "The subagent's own requests still draw on your usage". glossary는 에이전트 팀 "experimental and disabled by default", 팀원과 직접 대화. cli-reference는 `--max-budget-usd` "print mode only", 클라이언트 추정치, 하위 에이전트 지출 합산. permissions는 Read와 Edit 규칙이 gitignore 식 경로 패턴(항목 단위 규칙은 키워드 검색으로 찾지 못함, 전문 정독은 아님). hooks는 PreToolUse 훅이 종료 코드 2 또는 permissionDecision deny로 차단 가능, 시간 초과는 기본적으로 차단하지 않음. "맡긴 요청이 도구 입력으로 대화 기록에 남는다"는 직접 서술 없음(agent-loop "What consumes context" 표와 tools-reference의 Agent 도구 설명으로 추론). Edit의 tool_input 필드는 미확인.
- S-C6-18 예제 대조(내부 기록, 확인 2026-10-24): HEAD 59a5a53 이후 코드 상자 두 줄이 examples/expense-app/reference/tasks.example.json 3, 4번째 줄과 글자까지 같음(이전 판은 작업 3 완료 기준이 원본보다 짧았음, S-C6-9는 그 점에서 낡음). 표 6-4 다섯 행도 필드별 일치.
- S-C6-19 git 실행(git 2.43.0, Linux, 임시 저장소): 추적하지 않는 파일에서 git diff, git diff --cached, git diff HEAD -- tasks.json 모두 종료 코드 0, 출력 없음, status는 ??. git add 뒤에는 --cached와 HEAD가 new file로 출력, 스테이징 전후 git diff(스테이징 안 한 변경만), --cached(스테이징한 변경만), HEAD(마지막 commit과 지금 파일) 차이 확인.
- S-C6-20 예제 실행(python3.13, 2026-10-24): python -B check.py → tests 3건 실패 0건 project_code 시험 0건, acceptance 5건 실패 3건(test_1~3), 종료 코드 1. 수용 시험 4, 5 통과. DECISIONS.md D-012는 "운영 위원회 결정, 실시간 연동 규격 없음"(인사팀 합의 서술은 example-facts.md에서 옴).
```

## bibliography.json 새 키
필요 없음. 제안한 고침이 쓰는 `cli-reference`, `hooks`는 이미 있습니다. 6장이 쓰는 인용 키 6개(long-running-harness, cc-glossary, costs, sub-agents, agent-loop, permissions)는 모두 등록되어 있습니다.

필수 0, 권고 6, 참고 5, 확인한 사실 문장 52개
