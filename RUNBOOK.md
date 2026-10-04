# 집필 자동화 실행 절차 (RUNBOOK)

Claude Code를 중심으로 Skill, 에이전트, 훅, MCP, CI를 갖춘 집필 환경을 만들고, 현재 책(ai-book)의 남은 작업으로 시범 운영한 뒤, 다음 책에 그대로 재사용하는 절차입니다. 각 단계는 **명령 → 확인 방법 → 기대 결과**로 되어 있습니다. 기대 결과와 다르면 다음 단계로 넘어가지 않습니다.

- 대상 환경: Windows PC, PowerShell(설치 단계)과 Git Bash(저장소 작업)
- 소요 시간(예상): 0~4단계 설정 1~2시간, 5단계 시범 반나절
- 이 키트의 파일: `.claude/`(설정, 에이전트 6, 명령 3, Skill 5), `.github/workflows/`(3), `tools/`(hook_lint.py, verify_site.py, similarity_check.py), `DECISIONS.md`, `BOOK_SPEC.template.md`
- 검증 기록: 키트의 훅 스크립트, 배포 검증 스크립트, check.yml 단계는 현재 저장소(a6e7ddc 이후)에서 실행해 통과를 확인함(9절)

---

## 0. 전체 구조

| 구성 | 역할 | 위치 |
|---|---|---|
| Skill 5 | 25회 검수에서 얻은 규칙을 모델이 자동으로 따르게 함 | `.claude/skills/` |
| 에이전트 6 | 조사, 집필, 사실 확인, 문체, 입문 독자, 전문가 독자 | `.claude/agents/` |
| 명령 3 | `/review-chapter`, `/reader-sim`, `/apply-review` | `.claude/commands/` |
| 훅 | 원고를 고칠 때마다 빌드와 lint 자동 실행, 오류면 Claude에게 즉시 되돌림 | `.claude/settings.json`, `tools/hook_lint.py` |
| MCP | Notion(설계 인터뷰, 결정, 생각 기록), Figma(그림), Sheaf(작성 지침) | `.mcp.json` |
| CI | PR마다 빌드와 lint, 배포 뒤 실제 사이트 확인, (선택) Claude PR 검토 | `.github/workflows/` |
| 결정 기록 | 모든 결정의 단일 출처 | `DECISIONS.md` |

작업 흐름: 설계(인터뷰) → 조사 → 실험(실제 실행) → 집필(에이전트) → 자동 검사(훅, CI) → 검수(에이전트 + 독자 시뮬레이터) → 작가 승인 → 병합과 배포 → 배포 확인

---

## 1. 사전 준비 (PowerShell, 한 번만)

```powershell
winget install --id Git.Git -e
winget install --id OpenJS.NodeJS.LTS -e
winget install --id Python.Python.3.12 -e
winget install --id GitHub.cli -e
```
PowerShell을 닫았다가 다시 연 뒤:
```powershell
git --version
node --version
python --version
gh --version
```
**기대 결과**: 네 줄 모두 버전이 나옴(Node 18 이상, Python 3.12). `python`이 Microsoft Store를 열면 "앱 실행 별칭"에서 python.exe 별칭을 끄고 다시 확인합니다.

Claude Code 설치(둘 중 하나, 설치 전 공식 문서 code.claude.com/docs의 설치 절에서 현재 명령 확인):
```powershell
npm install -g @anthropic-ai/claude-code
claude --version
```
**기대 결과**: 버전 번호 출력. 이어서 `claude`를 실행해 Max 플랜 계정으로 로그인합니다.

GitHub 로그인:
```powershell
gh auth login
gh auth status
```
**기대 결과**: `Logged in to github.com account ...`와 `Token scopes`에 `repo`, `workflow` 포함.

---

## 2. 키트 설치 (Git Bash)

```bash
cd ~/projects/ai-book
git switch main
git pull --rebase origin main
git status --short
git switch -c setup/agent-kit
unzip -o ~/Downloads/book-agent-kit.zip -d .
ls -a .claude .github/workflows tools
```
**확인**: `git status --short` 첫 실행 결과가 비어 있어야 합니다(비어 있지 않으면 멈추고 정리).
**기대 결과**: `.claude`에 `agents commands settings.json skills`, `.github/workflows`에 `check.yml claude-review.yml verify-site.yml`, `tools`에 `hook_lint.py verify_site.py similarity_check.py`가 보임.

키트 동작 확인:
```bash
echo '{"tool_input":{"file_path":"src/chapters/ch02.html"}}' | python tools/hook_lint.py; echo "exit=$?"
python tools/build.py && git diff --exit-code -- index.html chapters appendix && echo "빌드 결과 일치"
```
**기대 결과**: `exit=0`, `빌드 결과 일치`.

커밋:
```bash
git add .claude .github tools docs DECISIONS.md BOOK_SPEC.template.md RUNBOOK.md
git commit -m "chore: Claude Code 집필 키트(Skill 5, 에이전트 6, 명령 3, 훅, CI 3, 결정 기록)"
git push -u origin setup/agent-kit
gh pr create --fill --base main
```
**기대 결과**: PR 주소 출력. PR 화면의 Checks에서 `book-check`가 초록색.

---

## 3. Claude Code에서 구성 확인

```bash
cd ~/projects/ai-book
claude
```
Claude Code 안에서 차례로 입력:
| 입력 | 기대 결과 |
|---|---|
| `/agents` | researcher, writer, fact-checker, style-reviewer, reader-novice, reader-expert 6개 표시 |
| `/help` 또는 `/` 입력 | review-chapter, reader-sim, apply-review 명령 표시 |
| `/hooks` | PostToolUse, matcher `Edit|Write|MultiEdit`, `python tools/hook_lint.py` 표시 |
| `ko-book-style skill의 어휘 치환표를 보여 줘` | Skill 내용(넣다, 바꾸다 … 표) 응답 |

훅 동작 시험(일부러 오류를 넣었다가 되돌림):
| 입력 | 기대 결과 |
|---|---|
| `src/chapters/ch02.html 첫 문단 맨 앞에 "문장을 써 줘. "를 추가해 줘` | 편집 직후 훅이 `경고 chapters/ch02.html … 써` 를 되돌려 주고 Claude가 오류를 인지함 |
| `방금 추가한 문장을 지워 줘` | 훅 통과, `git status --short`에 변경 없음 |

---

## 4. MCP 연결 (Claude Code)

```bash
claude mcp add --transport http --scope project notion https://mcp.notion.com/mcp
claude mcp add --transport http --scope project figma https://mcp.figma.com/mcp
claude mcp add --transport http --scope project sheaf https://sheaf-docs.vercel.app/api/mcp
claude mcp list
```
**기대 결과**: 세 서버가 목록에 표시되고, 저장소에 `.mcp.json` 생성. Claude Code 안에서 `/mcp`를 입력해 각 서버를 인증(브라우저 로그인)한 뒤 상태가 connected.
**쓰임**: Notion은 설계 인터뷰 기록, 결정 초안, 생각 일지. Figma는 도식 초안. Sheaf는 작성 지침(get_writing_guide)과 팀 검토 미션.
커밋:
```bash
git add .mcp.json && git commit -m "chore: 프로젝트 MCP(Notion, Figma, Sheaf)" && git push
```

---

## 5. CI와 브랜치 보호 (PR 병합 뒤)

```bash
gh pr merge --squash --delete-branch
git switch main && git pull
```
main 직접 push를 막고 `book-check` 통과를 병합 조건으로 지정:
```bash
cat > /tmp/protect.json <<'JSON'
{"required_status_checks":{"strict":true,"contexts":["check"]},
 "enforce_admins":false,
 "required_pull_request_reviews":null,
 "restrictions":null}
JSON
gh api -X PUT repos/seoulkorea-dev/ai-book/branches/main/protection --input /tmp/protect.json
gh api repos/seoulkorea-dev/ai-book/branches/main/protection --jq '.required_status_checks.contexts'
```
**기대 결과**: `["check"]`.
배포 확인 워크플로 수동 실행:
```bash
gh workflow run verify-site.yml
gh run list --workflow verify-site.yml --limit 1
```
**기대 결과**: 상태 `completed`, 결과 `success`. 로그 끝에 `확인한 쪽 26, 오류 0`(위키 삭제 뒤에는 12).

(선택) Claude PR 검토: `claude setup-token`으로 토큰 발급 → 저장소 Settings, Secrets에 `CLAUDE_CODE_OAUTH_TOKEN` 등록. 적용 전 공식 문서에서 액션 입력 이름 확인.

---

## 6. 시범 운영: 23차(위키 삭제)를 새 방식으로

```bash
git switch -c content/wiki-removal
claude
```
Claude Code 안에서:
| 순서 | 입력 | 확인 방법 | 기대 결과 |
|---|---|---|---|
| 1 | `DECISIONS.md와 reviews/2026-10-01-23차-wiki-removal.md를 읽고 작업 계획을 표로 보여 줘. 아직 고치지 마.` | 계획 표 | 2절 7가지, 4절 링크 10곳, 5절 이동 쪽, 6절 부록 이름이 모두 포함 |
| 2 | `writer 에이전트로 23차 2절 7가지를 반영해 줘. 장마다 끝나면 멈춰.` | 훅 결과, `git diff --stat` | 훅 오류 0으로 끝남, 4, 5, 6, 8장 변경 |
| 3 | `23차 4절, 5절, 6절을 반영해 줘(링크, 목차, 이동 쪽, 부록 이름).` | `grep -rn "wiki/\|위키" src chapters appendix index.html` | 이동 쪽 외 0건 |
| 4 | `/review-chapter ch08` | `reviews/ch08-review.md` | 검사 출력 원문, 사실 확인, 문체, 독자 지적이 한 문서에 |
| 5 | `/reader-sim ch02` | `reviews/reader/ch02-summary.md` | 채택 지적 표, 주장 일치도, 질문 5개. 25회 검수에서 못 찾은 지적이 있는지 작가가 판단 |
| 6 | `/apply-review ch08` | 반영 표, 훅 결과 | 수정 필요 항목 반영, 사용자 결정 항목은 목록으로 남음 |
Claude Code를 나와서:
```bash
git add -A && git commit -m "docs: 23차 위키 삭제와 본문 이동, 부록 이름 변경(시범 운영)"
git push -u origin content/wiki-removal
gh pr create --fill --base main
gh pr checks --watch
```
**기대 결과**: `check` 통과. (선택 시) Claude 검토 댓글.
병합과 배포 확인:
```bash
gh pr merge --squash --delete-branch
gh run list --workflow verify-site.yml --limit 1
```
**기대 결과**: verify-site `success`, 로그 `확인한 쪽 12, 오류 0`.
마지막으로 브라우저에서 사이트를 강력 새로 고침(Ctrl+Shift+R)해 목차에 위키가 없는지 눈으로 확인합니다.

---

## 7. 다음 책 시작 절차

```bash
gh repo create seoulkorea-dev/<새 책> --public --clone
cd <새 책>
cp -r ../ai-book/.claude ../ai-book/.github ../ai-book/tools ../ai-book/lint .
cp ../ai-book/BOOK_SPEC.template.md BOOK_SPEC.md
printf "# 결정 기록\n\n| 번호 | 날짜 | 결정 | 대체 | 이유 |\n|---|---|---|---|---|\n" > DECISIONS.md
git add -A && git commit -m "chore: 집필 키트 재사용" && git push -u origin main
claude
```
Claude Code 안에서 설계 인터뷰:
| 입력 | 기대 결과 |
|---|---|
| `BOOK_SPEC.md를 채우기 위해 나를 인터뷰해 줘. 한 번에 질문 하나씩, 장마다 '내 주장, 근거가 된 내 경험, 반대 의견'을 물어봐. 답은 Notion의 '책 설계 인터뷰' 페이지에도 기록해 줘.` | 질문이 하나씩 나오고, 답할 때마다 BOOK_SPEC.md와 Notion이 갱신 |
| `BOOK_SPEC.md를 검토해 미정 항목과 서로 충돌하는 결정을 표로 보여 줘.` | 미정 0이 될 때까지 반복. 확정분은 DECISIONS.md로 |
| `originality-check skill로 비교 도서와 목차를 비교해 줘.` | 장 제목, 부록 이름, 핵심 틀 일치 0 |
이후는 6절과 같은 흐름(조사 → 실험 → 집필 → 검수 → PR)으로 장마다 반복합니다.

---

## 8. 결과물 확인과 측정

PR마다 `docs/metrics.md`에 한 줄씩 기록합니다(작가의 기술 수준 공유 자료).
| 항목 | 확인 방법 |
|---|---|
| 자동 검출 건수 | 훅이 되돌린 횟수(Claude Code 세션 기록), check 실패 횟수(`gh run list`) |
| 사람 검수 지적 건수 | 작가가 직접 고친 항목 수 |
| 독자 시뮬레이터 채택률 | 채택 지적 수 ÷ 전체 지적 수, 실제 독자와 일치한 비율 |
| 소요 시간 | PR 생성부터 병합까지 |
| 실행 결과 예제 비율 | examples/ 기록이 있는 예제 수 ÷ 전체 예제 수 |
목표(제안): 사람 검수 지적이 장당 5건 이하, 배포 뒤 오류 0, 실행 결과 예제 비율 80% 이상.

---

## 9. 이 키트의 사전 검증 기록 (검수 Agent가 실행)

| 대상 | 방법 | 결과 |
|---|---|---|
| tools/hook_lint.py | 현재 원고(ch02)로 실행 | exit=0 |
| tools/hook_lint.py | ch02에 "문장을 써 줘."를 일부러 넣고 실행 | exit=2, `경고 chapters/ch02.html:62: 써` 출력 |
| tools/verify_site.py | 현재 빌드 결과를 로컬 웹 서버로 띄워 실행 | `확인한 쪽 26, 오류 0`, exit=0 |
| check.yml 단계 | 현재 저장소에서 같은 명령 순서로 실행 | 빌드 결과 일치, numbers, structure, style, 금칙어 모두 통과 |
| 워크플로 3개 | YAML 문법 검사 | 3개 모두 정상 |

검증하지 못한 것(사용자 환경에서 확인 필요): Windows에서의 설치 명령, Claude Code의 `/agents`, `/hooks` 화면 표시, MCP 인증, GitHub Pages의 `page_build` 이벤트 발생, claude-code-action 입력 이름. 각 단계의 "기대 결과"와 다르면 그 단계에서 멈추고 결과 원문을 알려 주십시오.
