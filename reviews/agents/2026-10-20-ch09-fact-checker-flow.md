# ch09 fact-checker 점검(2026-10-20, PR #42)

## 사실 점검 보고: src/chapters/ch09.html (9장 개정, PR #42)
확인 기준일 2026-10-20. 공식 문서 4건(permissions, permission-modes, sandboxing, costs)과 프롬프트 작성 문서 원문을 오늘 다시 열어 대조했다. 원문이 열린 문장 중 불일치와 낡음은 없다. 필수 항목은 없다. Codex 문장은 오늘도 열리지 않아 미확인이다(developers.openai.com과 .md 주소 모두 DNS 오류 ENOTFOUND). 파일은 쓰지 않았다.

| # | 심각도 | 위치 | 사실 문장 | 판정 | 근거(주소, 위치, 확인 날짜 2026-10-20) | 제안 |
|---|---|---|---|---|---|---|
| 1 | 참고 | 격리 절 마지막 문단 | "Codex도 승인 정책과 샌드박스의 두 계층을 두며(OpenAI, 2026)" | 미확인 | developers.openai.com/codex/agent-approvals-security와 .md가 DNS 오류로 열리지 않음. 웹 검색이 보여 준 공식 페이지 발췌에는 두 설정(정책 untrusted, on-request, never와 샌드박스 workspace-write, danger-full-access)이 별개라고 나옴. 발췌는 2차 확인이고 판정 근거로 쓰지 않음. 참고 자료의 "확인 2026년 10월 4일"은 오늘 재확인하지 못했으므로 갱신하지 말 것 | 원문을 열 수 있는 환경에서 재확인. 값 이름을 쓰지 않아 문장 자체는 현재 안전 |
| 2 | 권장 | 권한 규칙 절 둘째 문단 | "넓은 금지 규칙 Bash(git push *)는 더 좁은 허용 규칙 Bash(git push origin main)가 있어도 그 명령을 막습니다(2026b)" | 일치(원리). 예시는 책이 만든 것 | permissions 문서 "Rules are evaluated in order" 단락: "rule specificity doesn't change the order", "An allow rule can't carve an exception out of a deny rule". 원문 예시는 Bash(aws *)와 Bash(aws s3 ls)이고, git 예시는 원문에 없음. Bash(git push *)가 git push origin main을 막는다는 것은 "what a Bash rule doesn't match" 표에 있음 | "(2026b)"가 git 예시까지 원문인 것처럼 읽힘. 예시는 책의 적용이라고 구분하거나 원문 예시 병기 |
| 3 | 확인 | 권한 규칙 절 | "Claude Code 문서는 권한 규칙을 모델이 아니라 Claude Code가 강제" | 일치 | permissions 문서 Permission system 절 Note: "Permission rules are enforced by Claude Code, not by the model", CLAUDE.md 지시는 허용 범위를 바꾸지 못함 | 유지 |
| 4 | 확인 | 권한 규칙 절 | 금지, 확인 요청, 허용 순서, 처음 일치한 규칙, 어디에도 없으면 권한 모드 | 일치 | 같은 문서 평가 순서 단락. ask와 allow 사이도 같은 우선순위 | 유지 |
| 5 | 확인 | 격리 절 첫 문단 | Bash 규칙은 문자열만 대조, git -C . push는 불일치, "보안 경계가 아니다" | 일치 | permissions 문서 "what a Bash rule doesn't match" 표: Bash(git push *)는 git push origin main을 막고 git -C . push origin main, git -c push.default=current push, git 'push'는 막지 못함. 원문 "isn't a security boundary around the program". 원문은 복합 명령 분리와 래퍼 제거 뒤에 대조한다고 덧붙임 | 유지. "글자만"은 단순화이나 허용 범위 |
| 6 | 확인 | 격리 절 첫 문단 | 파일 수정 금지 규칙은 편집 도구와 Claude Code가 인식하는 셸 파일 명령에만 적용되고 스크립트의 간접 수정에는 적용 안 됨 | 일치 | permissions 문서 Read and Edit 절: deny는 내장 파일 도구, cat, head, tail, sed, tee 같은 인식 명령, 리다이렉션 대상에 적용. Python이나 Node 스크립트처럼 간접으로 쓰는 임의 하위 프로세스에는 적용 안 됨. OS 수준 강제는 샌드박스 | 유지 |
| 7 | 확인 | 격리 절 | 샌드박스는 셸 명령과 하위 프로세스의 파일, 네트워크를 OS 수준에서 제한, 파일 도구는 샌드박스 밖(2026d) | 일치 | sandboxing 문서 첫 문단과 "What runs outside the sandbox": Bash, PowerShell, Monitor 명령과 그 하위 프로세스가 대상이고 파일 도구, MCP 서버, 훅은 밖. 파일 도구는 permission rules를 따름 | 유지 |
| 8 | 확인 | 격리 절 | 권한과 샌드박스는 보완 계층, 프롬프트 주입에도 제한이 남음(2026b) | 일치 | permissions 문서 Sandboxing 절 "complementary security layers", "sandbox restrictions still apply even if a prompt injection bypasses Claude's decision-making" | 유지 |
| 9 | 확인 | 격리 절, 표 9-2 | 샌드박스는 기본 꺼짐, /sandbox로 켬(2026d) | 일치 | sandboxing 문서: "The sandbox is off by default", /sandbox 실행 또는 sandbox.enabled=true | 유지 |
| 10 | 확인 | 버전 주석 | macOS, Linux, WSL2에서 동작, 네이티브 Windows 미동작, Linux와 WSL2는 bubblewrap과 socat 필요 | 일치 | sandboxing 문서 첫 부분("On native Windows, Claude Code runs commands unsandboxed")과 Set up Linux and WSL2 절. WSL1은 미지원 | 유지 |
| 11 | 참고 | 버전 주석 | 주석 형식 | 형식 점검 | "버전 주석 (2026년 10월)" 형식은 STYLE 5절과 맞음. 다만 바뀐 사실이 아니라 현재 사실을 담았고 원문(본문)이 같은 사실을 쓰지 않음 | 별도 조치 불필요. 작가 취향 문제 |
| 12 | 확인 | 격리 절 | bypassPermissions는 권한 프롬프트와 안전 확인을 해제, 금지 규칙은 적용, 인터넷 없는 컨테이너나 VM에서만(2026c) | 일치 | permission-modes 문서: "disables permission prompts and safety checks", "Deny rules block in every mode, including bypassPermissions", "Only use this mode in isolated environments like containers, VMs, or dev containers without internet access" | 유지. 원문은 명시적 ask 규칙은 여전히 묻는다고 덧붙임. 본문 요지와 충돌 없음 |
| 13 | 확인 | 승인 절 | 프롬프트 작성 문서의 세 종류 동작 예시 | 일치 | Prompting best practices "Balancing autonomy and safety" 절: 파괴적(파일과 브랜치 삭제, 테이블 삭제, rm -rf), 되돌리기 어려운(git push --force, git reset --hard, 게시된 commit amend), 다른 사람에게 보이는(코드 push, PR과 이슈 댓글, 메시지, 공유 인프라). 본문은 rm -rf와 git reset --hard를 생략함 | 유지 |
| 14 | 확인 | 승인 절 | 파일 수정이나 테스트 실행처럼 되돌릴 수 있는 로컬 동작은 그대로 하도록 권함 | 일치 | 같은 절 샘플 프롬프트 "encouraged to take local, reversible actions like editing files or running tests" | 유지 |
| 15 | 참고 | 승인 절 | 프롬프트 작성 문서의 지침 | 범위 주의 | 원문 절은 "Claude Opus 4.6" 대상으로 쓰임. 본문은 모델을 밝히지 않고 일반 예로 서술 | 모델 한정을 밝히면 더 정확. 현재 서술이 틀리지는 않음 |
| 16 | 확인 | 승인 절 | 확인 요청이 오면 대화 화면에 실행할 동작이 표시되고 승인자가 승인하거나 거절 | 일치 | permissions 문서 "A permission prompt shows what Claude is about to do, followed by your options" | 유지 |
| 17 | 확인 | 비용 절 | API 과금은 토큰 사용량에 비례, 구독은 요금제 한도 안에서 사용(2026e) | 일치 | costs 문서 첫 문단 "Claude Code charges by API token consumption", Teams와 Enterprise 절은 시트 허용량(seat allowance)과 사용 크레딧 | 유지 |
| 18 | 권장 | 비용 절 첫 문단 | "비용 관리 방법으로 토큰 사용량 추적, 팀 지출 한도, 컨텍스트 관리, 모델 선택을 안내" | 부분 일치 | costs 문서 개요 문장은 이 넷에 확장 사고 설정(extended thinking)과 전처리 훅(preprocessing hooks)을 더해 여섯 가지를 듦. 방법 네 가지가 문서의 전부로 읽힐 수 있음 | "대표 방법"으로 쓰거나 확장 사고와 훅은 다루지 않는다고 덧붙임 |
| 19 | 권장 | 비용 절 목록 3 | "Teams와 Enterprise 요금제는 조직, 그룹, 개인 단위로, API 콘솔은 워크스페이스 단위로 한도" | 일치(조건 누락) | costs 문서 Claude for Teams and Enterprise 절 "turn on usage credits and set spend limits at the organization, group, or individual member level"과 Claude Console 절 "workspace spend limits". Teams와 Enterprise 한도는 사용 크레딧을 켠 경우의 한도임. 시트 허용량이 기본 상한 | 일치하나 "사용 크레딧 기준"을 한 구절 더하면 정확 |
| 20 | 확인 | 비용 절 /usage 문단, 표 9-3, 9-6 | /usage 첫 화면 위쪽 Session 항목은 현재 세션 토큰 사용량, API 사용자용, 금액은 정가 기준 추정치, 구독자는 같은 화면에서 요금제 사용량(2026e) | 일치 | costs 문서 Track your costs: "The Session block at the top of /usage", "intended for API users", "computes the dollar figure locally from token counts at list price", "The figure is an estimate", 구독자는 "plan usage bars, activity stats, and a usage breakdown". 관리자가 modelPricing을 설정하면 계약 요율 기준이고 이때도 추정치(v2.1.242 이상) | 유지. 본문 "정가 기준"은 기본 동작 기준임 |
| 21 | 확인 | 표 9-6 샌드박스 행 | touch ~/sandbox-probe: macOS Operation not permitted, Linux와 WSL2 Read-only file system | 일치 | sandboxing 문서 검증 표: "Fails with Operation not permitted on macOS, or Read-only file system on Linux and WSL2" | 유지 |
| 22 | 권장 | 표 9-6 샌드박스 행 | "성공하면 샌드박스가 꺼진 것이므로 만든 파일을 삭제" | 부분 일치 | 같은 절: 성공하고 홈 디렉터리가 샌드박스 쓰기 허용 경로가 아니면 파일을 지우고 /sandbox로 켜짐과 의존성을 확인하라고 안내. 실패 뒤 Claude가 샌드박스 밖 재시도를 묻는 경우 거절하라는 안내도 있음. 쓰기 허용 경로(작업 디렉터리, 임시, --add-dir)에 홈이 포함되면 성공해도 꺼진 것은 아님 | "성공하면 샌드박스가 꺼졌거나 홈이 쓰기 허용 경로이므로 /sandbox로 확인"으로 조정하고 재시도 거절 안내 추가 검토 |
| 23 | 권장 | 격리 절, 표 9-5 2행 | "샌드박스를 켜서 네트워크 접근을 운영 체제 수준에서 제한" (git -C . push 대응) | 일치(조건 누락) | sandboxing 문서 Network 행: 허용 도메인(allowedDomains)이 비어 있는 상태로 시작하고 새 도메인은 권한 모드에 따라 프롬프트. github.com을 허용 목록에 넣으면 git push도 통과 가능 | 본문 "제한"은 맞음. 허용 도메인 설정에 따라 막힘이 결정됨을 덧붙이면 정확 |
| 24 | 권장 | 표 9-4 웹 접근 행 | WebFetch, WebSearch 금지, 이유 "외부 자료를 읽지 않음" | 일치(과장 소지) | permissions 문서 Warning: "using WebFetch alone doesn't prevent network access. If Bash is allowed, Claude can still use curl, wget". 예제 JSON은 curl을 허용하지 않아 기본적으로 확인이 뜨지만, 이 규칙만으로 네트워크가 막히는 것은 아님 | 이유 열에 "Bash의 curl 등은 별도로 막아야 함(샌드박스)" 한 구절 검토 |
| 25 | 확인 | 격리 절, 예제 절 | 예제 설정에는 샌드박스 설정이 없고 기본으로 꺼져 있다 | 일치 | examples/expense-app/reference/settings.example.json에 sandbox 키 없음(permissions와 hooks만 있음) | 유지 |
| 26 | 확인 | 표 9-4, 표 9-5 1행 | 규칙과 동작 대응 | 일치 | settings.example.json: allow는 python -m unittest *, python check.py, python3 변형, git status, git diff *. ask는 Bash(git commit *). deny는 Edit(./data/**), Edit(./acceptance/**), Edit(./check.py), Edit(./CLAUDE.md), Edit(./DECISIONS.md), Edit(./.claude/**), Bash(git push *), WebFetch, WebSearch. "python3 형식을 표에서 생략"도 맞음. ch02 표 2-4와 ch03 표(120행)와도 동일 | 유지 |
| 27 | 확인 | 예제 절 마지막 | 같은 시험이 세 번 연속 실패하면 멈추는 중단 규칙, CR은 한도를 따로 두지 않음 | 일치 | ch03 33, 48, 110행과 ch02 55행. ch03 48행은 "턴 상한과 비용 상한을 따로 두지 않고" | 유지. 비용 항목의 "한 세션에 끝나는 작업 단위"는 ch06 연결로 확인 범위 밖 |
| 28 | 확인 | 확인 방법 절, 표 9-6 | 부록 실습 3과의 일치 | 일치 | src/appendix/practice.html 40-49행: settings.example.json의 permissions를 옮기고 /permissions 확인, "data/projects.csv에 PRJ-2604 행을 추가해 줘"와 push 요청. PRJ-2604는 examples/expense-app 전체에 없음(목록에 없는 새 코드와 일치). 실습 3은 샌드박스를 다루지 않으며, 본문이 /sandbox 확인을 표 9-6에서 따로 안내하므로 충돌 아님 | 유지 |
| 29 | 참고 | 표 9-6 1행 | "금지에 data/, acceptance/의 수정과 git push, 확인 요청에 git commit" | 일치 | ch03 120행 표와 JSON 일치. JSON의 deny에는 check.py, CLAUDE.md 등도 있으나 기준은 "있음" 수준이라 충돌 없음 | 유지 |
| 30 | 참고 | 참고 자료 | 참고 자료 a~e와 본문 인용 대응 | 일치(형식) | a는 비용이 아니라 승인 절 프롬프트 문서, b는 permissions, c는 permission-modes, d는 sandboxing, e는 costs. 본문 인용 a 1회, b 4회, c 1회, d 3회(주석 포함), e 3회, openai 1회로 모두 id 링크로 걸려 있고 참고 자료에 없는 인용과 미인용 항목 없음. 제목이 원문 페이지 제목과 같음. 확인일 10월 20일은 오늘 확인과 일치, OpenAI의 10월 4일은 재확인 불가로 유지 | 유지. 참고 자료에 URL이 없는 것은 다른 장과 같은 형식임(ch08 확인) |


## 처리(메인 세션)
| 항목 | 처리 | 내용 |
|---|---|---|
| 1 | 작가 확인 | Codex 원문 미확인(Q-030과 같은 사정, 확인일 10월 4일 유지) |
| 2 | 반영 | git 예는 이 책의 적용임을 밝힘 |
| 12 | 반영 | reader-novice 반영 때 쓴 "확인 요청 규칙 동작도 묻지 않고"를 "명시한 확인 요청 규칙은 이 모드에서도 묻지만, 규칙에 없는 동작은 묻지 않고"로 바로잡음 |
| 18, 19 | 반영 | "대표 방법", 다루지 않는 방법, "사용 크레딧을 켠 뒤" |
| 22, 23, 24 | 반영 | 샌드박스 확인 행, 허용 도메인 조건, 웹 금지 규칙은 셸 네트워크 명령을 막지 않음 |
| 11, 15 | 유지 | |
