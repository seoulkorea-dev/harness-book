# ch08 fact-checker 점검(2026-10-20, PR #41)

## 8장 사실 점검 보고 (PR #41, 브랜치 ch08-write, 확인일 2026-10-20)

범위는 src/chapters/ch08.html 전체입니다. 아래 주소는 모두 이번에 다시 열어 확인했습니다(Claude Code 문서 6건, Young 원문). Lopopolo 원문은 이번에도 열리지 않았습니다(openai.com이 ENOTFOUND). 파일은 쓰지 않았습니다.

### 지적 사항

| # | 심각도 | 위치 | 사실 문장 | 판정 | 근거 | 제안 |
|---|---|---|---|---|---|---|
| 1 | 필수 | 6행 "Claude Code는 장시간 실행 실험에서…", 26행 "Claude Code의 실험에서", 38행 "앞의 실험" | 실험 주체를 Claude Code로 씀 | 불일치 | Young 원문: 실험은 Claude Agent SDK와 Opus 4.5에서 진행했고 Claude Code를 하네스로 지칭하지 않음. S-C8-7과 같음. D-108과 Q-039는 작가 결정 대기 중이나 사실로는 원문과 다름 | 주체를 "Anthropic의 Young은 Claude Agent SDK 기반 장시간 실행 실험에서"로 고치거나, 유지하려면 작가 결정을 DECISIONS.md에 확정한 뒤 근거를 붙임 |
| 2 | 권장 | 26행 | "세 종류 가운데 진행 기록의 효과는 실험으로 확인되었습니다" | 근거 부족 | Young은 진행 파일, git 로그, 설명 있는 커밋을 쓰고 되돌리기와 복구가 가능했다고 서술하는 엔지니어링 글임. 효과를 측정하거나 비교한 실험은 아님. 뒤 문장(되돌리고 복구)은 원문과 일치 | "효과를 확인했다"를 "Young은 … 방식으로 되돌리기와 복구가 가능했다고 밝혔습니다"로 완화 |
| 3 | 참고 | 7행, 참고 자료 Lopopolo | "에이전트가 실행 중에 접근할 수 없는 지식은 없는 것과 같다. 문서 도구, 채팅, 사람의 기억" | 미확인 | openai.com 접속 실패. 검색은 게시일(2026-02), 작성자, Codex 실험이라는 개요만 확인되고 해당 문장은 확인되지 않음 | 작가 확인(Q-030과 같은 사안). 확인 전에는 인용 문구를 요약 수준으로 유지 |
| 4 | 권장 | 7행 | "Codex로 제품을 개발한 경험을 다룬 글도 … 밝혔습니다" | 형식 점검 | 문장 주어가 "글"이라 발표 주체가 없음. 원문 작성자는 OpenAI의 Lopopolo | "OpenAI의 Lopopolo는 Codex로 제품을 개발한 경험을 다룬 글에서 … 밝혔습니다" |
| 5 | 권장 | 6행 | "Claude Code 문서도 세션은 서로 독립적이고, 세션마다 새 컨텍스트에서 시작한다" 뒤에 ref-anthropic-2026a만 링크 | 링크 대응 불완전 | "Sessions are independent"는 How Claude Code works(2026b)의 Work with sessions 절. 2026a에는 "fresh context window"와 두 전달 수단(CLAUDE.md, 자동 메모리)만 있음 | 독립성 문장에 2026b 링크를 추가하고 2026a는 전달 수단 문장에 둠 |
| 6 | 권장 | 8행 | "이어 간 세션도 대화가 길어져 압축되면, 앞부분의 지시를 잃을 수 있습니다" | 일치, 링크 누락 | 2026b "When context fills up" 절: 초기 대화의 자세한 지시는 사라질 수 있고 지속 규칙은 CLAUDE.md에 둘 것을 안내. 이 문장에는 참고 자료 링크가 없고 Chapter 5 링크만 있음 | 2026b 링크 추가 |
| 7 | 권장 | 41행 | "모든 결과에 비용, 토큰 사용량, 턴 수, 세션 ID가 담겨, 작업이 오류로 끝나도 비용을 확인하고 세션을 이어 갈 수 있습니다" | 일치(단서 누락) | 2026d Handle the result 절과 일치. 같은 절의 단서: 세션 충돌 시 최종 결과가 error_during_execution이고 비용 필드가 0이거나 stop_reason이 null일 수 있음. 표 8-3에는 있으나 본문에는 없음 | 본문에 "세션이 충돌하면 비용이 0일 수 있음" 한 구절 추가 |
| 8 | 권장 | 7행 | "자동 메모리는 각자의 컴퓨터에 남습니다" | 일치, 버전 의존 | 2026c Cleaned up automatically 절: 정리 작업은 projects/<project>/memory/의 파일을 삭제하지 않음. 단 v2.1.228 이전에는 오래된 파일이 지워질 수 있었음. 2026a Auto memory 절: 자동 메모리는 machine-local | 본문 유지, 버전 주석 (2026년 10월) 추가(aside.footnote, v2.1.228 이전과 이후 차이) |
| 9 | 권장 | 표 8-3 첫 행 | "기본 30일이 지나면 삭제(cleanupPeriodDays)" | 일치, 표에 출처 링크 없음 | 값과 키는 2026c에서 확인(기본 30, 최솟값 1, 0은 검증 오류). 본문 7행과 53행에는 링크가 있으나 표에는 없음 | 표 8-3 설명이나 캡션에 2026c 링크 |
| 10 | 권장 | 표 8-6 둘째 행 | "통과 값이 true인 작업(작업 2, 3)마다 그 작업의 commit이 있음" | 예제와 불일치 소지 | tasks.example.json에서 작업 1도 통과 true이나 에이전트 commit 대상이 아님(합의 작업, 결정 기록 D-012). 표 6-4와 CLAUDE.example.md 기준 commit은 에이전트가 수행한 작업 단위마다 | "에이전트가 수행한 작업(작업 2, 3)마다"로 한정 |
| 11 | 참고 | 30~33행 | D-012 예시 행 | 일치(문구 차이) | examples/expense-app/DECISIONS.md의 D-012는 "…일 1회 갱신 자료(data/projects.csv) 사용"이고 본문 예시는 "(data/projects.csv)"가 빠짐. 날짜 2026-10-12, 대체 칸 비어 있음, 이유는 일치 | 요약 표기임을 한 구절로 알리거나 괄호를 맞춤(선택) |
| 12 | 참고 | 7행, 41행, 53행 | 기본 30일 삭제, "정가 기준 추정치" | 일치(예외 있음) | 예외: Claude Desktop과 Cowork 세션 기록은 desktopSessionCleanupPeriodDays 미설정 시 보관(v2.1.248 이상, 관리형 설정이 cleanupPeriodDays를 정하면 예외 없음). /usage 금액은 관리형 modelPricing이 있으면 계약 요율 기준이며 그래도 추정치. 기본값 설명으로는 정확 | 필요 없음. 독자 오해가 우려되면 버전 주석에 한 줄 |

### 확인한 일치 문장(요약)

| 문장(위치) | 판정 | 근거 |
|---|---|---|
| 세션은 서로 독립, 새 컨텍스트 시작, 자동 메모리와 CLAUDE.md로 전달(6행) | 일치 | 2026a 첫 문장과 두 수단 표, 2026b Work with sessions |
| 대화 기록 로컬 JSONL, 메시지, 도구 사용, 결과, 되감기, 이어 가기, 갈라 시작(41행) | 일치 | 2026b: ~/.claude/projects/ 아래 plaintext JSONL. 표 8-6과 71행의 "사용자 폴더의 .claude/projects/"도 일치 |
| --resume으로 같은 세션 다시 열기(8행) | 일치 | 2026b Resume or fork: --continue나 --resume은 같은 세션 ID로 다시 열고 새 메시지를 덧붙임 |
| 기본 30일 후 시작할 때 삭제, 키 cleanupPeriodDays(7행, 53행, 표 8-3) | 일치 | 2026c(30일, 최솟값 1), 2026e(시작 시 삭제 표현은 /insights 보고서 문단이 "세션 데이터와 같은 일정"으로 서술) |
| 결과 필드 4종, 오류로 끝나도 남음, 결과 종류, 충돌 시 비용 0(41행, 표 8-3) | 일치 | 2026d: "All result subtypes carry total_cost_usd, usage, num_turns, session_id", 하위 종류 5개(success, error_max_turns, error_max_budget_usd, error_during_execution, error_max_structured_output_retries). 표의 "종료 사유"는 이 책의 표현이라고 표에 밝혀 있음 |
| 훅 표: PostToolUse 출력 감사, SubagentStart/Stop 병렬 작업 추적, PreCompact 압축 전 대화 보관(42행, 표 8-3) | 일치 | 2026d Hooks 표(Audit outputs / Track and aggregate parallel task results / Archive full transcript before summarizing). 본문이 "Agent SDK 문서"로 주체를 밝히고 2026d에 링크함 |
| OpenTelemetry: 모든 이용 방식, 유일한 선택지, 켜야 동작(42행, 표 8-3) | 일치 | 2026e: "works on every setup and is the only option that streams per-user token and cost metrics … in near real time". 표의 setup은 Teams, Console, 클라우드 등 이용 방식. 2026f: CLAUDE_CODE_ENABLE_TELEMETRY=1과 OTEL_METRICS_EXPORTER, OTEL_LOGS_EXPORTER 설정 필요(기본 꺼짐). 뒤 56,414자는 이번에도 미열람 |
| /usage 금액은 정가 기준 추정치, 청구 근거 아님(41행, 표 8-6) | 일치 | 2026e Using the /usage command: 목록 가격으로 로컬 계산, "The figure is an estimate", 정식 청구는 Console 사용량 페이지 |
| Young: 분리된 세션, 새 세션은 이전 기억 없음(6행) | 일치 | 원문 "discrete sessions … no memory of what came before" |
| Young: 세션 시작 때 git 로그와 진행 파일을 먼저 읽음(38행) | 일치 | 원문 "Read the git logs and progress files to get up to speed" |
| Young: 설명 있는 커밋, 되돌리기와 복구(26행) | 일치 | 원문 descriptive commit messages, 되돌리기와 복구(2번 지적은 "효과 확인" 표현만) |
| 게시일 2025년 11월 26일(참고 자료) | 일치 | Young 원문 |
| 참고 자료 a~f와 본문 인용 대응 | 일치(5번과 6번 제외) | 6행 a, 7행 c와 Lopopolo, 8행 b, 41행 b, d, e, 42행 d, f, e, 53행 e. 참고 자료의 8개 id가 모두 본문에서 쓰이고 링크됨 |
| 결정 기록 형식 번호, 날짜, 결정, 대체, 이유와 "이 책의 저장소도 같은 형식"(34행) | 일치 | 루트 DECISIONS.md 머리글. CLAUDE.md가 시작 때 읽도록 지시하고 editor와 flow-reviewer 지침에도 있음 |
| 표 8-4 전체(CLAUDE.md 읽는 순서 CR.md, DECISIONS.md, tasks.json, HANDOFF.md, 갱신 주체, commit은 사람 확인 뒤, 작업 5 통과 값은 사람) | 일치 | reference/CLAUDE.example.md의 읽는 순서, 작업 순서, 수정 범위(DECISIONS.md와 acceptance/ 수정 금지, 통과 값과 HANDOFF.md는 수정 가능), commit은 사람 확인 후 |
| 수정 범위 예시 "acceptance 폴더는 수정하지 않음"(표 8-5) | 일치 | CLAUDE.example.md 수정 범위 |
| 작업 2~5 이름과 완료 기준, 작업 1 통과 true, 작업 5는 사람 승인(55행, 인계 메모 예) | 일치 | reference/tasks.example.json, 표 6-4와 동일. 인계 메모 예의 "시험 1~3이 아직 실패하는 것이 정상"은 표 6-4와 6장 56행(수용 시험 4, 5만 통과) 설명과 일치 |
| 인계 메모 다섯 항목(현재 상태, 읽을 문서, 미결정 사항, 다음 작업, 확인 명령) | 일치 | CLAUDE.example.md 중단 규칙과 같은 순서(그쪽 표기는 "미결정") |
| 부록 실습 5, 6과 "같은 상황", 실습 6 요청문 "HANDOFF.md를 읽고 이어서 작업해 줘" | 일치 | src/appendix/practice.html 실습 5(작업 2 후 작업 3), 실습 6. 앵커 lab-5, lab-6 존재 |
| 표 8-6 다른 행(인계 메모, 이어 받기, 결정 기록 D-012 한 건, 세션 기록, 사용량) | 일치 | 위 예제 파일과 부록 실습 6 확인 기준 |


## 처리(메인 세션)
| 항목 | 처리 | 내용 |
|---|---|---|
| 1 필수(Young 글 주체) | 작가 확인 | D-108에 따라 유지, Q-039에 8장 두 곳 추가함(7장과 같은 처리) |
| 2 | 반영 | "진행 기록의 쓰임은 앞의 실험에 나옵니다" |
| 3 | 작가 확인 | Q-030에 8장 추가함 |
| 4 | 반영 | "Lopopolo의 글도"(D-108에 따라 Codex 제품명 유지) |
| 5, 6, 7, 9, 10 | 반영 | 2026b 링크 두 곳, 충돌 시 비용 0, 표 8-3 출처 링크, 에이전트가 수행한 작업으로 한정 |
| 8 | 반영 | 버전 주석(자동 메모리 정리 제외, v2.1.228) |
| 11, 12 | 유지 | 예시는 요약 표기, 예외는 범위 밖 |
