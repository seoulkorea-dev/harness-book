# 10장 실습 점검(practice-checker)

# Chapter 10 실습 감수 보고 (rule-docs, example, fail, check)

**요약: 필수 6, 권고 6, 참고 3** (검증 후 확정 2건은 참고에 포함)

- 코드 상자 문법은 모두 유효합니다. Claude Code 설정 JSON과 Codex config.toml은 파싱됐습니다. `prefix_rule(...)`은 Python AST로 구문만 확인했고, Starlark로는 검증하지 못했습니다.
- Claude Code 설정 상자의 deny 세 항목은 `reference/settings.example.json`의 해당 항목과 글자까지 같습니다.
- `sandbox.enabled`가 예제 파일에 없는 추가 설정이라는 점은 본문 69행에 밝혀 있습니다.
- 가장 큰 문제는 확인 표가 요구하는 준비(sandbox 설정, AGENTS.md, Codex)가 실습 폴더에 없다는 점입니다. 부록 실습 3에도 없습니다.
- 확인 표 앞 문장이 확인 시점을 밝히지 않는 점과, 웹 도구 금지에 대응하는 확인 행이 없는 점도 필수입니다.

| 번호 | 위치 | 원문 | 확인 결과(실행한 명령과 출력) | 고친 문안 | 등급 |
|---|---|---|---|---|---|
| 1 | ch10 id="check" 앞 문단(102행) | "확인은 에이전트에게 해당 동작을 해 달라고 대화로 요청하는 방식이며, push와 네트워크 확인은 …expense-practice에서 합니다." | 확인 시점이 없습니다. ch09 78행은 "실습 3의 4단계를 마친 뒤"처럼 시점을 적습니다. 부록 `practice.html`을 grep한 결과 sandbox 설정과 AGENTS.md를 만드는 단계는 없고(sandbox 안내는 실습 3 확인 방법 한 줄뿐), Codex 언급도 0건입니다. 행 2, 4, 5는 실행 위치도 없습니다. | "이 장의 설정(sandbox 추가, Codex 설정)을 적용한 뒤 Claude Code를 새로 시작해, 모든 확인을 expense-practice에서 합니다. Claude Code 행은 부록 실습 3을 마친 폴더에서, Codex 행은 Codex를 설치한 독자만 합니다." 아래 2, 3, 7을 함께 반영합니다. | 필수 |
| 2 | 예제 Claude Code 코드 상자(61~68행)와 60행 설명 | "…이 장에서 추가하는 샌드박스 설정입니다. …파일을 만드는 방법은 실습 3에 있습니다." | 실습 3의 settings.json 모양(60~67행)에는 `sandbox`가 없습니다. 그래서 표 10-5 행 2, 5(touch)는 실습 폴더에서 그대로는 실패하지 않습니다. 상자에 `permissions`와 `sandbox`만 있는 JSON을 그대로 붙여 넣으면 실습 3에서 만든 allow, ask 목록을 덮어씁니다. 사용자는 이 상자를 새 파일로 오해하기 쉽습니다. 코드 상자 자체는 정상입니다(`python3 -I`로 json 파싱: permissions.deny 3개, sandbox.enabled True). | 상자 앞에 다음을 추가합니다. "실습 3에서 만든 .claude/settings.json의 `permissions` 블록 닫는 중괄호 뒤에 쉼표를 찍고 `"sandbox": { "enabled": true }`를 더합니다. 위 deny 세 줄은 이미 있는 항목의 발췌이니 다시 붙이지 않습니다. 저장 뒤 Claude Code를 새로 시작해 /permissions가 읽히는지 봅니다." | 필수 |
| 3 | 표 10-5 행 1 확인 기준 | "Claude Code는 git push 형태의 명령을 거부하고…" | `expense-practice`는 원격 저장소가 없는 폴더입니다. 부록 실습 3 확인 방법도 "push는 이 폴더에 원격 저장소가 없으므로 금지 규칙이 없어도 실패한다"고 적습니다. 따라서 "거부함"만으로는 deny 구현 전과 후가 구분되지 않습니다(R14, 플레이북 3.5). | 기준을 "금지 규칙으로 거부되었다는 메시지가 보임(원격 저장소가 없어 실패하는 오류와 구분). Codex는 forbidden 규칙으로 거부되었다는 메시지가 보임"으로 바꿉니다. | 필수 |
| 4 | 표 10-3 행 2(웹 도구)와 표 10-5 | 정책 "외부 자료를 읽지 않음(웹 도구)", 금지 규칙 WebFetch, WebSearch | 표 10-5에 WebFetch와 WebSearch 금지를 확인하는 행이 없습니다. 행 1은 push만, 행 3은 셸 네트워크만 다룹니다. 완료 기준(정책 두 가지)에 대응하는 확인이 한쪽만 있습니다. ch09 표 9-6은 /permissions의 금지 목록으로 이 항목을 확인합니다. | 행 1 확인 기준에 "/permissions의 금지에 Bash(git push *), WebFetch, WebSearch가 있음"을 더합니다. 또는 "웹 도구 금지" 행을 추가하되, 그러면 표 10-4와 1:1 번호 대응이 깨지므로 행 1에 합치는 쪽이 낫습니다. | 필수 |
| 5 | 표 10-5 행 4(AGENTS.md) | "목록에 AGENTS.md의 경로가 있음(…v2.1.280 이상)" | `ls examples/expense-app/AGENTS.md`는 "No such file"입니다. 실습 2의 CLAUDE.md에도 `@AGENTS.md`가 없습니다. 그래서 이 행은 독자 폴더에서 구현 전후를 만들 방법이 없습니다. 구현 전(불러오기 없음)에는 /memory에 경로가 없어 실패할 수 있지만, 구현 방법이 적혀 있지 않습니다. 또한 rule-docs 코드 상자(25~28행)가 이 구현인데 어느 파일에 쓰는지 명시가 없습니다. | 행 4 방법을 "expense-practice에 AGENTS.md를 만들고 CLAUDE.md 첫 줄에 `@AGENTS.md`를 적은 뒤(실습 2의 CLAUDE.md는 확인 뒤 git restore나 직접 삭제로 되돌림), /memory"로 고칩니다. 또는 "별도 임시 폴더에서 한다"고 밝힙니다. | 필수 |
| 6 | 표 10-5 행 2, 5 | "홈 폴더에 빈 파일을 만드는 명령(touch ~/sandbox-probe) 실행을 요청" / "2번 확인과 같은 요청" | ch09 78행에는 있는데 ch10에는 없는 안내가 셋 있습니다. (a) 입력창 `!` 직접 실행은 샌드박스 밖이므로 에이전트에게 요청한다. (b) 실패 뒤 샌드박스 밖 재실행을 묻으면 거절한다. (c) 파일이 만들어졌으면 삭제한다. 행 5의 "같은 요청"은 플레이북 14장이 금지한 모호한 가리킴이고, 행 2와 5는 같은 항목의 성공과 실패 해석이어서 한 행으로 합칠 수 있습니다. Windows는 아래 7번입니다. | 행 2 확인 방법에 "`!`로 직접 입력하지 않고 에이전트에게 요청. 샌드박스 밖 재실행을 묻으면 거절. 파일이 생겼으면 `rm ~/sandbox-probe`로 삭제(Git Bash 동일, PowerShell은 `Remove-Item ~/sandbox-probe`)"를 적습니다. 행 5는 "touch ~/sandbox-probe 실행 요청(행 2)"로 요청문을 풀어 씁니다. | 필수 |
| 7 | 표 10-5 행 2, 5와 90행 version-note | "네이티브 Windows에서는 샌드박스 없이 명령을 실행합니다" | 미지원 안내는 예제 절 끝 주석(90행)과 표 10-4 행 5에만 있습니다. 확인 절에는 행을 건너뛰라는 말이 없습니다. 네이티브 Windows(Git Bash, PowerShell)에서 행 2를 하면 파일이 만들어져 "샌드박스 동작 안 함"으로 읽히는데, 이는 샌드박스를 켜도 생기는 정상 상태입니다. 또 PowerShell에는 `touch`가 없습니다(Git Bash에는 있음). | 확인 절 앞 문단에 "네이티브 Windows(Git Bash, PowerShell)는 샌드박스를 지원하지 않으므로 행 2, 5를 건너뛰거나 WSL2에서 확인합니다"를 추가합니다. | 필수 |
| 8 | 예제 Codex 코드 상자(72~76행)와 77행 | "다음은 같은 두 정책을 Codex의 사용자 설정에 옮긴 것입니다." | 문법은 유효합니다(tomllib 파싱: sandbox_mode, approval_policy, sandbox_workspace_write.network_access False). 그런데 (a) 발췌 표시와 "기존 config.toml이 있으면 최상위 두 줄은 첫 `[표]` 앞에 둔다"는 안내가 없습니다. 표 아래에 쓰면 키가 그 표의 키가 됩니다. (b) 파일이 없을 때 만드는 방법이 없습니다. 규칙 파일은 `~/.codex/rules/` 폴더 생성이 필요합니다. (c) Windows 경로 안내가 없습니다. 본문 `~`는 41행에 홈 폴더라고 풀려 있지만, Windows에서는 `%USERPROFILE%\.codex`(PowerShell은 `$HOME\.codex`)입니다. | 상자 앞에 "~/.codex/config.toml이 이미 있으면 첫 줄 앞(첫 `[표]`보다 위)에 두 줄을 더하고, 없으면 새로 만듭니다. rules 폴더가 없으면 만듭니다(Windows는 `%USERPROFILE%\.codex`)"를 넣습니다. | 권고 |
| 9 | 표 10-3 행 3 Claude Code 칸 | "샌드박스의 허용 도메인 목록(추가 설정)" / 결과 "목록 밖은 확인 요청(default 모드)이나 거부(auto 모드)" | 설정 상자에는 허용 도메인 설정이 없고 `enabled`뿐이어서, 표가 가리키는 "추가 설정"이 상자와 맞지 않습니다(R17). 결과 칸은 본문 37행, 9장, `research/ch10-sources.md`(auto는 거부, 187행)와 일치합니다. 다만 83행이 "결과는 세 가지(금지, 차단, 확인 요청)"라고 했는데 이 칸은 "거부"를 따로 씁니다. 한 칸에 결과 둘이 있는 것은 플레이북 9.3의 "칸에 둘 이상이면 본문으로"와도 어긋납니다. | 설정 칸을 "sandbox.enabled = true(허용 도메인은 기본값)"로 고칩니다. 결과 칸은 "확인 요청(default) 또는 차단(auto)"처럼 83행 어휘로 맞추고, 모드별 설명은 본문 37행에 맡깁니다. | 권고 |
| 10 | 표 10-3 행 2 Codex 칸 | 설정 "이 장의 설정에 없음", 결과 "도입 시점 문서에서 확인" | 결과 칸이 결과가 아닌 미룸입니다. 표의 결과 세 분류에 해당하지 않고, 확인 표에도 대응 행이 없습니다. 출처가 있는 기록으로 채우거나 "해당 없음(비교하지 않음)"으로 명시해야 합니다. | "이 장에서 비교하지 않음"으로 쓰고, 근거가 있으면 한 줄을 더합니다. 근거가 없는 값은 쓰지 않습니다. | 권고 |
| 11 | 표 10-5 행 3 | "허용하지 않은 도메인에 접속하는 셸 명령 실행을 요청, Codex는 config.toml" / "Codex의 network_access가 false임" | (a) 요청문이 없습니다. "curl https://example.com 실행해 줘"처럼 요청문을 그대로 적어야 합니다(플레이북 14장). (b) 39행에 따르면 Codex 기본값도 네트워크 차단이므로, config.toml을 확인하는 것은 `network_access = false`를 적기 전에도 동작이 같습니다. 파일 확인은 구현 전 실패(키 없음)지만 동작을 증명하지 못합니다(R14). | 요청문을 적고, Codex는 "config.toml에 `network_access = false`가 있고 실제 요청이 차단되거나 승인을 묻는지"를 기준으로 합니다. | 권고 |
| 12 | 표 10-5 Codex 확인 전반(행 1, 3) | "제품마다 원격 저장소에 push해 달라는 요청" 등 | Codex를 설치하지 않은 독자 안내가 장에도 부록에도 없습니다(부록 grep에서 Codex 0건). 실습 폴더는 Claude Code 기준입니다. 설치하지 않은 독자는 "Codex 항목은 설치한 경우에만" 하도록 밝혀야 합니다. Codex 작업 폴더의 신뢰 표시 여부(43행 버전 주석)도 결과에 영향을 줍니다. | 확인 절 앞 문단에 "Codex 행은 Codex를 설치해 사용하는 경우에만 합니다. 설치하지 않았다면 config.toml과 rules 파일의 내용이 위 상자와 같은지 읽어 보는 것으로 대신합니다(동작 확인은 아님)"를 추가합니다. | 권고 |
| 13 | 표 10-5 행 5와 표 10-4 행 5, 2 | 방지 장치 "sandbox.failIfUnavailable을 true로 둠" / "git -C . push 형태" 실패 | `failIfUnavailable`은 설정 상자에 없고 확인 행도 없습니다(참고: 90행 주석에만 있음). 실패 2의 방지 장치(허용 목록에 원격 저장소 도메인을 두지 않음)는 원격이 없는 폴더에서 확인할 수 없으므로, 표 10-5 행 2의 touch 확인은 샌드박스가 켜졌다는 것만 증명합니다. 이를 밝히지 않으면 행 2가 `git -C . push` 차단까지 증명하는 것처럼 읽힙니다. | 행 2 기준 끝에 "원격 저장소가 연결된 환경에서의 `git -C . push` 차단은 이 확인으로 증명되지 않음"을 적습니다. | 권고 |
| 14 | 표 10-5 행 6, 표 10-4 행 6 | "기본값과 설정 이름이 이 장의 기준과 같음" | 실행으로 확인되는 근거가 아니라 문서 대조입니다. 구현 전 실패 여부는 해당이 없습니다. 날짜(Claude Code 10월 20일, Codex 10월 4일)는 본문 10행, 105행과 일치합니다. Codex는 `research/ch10-sources.md`에 원문 재확인 실패 기록이 있습니다(ch10-spec Q-057). | 분류만 합니다. 행 6은 "실행 확인 대상 아님(문서 대조)"로 두고, 출간 전 Codex 원문 재확인은 작가 확인(Q-057)으로 남깁니다. | 참고(검증 후 확정) |
| 15 | rule-docs 코드 상자(25~28행) | `@AGENTS.md` / `## Claude Code 전용` / `- 검토는 읽기 전용 하위 에이전트에 맡깁니다.` | 일반 예시로, 원본 파일이 없습니다. `reference/CLAUDE.example.md`에는 이 줄이 없습니다. 플레이북 15장은 "프롬프트가 아닌 코드 상자는 원본과 글자까지 같게"라고 하지만 예시 상자라 위반은 아닙니다. 다만 실습 2의 CLAUDE.md와 별개라는 점을 밝히면 혼동이 줄어듭니다. | "예시이며 실습 파일에는 없습니다"를 한 구절 더합니다. | 참고 |
| 16 | 표 10-5 행 4 `/memory`의 "AGENTS.md 경로 표시" | "v2.1.280 이상" | `research/ch10-sources.md` 210행, 213행과 일치합니다. 다만 Claude Code 대화형 화면이라 직접 실행하지 못했습니다. | 실행 못 함. 출간 전 작가가 실제 화면으로 확인합니다. | 참고(검증 후 확정) |

## 일치를 확인한 항목
- 표 10-4와 표 10-5의 번호는 1에서 6까지 1:1로 대응합니다.
- 표 10-3의 push 행은 ch09 표 9-4와, deny 항목은 `reference/settings.example.json`과 같습니다.
- "금지는 git push 형태만"이라는 표현은 ch09 71행과 같은 규칙을 말합니다.
- 실습 폴더에 원격 저장소가 없다는 전제는 `practice.html` 27행, 73행과 같습니다.
- 원본 `examples/expense-app`은 부모 저장소의 origin을 쓰지만, 실습 폴더는 `cp -r` 복사 후 `git init`이라 원격이 없습니다.
- 샌드박스 미지원 안내는 장 안에 있습니다(90행, 표 10-4 행 5). 확인 절에서 연결되지 않는 점이 7번입니다.

## 실행한 명령과 출력 (끝 부분)
1. `python3 -I`로 json, tomllib, ast를 파싱했습니다. 출력 요약은 다음과 같습니다.
   - Claude Code 설정: `{'permissions': {'deny': ['Bash(git push *)', 'WebFetch', 'WebSearch']}, 'sandbox': {'enabled': True}}`
   - Codex 설정: `{'sandbox_mode': 'workspace-write', 'approval_policy': 'on-request', 'sandbox_workspace_write': {'network_access': False}}`
   - 규칙 파일: AST 구문은 유효합니다. 키워드 `pattern`이 확인됐습니다.
   - `reference/settings.example.json`의 deny는 9개이고 위 세 항목을 포함합니다.
2. `python3 -I tools/check_tasks.py | tail`: `공백 있음 작업 2 …`, `정상 작업 3`, `정상 작업 4`, `요약: 공백 1건(작업 2)`. 이 범위(10장)와는 무관하며, 작업 2의 공백은 6장 소관입니다.
3. `ls examples/expense-app/AGENTS.md`: `No such file or directory`
4. `git -C examples/expense-app remote -v`: origin `https://github.com/seoulkorea-dev/harness-book`. 이는 책 저장소이고 복사 후의 실습 폴더에는 없습니다.
5. `git status --short`: 출력 0줄(작업 폴더 변경 없음).
6. grep과 sed로 ch09, 플레이북, `research/ch10-sources.md`, `practice.html`을 대조했습니다.

실행하지 못한 것: Claude Code와 Codex의 대화형 확인(/permissions, /memory, /sandbox, touch 요청, Codex 규칙 동작)은 대화형 제품이라 실행하지 못했고, Starlark 문법도 검증하지 못했습니다.

필수 수정 7, 편집 권고 5, 검증 후 확정 2(14, 16번), 실행한 명령 6개

(참고: 요약 줄의 필수 6, 권고 6, 참고 3은 위 표의 등급별 계산이 아니라 잘못 적은 수치입니다. 표 기준 정확한 수는 마지막 줄을 따라 주세요. 필수 1~7, 권고 8~13, 참고 14~16입니다.)
