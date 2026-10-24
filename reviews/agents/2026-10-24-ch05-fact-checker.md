# 5장 사실 점검(fact-checker, 2026-10-24, 커밋 127065a)

5장 사실 점검(fact-checker, 2026-10-24, 브랜치 ch05-playbook, HEAD 127065a). 원고와 파일은 고치지 않았고, 임시 파일은 scratchpad/ch05fc/ 아래에만 만들었습니다.

결론: 필수 3, 권고 12, 참고 6 (확인한 사실 문장 약 80개).

- 기준일 2026-10-24. 로컬 Claude Code 2.1.310입니다.
- 점검 도중 HEAD가 127065a로 바뀌었습니다. 표 5-7 "규칙의 실제 준수" 행(git show --stat HEAD로 바뀐 파일을, git show HEAD -- tasks.json으로 바뀐 줄을 봄)이 고쳐졌고, 아래 표는 이 상태를 기준으로 했습니다.
- openai.com, developers.openai.com은 이번 환경에서 DNS가 풀리지 않아(ENOTFOUND) 열 수 없었습니다. OpenAI 글과 Codex 문서는 미확인입니다.

## 일치로 판정한 문장 (표에는 올리지 않음)
Claude Code 문서 기준이며, 모두 2026-10-24에 다시 열었습니다.

- **commands**: `/context [all]`은 컨텍스트 사용량을 색 격자로 보여 주고, 전체화면 모드에서는 항목별 분류가 접히며 `all`로 펼칩니다. `/clear`는 새 대화를, `/compact`는 요약으로 공간 확보를 맡습니다.
- **how-claude-code-works, "When context fills up"**: 한도에 가까워지면 오래된 도구 출력을 먼저 지우고, 필요하면 대화를 요약합니다. 초반의 상세 지시는 사라질 수 있습니다.
- **같은 문서, "The context window"**: 윈도에는 대화, 파일 내용, 명령 출력, CLAUDE.md, 자동 메모리, 불러온 Skill, 시스템 지침이 들어갑니다.
- **skills**: 설명(description)은 상시 컨텍스트에 있고(목록에는 이름도 표시), 본문은 호출될 때 읽힙니다. `disable-model-invocation: true`이면 설명도 컨텍스트에 없습니다.
- **memory, "How Claude remembers your project"**:
  - 작성 기준: "concrete enough to verify", Size(200줄 미만이 목표, 길면 컨텍스트를 더 차지하고 준수율이 낮아질 수 있음), Consistency("may pick one arbitrarily").
  - 추가 시점 네 가지가 원고와 같습니다.
  - `@path`로 가져온 파일은 함께 읽혀 컨텍스트 비용이 줄지 않습니다.
  - "context, not enforced configuration"이고, 막으려면 PreToolUse 훅을 쓰라고 안내합니다.
  - `/context`의 **Memory files** 항목이 있습니다.
  - AGENTS.md는 v2.1.277 이상에서 읽고, Bedrock이나 텔레메트리를 끈 세션은 v2.1.281 이전에는 읽지 못합니다.
- **압축 뒤 동작(memory의 "Instructions seem lost after /compact"와 context-window의 "What survives compaction")**: 프로젝트 루트 CLAUDE.md는 디스크에서 다시 주입됩니다. 하위 폴더 CLAUDE.md와 `paths:` 규칙은 on demand로 다시 읽히고, 요약에 묻힙니다. 원고 57행과 일치합니다.
- **sub-agents, "What loads at startup"**: 비포크 하위 에이전트는 대화 기록을 보지 못하고, 위임 메시지와 CLAUDE.md 계층을 받습니다. 포크는 부모 대화를 상속합니다. 테스트 출력 같은 장황한 출력은 위임하면 요약만 돌아옵니다.
- **Rajasekaran 외(Anthropic, 2025-09-29)**:
  - "finite resource", 토큰이 늘면 정확히 떠올리는 능력이 떨어진다는 서술.
  - 임베딩 기반 사전 검색, 가벼운 식별자(파일 경로, 저장된 쿼리, 웹 링크).
  - "runtime exploration is slower than retrieving pre-computed data".
  - Claude Code 혼합 방식(CLAUDE.md는 먼저, glob과 grep으로 필요할 때).
  - "smallest possible set of high-signal tokens".
  - 압축은 "extensive back-and-forth", 노트는 "iterative development with clear milestones", 하위 에이전트는 "parallel exploration"에 맞는 작업.
  - 하위 에이전트 요약 "often 1,000-2,000 tokens", "overly aggressive compaction ... subtle but critical context", "Like Claude Code creating a to-do list".
  - 화자는 "At Anthropic, we"이고 저자는 Applied AI 팀입니다.
- **임베딩 풀이**("문장의 뜻을 수치로 변환해 비슷한 자료를 찾는 검색"): Anthropic Embeddings 문서의 "numerical representations of text that let you measure semantic similarity"와 맞습니다. bibliography에 키는 없습니다.
- **예제 사실**:
  - `wc -l CLAUDE.example.md` 출력은 32이고, `grep -c '^## '`는 6입니다(목적, 읽는 순서, 작업 순서, 수정 범위, 중단 규칙, 명령). 끝 줄바꿈이 있어 `splitlines()`도 32입니다.
  - 발췌 코드 상자의 모든 줄이 원본에 그대로 있습니다. 원본에서 "작업 순서" 절을 건너뛴 발췌이고, 본문도 "두 절의 발췌"라고 밝혀 두었습니다.
  - settings.example.json의 deny 6경로(data, acceptance, check.py, CLAUDE.md, DECISIONS.md, .claude)가 "수정하지 않음"과 같습니다.
  - 표 5-5의 여섯 절 32줄, 읽는 순서, 통과가 false인 첫 단위, 편집 뒤 훅, 요청 문장(practice.html 실습 5와 같음)이 example-facts.md와 reference/ 원본과 맞습니다.
  - reviewer의 tools는 Read, Grep, Glob라서 표 5-6 다섯째 행의 "시험을 실행하지 않음"이 맞습니다.
  - 표 5-7의 `wc -l`과 200줄 기준이 맞습니다. PowerShell은 이 환경에 없어 실행하지 못했고, 2026-10-23 기록(Count 32)에 의존합니다.
- **표 5-7 "규칙의 실제 준수" 행**: 127065a에서 이미 고쳐졌습니다. 임시 저장소(scratchpad/ch05fc/demo)에서 통과 값 두 개를 바꾼 commit을 만들어 확인한 결과, `git show --stat HEAD`는 "tasks.json | 4 ++--"만 보여 줘서 어느 값이 바뀌었는지 알 수 없었습니다. `git show HEAD -- tasks.json`은 줄 단위 차이를 보였습니다. 지금의 두 명령 조합은 맞습니다.

## 지적 표

| 번호 | 등급 | 위치(절, 문장 첫머리) | 원고 문장 | 확인 결과와 1차 출처 | 고칠 문안 |
|---|---|---|---|---|---|
| 1 | 필수 | 에이전트가 읽는 정보의 종류, 90행 부근 "규칙 문서에 위치와 순서만 두고…" 문단 끝 | "원고를 작성하는 에이전트는 작업을 시작할 때 원고 저장소 루트의 규칙 문서(CLAUDE.md)를 읽고, 거기 적힌 순서대로 인계 메모(HANDOFF.md)와 작가의 결정과 취향을 정리한 문서(AUTHOR_PREFS.md)를 이어서 읽습니다." | R7·R8 불일치. 지금 루트 CLAUDE.md "먼저 읽을 것"의 순서는 NEW_BOOK_PLAYBOOK.md, BOOK_SPEC.md, HARNESS_SETUP.md, HANDOFF.md의 "지금 상태", docs/AUTHOR_QUEUE.md와 DECISIONS.md 마지막 10건입니다. AUTHOR_PREFS.md는 "정리 예정"인 옛 기준 문서로 분류되어 있습니다(7a2942c). 본문은 이전 CLAUDE.md(e4c36bf 시기)를 설명하고 있습니다. | 원문 문자열: "거기 적힌 순서대로 인계 메모(HANDOFF.md)와 작가의 결정과 취향을 정리한 문서(AUTHOR_PREFS.md)를 이어서 읽습니다." → 바꿀 문장: "거기 적힌 순서대로 원고 기준 문서(플레이북과 책 설계서), 작업 진행 방식 문서, 인계 메모(HANDOFF.md), 작가에게 묻는 질문 목록과 결정 기록을 이어서 읽습니다." (옛 기준 문서 정리가 끝난 뒤에 다시 대조) |
| 2 | 필수 | 표 5-2 첫 행 "정보가 오는 곳", 기능적 제약 칸 (R1) | "컨텍스트에는 이 네 출처를 거친 정보만 들어오므로, 출처가 없는 자료는 에이전트가 읽지 못함" | 문서와 맞지 않는 단정이고, 같은 표 셋째 행("시스템 프롬프트, 도구 정의")과도 어긋납니다. how-claude-code-works "Context Claude Code adds on its own"는 제품이 직접 더하는 컨텍스트(시스템 지침, 출력 스타일, 첨부 줄)를 밝힙니다. memory 문서는 자동 메모리(MEMORY.md의 첫 200줄 또는 25KB)가 매 세션 로드된다고 합니다. context-window 문서는 훅이 더한 컨텍스트도 다룹니다. 네 출처 밖의 입력이 있습니다. 그림 5-1의 제목·접근성 설명 "네 경로로 들어갑니다"도 같은 단정입니다. | 원문 문자열: "컨텍스트에는 이 네 출처를 거친 정보만 들어오므로, 출처가 없는 자료는 에이전트가 읽지 못함" → 바꿀 문장: "컨텍스트에는 이 네 출처의 정보와 제품이 자동으로 더하는 정보(시스템 지침, 자동 메모리 등)가 들어오므로, 어느 출처에도 두지 않은 자료는 에이전트가 읽지 못함". 그림 5-1 제목과 접근성 설명의 "네 경로"는 작가·그림 담당 확인(이번엔 본문만 제안) |
| 3 | 필수 | 도입 첫 문단(3행) | "컨텍스트 엔지니어링은 모델에 넘길 정보를 선별하고 최신 상태로 유지하는 일입니다" ("Chapter 1에서 정한 대로"로 시작하는 문장 안) | R13·일관성. Chapter 1(137행)의 정의는 "모델이 응답을 생성하는 동안 필요한 정보를 선별하고 유지하는 전략"이고 Anthropic 글("curating and maintaining the optimal set of tokens")을 따릅니다. 5장은 "정한 대로"라면서 "최신 상태로"를 더해 정의가 달라졌습니다. 최신성은 이 장 둘째 문단의 주장이지 Chapter 1의 정의가 아닙니다. 핵심 정의는 작가만 바꿀 수 있습니다. | 원문 문자열: "컨텍스트 엔지니어링은 모델에 넘길 정보를 선별하고 최신 상태로 유지하는 일입니다" → 바꿀 문장: "컨텍스트 엔지니어링은 모델이 응답을 생성하는 동안 필요한 정보를 선별하고 유지하는 전략입니다". 최신성 문장은 "그래서 필요한 자료가 없거나 오래된 자료가 남아 있으면…"이 이미 맡고 있음 |
| 4 | 권고 | 미리 제공하는 정보와 필요할 때 찾는 정보, 두 방법의 설명 문단(39행) (낡음 가능성, R4) | "Claude Code는 CLAUDE.md를 작업 전에 컨텍스트에 포함하고, 파일은 이름 패턴으로 찾는 glob과 내용으로 찾는 grep 같은 도구로 필요할 때 찾습니다" | 2025-09 글의 서술을 현재 제품 동작처럼 씁니다. tools-reference(Glob tool behavior)에 따르면 macOS, Linux, WSL에서는 Glob과 Grep이 기본 도구 집합에 없고, Claude가 Bash의 find와 grep(내장 bfs, ugrep)으로 검색합니다. Windows는 기본 도구입니다. 원리(필요할 때 검색)는 같습니다. | 원문 문자열: "Claude Code는 CLAUDE.md를 작업 전에 컨텍스트에 포함하고, 파일은 이름 패턴으로 찾는 glob과 내용으로 찾는 grep 같은 도구로 필요할 때 찾습니다" → 바꿀 문장: "글은 Claude Code가 CLAUDE.md를 작업 전에 컨텍스트에 포함하고, 파일은 이름 패턴으로 찾는 glob과 내용으로 찾는 grep 같은 검색으로 필요할 때 찾는다고 설명합니다". 필요하면 버전 주석(2026년 10월)에 "지금 Claude Code 문서는 macOS, Linux, WSL에서 find와 grep을 Bash로 실행한다고 안내합니다[tools-reference]" 추가. tools-reference는 bibliography에 이미 있음 |
| 5 | 권고 | 같은 절, 36행 (R4, 인용 범위) | "글은 많은 AI 네이티브 애플리케이션이 임베딩 기반 검색으로 중요한 자료를 모델이 추론하기 전에 찾아 둔다고 설명합니다" | 원문은 "many AI-native applications employ some form of embedding-based pre-inference time retrieval"입니다. research C5-7은 "어떤 형태로든"으로 맞췄다고 기록했지만 현재 본문에는 그 구가 없어 범위가 넓어졌습니다. | 원문 문자열: "많은 AI 네이티브 애플리케이션이 임베딩 기반 검색으로" → 바꿀 문장: "많은 AI 네이티브 애플리케이션이 어떤 형태로든 임베딩 기반 검색으로" |
| 6 | 권고 | 같은 절, 37~38행 (R4·R11, 인용 누락) | "같은 글에 따르면 미리 제공하는 방법은 실행 중에 탐색하지 않으므로 빠를 수 있습니다." / "도구와 탐색 기준이 없으면 관련 없는 탐색을 이어 가며 컨텍스트를 낭비할 수도 있습니다." | 두 문장 모두 "같은 글에 따르면" 계열인데 인용 번호가 없습니다. 원문 근거: "runtime exploration is slower than retrieving pre-computed data", "an agent can waste context by misusing tools, chasing dead-ends". 같은 문단의 "미리 찾아 둔 범위 밖의 자료가 …" 문장은 글에 없는 이 책의 추론이라, 인용을 붙이면 안 됩니다. | 37행의 "…빠를 수 있습니다." 뒤(마침표 앞)와 38행 문장 끝에 context-engineering 인용 추가. "반면 미리 찾아 둔 범위 밖의 자료가…" 문장은 인용 없이 둡니다(이 책의 정리임을 앞 문장 구조로 구분) |
| 7 | 권고 | 컨텍스트는 한정된 자원, 10행 (R11, 인용이 주장을 일부만 받침) | "관련 없는 작업으로 넘어갈 때는 /clear 명령으로 새 대화를 시작하고, 긴 대화는 /compact 명령으로 요약해 공간을 확보할 수 있습니다[commands]" | commands는 명령의 뜻(새 대화, 요약으로 공간 확보)만 받칩니다. "관련 없는 작업으로 넘어갈 때"라는 사용 시점은 context-window("Clear between tasks: run /clear when switching to unrelated work")와 costs 문서에 있습니다. 인용 하나에 문서 하나 원칙상 문서가 맞지 않습니다. | 원문 문자열: "관련 없는 작업으로 넘어갈 때는 /clear 명령으로 새 대화를 시작하고," → 바꿀 문장: "/clear 명령은 새 대화를 시작하고," 로 줄여 commands 인용에 맞추거나, 시점 문장을 분리해 context-window 인용을 붙임. 권장은 앞의 축약 |
| 8 | 권고 | 에이전트가 읽는 정보의 종류, 15행 (R11, 인용 위치) | "Skill은 필요할 때 읽히는 지침과 자료의 묶음으로, 기본 설정에서는 이름과 설명만 늘 컨텍스트에 있고 본문은 필요할 때 읽힙니다. 경로별 규칙은 지정한 경로의 파일을 다룰 때 읽히는 규칙입니다[context-window][skills]." | 인용 두 개가 두 문장 끝에 겹쳐 있어 어느 문서가 어느 주장을 받치는지 알 수 없습니다. Skill 문장은 skills(다만 근거는 "description always in context"이고 이름은 목록 표시), 경로별 규칙은 context-window의 "path-scoped rules load automatically alongside matching files"가 받칩니다. | Skill 문장 끝에 skills 인용을, 경로별 규칙 문장 끝에 context-window 인용을 각각 한 개씩 붙임(지금의 겹침 제거) |
| 9 | 권고 | 같은 절 표 5-1 캡션과 15행 (일관성, R2) | "상시 규칙만 매 세션 읽히고, 나머지 세 종류는 조건이나 작업에 따라 들어옴" | 15행이 Skill의 이름과 설명은 늘 컨텍스트에 있다고 하므로 캡션과 어긋납니다. memory 문서는 자동 메모리와 paths 없는 `.claude/rules/`도 시작 때 로드된다고 합니다. 분류에 자동 메모리가 없다는 점은 작가 확인 사항입니다. | 원문 문자열: "상시 규칙만 매 세션 읽히고, 나머지 세 종류는 조건이나 작업에 따라 들어옴" → 바꿀 문장: "상시 규칙은 매 세션 읽히고, 나머지 세 종류의 본문은 조건이나 작업에 따라 들어옴" |
| 10 | 권고 | 표 5-2 셋째 행 "컨텍스트 윈도", 기능적 제약 칸 (R4) | "네 종류와 시스템 프롬프트, 도구 정의가 같은 한도를 나누어 씀" | 인용이 없습니다. 도구 정의는 research 2026-10-23 기록에서 "context-window 문서에 명시 문장 없음"으로 남았습니다. 근거가 되는 곳: agent-loop 문서 "Keep context efficient"(2장 점검 보고 #1이 확인)에 "Every tool definition takes context space"가 있고, 핵심 내장 도구는 매 요청에 정의가 들어가며 MCP 도구는 기본 지연 로드로 이름과 서버 안내만 들어갑니다(how-claude-code-works). | 원문 문자열: "네 종류와 시스템 프롬프트, 도구 정의가 같은 한도를 나누어 씀" → 바꿀 문장: "네 종류와 시스템 프롬프트, 도구 정의(MCP 도구는 기본 설정에서 이름과 서버 안내만)가 같은 한도를 나누어 씀<sup class=\"cite\" data-ref=\"how-cc-works\"></sup>" (how-cc-works가 이름만 들어간다는 부분을 받침. "핵심 내장 도구의 정의는 매 요청에"까지 쓰려면 agent-loop 인용 추가) |
| 11 | 권고 | 미리 제공하는 정보와 필요할 때 찾는 정보, 하위 에이전트 문단(42행) (R2) | "새 컨텍스트에서 시작해 주 대화(사람과 에이전트가 주고받는 세션의 대화)의 내용을 보지 못하고, 위임할 때 받은 지시와 규칙 문서(CLAUDE.md)를 근거로 작업합니다." | sub-agents 문서 "What loads at startup": 내장 Explore와 Plan은 CLAUDE.md를 읽지 않고, 사용자 정의 하위 에이전트도 `omitClaudeMd`를 설정하면 읽지 않습니다. 주 대화의 자동 메모리도 하위 에이전트에 전달되지 않습니다(memory 문서). 예제의 reviewer(사용자 정의, 설정 없음)는 CLAUDE.md를 읽으므로 예제는 맞습니다. | 원문 문자열: "위임할 때 받은 지시와 규칙 문서(CLAUDE.md)를 근거로 작업합니다." → 바꿀 문장: "위임할 때 받은 지시와 규칙 문서(CLAUDE.md)를 근거로 작업합니다(내장 Explore와 Plan, `omitClaudeMd`를 설정한 하위 에이전트는 규칙 문서를 읽지 않음)." |
| 12 | 권고 | 규칙 문서의 작성, 버전 주석(60행) (R8·R2) | "저장소에 CLAUDE.md가 없고 AGENTS.md만 있으면 AGENTS.md를 읽는다고 안내합니다." | memory 문서 "When Claude Code reads AGENTS.md": 작업 폴더나 그 위 폴더에 CLAUDE.md(`.claude/CLAUDE.md`, `CLAUDE.local.md` 포함)가 없을 때 읽습니다. 기준은 "저장소"가 아니라 작업 폴더와 상위 폴더입니다. 또한 v2.1.280 이전에는 `/memory`와 `/context`가 직접 읽은 AGENTS.md를 목록에 보이지 않아, 표 5-7 첫 행(Memory files)으로 확인하려면 버전을 봐야 합니다. | 원문 문자열: "저장소에 CLAUDE.md가 없고 AGENTS.md만 있으면 AGENTS.md를 읽는다고 안내합니다." → 바꿀 문장: "작업 폴더와 그 위 폴더에 CLAUDE.md가 없고 AGENTS.md만 있으면 AGENTS.md를 읽는다고 안내합니다." (v2.1.280 이전 `/context` 목록 문제는 작가 확인 후 추가) |
| 13 | 권고 | 표 5-3 넷째 행 "컨텍스트 윈도를 넘는 긴 작업", 기능적 제약 칸 (R16) | "덜어 낸 정보 가운데 무엇을 남길지는 사람이 정해야 함" | 압축은 모델이 요약하고(how-claude-code-works), 구조화된 노트는 에이전트가 쓰며, 사람은 `/compact` 지시나 CLAUDE.md의 "Compact Instructions" 절로 안내합니다. "사람이 정해야 함"은 이 책의 설계 주장이고 제품이 사람에게 맡기는 일이 아닙니다. 표 5-4 캡션 "정해야 함"과도 주체가 다릅니다. | 원문 문자열: "덜어 낸 정보 가운데 무엇을 남길지는 사람이 정해야 함" → 바꿀 문장: "덜어 낸 정보 가운데 무엇을 남길지는 요약 지시, 노트 형식, 위임 지시로 사람이 안내해야 함" |
| 14 | 권고 | 표 5-4 셋째 행, 역할 칸 (R4, 발표 주체) | "분리된 컨텍스트에서 탐색하고 요약(흔히 1,000~2,000 토큰)만 돌려줌[context-engineering]" | 수치는 글이 하위 에이전트 구조 일반에 대해 "often 1,000-2,000 tokens"라고 쓴 값입니다. 표에는 주체가 없고 Claude Code 하위 에이전트의 제품 제한으로 읽힐 수 있습니다(sub-agents 문서에는 이 수치가 없음). 본문에는 이미 "같은 글은 … 소개합니다" 문장이 있습니다. | 원문 문자열: "요약(흔히 1,000~2,000 토큰)만 돌려줌" → 바꿀 문장: "요약(글은 흔히 1,000~2,000 토큰이라고 설명)만 돌려줌" |
| 15 | 권고 | 규칙 문서의 작성, 61행 (R13) | "Claude Code 문서의 CLAUDE.md 작성 안내는 다음 네 가지로 정리할 수 있습니다" | memory 문서의 구조는 "concrete enough to verify" 한 항목과 "Size, Structure, Consistency" 세 항목입니다. 원고의 "나누어서"는 Size 항목의 path-scoped 분리 안내와 "When to add"의 skill 이동 안내에서 이 책이 만든 항목이고, 문서의 Structure("제목과 목록으로 묶기")는 빠졌습니다. 내용 자체는 문서와 어긋나지 않습니다. | 원문 문자열: "Claude Code 문서의 CLAUDE.md 작성 안내는 다음 네 가지로 정리할 수 있습니다" → 바꿀 문장: "Claude Code 문서의 CLAUDE.md 작성 안내를 이 책은 다음 네 가지 기준으로 정리합니다" |
| 16 | 권고 | 예제 절, 72행 (R4) | "reference/ 폴더의 예시 파일은 Claude Code가 자동으로 읽지 않습니다." | 로드 규칙(CLAUDE.md, `.claude/rules/`, 하위 폴더의 CLAUDE.md, 가져온 파일)상 맞지만 인용이 없습니다. 제품 동작 주장입니다. | 문장 끝에 memory 인용 추가(문서 하나) |
| 17 | 참고 | 도입과 1장 전체, 발표 주체 표기 판정 | 5장 8행, 36행, 56행 "Anthropic의 컨텍스트 엔지니어링 글" / 1장 137행, 177행 "Claude Code의 컨텍스트 엔지니어링 글" | 글은 Anthropic Applied AI 팀이 쓴 "AI 에이전트를 위한" 일반 글이고 화자는 "At Anthropic, we"입니다. 제품 설명이 아닙니다. BOOK_SPEC 7절의 "제품과 무관한 글은 회사 이름", 플레이북 7.1의 "엔지니어링 글을 제품이 말한 것처럼 쓰지 않는다"에 맞는 쪽은 5장(와 4장)의 "Anthropic의"입니다. 다만 7절 문구("Claude Code의 … 글은"처럼 글을 주어로)는 예시 형태라서 1장 표기를 바로 틀렸다고 단정하기 어렵습니다. 5장 39행 "같은 글은 Claude Code를 혼합 방식의 예로 듭니다"는 글을 주어로 둔 서술이라 문제없습니다. | 5장은 유지. 1장 두 곳은 이 장 범위 밖이며 Q-039, Q-101(작가 결정 대기)에 이미 올라 있어 "Anthropic의 컨텍스트 엔지니어링 글"로 맞추는 안을 그대로 권합니다 |
| 18 | 참고 | 에이전트가 읽는 정보의 종류, 32행 | "Codex로 제품을 개발한 OpenAI의 팀은 지침을 AGENTS.md 한 파일에 모두 담는 방식이 기대만큼 작동하지 않았다고 밝히고, 약 100줄의 AGENTS.md가 세부 문서의 위치를 안내하는 구성을 쓴다고 설명했습니다" | 미확인. openai.com 계열 주소 DNS 실패. 찾은 범위: 검색 결과 요약(Ryan Lopopolo, 2026-02-11, AGENTS.md를 목차로 쓰고 거대한 파일은 실패했다는 2차 서술, 약 100줄을 말하는 2차 글 하나)이 원고와 방향은 같지만 2차 출처라 일치 판정에 쓰지 않습니다. research/ch01-sources.md S2(2026-10-04)에 의존하며 "큰 AGENTS.md 하나는 실패"로 기록되어 있어, "기대만큼 작동하지 않았다"는 완화된 옮김입니다. 주어 "OpenAI의 팀은"은 BOOK_SPEC 7절의 "글을 주어로"와 다릅니다(Q-101 범주). | 원문을 열 수 있는 환경에서 재확인(Q-030 유지). 확인 전에는 문장을 바꾸지 않음 |
| 19 | 참고 | 규칙 문서의 작성, 59행 | "Claude Code는 CLAUDE.md를, Codex는 AGENTS.md를 읽습니다." | Claude Code 쪽은 일치. Codex 쪽은 developers.openai.com DNS 실패로 미확인(Q-132). 찾은 범위: ch03-10-sources.md의 기존 Codex 문서 기록(AGENTS.override.md → AGENTS.md → 대체 이름 순)만 있음 | 그대로 두고 10장 정비 때 재확인 |
| 20 | 참고 | 규칙 문서의 관리, 67행 | "수정하거나 삭제할 항목은 폴더 구조나 명령이 변경되었을 때, 같은 내용이 다른 문서에 생겼을 때, 문서가 권장 길이를 넘었을 때 찾아봅니다." | 인용이 없고 이 책의 기준입니다. memory 문서는 "정기적으로 검토해 오래되거나 충돌하는 지침을 제거"만 안내하고, 200줄을 넘으면 시작 때와 `/status`에서 경고하는 것도 문서에 있습니다. 필수는 아님 | 이 책의 기준이면 "이 책은 … 찾아보도록 권합니다"로 주체를 밝히거나 그대로 둠 |
| 21 | 참고 | 예제 절, 90행 | "이전 세션을 이어 가지 않고(claude --continue) 새로 시작한 세션에는" | how-claude-code-works: `claude --continue`는 직전 세션을 같은 세션 ID로 다시 열어 새 메시지를 덧붙이는 명령입니다. 문장은 "claude --continue로 이어 가지 않고"의 뜻이지만 괄호가 "새로 시작한 세션"에 붙은 것처럼 읽혀 입문 독자가 `--continue`를 새로 시작하는 명령으로 오해할 수 있습니다. 사실 오류는 아님 | 원문 문자열: "이전 세션을 이어 가지 않고(claude --continue) 새로 시작한 세션" → 바꿀 문장: "claude --continue로 이전 세션을 이어 가지 않고 새로 시작한 세션" |
| 22 | 참고 | 규칙 문서의 작성·확인 방법 | (원고에 없음) | 실무 주의점 후보. (a) CLAUDE.md는 작업 폴더와 그 위 폴더에서 시작 때 읽히고 하위 폴더의 것은 필요할 때 읽힙니다(memory). 세션을 어느 폴더에서 시작했는지에 따라 읽히는 규칙 문서가 달라집니다. (b) 규칙 문서의 수정은 새 메시지부터 적용되지 않고 새 세션에서 반영되는지 이번에 문서에서 직접 문장을 찾지 못해 미확인입니다. (c) `/init`은 CLAUDE.md 초안을 만듭니다. 장 범위 밖이면 생략 가능 | 작가 판단. 필요하면 부록 실습 2에 "예제 폴더에서 Claude Code를 시작했는지 `/context`로 확인" 안내 |

## 실행 기록
확인일 2026-10-24, 브랜치 ch05-playbook, 로컬 Claude Code 2.1.310.

```
$ wc -l examples/expense-app/reference/CLAUDE.example.md
32 examples/expense-app/reference/CLAUDE.example.md
$ grep -n '^## ' examples/expense-app/reference/CLAUDE.example.md
3:## 목적 / 6:## 읽는 순서 / 12:## 작업 순서 / 19:## 수정 범위 / 24:## 중단 규칙 / 28:## 명령   (6개)
$ python3 -c "d=open(...,'rb').read(); print(d.count(b'\n'), d.endswith(b'\n'), len(d.decode().splitlines()))"
32 True 32
```

발췌 코드 상자(73~81행)는 `<pre>` 안의 줄을 `html.unescape`한 뒤 원본 파일 줄과 한 줄씩 대조해 9줄(빈 줄 포함) 모두 원본에 있음을 확인했습니다.

표 5-7 "규칙의 실제 준수" 행의 명령 검증(임시 저장소 scratchpad/ch05fc/demo):
```
$ git show --stat HEAD     ->  tasks.json | 4 ++--   (1 file changed, 2 insertions(+), 2 deletions(-))   # 어느 값이 바뀌었는지 알 수 없음
$ git show HEAD -- tasks.json  ->  - {"작업":2,"통과":false} / + {"작업":2,"통과":true} ...           # 줄 단위 차이 확인 가능
```

`git log` 확인: `git log --oneline -1`은 127065a "5장: 실습 점검 반영(표 5-7 확인 방법, 부록 실습 5 확인 명령)". 루트 CLAUDE.md는 7a2942c에서 교체되어 AUTHOR_PREFS.md를 "정리 예정"으로 분류합니다.

## research/ch05-sources.md에 덧붙일 기록 문안
```
## C5-9. 5장 사실 점검(fact-checker, 2026-10-24, HEAD 127065a)
확인일 2026-10-24. 원문은 영어, 인용은 짧게. 로컬 Claude Code 2.1.310.
- Anthropic, How Claude remembers your project (https://code.claude.com/docs/en/memory): "target under 200 lines per CLAUDE.md file", 추가 시점 네 가지, "may pick one arbitrarily", "context, not enforced configuration ... PreToolUse hook", @path 가져온 파일은 가져오는 CLAUDE.md와 함께 로드. AGENTS.md는 "no CLAUDE.md in your working directory or above it"일 때 읽음, v2.1.277 이상, Bedrock과 텔레메트리 끈 세션은 v2.1.281 미만에서 불가, v2.1.280 미만은 /memory와 /context 목록에 직접 읽은 AGENTS.md가 보이지 않음. 압축 뒤 루트 CLAUDE.md는 다시 주입, 하위 폴더 CLAUDE.md와 paths 규칙은 on demand. 하위 에이전트의 자동 메모리는 전달되지 않고 포크는 예외.
- Anthropic, Explore the context window (https://code.claude.com/docs/en/context-window), "What survives compaction": 루트 CLAUDE.md와 paths 없는 규칙은 디스크에서 재주입, paths 규칙과 하위 폴더 CLAUDE.md는 on demand 재로드이며 메시지 이력에 있다가 요약에 묻힘. Skill 설명 재주입은 v2.1.304 이상.
- Anthropic, How Claude Code works (https://code.claude.com/docs/en/how-claude-code-works): "When context fills up"(오래된 도구 출력 먼저 삭제, 이어서 요약), "The context window", "Context Claude Code adds on its own"(제품이 직접 더하는 컨텍스트가 네 출처 밖에 있음), 하위 에이전트는 포크가 아니면 새로 시작, `claude --continue`와 `--resume`은 같은 세션 ID로 다시 열기.
- Anthropic, Create custom subagents (https://code.claude.com/docs/en/sub-agents), "What loads at startup": 비포크는 대화 기록 불가, 시스템 프롬프트, 위임 메시지, CLAUDE.md 계층, git 상태를 받음. Explore와 Plan은 CLAUDE.md와 git 상태를 받지 않음. `omitClaudeMd`로 제외 가능. 포크는 부모 대화를 상속하며 인터랙티브 세션에서 기본 켜짐(CLAUDE_CODE_FORK_SUBAGENT=0으로 끔).
- Anthropic, Tools reference (https://code.claude.com/docs/en/tools-reference), "Glob tool behavior": macOS, Linux, WSL에서는 Glob과 Grep이 기본 도구 집합에 없고 Bash의 find와 grep(내장 bfs, ugrep)으로 검색. Windows는 기본 도구. (원고 39행 "glob, grep 같은 도구"의 현재 동작 조건)
- Anthropic, Extend Claude with skills (https://code.claude.com/docs/en/skills): 설명(description)이 상시 컨텍스트, 목록에는 이름도 표시, 본문은 호출될 때 로드, disable-model-invocation: true이면 설명도 컨텍스트에 없음. 설명과 when_to_use는 목록에서 1,536자에서 잘림.
- Anthropic, Commands (https://code.claude.com/docs/en/commands): /context [all], /clear, /compact 설명이 원고와 일치. 사용 시점("관련 없는 작업으로 넘어갈 때")은 context-window의 "Clear between tasks"에 있고 commands에는 없음.
- Anthropic, Embeddings (https://platform.claude.com/docs/en/build-with-claude/embeddings): "Text embeddings are numerical representations of text that let you measure semantic similarity". 원고 임베딩 풀이와 일치.
- Rajasekaran 외(Anthropic, 2025-09-29) 재열람: "context ... must be treated as a finite resource", "embedding-based pre-inference time retrieval"("many AI-native applications employ some form of"), "runtime exploration is slower than retrieving pre-computed data", "smallest possible set of high-signal tokens", "often 1,000-2,000 tokens", "overly aggressive compaction", "Like Claude Code creating a to-do list", 화자 "At Anthropic, we", 저자 Applied AI 팀(Rajasekaran, Dixon, Ryan, Hadfield).
- 예제 대조: CLAUDE.example.md wc -l 32, 여섯 절, 끝 줄바꿈 있음. 발췌 코드 상자 9줄이 원본과 글자까지 같음. settings.example.json deny 6경로 일치. 표 5-7의 git show --stat HEAD는 파일 단위 통계만 보여 통과 값 한 개만 바뀌었는지는 git show HEAD -- tasks.json으로 확인해야 함(임시 저장소에서 재현, 127065a에서 이미 반영).
- 발표 주체 판정: 컨텍스트 엔지니어링 글은 Anthropic Applied AI 팀의 에이전트 일반 글이므로 5장 "Anthropic의"가 글의 화자와 맞음. 1장 "Claude Code의 …"는 Q-039, Q-101 대기.
- 미확인: OpenAI Harness engineering(openai.com DNS 실패, 2차 요약은 방향만 같음, "기대만큼 작동하지 않았다"는 S2의 "실패"를 완화한 옮김), Codex가 AGENTS.md를 읽는다는 문장(developers.openai.com DNS 실패), PowerShell 실행(이 환경에 pwsh 없음, 2026-10-23 기록 의존).
- 원고 대조 불일치(권고 4~16과 필수 1~3 참조): 루트 CLAUDE.md 읽는 순서와 AUTHOR_PREFS.md, "정보가 오는 곳" 단정, 컨텍스트 엔지니어링 정의의 "최신 상태로".
```

## bibliography.json 새 키
필수는 없습니다. 모두 기존 키(tools-reference, agent-loop, how-cc-works, memory, context-window, skills)로 인용할 수 있습니다. 임베딩 풀이에 인용을 붙이기로 하면 다음 키를 추가할 수 있습니다(선택).
```
"embeddings": {"type": "web", "author": "Anthropic", "title": "Embeddings", "venue": "Claude Code Docs가 아니라 Claude Docs", "url": "https://platform.claude.com/docs/en/build-with-claude/embeddings"}
```
(venue 칸은 기존 platform.claude.com 항목들의 표기와 같게 맞추세요. 예: prompt-overview의 venue 형식)

필수 3, 권고 13, 참고 6, 확인한 사실 문장 약 80개.

(참고: 본문 표는 번호 1~22이고, 필수 3은 1~3번, 권고는 4~16번(13개), 참고는 17~22번(6개)입니다. 결론 첫 줄의 "권고 12"는 13으로 바로잡습니다.)
