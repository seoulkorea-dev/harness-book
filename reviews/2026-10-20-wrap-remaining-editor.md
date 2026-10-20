# 남은 할 일 정리 검수(editor)

판정: 병합 가능 (필수 0, 권장 3)

범위: `git diff origin/main...HEAD`는 docs/AUTHOR_QUEUE.md(Q-071, Q-072 추가)와 HANDOFF.md뿐입니다. 원고(src/), tools/, 설정 변경은 없습니다.

| # | 분류 | 위치 | 발견 | 근거 | 제안 |
|---|---|---|---|---|---|
| 1 | 확인(문제 없음) | AUTHOR_QUEUE Q-071, Q-072 | 열이 기존 5열(# / 날짜 / 위치 / 질문 / 진행한 권장안)과 같고, 번호가 Q-070 다음으로 이어집니다. 날짜와 괄호 출처 표기도 Q-068~070과 같은 방식입니다. | AUTHOR_QUEUE 머리글과 기존 행 | 없음 |
| 2 | 확인(문제 없음) | 역할과 쓰기 범위 | tools/는 CLAUDE.md 쓰기 범위 표에 없습니다(메인 세션 범위는 src/, assets/, examples/, HANDOFF.md, FAILURES.md, reviews/, research/ 등). 그래서 Q-072를 작가 항목으로 넘긴 것이 맞습니다. 하위 Claude Code 세션 실행이 권한 판정에서 거부된 것을 우회하지 않고 Q-071로 적은 것도 맞습니다. 두 항목 모두 "멈추지 않고 AUTHOR_QUEUE에 적음" 규칙을 따랐습니다. | CLAUDE.md "작가만 정할 일", 멀티 에이전트 표 | 없음 |
| 3 | 확인(문제 없음) | Q-072의 사실 | `python tools/check_all.py --strict-figures`가 빌드, 금칙어, 번호, 구조, 문체, 그림 안 이름, 그림 체계, 그림 글자 크기 모두 통과했고 exit 0입니다. 기본 실행은 그림 두 항목이 목록에 안 나오고 통과하며 경고는 0건입니다. 코드에 `STRICT_FIG`(tools/check_all.py 8행)와 `STRICT_SYSTEM`(78행)이 실제로 있습니다. | check_all 출력 원문(아래) | 없음 |
| 4 | 권장 | Q-072 "진행한 권장안" 칸 | CI는 `python tools/check_all.py --ci`(.github/workflows/check.yml 15행)로 돌립니다. `--ci`와 `--strict-figures`가 함께 동작하는지는 이번 검수에서 실행해 보지 않았고, `.claude/settings.json`의 허용 규칙(`Bash(python tools/check_all.py:*)`)과 종료 훅의 위치도 적혀 있지 않습니다. | 정확성 | 권장안에 "CI는 .github/workflows/check.yml의 `--ci`, 종료 훅은 .claude/settings.json"이라고 위치를 적고, `--ci --strict-figures` 조합을 작가가 전환 전에 한 번 확인하라고 덧붙이십시오. |
| 5 | 권장 | Q-071 "진행한 권장안" 칸 | 칸 이름은 "진행한 권장안"인데, 내용이 작가가 해 줘야 할 일뿐이고 "지금 어떻게 진행했는지"가 없습니다. Q-068의 "실행 전 예상 고지를 붙여 병합" 같은 현재 상태 문장이 없습니다. | 기존 항목 형식(Q-068, Q-069) | "현재는 Q-068대로 실습 2~6을 '실행 기록 확인 전의 예상'으로 두고 진행. 작가 선택지는 …" 순서로 현재 상태를 앞에 넣으십시오. |
| 6 | 권장 | HANDOFF "지금 상태" 새 줄 | "열린 작가 요청은 이슈 #34뿐"이라는 문장은 이 환경에서 확인하지 못했습니다(`gh issue list`가 GraphQL 403으로 막힘). 나머지 내용(PR #45, Q-066~Q-072, v1.1-backlog)은 diff와 일치합니다. 새 줄이 기존의 긴 줄들보다 위에 놓여 최신순이라는 점도 기존 배치와 맞습니다. | HANDOFF 정확성 | 이슈 상태는 REST(`gh api repos/{owner}/{repo}/issues?labels=request`)로 병합 전에 한 번 확인하십시오. |

필수 건수: 0

참고: 작업 목록에서 Q-071 항목은 "실습 5, 6 실행"만 적고, Q-071 본문은 "실습 2~6"입니다. 같은 일의 일부라 모순은 아니고, HANDOFF 작업 목록 줄 끝에 "(실습 2~6 전체는 Q-071)"를 덧붙이면 더 분명합니다. 이것도 권장입니다.

## check_all 출력 원문 요약
`python tools/check_all.py` 기본 실행(마지막 줄들):
```
검사 요약
  통과  빌드
  통과  금칙어
  통과  번호
  통과  구조
  통과  문체
  통과  그림 안 이름
```
`python tools/check_all.py --strict-figures`:
```
검사 요약
  통과  빌드
  통과  금칙어
  통과  번호
  통과  구조
  통과  문체
  통과  그림 안 이름
  통과  그림 체계
  통과  그림 글자 크기
```
종료 코드 0.

## 처리
권장 4, 5와 참고: 반영(Q-071, Q-072에 현재 상태와 위치, --ci --strict-figures exit 0 확인, HANDOFF 작업 목록 보완). 권장 6: 이슈 목록은 GitHub 도구로 확인함(열린 request 이슈는 #34뿐).
