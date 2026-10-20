# Chapter 10 fact-checker 점검(2026-10-20, PR #43)

## ch10 사실 확인 보고 (src/chapters/ch10.html, PR #43, 확인일 2026-10-20)

범위와 방법
- Claude Code Docs 5건(memory, permissions, permission-modes, sandboxing, settings)은 직접 열어 대조했습니다.
- permission-modes는 끝 262자를 읽지 못했습니다. 아래 판정에는 영향이 없습니다.
- Codex 문서는 developers.openai.com/codex/agent-approvals-security를 한 번 시도했고 `getaddrinfo ENOTFOUND`로 열리지 않았습니다. Codex 문장은 research/ch10-sources.md(S-C10-5)와 research/ch03-10-sources.md(S6, 2026-10-04)의 기록과의 일치만 봤습니다. 이 문장들은 1차 출처로 일치 확정을 하지 못했으므로 "기록 일치, 원문 미확인"으로 적습니다.
- 파일은 수정하지 않았습니다.

### 발견 표
발견 | 위치 | 근거 | 제안 | 확신 | 심각도

| # | 발견 | 위치 | 근거 | 제안 | 확신 | 심각도 |
|---|---|---|---|---|---|---|
| 1 | "허용 목록 밖 도메인은 default 확인, auto 거부"가 예외 없이 단정됨. 불일치(불완전) | permissions 절 perm-claude 2문단 끝, 표 10-3 3행 Claude 칸 | sandboxing, "Hosts outside your allowed domains" 표. 이 표는 대화형 터미널 기준이다. Manual과 acceptEdits는 확인(prompt), auto는 거부이나 "명령이 호스트를 직접 적고 분류기가 승인한 경우"는 예외다. 절 "Per-command allowed domains in auto mode"는 v2.1.271 이상이며, 승인되면 그 명령 하나에 한해 열린다. dontAsk는 거부, bypassPermissions는 허용이다. research S-C10-7이 "호스트 지정 승인 시 예외"를 포함한 표현만 근거 있다고 적었는데 본문에 빠졌다. | "대화형 터미널에서, 명령이 호스트를 직접 적고 분류기가 승인한 경우를 제외하고 auto는 거부"로 한정한다. 표 10-3 3행에도 같은 조건을 넣는다. | 높음 | 필수 |
| 2 | Codex push 결과가 표 10-3 1행에서 조건 없이 "규칙이 없으면 확인 요청"으로 적힘. 기록보다 강한 단정 | 표 10-3 1행 Codex 칸. 같은 취지의 표 10-4 1행 | S6(2026-10-04)은 "작업 공간 밖 수정과 네트워크가 필요한 명령은 승인 요청"까지만 기록한다. research 보충 조사는 "network_access=false인 workspace-write에서 on-request가 네트워크 명령을 승인 요청으로 넘기는지"를 미확인으로 남겼다. 명세 Q-058도 조건부 표현을 요구한다. 본문 67행은 "넘어갈 수 있으며"로 완화했으나 표는 완화하지 않았다. | 표 10-3 1행을 "규칙이 없으면 확인 요청으로 넘어갈 수 있음(2026년 10월 4일 기록)"으로 맞춘다. 표 10-4 1행 제목은 "확인 요청으로 넘어갈 수 있음"으로 한다. | 중간 | 필수 |
| 3 | "작업 폴더 밖의 파일 수정은 금지가 아니라 승인 대상"이 모드 조건 없이 단정됨 | perm-claude 3문단 첫머리(Anthropic, 2026b 인용) | permissions의 Manual 표(파일 수정은 승인 필요)는 default에서만 근거가 된다. permission-modes에서 acceptEdits는 범위 밖이면 확인, plan은 계획 승인 전 수정 없음, auto는 작업 폴더 안만 자동 승인하고 그 밖은 분류기 판단이며(심볼릭 링크로 밖에 풀리는 쓰기는 사용자 확인), dontAsk는 거부, bypassPermissions는 허용이다. 이 장의 버전 주석은 터미널 시작 모드가 auto라고 하므로 "승인 대상"이 시작 모드와 어긋난다. 근거 문서도 2026b 하나인데 모드별 내용은 2026c에 있다. | "default와 acceptEdits에서는 확인 요청이며, auto는 분류기가 판단하고 dontAsk는 거부"로 조건을 붙이고 2026c를 함께 링크한다. | 중간 | 권장 |
| 4 | Codex "승인 정책은 … 동작을 금지하지는 않습니다"가 기록에 없는 일반화 | perm-codex 1문단, 표 10-4 1행 원인 | S6은 "승인은 Codex가 멈추는 시점"까지만 기록한다. "금지하지 않는다"는 직접 근거가 없고, never처럼 묻지 않는 정책값의 동작도 기록이 없다. 원문 열기 실패. | "승인 정책은 확인을 요청하는 시점을 정하며, 금지는 규칙 파일의 forbidden이 맡습니다(OpenAI, 2026a)"로 기록 범위에 맞춘다. | 중간 | 권장 |
| 5 | Codex 기본값("로컬 실행에는 운영 체제 수준 샌드박스가 기본으로 적용, 기본은 네트워크 차단과 작업 공간 안 수정")이 본문 문장에 날짜와 조건 없이 단정됨 | perm-codex 1문단, 표 10-1 격리 행(날짜는 표 10-2에만 있음) | 기록은 S6(2026-10-04) 한 건이고 S-C10-5 확신은 낮음이다. 미러 문서 단서에 따르면 신뢰하지 않은 프로젝트는 read-only로 시작하고 신뢰하면 workspace-write와 on-request가 기본이다. 이 장의 버전 주석(38행)이 신뢰 여부 차이를 다루지만 본문 문장과 떨어져 있다. 원문 미확인. | 본문 문장에 "OpenAI 문서(2026년 10월 4일 확인) 기준"을 넣고, 표 10-1에도 "(2026년 10월 4일 확인)"을 붙인다. 출간 전 Codex 원문 재확인은 Q-057대로 유지한다. | 중간 | 권장 |
| 6 | 관리형 설정 "사용자와 프로젝트 설정으로 덮어쓸 수 없습니다"에 예외 없음 | perm-diff 1문단(Anthropic, 2026e) | settings는 관리형이 최상위(Managed is the top level)라고 하고 관리형 설정을 managed-settings.json, MDM, claude.ai 콘솔 배포로 설명한다. 그러나 permissions 문서(Managed settings)와 settings 문서 "Exceptions to managed settings precedence"는 일부 보안 민감 키에서 낮은 단계의 더 엄격한 값을 따른다고 적는다. 본문 설명(조직이 배포, 덮어쓸 수 없음)은 이 예외 외에는 일치한다. | "일부 보안 민감 키의 예외를 제외하고"를 한 구절 추가한다. | 높음 | 권장 |
| 7 | AGENTS.md 직접 읽기 버전 주석이 v2.1.277 하나로만 적힘 | rule-docs 버전 주석 | memory 문서는 v2.1.277 이상을 요구하되 "v2.1.281 이전에는 Amazon Bedrock이나 텔레메트리를 끈 세션처럼 일부 세션은 CLAUDE.md만 읽는다"고 쓴다. 그런 세션에서는 @AGENTS.md 불러오기를 쓴다. 본문의 v2.1.277과 @AGENTS.md 방식은 일치한다. | 주석에 "일부 세션(Bedrock, 텔레메트리 비활성)은 v2.1.281 이상"을 추가한다. | 높음 | 권장 |
| 8 | 표 10-5 5행 "샌드박스 없이 파일 생성이 성공하면 지원하지 않는 환경임"이 원인을 단정 | 표 10-5 5행 확인 기준 | sandboxing, 확인 절은 touch가 성공하면 `/sandbox`로 샌드박스가 켜져 있는지, 의존성이 설치되어 있는지 확인하라고 안내한다. 의존성 누락이나 꺼짐도 같은 결과를 낳는다. 또 홈 디렉터리가 쓰기 허용 경로가 아닐 때만 성립한다. | "샌드박스가 동작하지 않음. /sandbox로 켜짐과 의존성, 지원 플랫폼을 확인"으로 바꾼다. | 높음 | 권장 |
| 9 | "git -C . push 같은 다른 형태의 명령과 셸 명령의 네트워크 접근은 샌드박스가 제한합니다"가 차단으로 읽힘 | example-claude 설명 끝(60행), 표 10-4 2행 막는 장치 | permissions, "What a Bash rule doesn't match"는 `git -C . push`가 `Bash(git push *)`와 일치하지 않는다고 적고(일치 확인), 명령 문자열에 의존하지 않는 강제는 샌드박스를 쓰라고 안내한다. 다만 샌드박스의 네트워크 제한은 허용 목록 밖 호스트에 대한 확인 요청이나 거부이며, 허용한 도메인(예: git 호스트)이면 통과한다. 이 장의 표 10-3 3행 취지와도 어긋난다. | "샌드박스가 네트워크 접근을 허용 목록으로 제한하고 목록 밖 호스트는 확인 요청이 됩니다. 허용한 호스트로의 push는 막지 못합니다"로 조건을 밝힌다. 표 10-4 2행 막는 장치에도 같은 한정을 넣는다. | 중간 | 권장 |
| 10 | 표 10-5 3행 "두 제품 모두 바로 접속하지 않고 승인을 묻거나 차단함"이 모드 조건 없이 적힘 | 표 10-5 3행 | sandboxing 표상 bypassPermissions는 확인 없이 허용하고, 비대화형(`claude -p`)은 원문 표가 대상으로 삼지 않는다. 발견 1과 같은 조건이 필요하다. | 확인할 모드를 "default 또는 auto 모드의 대화형 터미널"로 적는다. | 중간 | 권장 |
| 11 | 본문 문장에 발표 주체(Anthropic, OpenAI)가 없고 괄호 인용 링크로만 표시됨 | rule-docs, permissions, perm-diff, example 각 문단 전반 | STYLE 4절은 "본문에서 발표 주체를 문장으로 밝히고 id로 링크"를 요구한다. 링크 id와 참고 자료 라벨(ref-anthropic-2026a~e, ref-openai-2026a)은 모두 존재하고 순서가 맞다. | 문단마다 최소 한 문장은 "Anthropic은 문서에서 …라고 안내합니다" 형태로 한다. | 높음 | 권장 |
| 12 | OpenAI 2026a 한 항목에 문서 네 개(AGENTS.md, approvals, Config basics, Rules)를 묶어서 어느 문장의 근거인지 알 수 없음 | 참고 자료 마지막 항목, perm-codex, example-codex | 명세 2차 보강 지시와는 맞다. 다만 S6 기록에는 Permissions 문서와 Sandbox 문서도 있는데 참고 자료에 없다. 규칙(forbidden) 문장은 Rules 문서 한정 근거다. | 현 구조를 유지하려면 본문 인용을 "OpenAI, 2026a(Rules)"처럼 문서명을 병기한다. | 중간 | 권장 |
| 13 | 출발점 대비 문장("Claude Code는 도구별 규칙에서 출발하고 … Codex는 운영 체제 수준 격리에서 출발")이 해석인데 표시가 없음 | perm-diff 2문단, 요약 2번째 항목 | research는 이를 "책의 해석, 단정 피함"으로 분류했다(Claude 쪽만 원문 확인, Codex 쪽은 기록 한 건). choice 절은 "이 책의 판단"을 표시했으나 이 문단에는 없다. | 문장 앞에 "이 책의 정리로는" 또는 근거 표시를 한다. | 중간 | 권장 |
| 14 | 표 10-4 4행 원인 "CLAUDE.md나 CLAUDE.local.md가 있으면" | 표 10-4 4행 | memory 문서는 .claude/CLAUDE.md도 셈에 넣고, 대상은 작업 폴더와 그 위 폴더이며 ~/.claude/CLAUDE.md와 관리형 CLAUDE.md는 세지 않는다고 적는다. 본문 rule-docs의 세 파일 서술은 일치한다. | 원인에 ".claude/CLAUDE.md"를 추가한다. | 높음 | 참고 |
| 15 | 시작 권한 모드 버전 주석이 perm-claude 문단 바로 뒤가 아니라 perm-diff 끝에 있음 | perm-diff 끝 버전 주석 | STYLE 5절은 해당 설명 바로 뒤에 둔다. 내용 자체는 일치(시작 모드는 실행 방식에 따라 다름, 프로젝트 settings의 auto와 bypassPermissions는 무효). v2.1.283 이상 터미널과 VS Code는 auto, `claude -p`와 SDK는 default인 점은 주석에 일부만 있다. | 위치 이동과 v2.1.283, `claude -p` 단서를 검토한다. | 중간 | 참고 |
| 16 | Codex 전역 읽기 문장 "~/.codex/AGENTS.md부터 저장소 루트, 하위 폴더 차례" | rule-docs 2문단 | S6은 "~/.codex의 AGENTS.override.md 또는 AGENTS.md, 디렉터리마다 override, AGENTS.md, 대체 이름 순"이다. 전역 단계에도 override가 있고, 하위 폴더는 "작업 폴더까지 이르는 경로"일 수 있다는 점은 미확인이다. | 원문 재확인 전까지 현 표현은 기록과 대체로 일치한다고만 본다. | 중간 | 참고 |
| 17 | 참고 자료 확인일과 인용 라벨 | 참고 자료 | Anthropic 2026a~e는 모두 확인 2026년 10월 20일로 실제 확인과 일치한다. 본문 사용처도 맞다(a: memory, b: permissions, c: permission-modes, d: sandboxing, e: settings). OpenAI 2026a의 "2026년 10월 4일"은 이번 열기 실패 때문에 정확한 기록 기준이다. 본문 8행의 두 날짜 서술도 일치한다. | 변경 없음. 출간 전 Codex 재확인은 Q-057. | 높음 | 참고 |

### 일치로 판정한 문장(요약)
- 권한 모드 설정값 여섯 가지(default, acceptEdits, plan, auto, dontAsk, bypassPermissions), default의 "파일 수정, 셸 명령, 네트워크 접근 대부분을 실행 전에 확인", plan의 "계획 승인 전 수정 없음", auto의 "별도 분류기, 명시한 ask 규칙은 auto에서도 확인", bypassPermissions의 확인 해제: permission-modes에서 일치.
- 프로젝트 `.claude/settings.json`의 auto와 bypassPermissions 무효(Manual로 시작): 일치.
- 샌드박스 기본 꺼짐, `/sandbox` 또는 `sandbox.enabled`, 셸 명령과 하위 프로세스, 쓰기는 작업 폴더와 임시 폴더(추가 디렉터리도 포함), 허용 도메인 처음에 비어 있음, macOS/Linux/WSL2 동작, 네이티브 Windows 미동작, `failIfUnavailable`: sandboxing에서 일치.
- 표 10-5의 touch ~/sandbox-probe 결과(macOS Operation not permitted, Linux와 WSL2 Read-only file system): sandboxing 확인 절 표와 일치.
- `Bash(git push *)`는 git push로 시작하는 명령을 막고 `git -C . push`는 일치하지 않음, deny 배열의 WebFetch와 WebSearch 규칙명, `/permissions`가 규칙과 출처 settings.json을 보여 줌: permissions에서 일치.
- 설정 파일 위치(.claude/settings.json, ~/.claude/settings.json, 관리형): settings와 permissions에서 일치.
- CLAUDE.md 세션마다 읽음, 작업 폴더와 상위 폴더를 이어 붙임(덮어쓰지 않음), AGENTS.md는 CLAUDE.md, .claude/CLAUDE.md, CLAUDE.local.md가 없을 때 읽음, v2.1.277 이상, `@AGENTS.md` 아래에 전용 지침을 두는 형식, `/memory`에서 AGENTS.md 경로 확인은 v2.1.280 이상: memory에서 일치.
- Codex(기록과 일치, 원문 미확인): AGENTS.md를 작업 전에 읽음, AGENTS.override.md가 있으면 대체, 샌드박스 모드 세 가지와 on-request, `~/.codex/config.toml`과 신뢰한 프로젝트의 `.codex/`, `~/.codex/rules/default.rules`와 `prefix_rule`의 forbidden, 규칙 기능 실험 단계, `network_access` 키. untrusted와 권한 프로필 문장은 삭제되어 있어 기록보다 강한 단정이 없습니다.

### research/ch10-sources.md에 추가할 기록 문안
```
### S-C10-11. Anthropic, Claude Code Docs 5건 재확인 (ch10 fact-checker, PR #43)
- URL: https://code.claude.com/docs/en/memory , /permissions , /permission-modes , /sandboxing , /settings
- 게시일: 표기 없음, 확인일: 2026-10-20 (원문 열어 확인)
- 작성: Anthropic
- 사용한 내용
  - sandboxing "Hosts outside your allowed domains" 표(대화형 터미널 기준): Manual, acceptEdits는 확인, auto는 거부(명령이 호스트를 적고 분류기가 승인하면 예외, v2.1.271 이상), dontAsk는 거부, bypassPermissions는 허용.
  - permission-modes: 작업 폴더 밖 쓰기는 acceptEdits 확인, auto 분류기 판단, dontAsk 거부, bypassPermissions 허용. 명시적 ask 규칙은 auto에서도 확인. 프로젝트 settings의 auto, bypassPermissions는 무효.
  - memory: AGENTS.md 직접 읽기 v2.1.277 이상, v2.1.281 이전에는 Bedrock과 텔레메트리 비활성 세션은 CLAUDE.md만 읽음. /memory와 /context의 AGENTS.md 목록은 v2.1.280 이상.
  - permissions: Bash(git push *)와 git -C . push 불일치, /permissions는 규칙과 출처 파일 표시, 관리형 설정은 보안 민감 키 일부를 제외하고 덮어쓸 수 없음.
  - settings: Managed가 최상위. 예외는 "Exceptions to managed settings precedence" 절.
  - sandboxing 확인 절: touch ~/sandbox-probe 실패 메시지(macOS Operation not permitted, Linux와 WSL2 Read-only file system). 성공 시 /sandbox로 켜짐과 의존성 확인.
- 확신: 높음
### S-C10-12. OpenAI, Codex 문서 (ch10 fact-checker)
- URL: https://developers.openai.com/codex/agent-approvals-security
- 확인일: 2026-10-20 시도(getaddrinfo ENOTFOUND, 열기 실패). 판정은 S-C10-5와 S6(2026-10-04) 기록 일치만 근거.
- 확신: 낮음
```

필수 2, 권장 11, 참고 4, 확인한 사실 문장 약 46개(일치 약 35, 기록 일치이나 원문 미확인 약 8, 불일치 또는 조건 누락 약 3)

주의: Codex 문장은 모두 원문을 열지 못한 채 research 기록과만 대조했으므로, 출간 전에 사람이 원문으로 재확인해야 합니다. 이 점은 명세 Q-057에도 적혀 있습니다.

## 처리(2026-10-20, 메인 세션)
| # | 처리 | 내용 |
|---|---|---|
| 1 | 반영 | 허용 목록 밖 도메인: 대화형 터미널, auto 예외(도메인을 적고 분류기 승인 시 그 명령만) 추가, 표 10-3 3행 모드 표기 |
| 2 | 반영 | 표 10-3 1행, 표 10-4 1행 "확인 요청으로 넘어갈 수 있음" |
| 3 | 반영 | 작업 폴더 밖 수정을 모드별로(default, acceptEdits 확인 요청, auto 분류기, dontAsk 거부), 2026c 인용 |
| 4 | 반영 | "승인 정책은 확인 시점을 정하며, 금지는 규칙 파일의 forbidden이 맡음" |
| 5 | 반영 | perm-codex 첫 문장 "OpenAI 문서(2026년 10월 4일 확인)에 따르면", 표 10-1 격리 행과 표 10-2, 10-3 캡션에 날짜 |
| 6 | 반영 | 관리형 설정 "일부 보안 설정을 제외하고" |
| 7 | 반영 | 버전 주석에 Bedrock, 텔레메트리 해제 세션은 v2.1.281 이상 |
| 8 | 반영 | 표 10-5 5행 "/sandbox로 켜짐 상태, 필요한 구성 요소, 지원 환경을 확인" |
| 9 | 반영 | git -C . push는 샌드박스를 켜면 허용 목록과 대조, 원격 도메인을 허용하면 제한되지 않음. 표 10-4 2행 장치 보강 |
| 10 | 반영 | 확인 방법 문단에 "default 모드나 auto 모드의 대화형 터미널" |
| 11 | 반영 | rule-docs, perm-claude, 샌드박스 문단을 "Anthropic은 문서에서", perm-codex와 rule-docs를 "OpenAI는 문서에서"로 |
| 12 | 보류 | OpenAI 2026a 문서 묶음 유지(이번에 원문 확인 불가, 문서별 분리는 Q-057 재확인 때) |
| 13 | 반영 | "이 책의 정리로는, 두 제품의 차이는 출발점에 있습니다" |
| 14 | 반영 | 표 10-4 4행에 .claude/CLAUDE.md |
| 15 | 반영 | 시작 모드 버전 주석을 모드 목록 바로 뒤로, v2.1.283과 claude -p 단서 |
| 16 | 보류 | 기록과 대체로 일치, Q-057 재확인 |
| 17 | 해당 없음 | 변경 없음 |
- 기록 문안 S-C10-11, 12는 research/ch10-sources.md에 추가
