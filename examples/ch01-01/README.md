# Chapter 1 핵심 예제 실행 절차 (주간 보고서, 세 층)

Chapter 1 "같은 요청, 세 층의 개선"의 실행 결과를 얻기 위한 절차입니다. 같은 모델로 세 단계를 실행하고, 출력 원문을 작성 채팅에 전달합니다.

## 준비물

- 가상 프로젝트: 경비 정산 시스템 개편(이번 주 보고 기간 2026-09-28 월 ~ 2026-10-02 금)
- `data/`: 지난주 보고서, 이번 주 작업 목록(작업 관리 도구), 이슈 목록(이슈 관리 도구)
- `prompts/1-prompt.txt`: 1단계 프롬프트
- `prompts/2-context.txt`: 2단계 프롬프트(자료 포함, 그대로 복사)
- `CLAUDE.md`, `.claude/settings.json`, `verify_counts.py`: 3단계 하네스(규칙, 권한, 검증)

## 1단계 프롬프트, 2단계 컨텍스트 (claude.ai)

1. claude.ai에서 **임시 채팅(incognito)** 을 엽니다. 메모리와 Project 자료가 결과에 섞이지 않게 하기 위해서입니다.
2. 3단계와 같은 모델을 선택하고, 모델 이름을 기록합니다.
3. `prompts/1-prompt.txt` 내용을 그대로 붙여 넣고 실행합니다. 출력 전체를 `output/stage1-output.md`로 저장합니다.
4. 새 임시 채팅을 열어 `prompts/2-context.txt` 내용을 그대로 붙여 넣고 실행합니다. 출력 전체를 `output/stage2-output.md`로 저장합니다.

## 3단계 하네스 (Claude Code, Git Bash)

```
cd ~/projects
[ -d harness-book ] || git clone https://github.com/seoulkorea-dev/harness-book.git
cd harness-book
git pull --rebase origin main
cd examples/ch01-01
claude --version
claude
```

Claude Code가 열리면 다음 순서로 입력합니다.

1. `/permissions` 입력: 허용(allow)과 거부(deny) 규칙 목록을 화면 그대로 기록합니다.
2. `/model` 입력: 1, 2단계와 같은 모델인지 확인하고 기록합니다.
3. 다음 요청을 입력합니다.

```
CLAUDE.md의 규칙대로 이번 주 주간 보고서 초안을 작성하고 검증해 줘.
```

4. 허용 목록에 없는 동작(다른 명령 실행 등)의 승인 요청이 나오면 거부하고, 요청 내용을 기록합니다.
5. 작업이 끝나면 `/exit`로 나온 뒤, Git Bash에서 검증을 직접 한 번 더 실행합니다.

```
python verify_counts.py || python3 verify_counts.py
```

## 작성 채팅에 전달할 것

- `output/stage1-output.md`, `output/stage2-output.md`, `output/weekly-report-2026-10-02.md`
- `claude --version` 출력, 모델 이름, `/permissions` 화면 기록, 거부한 승인 요청(있으면)
- 마지막 `verify_counts.py` 출력 원문

`output/` 파일은 커밋하지 않고 작성 채팅에 업로드합니다. 작성 채팅이 실행 기록(`examples/ch01-01.md`)과 원고를 함께 반영하고 push합니다.
