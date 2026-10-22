# 명세: 자동 실행 자가 복구와 상태 알림(이슈 #34)

- 근거: 작가 요청 이슈 #34(2026-10-20), 이슈 #22(tools/autorun.py), F-19, Q-036, logs/autorun.log(2026-10-20 18:49 "You've hit your session limit"가 "실행 오류(success)"로 분류되어 멈춤)
- 대상: tools/autorun.py, docs/staged-claude/(설정 반영 대기 폴더, 이번에 next.md 새 판), HANDOFF.md "자동 반복 실행" 절, .gitignore(logs/는 이미 있음, 잠금 파일은 logs/ 안)
- 원고 변경 없음

## 지금 상태와 범위 조정
- 이슈가 옮기라고 한 docs/specs/flow-criteria-claude/는 PR #33이 대화형 세션에서 이미 .claude/에 반영하고 지웠음(2026-10-20). 그래서 할 일 1의 "옮기기"와 "PR #33을 닫기"는 해당 없음. 대신 같은 상황이 다시 생길 때 쓰는 일반 방식(docs/staged-claude/)을 만든다.
- tools/는 작성 에이전트의 보통 쓰기 범위 밖이지만 이 작업은 작가 요청이 tools/와 문서 변경을 지시함(이슈 #22와 같음)

## 1. 설정 반영(docs/staged-claude/ → .claude/)
- 규칙: 에이전트가 .claude/(agents, commands, settings.json)를 바꿔야 할 때는 새 판을 docs/staged-claude/ 아래 같은 경로(agents/<이름>.md, commands/<이름>.md, settings.json)로 두고 보통 PR처럼 editor 검수를 거쳐 병합한다. 이 규칙은 next.md 새 판과 HANDOFF 사용법에 적는다.
- autorun.py는 시작할 때와 단위가 끝날 때마다, 작업 트리가 깨끗하면 main으로 옮겨 pull하고, docs/staged-claude/가 있으면 직접(파이썬 파일 복사) 반영한다.
  1. 허용 경로만: agents/*.md → .claude/agents/, commands/*.md → .claude/commands/, settings.json → .claude/settings.json. 그 밖의 파일이 있으면 반영하지 않고 실패
  2. settings.json은 JSON으로 읽히는지 검사
  3. 브랜치 autorun-apply-<시각>, 파일 복사, docs/staged-claude/ 삭제, python tools/check_all.py 통과, 커밋, push, PR(제목 "설정 반영(docs/staged-claude → .claude)"), CI 통과 기다림, 병합(--merge --delete-branch), main pull
  4. 어느 단계든 실패하면 되돌림(작업 트리 복원, main으로, 로컬 브랜치 삭제, 만든 PR은 닫고 원격 브랜치 삭제)과 상태 이슈에 작가 알림
- 새 플래그 --apply-only: 설정 반영만 하고 끝냄(단위 실행 없음)

## 2. 자기 자신 다시 시작
- 시작 때 origin/main의 tools/autorun.py 내용 해시를 기억. 단위가 끝난 뒤(설정 반영 뒤) 해시가 바뀌었으면 main을 pull하고 잠금을 풀고 같은 인자로 자신을 다시 실행(os.execv). 작업 트리가 깨끗하지 않으면 다시 시작하지 않고 상태 이슈에 알림

## 3. 상태 알림(GitHub 이슈 "자동 실행 상태", 라벨 status)
- 없으면 라벨과 이슈를 만들고, 단위가 끝날 때마다 댓글: 시각, 단위 번호, 작업, PR, 결과(병합, 진행, 멈춤, 재시도, 대기), editor 결론(단위 보고에 "병합 가능", "병합 불가"가 있으면), 비용
- 작가 조치가 필요한 멈춤일 때만 댓글에 @seoulkorea-dev와 "작가가 할 일" 한 줄. 같은 내용을 HANDOFF.md "지금 상태"에 한 줄(기존 멈춤 기록 방식)
- --dry-run과 --selftest는 상태 이슈를 건드리지 않음

## 4. 멈춤 분류
| 종류 | 판정 | 처리 |
|---|---|---|
| 설정(.claude/) 쓰기 필요 | /next가 docs/staged-claude/에 둠 | 1번으로 자동 반영, 멈추지 않음 |
| 일시 오류 | 실패한 실행의 출력에 시간 초과, 네트워크, 연결 오류, 과부하(529, overloaded), 5xx | 같은 단위를 3회까지 간격을 늘려 재시도(기본 1분, 2분, 4분). 넘으면 작가 알림과 멈춤 |
| 사용량 한도 | usage limit, rate limit, session limit, "hit your … limit", limit reached, 사용량 한도 | 출력의 "resets 7:30pm" 같은 시각까지(못 읽으면 기본 60분) 기다렸다가 같은 단위를 다시 실행. 대기가 --max-wait-hours(기본 6)를 넘으면 작가 알림과 멈춤 |
| editor "병합 불가" 3회, 같은 검사나 CI 실패 2회, 진전 없음 2회 | PR 맨 위 "멈춤:"(굵게 쓴 "**멈춤:"도 인정), 기존 판정 | 멈추고 작가 알림 |
| 단위 시간 초과(--unit-timeout) | 기존 | 같은 이유 2회면 멈추고 작가 알림 |
| 그 밖의 실행 오류 | 위에 해당하지 않는 실패 | 바로 멈추고 오류 원문 요약을 작가 알림 |

## 5. 한 번에 하나만 실행
- 잠금 파일 logs/autorun.lock(pid, 시작 시각). 살아 있는 다른 프로세스의 잠금이 있으면 실행하지 않고 끝냄. 프로세스가 없는 낡은 잠금은 지우고 진행. 끝날 때(정상, 예외, Ctrl+C) 잠금을 지움
- autorun이 띄우는 단위 세션에는 환경 변수 AUTORUN_UNIT=1을 줌. next.md 새 판(docs/staged-claude/commands/next.md): logs/autorun.lock이 있고 AUTORUN_UNIT이 없으면 아무 것도 하지 않고 "자동 실행 중"이라고만 답함. 그리고 .claude/ 변경은 docs/staged-claude/에 둔다는 규칙

## 6. 시험(--selftest)
- 기존 시험 유지, 추가: 잠금(살아 있는 pid 거부, 낡은 잠금 회수), 멈춤 분류(일시 오류, 한도와 재개 시각 계산, 그 밖의 오류, "**멈춤:" 표시), 설정 반영 성공(임시 저장소, 허용 경로 복사, 폴더 삭제, gh 호출 순서)과 실패 되돌림(잘못된 settings.json, 허용 밖 경로: 브랜치 없음, main, 깨끗한 작업 트리, 작가 알림), 상태 이슈 댓글(이슈가 없으면 만들고 댓글, 작가 알림에만 @), 자기 다시 시작 판정

## 완료 기준
- --selftest 통과(출력 원문을 PR에)
- 병합 뒤 python tools/autorun.py --apply-only로 docs/staged-claude/(next.md 새 판)가 .claude/에 반영되는 것을 실제로 확인하고, 상태 이슈 댓글 원문을 PR에 붙임
- check_all 통과, editor "병합 가능"
- 작가 확인: 자기 다시 시작의 실제 확인은 다음 autorun 실행 중 autorun.py가 바뀔 때(이번 PR 병합 시점에는 실행 중인 autorun이 없음) → AUTHOR_QUEUE

## 명세 검토 반영(editor 1차 수정 필요, 필수 7)
1. 단위 세션 구분: 환경 변수 대신 명령 인자. autorun은 `claude -p "/next unit"`으로 띄우고, next.md 새 판은 `$ARGUMENTS`가 unit이면 잠금 확인을 건너뜀. 잠금 확인은 Read 도구로 logs/autorun.lock을 읽는 것뿐(Bash 불필요)
2. 낡은 잠금: 잠금 파일에 pid, 시작 시각, 마지막 갱신 시각(updated). autorun은 단위 시작과 끝, 대기 중 5분마다 갱신. 잠금은 배타 생성(O_EXCL). autorun은 pid가 살아 있고 updated가 (단위 시간 상한 + 60분) 안이면 다른 실행으로 보고, 아니면 낡은 잠금으로 지우고 진행(Windows는 tasklist로 pid 확인, pid 재사용은 updated로 거름). next.md는 잠금 파일이 있으면 "자동 실행 중"과 pid, 마지막 갱신 시각을 보여 주고, autorun이 실행 중이 아니면 logs/autorun.lock을 지운 뒤 다시 /next를 실행하라고 안내만 함(Read만 쓰는 세션은 현재 시각과 비교할 수 없어 최신 여부는 판정하지 않음. editor 검수 권장 3)
3. 자기 다시 시작: 기준은 실행 중인 파일 자신의 해시(시작 때 읽은 내용). 단위가 끝난 뒤 작업 트리가 깨끗하면 main을 pull하고 디스크의 tools/autorun.py 해시와 비교, 다르면 새 판을 자식 프로세스로 실행하고 부모는 기다렸다가 그 종료 코드로 끝남(Windows와 POSIX 같은 방식). 잠금은 넘겨줌(자식이 부모 pid의 잠금을 넘겨받아 자기 pid로 고침, 부모는 자기 pid가 아니면 지우지 않음). 남은 단위 수(--max), 직전 실패 이유(--last-fail), 다시 시작 횟수(--restarts, 상한 3)를 인자로 넘김
4. settings.json 정책(editor 검수 필수 1로 허용 목록 방식): permissions.deny와 ask는 추가만, allow는 삭제만 허용하고 그 밖의 키(env, apiKeyHelper, hooks, permissions.additionalDirectories 등)가 하나라도 다르면 반영하지 않고 작가 알림(Q-077). agents, commands는 머리말의 tools, allowed-tools, disallowedTools, hooks, permissionMode, mcpServers가 바뀌면 반영하지 않음(새 에이전트는 tools 줄이 있어야 함). 반영 PR 본문에 파일별 바뀐 줄 수(git diff --stat)
5. 설정 반영은 임시 작업 폴더(git worktree, origin/main 기준)에서 함. 사용자의 작업 트리와 브랜치는 건드리지 않음. 되돌림은 작업 폴더 삭제, 브랜치 삭제, 만든 PR 닫기. CI 대기 상한 20분(넘으면 PR 닫고 작가 알림). 병합 뒤 단계 실패는 되돌리지 않고 상태 알림만. 폴더 삭제는 반영 PR 안에서 함(원자적, 이슈 문구와 다른 점을 PR에 적음)
6. 분류 순서: 사용량 한도 → 단위 시간 초과(--unit-timeout, out.timeout) → 일시 오류 → 그 밖. 일시 오류의 5xx는 "API Error: 5xx", "HTTP 5xx", "5xx Internal/Bad Gateway/Service Unavailable/Gateway Timeout", 529, overloaded처럼 문맥이 있을 때만. 재시도와 한도 대기는 "같은 이유 2회 연속"과 "진전 없음" 판정에 세지 않음(단위 하나의 재시도 안에서 처리). 재개 시각은 메시지의 시각을 이 컴퓨터의 현지 시각으로 읽고(작가 환경 Asia/Seoul), 이미 지났으면 다음 날. 실제 로그 사례("You've hit your session limit · resets 7:30pm (Asia/Seoul)", 종료 코드 1, subtype success)를 시험 입력으로
7. 작가 알림: GitHub는 자기 계정이 쓴 댓글의 자기 언급에는 알림을 보내지 않음. 그래서 환경 변수 AUTORUN_GH_TOKEN(별도 계정이나 봇의 토큰)이 있으면 상태 이슈 댓글을 그 토큰으로 써서 작가 언급이 알림을 일으키게 함. 없으면 지금 계정으로 쓰고 알림은 가지 않을 수 있음(작가 확인 Q-078). 상태 댓글 쓰기 실패는 로그에 남기고 실행은 계속함

## 권장과 작가 확인
- 반영 PR을 editor 없이 병합하는 예외(내용은 editor 검수를 거쳐 main에 병합된 docs/staged-claude/의 기계적 복사, 대상은 허용 경로로 제한): DECISIONS D-119
- CLAUDE.md에 "docs/staged-claude/" 규칙 한 줄: CLAUDE.md는 작가 영역이라 Q-079(권장: 추가)
- 자기 다시 시작의 실제 확인: 이번 PR은 --apply-only로 설정 반영을 실제 확인하고, 다시 시작은 selftest와 다음 autorun 실행 중 autorun.py가 바뀔 때 확인(Q-080)
- --apply-only의 실행 주체: 병합 뒤 이 대화형 세션(작성 에이전트)이 실행하고 출력과 상태 이슈 댓글 원문을 PR #52 댓글에 붙임
- 한도 대기 중에는 5분마다 잠금을 갱신하고 대기 시작을 상태 댓글(@ 없음)로 남김. 절전이면 대기가 늦어질 수 있음(HANDOFF 사용법의 절전 끄기)
