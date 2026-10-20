# .claude/ 반영본(이슈 #31, D-117)

이 폴더의 파일은 .claude/ 아래 같은 경로 파일의 새 판입니다. 2026-10-20 /next 세션에서 .claude/ 쓰기 권한이 허용되지 않아 직접 고치지 못했습니다. 쓰기를 허용한 세션에서 아래처럼 덮어쓰고, 이 폴더를 지웁니다.

```
cp docs/specs/flow-criteria-claude/agents/editor.md .claude/agents/editor.md
cp docs/specs/flow-criteria-claude/agents/flow-reviewer.md .claude/agents/flow-reviewer.md
cp docs/specs/flow-criteria-claude/agents/reader-novice.md .claude/agents/reader-novice.md
cp docs/specs/flow-criteria-claude/commands/review-chapter.md .claude/commands/review-chapter.md
cp docs/specs/flow-criteria-claude/commands/next.md .claude/commands/next.md
```

| 파일 | 바뀐 것 |
|---|---|
| agents/editor.md | 점검 0번 흐름과 이해도(첫째 필수), 장 전체 통독, 논지 사슬 표 확인, 필수 목록, 출력에 "흐름과 이해도" 절 |
| agents/flow-reviewer.md | 장 전체 통독, 1단계 논지 사슬 표, 점검 1~3(장의 흐름, 절 첫 문단 순서, 문단과 인용), 끊김은 필수, F-18 |
| agents/reader-novice.md | model haiku → sonnet, 장 전체 통독, 막힌 곳 유형 "왜?", "그래서?", "이게 무슨 말?", 예제가 원리 이해에 쓰였는지 |
| commands/review-chapter.md | flow-reviewer와 reader-novice는 장 개정과 흐름 재점검 때 항상, 논지 사슬 표 저장(reviews/flow/) |
| commands/next.md | 점검 단계에 논지 사슬 표, editor에 통독과 표 경로, PR 설명에 표 링크와 고친 곳(이전, 이후) |
