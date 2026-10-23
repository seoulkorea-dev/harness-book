# 5장 실습 감수(practice-checker, 2026-10-23, PR #94)

## 총평
범위 안의 사실은 모두 일치, 필수 0. 표 5-7의 wc -l과 git show --stat HEAD는 임시 폴더에서 설명대로 나옴. 실습 흐름에서 CLAUDE.md와 .claude/가 처음 commit되면 "바뀐 파일이 모두 수정할 수 있음 안" 기준을 오판할 수 있어 권고. Claude Code 대화형 화면(/context, 응답 확인)은 실행하지 못함.

## 실행한 명령과 결과
1. python tools/check_tasks.py → 공백 2건(작업 2, 작업 3). 5장 범위 아님
2. 스크래치 ep 폴더에 examples/expense-app 복사, git init, commit
3. cp reference/CLAUDE.example.md CLAUDE.md, wc -l CLAUDE.md → 32(빈 줄 6). "여섯 절, 빈 줄 포함 32줄"과 같음
4. python -m unittest discover tests -q → Ran 3 tests OK(훅 명령과 같음)
5. 파일 변경 뒤 commit 전 git status --short → ?? CLAUDE.md, ?? HANDOFF.md, ?? tests/__init__.py
6. commit 뒤 git show --stat HEAD → 세 파일 목록
7. 저장소 작업 폴더 git status --short → 출력 없음

파일 대조: 발췌 두 절은 CLAUDE.example.md 7~10, 19~21줄과 글자 그대로. 여섯 절 이름과 순서 같음. settings.example.json deny의 Edit 경로 여섯 개가 수정하지 않음과 같음, PostToolUse(Edit|Write) 훅 `python -m unittest discover tests -q || exit 2`가 표 5-5와 맞음(example-facts 23~34줄). 표 5-5 요청 문장은 실습 5, 6과 글자 그대로. claude --continue는 실습 6 준비물. 실습 2는 예시를 본떠 작성.

실행 못 함: /context Memory files 표시, /context all, 실습 2 응답, 실습 5 도구 호출 순서, claude --continue.

## 발견
| 발견 | 위치 | 근거 | 제안 | 확신 | 등급 |
|---|---|---|---|---|---|
| 실습 2, 3에서 만든 CLAUDE.md와 .claude/는 untracked라 실습 5의 commit에 섞여 git show --stat HEAD에 나오고 기준과 어긋나 보임 | 표 5-7 규칙의 실제 준수, 실습 2~5 | 재현에서 CLAUDE.md 32줄 포함 | 기준에 "실습에서 처음 만든 CLAUDE.md와 .claude/는 제외"를 더하거나 실습 4 끝에 commit 안내 | 중간 | 권고 |
| commit 전 git status에도 같은 파일이 ??로 섞임 | 표 5-7 | 재현 | 위와 함께 | 중간 | 권고 |
| 나머지 사실 | 여러 곳 | 실행과 대조 일치 | 해당 없음 | 높음 | 불일치 없음 |

## 결론
필수 0, 권고 2(같은 원인). 검증 후 확정: Claude Code 대화형 항목.
