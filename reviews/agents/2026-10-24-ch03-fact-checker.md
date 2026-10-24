# 3장 사실 점검(fact-checker, 2026-10-24, 커밋 1024254)

# 3장 사실 점검 (fact-checker, 2026-10-24, 브랜치 ch03-playbook)

**결론: 필수 1, 권고 7, 참고 7 (확인한 사실 문장 약 48개).** 원고와 파일은 고치지 않았습니다. 임시 파일은 /tmp/claude-0/-home-user-harness-book/4fa31d71-64a2-5605-bad4-d31a3ffd2331/scratchpad/ch03fc/ 아래에만 만들었습니다. 로컬 Claude Code는 2.1.310이고, 기준 문서는 모두 2026-10-24에 code.claude.com에서 다시 열었습니다. 대화형 화면(TUI)은 열 수 없어 화면에 보이는 모습은 확인하지 못했습니다.

## 일치로 판정한 문장 (표에는 올리지 않음)
- **Edit 규칙의 적용 범위**: 내장 편집 도구 전체에 적용됩니다(permissions 문서 "Read and Edit" 절 "Edit rules apply to all built-in tools that edit files"). tools-reference의 규칙 표에는 Edit, Write, NotebookEdit이 함께 나옵니다.
- **\*\* 와 \***: 두 기호 모두 gitignore 방식입니다(permissions 문서 경로 규칙 절). `*`는 한 경로 마디 안에서, `**`는 폴더를 넘어서 일치합니다. Bash 규칙의 `*`는 그 자리의 아무 텍스트와 일치합니다("The * stands in for whatever text is in its place").
- **`./` 경로**: `path`와 `./path`는 현재 디렉터리 기준입니다(같은 절). 원고가 시작 위치를 "실습 폴더(examples/expense-app/)에서 시작"으로 전제한 것도 맞습니다.
- **Edit 금지 규칙의 한계**: 내장 도구, Bash가 알아보는 파일 명령(cat, sed, tee 등), 리다이렉션에는 적용됩니다. 파일을 스스로 여는 Python 스크립트에는 적용되지 않습니다(같은 절 NOTE). 대응하는 OS 수준 차단은 샌드박스입니다.
- **git -C . push**: "What a Bash rule doesn't match" 표에서 `Bash(git push *)`가 `git -C . push origin main`을 막지 못한다고 합니다.
- **평가 순서와 도구 이름만 쓴 금지 규칙**: deny, ask, allow 순서입니다. 도구 이름만 쓴 금지 규칙은 도구를 컨텍스트에서 없앱니다("removes the tool from Claude's context entirely").
- **WebFetch와 WebSearch가 기본 도구인지**: tools-reference 표에 둘 다 내장 도구로 나옵니다.
- **권한 모드**: Manual의 설정 값은 `default`입니다. `--permission-mode`는 `default`를 받고, `permissions.defaultMode`로도 지정할 수 있습니다. 이 플래그는 settings의 defaultMode를 덮어씁니다(permission-modes 문서, cli-reference의 `--permission-mode` 행). 금지 규칙과 ask 규칙은 auto 모드에서도 적용됩니다.
- **`--max-turns`와 `--max-budget-usd`**: 둘 다 "print mode only"입니다(cli-reference). 기본값은 제한 없음입니다.
- **훅**:
  - `matcher: "Edit|Write"`는 두 도구 이름과 정확히 일치합니다.
  - `$CLAUDE_PROJECT_DIR`은 "the project root where the session started"입니다.
  - PostToolUse의 종료 코드 2는 "Shows stderr to Claude; the tool already ran"입니다. PreToolUse의 종료 코드 2는 호출을 막습니다.
  - `/hooks`는 읽기 전용 목록입니다. 훅을 고르면 전체 명령과 정의 위치가 보입니다.
- **하위 에이전트**: `tools`를 생략하면 "Inherits every tool available to subagents"입니다. `tools`는 허용 목록이고, 필수 항목은 name과 description뿐입니다. 프로젝트 정의 위치는 `.claude/agents/`입니다. Grep과 Glob은 macOS, Linux, WSL의 기본 도구 집합에 없지만, 하위 에이전트가 `tools`에 적고 Bash를 빼면 그 하위 에이전트에서는 쓸 수 있습니다(tools-reference Glob 절). 그래서 reviewer의 `tools: Read, Grep, Glob`은 의도대로 동작합니다.
- **규칙 문서**: CLAUDE.md는 "context, not enforced configuration"입니다. memory 문서에 "no guarantee of strict compliance"가 있는지는 이번에 문구를 다시 찾지 못했습니다(memory 문서 앞부분과 research C3-6 기록으로 갈음). 규칙 문서는 매 세션 시작 때 로드됩니다.
- **명령 화면**: `/permissions`는 허용, 확인, 금지 규칙을 범위별로 보고 고치는 대화 상자입니다. `/hooks`는 "View hook configurations"입니다(commands 문서).
- **unittest의 출력 스트림**: 실행해서 확인했습니다(아래 실행 기록).
- **발표 주체와 인용**: 발표 주체 표기("Claude Code 문서는/에 따르면")는 이 장 안에서 모두 맞습니다. 인용 12개 가운데 주장을 뒷받침하지 못하는 것은 없습니다. 위치가 어긋난 곳은 아래 2번과 7번에 올렸습니다.
- **예제 사실**:
  - 설정 JSON 코드 상자는 `reference/settings.example.json`에서 python3 허용 두 줄만 뺀 것과 의미와 글자가 같습니다(`&amp;&amp;`는 `&&`의 HTML 이스케이프). 본문에도 생략했다고 밝혀 두었습니다.
  - reviewer.md 코드 상자는 `reviewer.example.md`와 글자가 같습니다(끝 줄바꿈 차이만 있음).
  - 표 3-1~3-7과 본문의 작업 1~5, 수용 기준 5개, 요청일 2026-10-05, D-012, 중단 규칙(세 번 연속 실패), 읽는 순서, 수정 범위는 `example-facts.md`, `CLAUDE.example.md`, `tasks.example.json`, `docs/CR.md`, `check.py`, `DECISIONS.md`와 일치합니다.
  - 표 3-7의 구현 전 기준 상태(수용 시험 5건 중 3건 실패, project_code 시험 0건, 종료 코드 1)는 실제 실행으로 확인했습니다.
  - 수용 시험 3은 등록 뒤 목록에 코드가 보이는지 보는 시험이라, 본문 45행의 "등록한 요청에 코드가 저장되는지는 수용 시험 3에서"가 맞습니다.

## 지적 표

| 번호 | 등급 | 위치 | 원고 문장 | 확인 결과와 1차 출처 | 고칠 문안 |
|---|---|---|---|---|---|
| 1 | 필수 (R1, R4, 7.2 같은 장 안 일관성) | files 절, 74행(금지 규칙의 한계 문단) | "대화형 세션은 버전에 따라 Claude Code가 호출을 자동으로 판단하는 auto 모드로 시작하며, 문서에 따르면 auto 모드는 작업 중인 저장소로의 push를 기본으로 허용하므로 다른 형태로 작성한 push 명령은 차단되지 않습니다." | (a) "버전에 따라"만 있고 버전이 없어 독자가 확인할 수 없습니다. permission-modes 문서 "Auto mode" 절: v2.1.283 이상에서 대화형 터미널과 VS Code가 auto로 시작합니다. 이전 버전은 Pro, Max, Team 요금제에서만 auto로 시작합니다. 설정에서 `disableAutoMode`를 지정했거나 `claude -p`, Agent SDK, HIPAA 설정이면 default로 시작합니다. (b) "차단되지 않습니다"는 단정입니다. 같은 문서는 작업 중인 저장소의 어느 브랜치로든 push는 프롬프트 없이 실행되지만 "unless the push or pull request falls under the blocked list"라고 합니다. 차단 목록에는 강제 push, 민감 정보를 저장소 밖으로 보내는 push, `production`이나 `gh-pages`처럼 배포 대상을 뜻하는 이름의 비기본 브랜치로의 push가 있습니다. 같은 장 표 3-6 넷째 행은 "auto 모드에서는 허용될 수 있음"이라고 조건을 달았습니다. 이 문단은 더 강하게 써서 일관성이 깨집니다. (c) 이 두 문장에는 인용이 없고, 인용(permission-modes)은 그 뒤 문장 끝에만 있습니다. 같은 사실을 10장 33행 버전 주석이 이미 v2.1.283 기준으로 씁니다. 근거: permission-modes 문서 "Auto mode" 절, "Setting the mode" 절, 2026-10-24. | 위 원문을 다음으로 바꿉니다. "v2.1.283 이상의 대화형 터미널과 VS Code 세션은 Claude Code가 호출을 자동으로 판단하는 auto 모드로 시작하며(이전 버전은 요금제에 따라 다름), 문서에 따르면 auto 모드는 작업 중인 저장소로의 push를 강제 push 같은 차단 대상이 아니면 기본으로 허용합니다. 그래서 다른 형태로 작성한 push 명령은 확인 없이 실행될 수 있습니다<sup class="cite" data-ref="permission-modes"></sup>." 이어지는 "이 예제의 설정 파일은 모드를 정하지 않으므로, 수동 모드로 진행하려면 …defaultMode에 default를 적습니다" 뒤의 기존 인용은 그대로 둡니다. 10장 33행 버전 주석 문구와 맞추기를 권합니다. |
| 2 | 권고 (R11, 인용 위치) | 같은 문단 | "Claude Code 문서에 따르면 Edit 금지 규칙은 …에이전트가 실행한 스크립트가 파일을 직접 여는 경우에는 적용되지 않습니다." | 이 문장은 인용 없이 끝나고, 다음 문장 끝의 permissions 인용이 받칩니다. 근거 자체는 permissions 문서 "Read and Edit" 절 NOTE로 맞습니다. 위치가 문장과 떨어져 있어 R11(한 문장에 한 근거)을 약하게 지킵니다. | "에이전트가 실행한 스크립트가 파일을 직접 여는 경우에는 적용되지 않습니다." → "에이전트가 실행한 스크립트가 파일을 직접 여는 경우에는 적용되지 않습니다<sup class=\"cite\" data-ref=\"permissions\"></sup>." |
| 3 | 권고 (R8, 실무 3번) | 훅 문단, 110행 | "$CLAUDE_PROJECT_DIR은 Claude Code가 프로젝트 폴더의 경로를 담아 주는 환경 변수입니다." / "훅의 명령은 세션의 현재 폴더에서 실행됩니다" | hooks 문서: 핸들러는 "run in the current directory"에서 실행되고, `CLAUDE_PROJECT_DIR`은 "the project root where the session started"입니다. 문서의 `cwd` 필드는 Claude가 `cd`를 한 뒤의 새 디렉터리를 가리킵니다. 그래서 "세션의 현재 폴더"는 시작 폴더로 읽히기 쉽습니다. "프로젝트 폴더"도 git 저장소 루트로 읽힐 수 있습니다. 이 예제는 저장소 루트가 아니라 `examples/expense-app/`(또는 복사한 실습 폴더)에서 시작한다고 전제하므로, 루트에서 시작하면 `tests` 폴더가 없어 훅이 매번 실패합니다. 이 점은 본문 전제 문장이 있어 틀리지는 않고 오해 소지입니다. 근거: hooks 문서 "Handlers run in the current directory…" 문장과 "CLAUDE_PROJECT_DIR" 설명, 2026-10-24. | "훅의 명령은 세션의 현재 폴더에서 실행됩니다" → "훅의 명령은 Claude Code의 현재 작업 폴더에서 실행되며, 작업 폴더는 Claude가 cd로 옮기면 따라 바뀝니다". "$CLAUDE_PROJECT_DIR은 Claude Code가 프로젝트 폴더의 경로를 담아 주는 환경 변수입니다." → "$CLAUDE_PROJECT_DIR은 Claude Code가 세션을 시작한 프로젝트 폴더의 경로를 담아 주는 환경 변수입니다." |
| 4 | 권고 (R1, 실무 2·3번) | files 절, 72행 | "Edit 규칙은 파일을 수정하거나 새로 작성하는 Claude Code의 편집 도구(Edit, Write) 전체에 적용되고, Bash 규칙은 명령 실행 도구(Bash)에 적용됩니다." | 문장은 맞습니다. 실무에서 틀리게 이어지는 부분이 둘 있습니다. permissions 문서의 "`Write(path)`, `NotebookEdit(path)`, and `Glob(path)` rules never match" 절은 `Write(./data/**)` 같은 규칙은 받아들이지만 어떤 수정과도 일치하지 않으므로 경로 규칙은 `Edit(path)`로 쓰라고 합니다. 또 Edit 규칙의 대상은 NotebookEdit까지 포함합니다. 반면 이 장의 훅 matcher `Edit\|Write`는 NotebookEdit에서 실행되지 않습니다(hooks 문서의 정확 일치). 근거: permissions 문서 "Read and Edit" 절, 2026-10-24. | "Bash 규칙은 명령 실행 도구(Bash)에 적용됩니다." → "Bash 규칙은 명령 실행 도구(Bash)에 적용됩니다. 파일 경로 규칙은 Write(경로)로 쓰지 않고 Edit(경로)로 씁니다. Write(경로) 규칙은 어떤 수정과도 일치하지 않습니다<sup class=\"cite\" data-ref=\"permissions\"></sup>." |
| 5 | 권고 (R7) | 표 3-2 권한 행과 도구 행 | "허용: 테스트와 검사 스크립트 실행. 확인 요청: commit." / "파일 읽기와 수정, 테스트 실행, git 상태 확인과 commit(웹 접근 도구는 제외)" | `docs/example-facts.md` "권한" 절과 `settings.example.json`의 허용은 단위 테스트, `python check.py`, `git status`, `git diff *` 네 가지입니다. 표는 git status와 git diff 허용을 빼서 /permissions 확인 기준(표 3-7)이나 CLAUDE.md 작업 순서(git status, git diff 출력을 reviewer에 전달)와 맞춰 읽을 때 빠진 느낌을 줍니다. 표 3-2 도구 행도 "git 상태 확인"만 있고 diff가 없습니다. 값 불일치라기보다 누락입니다. | "허용: 테스트와 검사 스크립트 실행. 확인 요청: commit." → "허용: 테스트와 검사 스크립트 실행, git status, git diff. 확인 요청: commit." / "파일 읽기와 수정, 테스트 실행, git 상태 확인과 commit(웹 접근 도구는 제외)" → "파일 읽기와 수정, 테스트 실행, git 상태와 변경 내용 확인, commit(웹 접근 도구는 제외)" |
| 6 | 권고 (R1, 실무 3번 비용과 한도) | 48행 | "이 예제는 사람이 지켜보는 대화형 세션에서 진행하므로 상한 대신 완료 판정과 중단 규칙으로 종료 조건을 정했습니다." (앞 문장의 -p 전용 서술은 일치) | 본문은 "-p 전용"까지만 쓰고 상한의 성격을 쓰지 않습니다. cli-reference의 `--max-budget-usd` 행: 비용은 Claude Code의 클라이언트 쪽 추정 비용이라 청구서와 다를 수 있고, 지출이 상한을 넘을 수 있으니 여유를 두라고 합니다. 하위 에이전트의 지출도 포함됩니다. 표 3-1의 "비용 상한" 값을 정하는 독자에게 필요한 주의점입니다. 근거: cli-reference 문서 `--max-budget-usd` 행, 2026-10-24. | "이 예제는 사람이 지켜보는 대화형 세션에서 진행하므로" 앞에 문장을 하나 덧붙입니다. "--max-budget-usd의 비용은 Claude Code가 계산한 추정치라 실제 청구와 다를 수 있고, 지출이 상한을 조금 넘을 수도 있습니다." 같은 cli-reference 문서이므로 인용 키는 그대로 둡니다. |
| 7 | 권고 (R4) | 75행 | "웹 페이지를 가져오는 WebFetch와 웹을 검색하는 WebSearch는 Claude Code의 기본 도구이므로" | 사실은 맞습니다(tools-reference 표에 두 도구가 내장 도구로 나옴). 인용이 없고, 뒤의 permissions 인용은 이 문장을 받치지 않습니다. `bibliography.json`에 tools-reference 키가 없습니다. | "Claude Code의 기본 도구이므로" → "Claude Code의 기본 도구<sup class=\"cite\" data-ref=\"tools-reference\"></sup>이므로". 새 키가 필요합니다(아래 bibliography.json 항목). 위첨자를 문장 가운데 두지 말라는 규칙(7.4)이 걸리면 문장 끝으로 옮겨 "…이 형식의 금지 규칙으로 막습니다<sup …tools-reference></sup>"처럼 씁니다. 인용 위치는 작가 결정입니다. |
| 8 | 권고 (R8) | 111행 | "단위 테스트를 실행하는 Python의 시험 모듈(unittest)은 결과를 오류 출력에 작성하므로, 실패 내용이 모델에 전달됩니다." | 실제 실행으로 맞음을 확인했습니다(아래 실행 기록). 다만 인용이 없고 research에는 실행 기록만 있으며, Python 공식 문서(docs.python.org)는 이 환경에서 접속 실패(ENOTFOUND)로 열지 못해 "TextTestRunner의 기본 stream이 sys.stderr"라는 1차 문서 확인은 미확인입니다. | 근거를 문서로 확정하려면 `python-unittest` 키를 추가하고 문장 끝에 인용을 답니다. 작가가 열람해 확인하기 전에는 문장을 바꾸지 않습니다. 실행 확인만으로 두려면 research 기록(아래)을 남기면 됩니다. 이 문장 자체는 고치지 않아도 됩니다. |
| 9 | 참고 (실무 3번) | 110행 훅 명령 | `cd "$CLAUDE_PROJECT_DIR" && python -m unittest discover tests -q \|\| exit 2` | hooks 문서: 훅 셸은 Windows에서 Git Bash이고, Git Bash가 없으면 PowerShell입니다. 이 명령은 bash 문법이라 PowerShell에서 그대로 동작하는지는 확인하지 못했습니다(미확인, 열어 본 범위는 훅 문서의 shell 항목뿐). | Windows 독자가 있으면 한 줄을 덧붙이는 것을 검토합니다. 예: "Windows에서는 Git Bash가 있어야 이 훅 명령이 그대로 동작합니다." 이 문장은 PowerShell 실행 결과를 확인한 뒤에 쓰는 것을 권합니다. 지금은 조건부 표현으로도 쓰지 않는 편이 안전합니다. |
| 10 | 참고 (실무 3번 설정 다시 읽기) | 112행 하위 에이전트 정의 | reviewer.md 정의 | sub-agents 문서: `.claude/agents/`는 파일 변경을 감시해 다음 위임부터 반영하지만, "after creating a scope's first agent file in a new `agents` directory, restart to load it". 부록 실습 4에는 "재시작" 언급이 없습니다. 이 장 본문은 실습을 "새로 시작한 세션"이라고 가정하므로 틀리지 않으나, 실습 도중 reviewer가 보이지 않을 때의 원인입니다. | practice-checker가 실습 4에서 재현한 뒤 부록 "막혔을 때"에 한 줄 추가를 검토합니다. 3장 본문은 그대로 둡니다. |
| 11 | 참고 (R16, 장치의 역할) | 그림 3-1 "수정할 수 없는 파일", "구현 에이전트 금지" | 영역 제목과 행 | 74행이 스스로 밝힌 한계(스크립트가 직접 여는 경우는 막지 못함)보다 그림의 영역 제목이 단정적입니다. 하단 주석("에이전트의 편집 도구에는 수정 금지")과 표 3-4 해당 행("편집 도구의 수정은 금지 규칙이 막음")은 한정이 있어 맞습니다. 그림은 production-checker 범위입니다. | 그림 문구를 바꾼다면 "수정할 수 없는 파일" → "편집 도구로 수정할 수 없는 파일". 지금 상태로도 하단 주석이 한정하므로 사실 오류는 아닙니다. |
| 12 | 참고 (실무 2번) | 74행 | "설정 파일의 defaultMode에 default를 적습니다" | 설정 위치가 빠졌습니다. permission-modes 문서의 예는 `{"permissions": {"defaultMode": "default"}}`입니다. 같은 문서에서 `--permission-mode`가 settings의 defaultMode를 덮어쓴다고 합니다. 또 프로젝트 `.claude/settings.json`에서 `"auto"`는 적용되지 않지만 `"default"`는 해당 제한이 없습니다. 위 1번의 대체 문장과 이어 읽으면 문제는 없습니다. | "설정 파일의 defaultMode에 default를 적습니다" → "설정 파일의 permissions.defaultMode에 default를 적습니다". |
| 13 | 참고 (실무 2번) | 74행 | "허용 목록에 없는 명령은 실행 전에 확인을 요청하므로" | Manual 모드에서도 허용 목록 밖에 읽기 전용 명령의 내장 목록(permissions 문서 "read-only commands")은 묻지 않고 실행합니다. push에는 해당하지 않으므로 이 문단의 결론은 맞습니다. 일반 문장으로는 약간 넓습니다. | 수정 없이 둘 수 있습니다. 고친다면 "허용 목록에 없는 명령(읽기 전용 내장 명령 제외)은". |
| 14 | 참고 (미확인) | 표 3-7 훅 행 | "PostToolUse에 훅이 있고, 선택하면 단위 테스트 명령이 보임" | hooks 문서 `/hooks` 절: 읽기 전용 목록이고 훅 출처를 표시하며, 훅을 고르면 전체 명령과 정의 위치가 보입니다. 이 문장의 "단위 테스트 명령이 보임"은 일치합니다. 목록에 matcher(`Edit\|Write`)가 표시되는지는 문서 앞부분에서 찾지 못해 미확인입니다. 본문은 matcher 표시를 주장하지 않으므로 문제는 없습니다. | 수정 없음. 실습 4 실행 때 화면을 보고 RUNLOG.md에 남기는 기존 방침을 유지합니다. |
| 15 | 참고 (R8) | 62~74행 | 인용 `memory` 근거 문구 | memory 문서에서 "context, not enforced configuration"은 이번에 직접 확인했습니다. "no guarantee of strict compliance"는 research C3-6 기록(2026-10-20)이 있고 이번 조회에서는 문구를 찾지 못했습니다(문서가 길어 일부만 열람). 같은 문서가 `AGENTS.md`를 CLAUDE.md 대신 읽는다고 합니다(규칙 문서가 없을 때 다른 이름의 규칙 문서를 읽는 동작). 3장 본문은 이 동작을 주장하지 않으므로 오류는 없습니다. | 수정 없음. 두 번째 문구는 fact-checker가 전체 문서에서 다시 찾는 항목으로 남깁니다. |

(참고: 15번은 확인 범위를 알리는 행이고 문장 수정이 필요한 지적은 아닙니다. 위 결론의 참고 7은 9~15번입니다.)

## 실행 기록 (원문 요약)
- `claude --version` → `2.1.310 (Claude Code)`. Python 3.13.16.
- `cd examples/expense-app && python3 -m unittest discover tests -q 2>/dev/null | wc -c` → `0`. 같은 명령을 `2>&1`로 실행하면 `Ran 3 tests in 0.003s` / `OK`가 나옵니다. 정상 결과도 stderr로 나갑니다.
- 실패 상황의 확인: 실습 폴더를 임시 폴더(scratchpad의 ch03fc/w)로 복사해 `python3 -m unittest discover acceptance -q > out.txt 2> err.txt`를 실행했습니다. 종료 코드 1, out.txt 0바이트, err.txt 2802바이트(`FAIL: test_1_...` 등 실패 내용)였습니다. 실패 내용이 모두 stderr에 있어 PostToolUse 종료 코드 2의 stderr 전달 경로와 맞습니다.
- `python3 check.py`(원본 폴더) 출력:
  ```
  tests: 실행 3건, 실패 0건, 건너뜀 0건, project_code 시험 0건
  acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)
  exit=1
  ```
  (acceptance 쪽 FAIL은 test_1_form_offers_project_codes, test_2_unknown_code_rejected_with_reason, test_3_list_shows_project_code.) 표 3-7 "구현 전 기준 상태"와 일치합니다.
- 코드 상자 대조: `src/chapters/ch03.html`의 `<pre>` 두 개를 HTML 이스케이프를 풀어 비교했습니다. 설정 JSON은 `settings.example.json`에서 `python3` 줄 두 개를 뺀 텍스트와 글자까지 같고(`text equal: True`, JSON 의미도 같음), reviewer.md는 `reviewer.example.md`와 같습니다(끝 줄바꿈만 다름).

## research/ch03-sources.md에 덧붙일 기록 문안
```
## C3-12. fact-checker 4차 확인(2026-10-24, 브랜치 ch03-playbook, 플레이북 7장·8장 기준 점검)
- Permission modes(https://code.claude.com/docs/en/permission-modes), 확인 2026-10-24, 작성 Anthropic(게시일 표기 없음): v2.1.283 이상 대화형 터미널·VS Code는 auto로 시작, 이전 버전은 Pro·Max·Team에서만 auto로 시작. `disableAutoMode` 지정, claude -p·Agent SDK(v2.1.302부터 허용 규칙 등이 없으면 거부), HIPAA 설정(v2.1.285 이상)이면 default로 시작. auto는 작업 중인 저장소로의 push를 차단 목록(강제 push, 민감 정보 반출, production·gh-pages 같은 배포 대상 이름의 비기본 브랜치)이 아니면 프롬프트 없이 허용. deny 규칙은 모든 모드에서, ask 규칙은 auto에서도 확인 요청. 설정 값은 default(별칭 manual), 프로젝트 settings의 auto는 적용 안 됨. 3장 files 절 권한 모드 문단에 반영 필요(지적 1)
- Configure permissions(https://code.claude.com/docs/en/permissions), 확인 2026-10-24: Edit 규칙은 내장 편집 도구 전체. Write(path)·NotebookEdit(path)·Glob(path) 규칙은 받아들이지만 일치하지 않음(Edit로 씀). Read·Edit 금지는 내장 도구, Bash가 알아보는 파일 명령, 리다이렉션에 적용되고 스크립트가 직접 여는 경우는 적용 안 됨. Bash(git push *)는 git -C . push origin main, git -c push.default=current push, git 'push'를 막지 못함. 평가 순서 deny→ask→allow. `./path`는 현재 디렉터리 기준. 이름만 쓴 규칙은 도구를 컨텍스트에서 없앰
- Hooks reference(https://code.claude.com/docs/en/hooks), 확인 2026-10-24: 핸들러는 현재 디렉터리에서 실행, CLAUDE_PROJECT_DIR은 세션을 시작한 프로젝트 루트. PostToolUse 종료 코드 2는 stderr를 Claude에 보이고 도구는 이미 실행됨, PreToolUse는 호출 차단. matcher는 영문·숫자·_·-·공백·,·| 만으로 된 값이면 정확 일치 목록. /hooks는 읽기 전용 목록이고 출처를 표시하며 훅을 고르면 전체 명령과 정의 위치가 보임(matcher 표시는 미확인). 훅 셸은 기본 bash, Windows에서 Git Bash가 없으면 PowerShell. 설정 파일의 훅 변경은 파일 감시로 자동 반영(보통)
- CLI reference(https://code.claude.com/docs/en/cli-reference), 확인 2026-10-24: --max-turns와 --max-budget-usd는 print mode only, 기본값 제한 없음. --max-budget-usd는 클라이언트 쪽 추정 비용이라 청구서와 다를 수 있고 상한을 넘을 수 있으며 하위 에이전트 지출도 포함. --permission-mode는 default, acceptEdits, plan, auto, dontAsk, bypassPermissions를 받고 manual은 v2.1.200 이상의 별칭, settings의 defaultMode를 덮어씀
- Tools reference(https://code.claude.com/docs/en/tools-reference), 확인 2026-10-24: WebFetch, WebSearch, Edit, Write, NotebookEdit은 내장 도구(권한 필요 Yes). Edit(경로) 규칙의 대상은 Edit, Write, NotebookEdit. Glob·Grep은 macOS·Linux·WSL에서 기본 도구 집합에 없고(Windows는 있음), 하위 에이전트가 tools에 적고 Bash를 빼면 그 하위 에이전트에서만 쓸 수 있음
- Create custom subagents(https://code.claude.com/docs/en/sub-agents), 확인 2026-10-24: tools 생략 시 모든 도구 상속, tools는 허용 목록, 필수는 name·description, 프로젝트 정의는 .claude/agents/. agents 폴더에 처음 만든 파일은 세션 재시작 뒤 로드됨(이후 변경은 파일 감시로 반영)
- Commands(https://code.claude.com/docs/en/commands), 확인 2026-10-24: /permissions는 허용·확인·금지 규칙을 범위별로 보고 추가·삭제하는 대화 상자, /hooks는 훅 설정 보기
- How Claude remembers your project(https://code.claude.com/docs/en/memory), 확인 2026-10-24: CLAUDE.md와 자동 메모리는 매 세션 시작에 로드, "context, not enforced configuration". 강제하려면 PreToolUse 훅. AGENTS.md를 CLAUDE.md 대신 읽을 수 있음
- unittest 출력 스트림, 실행 확인 2026-10-24(fact-checker, Python 3.13.16, Linux): examples/expense-app에서 `python3 -m unittest discover tests -q 2>/dev/null | wc -c` → 0, 실패하는 시험(복사본의 acceptance) 실행 시 stdout 0바이트·stderr 2802바이트. docs.python.org는 ENOTFOUND로 열지 못해 공식 문서 확인은 미확인
- 예제 대조(2026-10-24): 3장 코드 상자 2개는 settings.example.json(python3 허용 두 줄 제외)·reviewer.example.md와 글자까지 일치. python3 check.py(구현 전) 출력은 tests 실행 3건·실패 0건·project_code 시험 0건, acceptance 실행 5건·실패 3건, exit=1. 표 3-2 권한·도구 칸은 허용 중 git status·git diff를 적지 않음(example-facts 대비 누락, 권고)
- 미확인: PowerShell에서 훅 명령(cd "$CLAUDE_PROJECT_DIR" && … || exit 2)의 동작, /hooks 목록의 matcher 표시, memory 문서의 "no guarantee of strict compliance" 재열람, Python 공식 문서의 TextTestRunner 기본 stream
```

## bibliography.json 새 키 (필요하면)
- 지적 7을 반영할 때만 필요합니다:
```json
"tools-reference": {"type": "web", "author": "Anthropic", "title": "Tools reference", "venue": "Claude Code Docs", "url": "https://code.claude.com/docs/en/tools-reference"}
```
- 지적 8을 문서 인용으로 확정할 경우(작가가 docs.python.org를 직접 열람한 뒤)에만 추가합니다:
```json
"python-unittest": {"type": "web", "author": "Python Software Foundation", "title": "unittest — Unit testing framework", "venue": "Python 3 Documentation", "url": "https://docs.python.org/3/library/unittest.html"}
```
(이 항목은 아직 열람하지 못해 제목과 문구를 확정하지 않았습니다.)

필수 1, 권고 7, 참고 7, 확인한 사실 문장 약 48개
