# 하네스 작동 시험(2026-10-19)

- 환경: Windows 11, VS Code 확장의 Claude Code(`claude --version`: 2.1.302 (Claude Code), 세션 기록의 확장 버전 2.1.301), Git Bash
- 저장소: C:/Users/Admin/projects/harness-book, 시작 커밋 fc1443d(main = origin/main)
- 브랜치: 시험 5부터 harness-test
- 시험이 끝난 뒤 원고 변경은 모두 되돌렸다(`git status --short` 출력 없음).

## 결과 표

| 시험 | 명령 | 기대 | 실제 출력 원문 | 판정 |
|---|---|---|---|---|
| 1. 세션 시작 훅 | (세션 시작, `python tools/hooks/session_start.py`) | 작업 공간 상태, HANDOFF, 최근 결정이 세션에 들어옴 | 아래 "시험 1 원문" | 통과 |
| 2. CLAUDE.md 적용 | (요약) | 역할과 멀티 에이전트 규칙을 세션이 알고 있음 | 아래 "시험 2 요약" | 통과 |
| 3. main 커밋 차단 | `git commit --allow-empty -m "test: 훅 확인"`(main) | pre_bash 훅이 막음 | `PreToolUse:Bash hook error: [python tools/hooks/pre_bash.py]: main 브랜치에서는 커밋하지 않습니다. 작업 브랜치를 만든 뒤 커밋하십시오(git switch -c <브랜치>).` | 통과 |
| 4. main push 차단 | `git push origin main` | 막힘 | `PreToolUse:Bash hook error: [python tools/hooks/pre_bash.py]: main에는 push하지 않습니다. 작업 브랜치를 push하고 PR을 만드십시오.` | 통과(훅이 먼저 막음. 설정의 deny 규칙은 이번 시험으로는 따로 확인되지 않음) |
| 5-1. 편집 직후 검사 | ch02.html 첫 문단 앞에 "잘 되는 " 삽입(Edit) | PostToolUse 훅이 금칙어를 알림 | `[금칙어] chapters/ch02.html:47:<p class="lead">잘 되는 에이전트(Agent)는 …` (같은 출력에 구조 검사 Traceback 포함) | 통과 |
| 5-2. 전체 검사 | `python tools/check_all.py` | 금칙어 실패, exit 1 | `실패  금칙어` … `chapters\ch02.html:47: (^|[ >(])잘` / `실패  구조`(FileNotFoundError) / `exit=1` | 통과(금칙어). 구조 실패는 결함(F-13) |
| 5-3. 종료 훅 | 변경을 남긴 채 턴 종료 | stop_check가 exit 2로 종료를 막음 | 막지 않음. 세션 기록: `"type":"hook_non_blocking_error","hookName":"Stop"`, `"stderr":"Hook script appears to be missing — \"python tools/hooks/stop_check.py\" exited 2 with: [검사 실패] …"`, `"preventedContinuation":false` | **실패**(아래 "시험 5-3 분석") |
| 5-4. 되돌림 | `git checkout -- src/chapters/ch02.html chapters/ch02.html` 후 `git status --short` | 변경 없음 | (출력 없음) | 통과 |
| 6. 하위 에이전트 읽기 전용 | flow-reviewer에 ch01.html 1~16행 점검을 맡김 → `git status --short` | 보고만 하고 파일을 바꾸지 않음 | 보고 6건(reviews/agents/2026-10-19-ch01-flow-reviewer.md) / `git status --short`: (출력 없음) | 통과 |

## 시험 1 원문(세션 시작 출력의 앞 5줄)

```
== 작업 공간 상태 ==
현재 브랜치: main  (main입니다. 작업 전에 작업 브랜치를 만드십시오)

== HANDOFF.md ==
# 인계(HANDOFF)
```

## 시험 2 요약(CLAUDE.md)

1. 이 세션은 원고 작성 담당으로, src/, assets/, examples/와 기록 문서를 고치고 검사를 통과시킨 뒤 작업 브랜치에서 PR을 만든다. main 병합은 작가가 한다.
2. 원고(src/)를 쓰는 주체는 한 번에 하나이고, 하위 에이전트 6개는 읽기만 하며 보고 문안을 돌려준다. 메인 세션이 그 문안을 reviews/agents/에 저장한다.
3. 의견이 부딪히면 DECISIONS.md > 검수 Project 지침 > 하위 에이전트 의견 순서로 따르고, 목차·정의·DECISIONS 수정·push·PR은 작가에게 먼저 묻는다.

## 시험 5-3 분석

- 같은 상태에서 훅 스크립트를 직접 실행하면 막는다: `echo '{"stop_hook_active": false}' | python tools/hooks/stop_check.py` → `[검사 실패] … [구조] Traceback … FileNotFoundError: [Errno 2] No such file or directory: '…\\lint\\check_structure.py/index.html'` … `[인계] 원고(src/)를 바꿨는데 HANDOFF.md를 갱신하지 않았습니다.` `위 문제를 고친 뒤 끝내십시오.` `exit=2`
- 그런데 실제 종료에서는 Claude Code가 이 exit 2를 "Hook script appears to be missing"으로 분류하고 막지 않는 오류로 처리했다. stderr에 구조 검사 Traceback의 `No such file or directory`가 들어 있어 스크립트가 없는 것으로 잘못 판정된 것으로 보인다(추정, 세션 기록 기준).
- 결론: Windows 경로 결함(F-13)이 구조 검사를 실패시키는 데서 그치지 않고 종료 훅의 차단까지 무력화했다. 수정 뒤 시험 5-3을 다시 해야 한다.

## 발견한 결함

- lint/check_structure.py가 `__file__.rsplit('/lint/', 1)`로 루트를 구해 Windows 경로(역슬래시)에서 실패한다. check_all의 "구조"와 PostToolUse 훅(hook_lint.py)이 Windows에서 항상 실패한다. 같은 브랜치의 별도 커밋에서 고친다.

## 결함 수정과 확인(F-13)

수정(lint/check_structure.py, 검사 규칙은 그대로):
- `ROOT = Path(__file__).resolve().parent.parent.as_posix()`
- glob 결과는 `glob_()`로 받아 구분자를 `/`로 맞춤(`path[len(ROOT) + 1:]` 이름이 맞게 나옴)
- `_f.startswith('/')` → `os.path.isabs(_f)`

| 확인 | 명령 | 기대 | 실제 출력 원문 | 판정 |
|---|---|---|---|---|
| 원고 되돌린 상태의 구조 검사 | `python lint/check_structure.py` | 출력 없음, exit 0 | (출력 없음) `exit=0` | 통과 |
| 전체 검사 | `python tools/check_all.py` | 구조 통과 | 아래 원문 | 통과 |
| 실패 시험 | src/chapters/ch01.html 표 1-1 capnote에 `<li>시험용 둘째 줄</li>` 추가 → `python tools/build.py` → `python lint/check_structure.py` | "캡션 설명 2줄"로 실패 | `chapters/ch01.html: 표 1-1 캡션 설명 2줄` `exit=1` (편집 직후 PostToolUse 훅도 `[python lint/check_structure.py] exit=1` `chapters/ch01.html: 표 1-1 캡션 설명 2줄`) | 통과 |
| 되돌림 | `git checkout -- src/chapters/ch01.html chapters/ch01.html` → 빌드 → `git status --short` | 수정 파일만 남음 | ` M lint/check_structure.py` | 통과 |

check_all 원문:

```
[경고] 그림 글자 크기(기준 미달, 아직 실패로 보지 않음)
chapters\ch02.html fig-2-2: 가장 작은 글자 11.0px, 모바일 약 8.1px(기준 11.0)
chapters\ch04.html fig-4-2: 가장 작은 글자 12.5px, 모바일 약 9.2px(기준 11.0)
chapters\ch05.html fig-5-2: 가장 작은 글자 12.5px, 모바일 약 9.2px(기준 11.0)
chapters\ch06.html fig-6-2: 가장 작은 글자 12.0px, 모바일 약 8.8px(기준 11.0)
chapters\ch07.html fig-7-2: 가장 작은 글자 11.5px, 모바일 약 8.5px(기준 11.0)
chapters\ch08.html fig-8-2: 가장 작은 글자 12.5px, 모바일 약 9.2px(기준 11.0)
chapters\ch09.html fig-9-2: 가장 작은 글자 12.5px, 모바일 약 9.2px(기준 11.0)
chapters\ch11.html fig-11-1: 가장 작은 글자 11.5px, 모바일 약 8.5px(기준 11.0)

검사 요약
  통과  빌드
  통과  금칙어
  통과  번호
  통과  구조
  통과  문체
  통과  그림 안 이름
exit=0
```

## 시험 5-3 재시험(수정 뒤)

| 시험 | 명령 | 기대 | 실제 출력 원문 | 판정 |
|---|---|---|---|---|
| 편집 직후 검사 | ch02.html 첫 문단 앞에 "잘 되는 " 삽입(Edit) | 금칙어만 알림(Traceback 없음) | `[python tools/hook_lint.py]: [금칙어]` `chapters/ch02.html:47:<p class="lead">잘 되는 에이전트(Agent)는 …` | 통과 |
| 종료 훅 | 변경을 남긴 채 턴 종료 | stop_check가 종료를 막고 메시지를 세션에 돌려줌 | 아래 원문 | 통과 |
| 되돌림 | `git checkout -- src/chapters/ch02.html chapters/ch02.html` → `git status --short` | 변경 없음 | (출력 없음) | 통과 |

종료 훅 메시지 원문(세션에 "Stop hook feedback"으로 돌아옴):

```
[python tools/hooks/stop_check.py]: [검사 실패]
[경고] 그림 글자 크기(기준 미달, 아직 실패로 보지 않음)
(그림 8개 경고 줄 생략, 위 check_all 원문과 같음)

검사 요약
  통과  빌드
  실패  금칙어
  통과  번호
  통과  구조
  통과  문체
  통과  그림 안 이름

[금칙어]
chapters\ch02.html:47: (^|[ >(])잘 


[인계] 원고(src/)를 바꿨는데 HANDOFF.md를 갱신하지 않았습니다.

위 문제를 고친 뒤 끝내십시오.
```

결론: 오류 출력에 `No such file or directory`가 없어지자 exit 2가 정상적으로 종료를 막았다. 첫 시험의 실패 원인이 구조 검사 결함(F-13)이었다는 추정과 맞는다. 다만 훅 오류 출력에 이 문구가 다시 섞이면 같은 일이 생길 수 있다.
