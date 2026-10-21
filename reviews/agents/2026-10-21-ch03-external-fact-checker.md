# 3장 사실 확인(fact-checker, 이슈 #47)

# ch03 사실 확인 보고 (브랜치 ch03-external-review, 확인일 2026-10-21)

범위와 한계: 이 세션에는 셸이 없어 `git diff`를 실행하지 못했습니다. 그래서 diff 대신 src/chapters/ch03.html 전체와 예제 파일을 직접 읽고 요청한 7개 항목을 대조했습니다. 원고와 파일은 고치지 않았습니다. 필수 항목은 없습니다.

| # | 심각도 | 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|---|---|
| 1 | (일치) | 훅 문단 마지막 문장은 문서와 일치합니다. 문서의 PostToolUse 종료 코드 2 행은 "Can block? No / Shows stderr to Claude; the tool already ran"이고, 막으려면 PreToolUse를 쓰라고 합니다. 본문의 "이미 실행된 편집을 막지 않고, 실패를 알려 다시 작업하게 하는 장치"는 이 내용과 같습니다. | ch03 95행, ref-anthropic-2026b | Hooks reference의 종료 코드 2 표를 2026-10-21에 다시 열어 확인했습니다. `|| exit 2` 설명도 같은 근거로 맞습니다. 본문 설정 블록은 settings.example.json의 hooks와 글자 단위로 같습니다. | 변경 없음 | 높음 |
| 2 | (일치) | 표 2-4 링크는 "파일의 수정 금지는 권한 규칙이 맡는다"를 뒷받침합니다. | ch03 95행, ch02 49~55행 (id tbl-2-4 존재) | 표 2-4는 수용 시험과 check.py의 수정 금지를 금지 규칙 `Edit(./acceptance/**)`, `Edit(./check.py)`로, 원본 자료를 `Edit(./data/**)`로 처리합니다. 완료 판정은 표 2-4에 없고 7장에 있습니다. 본문 문장도 완료 여부는 검사 스크립트가 판정한다고 따로 씁니다. | 변경 없음 | 높음 |
| 3 | 권장 | 48행 서술은 1장과 9장에 맞고, 1차 출처(Agent SDK 문서)도 지지합니다. 다만 문장에 발표 주체와 참고 자료 링크가 없습니다. "범위가 열린 요청이나 운영 환경의 에이전트에는 비용 상한을 둡니다"는 Anthropic 문서의 권고(production agent에는 예산 설정이 좋은 기본값)인데, 본문은 이를 장 링크만 달고 평서문으로 씁니다. | ch03 48행 | ch01 91행은 같은 구조로 서술하고 ref-anthropic-2026b를 답니다. ch09 41행은 "실행 한 번의 비용 상한(Chapter 1)과 팀·사용자별 지출 한도는 서로를 대신하지 않는다"고 씁니다. Agent SDK 문서(How the agent loop works, Turns and budget)에는 "fine for well-scoped tasks but can run long on open-ended prompts"와 "Setting a budget is a good default for production agents"가 있고, max_turns와 max_budget_usd의 기본값은 제한 없음입니다. | "Agent SDK 문서는 운영 환경의 에이전트에 예산 상한을 기본으로 두라고 권합니다(Anthropic, 2026)"처럼 주체와 ref-anthropic-2026 링크를 붙이거나, 이 책의 판단이면 그렇게 표시합니다. | 높음 |
| 4 | 참고 | 두 장의 서술이 약하게 어긋납니다. ch01 91행의 "그래서 하네스는 두 가지 상한을 둡니다"는 조건 없이 읽히는데, ch03의 CR은 두 상한을 모두 두지 않습니다. ch01 92행은 두 상한의 값을 "맡기기 전에 정합니다"라고 쓰므로 "두지 않기로 정함"은 모순이 아닙니다. ch03 쪽 표현은 정확합니다. | ch01 91행 (이번 diff 밖) | ch01 91~92행과 ch03 33행, 48행을 비교했습니다. 문서의 두 옵션 표 "Default: No limit"과도 어긋나지 않습니다. | ch01에서 "범위가 열린 요청에는"이라는 조건을 붙일지 작가 확인이 필요합니다. 이번 PR의 범위 밖입니다. | 중간 |
| 5 | 참고 | research의 미확인 항목 "max_turns, max_budget_usd에 대응하는 대화형 CLI 설정"을 이번에 확인했습니다. CLI 플래그 `--max-turns`와 `--max-budget-usd`가 있고 둘 다 print mode(`-p`) 전용입니다. 대화형 세션에는 이 상한이 없습니다. 따라서 ch03이 "CR에는 상한을 두지 않는다"고 쓴 것은 사실과 어긋나지 않으며, 대화형 CLI에 쓸 수 있는 설정 키가 없다는 근거도 된다는 점만 알려 둡니다. | ch03 33행, 48행 | CLI reference의 CLI flags 표, 2026-10-21 확인. | 본문 변경 없음. 아래 research 문안을 추가합니다. | 높음 |
| 6 | (일치) | 표 3-1의 종료 조건 행에서 Chapter 7(완료 기준) 링크 `ch07.html#criteria`는 맞습니다. ch07 11행에 `id="criteria"`가 있고, 제목은 "완료 기준을 검사로 변환"이며 완료 기준을 다룹니다. 같은 id가 ch10에도 있지만 파일이 달라 충돌하지 않습니다. 같은 표의 검증 행도 같은 링크를 씁니다. 상한은 `ch01.html#loop`(ch01 76행 "에이전트 루프와 종료 조건")이 맞습니다. | ch03 14~15행 | ch07 11행, ch01 76~92행 | 변경 없음 | 높음 |
| 7 | (일치) | 예제 규칙 문서의 작업 순서 변경과 본문 105행 인용이 같습니다. CLAUDE.example.md 15행 "check.py가 통과하면 commit 전에 reviewer 하위 에이전트에게 수용 기준 대조를 요청한다"가 105행 인용과 같고, 16~17행의 순서(완료 보고 → 대조 보고 뒤 commit, 사람 확인 후)도 표 3-2 검증 행과 그림 3-1과 맞습니다. 파일은 빈 줄 포함 32줄이라 ch05 56행의 "32줄"도 유지됩니다. ch05의 발췌는 읽는 순서와 수정 범위 두 절뿐이라 영향이 없습니다. 부록 실습(practice.html)은 작업 순서 문장을 인용하지 않고, 실습 5와 6은 "CLAUDE.md의 규칙대로"라고만 씁니다. | ch03 105행, CLAUDE.example.md 12~17행 | 위 파일을 직접 대조했습니다. src 전체에서 옛 문장("그 단위의 변경을 commit한다" 단독 문장 등)을 검색했고 원고에는 남은 곳이 없습니다. | 변경 없음 | 높음 |
| 8 | 권장 | ch02의 표 2-4 마지막 행이 새 순서와 어긋납니다. "작업 단위를 마치기 전에 검토를 요청함 / 작업 순서"인데, 예제 규칙 문서는 작업 단위를 마친 뒤 check.py를 실행하고, 통과하면 commit 전에 reviewer를 부릅니다. "마치기 전"은 새 순서와 맞지 않을 수 있습니다. 이번 diff 밖이지만 같은 규칙의 서술입니다. | ch02 56행 | CLAUDE.example.md 14~15행 | "check.py 통과 뒤 commit 전에 검토를 요청함" 같은 표현으로 맞추는 방안을 제안합니다. | 중간 |
| 9 | 참고 | docs/specs/ch06-spec.md 39행과 59행이 옛 문장("작업 단위를 마치면 그 단위의 변경을 commit한다(commit은 사람 확인 후)")을 인용합니다. 원고가 아니라 명세 기록이어서 독자에게는 영향이 없습니다. | docs/specs/ch06-spec.md | grep으로 확인했습니다. | 명세를 갱신하거나 "그 뒤 변경됨"을 덧붙입니다. | 높음 |
| 10 | (일치) | 실습 설정에 턴 상한과 비용 상한은 없습니다. settings.example.json은 permissions(allow 6, ask 1, deny 9)와 hooks만 있고 상한 관련 키가 없습니다. CLAUDE.example.md에도 상한 언급이 없습니다. examples/ 전체에서 `max_turns`, `max_budget`, `상한`, `예산`을 검색했을 때 결과가 0건입니다. 본문 설정 블록은 python3 허용 두 줄만 생략했고, 본문에 그 사실을 밝힙니다. | ch03 33행, 48행, 60~94행 | settings.example.json 전체, CLAUDE.example.md 전체, examples/ grep | 변경 없음 | 높음 |
| 11 | (일치) | 표 3-6 실습 6 링크와 확인 방법이 맞습니다. `practice.html#lab-6`이 있고, 확인 방법 둘째 항목이 "python check.py가 종료 코드 0으로 끝나면 CR의 수용 기준을 모두 충족"입니다. check.py는 실행 건수가 0보다 크고 실패가 0이면 종료 0이고, 아니면 1입니다(check.py 13행). 실습 5는 종료 코드 0을 실습 6에서 확인한다고 안내합니다. 실습 1, 3, 4 링크의 id도 모두 존재합니다. | ch03 119~123행, practice.html 22, 55, 74, 100행 | practice.html 확인 방법 절, check.py, RUNLOG.md | 변경 없음 | 높음 |
| 12 | 참고 | 표 3-6의 "모든 작업 단위를 마친 뒤의 목표 상태"와 실습 6의 시점이 약간 다릅니다. 실습 6은 작업 4까지 끝난 뒤 종료 코드 0을 확인하고, 작업 5는 사람 승인을 기다립니다. check.py 결과는 작업 5와 무관하므로 사실 오류는 아닙니다. 또 RUNLOG.md에는 구현 전 exit=1만 있고 exit 0 실행 기록은 없습니다(원고도 "예상"이라고 밝힘, ch07 86행은 "0이어야 합니다"). | ch03 123행, RUNLOG.md 13행 | RUNLOG.md, practice.html 실습 6 | 실습 6 실행 때 exit 0 출력을 RUNLOG에 남기면 "예상"을 "확인"으로 바꿀 수 있습니다. 표현을 "작업 4까지 마친 뒤"로 바꿀지는 작가 선택입니다. | 중간 |

## research/ch03-sources.md에 추가할 기록 문안

```
## C3-10. fact-checker 3차 확인(2026-10-21, 외부 검토 반영 PR, 브랜치 ch03-external-review)
- Hooks reference(https://code.claude.com/docs/en/hooks), 확인 2026-10-21, 작성 Anthropic(게시일 표기 없음): 종료 코드 2 표에서 PostToolUse는 "Can block? No", "Shows stderr to Claude; the tool already ran". 막으려면 PreToolUse. 본문 95행 마지막 문장과 일치
- How the agent loop works(https://code.claude.com/docs/en/agent-sdk/agent-loop), 확인 2026-10-21, 작성 Anthropic(게시일 표기 없음): 상한이 없으면 범위가 분명한 작업에는 괜찮지만 열린 요청에서는 오래 실행될 수 있음. "Setting a budget is a good default for production agents." max_turns와 max_budget_usd의 기본값은 No limit. 상한 도달 시 subtype error_max_turns, error_max_budget_usd. ch01 91행, ch03 48행과 일치
- CLI reference(https://code.claude.com/docs/en/cli-reference), 확인 2026-10-21, 작성 Anthropic(게시일 표기 없음): --max-turns와 --max-budget-usd는 print mode(-p) 전용이고 기본값은 제한 없음. 대화형 세션 설정으로는 확인하지 못함. C3 "확인하지 못한 것"의 첫째 항목(대화형 CLI 대응 설정)은 이 확인으로 해소
- 예제 파일 대조: CLAUDE.example.md 작업 순서 15행이 본문 105행 인용과 같음(32줄 유지). settings.example.json에 상한 키 없음(allow 6, ask 1, deny 9, PostToolUse Edit|Write). examples/ 전체에서 max_turns, max_budget, 상한, 예산 검색 0건
- 내부 링크: ch07.html#criteria, ch01.html#loop, ch09.html#cost, ch02.html#tbl-2-4, practice.html#lab-1, lab-3, lab-4, lab-6 모두 존재
- 미확인: RUNLOG.md에 python check.py 종료 코드 0 실행 기록 없음(실습 6 실행 때 기록할 것). /hooks 목록의 matcher 표시, /context의 하위 에이전트 항목은 계속 미확인
```

필수 0, 권장 2, 참고 4, 확인한 사실 문장 12개
(권장: #3, #8 / 참고: #4, #5, #9, #12 / 일치: #1, #2, #6, #7, #10, #11)

관련 파일 경로
- /home/user/harness-book/src/chapters/ch03.html
- /home/user/harness-book/examples/expense-app/reference/CLAUDE.example.md
- /home/user/harness-book/examples/expense-app/reference/settings.example.json
- /home/user/harness-book/src/chapters/ch01.html (91~92행)
- /home/user/harness-book/src/chapters/ch02.html (56행)
- /home/user/harness-book/src/chapters/ch09.html (41행)
- /home/user/harness-book/src/appendix/practice.html (실습 6)
- /home/user/harness-book/docs/specs/ch06-spec.md (39행, 59행)

Sources:
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/agent-sdk/agent-loop
- https://code.claude.com/docs/en/cli-reference
