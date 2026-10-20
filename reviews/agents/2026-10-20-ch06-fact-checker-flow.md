# ch06 fact-checker 점검(2026-10-20, PR #30)

ch06 사실 점검 보고 (PR #30, 브랜치 ch06-write, 확인일 2026-10-20). 원고와 파일은 고치지 않았다. 셸이 없어 check.py와 단위 테스트는 실행하지 못했고, 소스를 읽어 RUNLOG와 대조했다.

## 요약
사실 문장 대부분은 일치한다. 불일치는 1건(필수)이다. 권장 4건, 참고 4건이다.

| # | 심각도 | 위치 | 사실 문장(앞부분) | 판정 | 근거(주소, 확인 위치, 확인 날짜) | 제안 |
|---|---|---|---|---|---|---|
| 1 | 필수 | 그림 6-2 SVG와 aria-label(하위 에이전트 영역 "모두 자기 컨텍스트 윈도에서 새 대화로 작업, 주 대화는 보지 않음"), 표 6-3 "하위 에이전트" 행, 4개 항목 글머리 "하위 에이전트는 주 대화를 보지 않으므로" | 하위 에이전트는 새 대화로 시작하고 주 대화를 보지 않는다 | 불일치(일반화 과다). 본문 "일반 하위 에이전트" 문장(30행)은 일치 | https://code.claude.com/docs/en/sub-agents, "How forks differ from other subagents" 표와 "Turn fork mode off": 포크는 "주 대화 전체 이력을 물려받는" 하위 에이전트다. 같은 절에 포크 모드는 v2.1.302부터 기본 켜짐(대화형 터미널은 v2.1.232부터)이고 Claude가 스스로 포크를 시작할 수 있다고 적혀 있다. 이 절의 일반 하위 에이전트 쪽 기술은 "Fresh context with the prompt you pass"로 30행과 일치. 확인 2026-10-20 | 본문 30행은 "일반"으로 한정돼 있어 맞다. 그림 6-2와 표 6-3은 "모두"와 무한정 서술이라 한정이 필요하다("일반 하위 에이전트" 또는 포크 예외 한 줄). 포크는 책이 다루지 않으므로 버전 주석 또는 표 각주로 "포크는 주 대화를 물려받는다"를 덧붙이는 방안. 확신 중간(책에서 포크를 다루지 않기로 했다면 "일반" 한정만으로 충분) |
| 2 | 권장 | 31행 "하위 에이전트의 요청도 사용량에 포함되고, Agent SDK의 비용 상한은 …" | 요청이 사용량에 포함되고 비용 상한이 하위 지출을 포함 | 일치 | costs 문서 "Delegate verbose operations to subagents" 절: "The subagent's own requests still draw on your usage." agent-loop 문서 "Turns and budget" 절: "The budget cap covers subagents: their spend counts toward the total." 확인 2026-10-20 | 이 두 문장에는 발표 주체와 링크가 없다(다음 문장만 링크). "Anthropic의 비용 문서와 Agent SDK 문서는 … 설명합니다"로 주체를 밝히고 ref-anthropic-2026 링크 |
| 3 | 권장 | 31행 "에이전트 팀에서 토큰 사용량이 팀 크기에 거의 비례" | 일치 | costs 문서 "Agent team token costs" 절: "token usage is roughly proportional to team size". "비용 문서는 … 설명합니다"로 주체·링크 충족 | 조치 없음 |
| 4 | 권장 | 33행 "용어집에 따르면 …" | 하위 에이전트는 맡긴 쪽에만 보고, 팀원은 각자 컨텍스트 윈도와 직접 대화, 에이전트 팀은 기본으로 꺼진 실험 기능 | 일치 | Glossary "Agent teams" 항목: "Unlike subagents, which run within a single session and report only to the parent, teammates each have their own context window and you can interact with any of them directly. Agent teams are experimental and disabled by default". costs 문서에도 "disabled by default". 확인 2026-10-20 | 주체 표기("Claude Code 용어집")와 링크가 문단 끝에만 있다. 문장 앞에 "Claude Code 용어집은 … 설명합니다" 정도로 주체를 밝히면 충족 |
| 5 | 권장 | 30행 "작업이 끝나면 최종 응답의 요약만 … 돌아옵니다" | 일치(표현 미세 차이) | sub-agents 문서: "Only its summary returns to the parent". agent-loop "Keep context efficient"절: "A subagent returns only its final response, so your main agent's context grows by a summary, not by the subtask's transcript." 확인 2026-10-20 | 문서는 "최종 응답이 곧 돌아오는 요약"이다. "최종 응답의 요약"은 최종 응답을 다시 요약한다는 뜻으로 읽힐 수 있어 "최종 응답만 요약으로 돌아옵니다"가 더 가깝다. 표현 선택은 작성 쪽. 확신 중간 |
| 6 | 필수 아님(참고) | 32행 버전 주석 "v2.1.217 이상에서 비용 상한에 이르면 새 하위 에이전트를 만들 수 없다" | 일치 | agent-loop "Turns and budget" 절: 상한에 이르면 "spawning another subagent fails with Budget limit reached", "The cap-enforcement behaviors require Claude Code v2.1.217 or later." 확인 2026-10-20 | 같은 절에 "상한은 응답 도착 뒤 비교해 한 응답만큼, 그리고 아직 실행 중인 하위 에이전트의 지출만큼 넘을 수 있다"가 있다. 그림 6-2와 31행은 "상한에 포함"까지만 쓰므로 필요하면 주석에 한 문장 추가(선택). 형식(aside.footnote, "버전 주석 (2026년 10월)")은 맞다 |
| 7 | 참고 | 16~17행 "Claude Code는 … 보고했습니다 / 밝혔습니다"(Young, 2025) | 인용 주체 표기 | Q-039와 같은 종류의 문제 | 원문(https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)은 Justin Young의 글이다. 실험 주체는 "Claude Agent SDK" 위의 에이전트이고, "Claude Code"는 감사의 말의 팀 이름("the code RL & Claude Code teams")에만 나온다. 본문에 제품명으로 쓸 근거 문장이 글에 없다. 확인 2026-10-20 | 판정만 적는다. Q-039(Rajasekaran 외 글의 주체를 D-108 때문에 Claude Code로 바꾼 문제)와 같은 유형이다. 글이 Claude Code 제품이 아니라 Claude Agent SDK 하네스 실험을 다룬다는 점에서 근거가 약하다. research/ch06-sources.md의 "D-108에 따라 유지"는 맞는 처리이나, Q-039의 목록에 ch06 16행과 17행을 추가하는 것을 권장. 되돌릴지는 작가 결정 |
| 8 | 일치(확인) | 16행 두 가지 실패 | 일치 | 원문: "tended to try to do too much at once—essentially to attempt to one-shot the app", "running out of context in the middle of its implementation … next session to start with a feature half-implemented and undocumented", 뒤의 인스턴스가 진행을 보고 "declare the job done". 확인 2026-10-20 | 조치 없음 |
| 9 | 일치(확인) | 17행 200개 넘는 기능, "실패" 상태, 한 번에 하나, 점진적 방식 결정적 | 일치 | 원문: "over 200 features", 모두 초기 "failing", "work on only one feature at a time", "This incremental approach turned out to be critical …". 확인 2026-10-20 | 조치 없음 |
| 10 | 일치(확인) | 56행 JSON이 Markdown보다 덮어쓰기가 적음, 상태 항목만 수정 | 일치 | 원문: "the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files", 에이전트에게 "only by changing the status of a passes field" 지시. 확인 2026-10-20 | 조치 없음. 원문 필드 이름은 passes, 책은 "통과 값"으로 옮겼고 문제 없음 |
| 11 | 일치(확인) | 표 6-4와 57~72행 JSON | tasks.example.json과 글자 일치 | 일치 | examples/expense-app/reference/tasks.example.json의 작업 1~5와 작업/완료 기준/확인 방법/통과 값, 본문 JSON의 작업 2, 3이 글자까지 같다. 담당 열은 JSON에 없고 본문 근거(합의 필요, 판단 필요)로 설명됨. D-012는 examples/expense-app/DECISIONS.md와 docs/CR.md에 있음 | 조치 없음 |
| 12 | 일치(확인) | 55행 "작업 2와 작업 3의 확인 방법은 구현 전에도 통과" | 일치 | acceptance/test_cr07.py의 test_4(기존 요청 목록 표시)와 test_5(projects.csv 해시 불변)는 expense/service.py가 project_code를 무시해도 통과한다. test_1~3은 project_code 필요. tests/test_basic.py 3건은 기준 상태 단위 테스트. 소스 읽기로 확인, 실행은 못 함 | 조치 없음 |
| 13 | 일치(확인), 참고 | 55행 "단위 테스트는 실패 0건이고, 수용 시험은 넷째와 다섯째만 통과" | 일치(RUNLOG에서 추론) | examples/expense-app/RUNLOG.md(2026-10-16): "tests: 실행 3건, 실패 0건 / acceptance: 실행 5건, 실패 3건(실패: test_1, test_2, test_3)". "넷째와 다섯째가 통과"는 RUNLOG에 명시돼 있지 않고 실패 목록에서 도출된다. 링크한 부록 실습 1(practice.html lab-1)에는 "5건 중 3건 실패"만 있다 | 본문 문장은 맞다. 근거를 더 단단히 하려면 RUNLOG 기록 줄에 "통과: test_4, test_5"를 덧붙이거나(예제 폴더는 고치는 쪽 판단) 본문 문구를 "실패 3건(시험 1, 2, 3)"으로 바꾸는 방안. 기록이 2026-10-16이라 이후 변경이 없는지 PR 시점에 재실행 권장 |
| 14 | 일치(확인) | 73행 "작업 3은 작업 2가 변경한 데이터 모델에 맞춰 …, 작업 4는 그 데이터 모델 위에 …" | 일치 | tasks.example.json의 작업 3 완료 기준 "변경된 데이터 모델의 테스트 반영", 작업 4 "화면에서 프로젝트 코드 선택 가능, 목록에 없는 코드 거부". acceptance test_3은 register가 project_code를 저장해야 통과하므로 작업 4의 시험이 작업 2의 데이터 모델에 의존한다 | 조치 없음. "구현 에이전트가 통과 값이 false인 첫 단위부터"는 reference/CLAUDE.example.md 13행과 일치 |
| 15 | 일치(확인) | 그림 6-1 SVG 문구와 aria-label | 본문, 표 6-1, 6-2와 일치 | 세 종류 단위의 담당과 확인(사람/결정 기록, 에이전트/검사, 에이전트 작성·사람 승인/사람 승인), 통과 값 false에서 true, 미달 시 같은 단위 다시, 다음 단위로 반복이 모두 본문 18행, 표 6-2와 같다. aria-label이 SVG text를 빠짐없이 옮김. 캡션 "(이 책의 정리)"로 분류가 책의 정리임을 밝힘(Q-044) | 조치 없음 |
| 16 | 일치(확인), 참고 | 그림 6-2 SVG 문구와 aria-label | 요약 반환, 비용 합산은 일치. 예시 3종(테스트 실행, 자료 조사, 로그 분석)은 이 책의 예 | 비용 띠의 "비용 상한과 사용량에 포함"은 31행과 일치(다만 상한은 SDK 기준이라는 한정이 그림에는 없음). 테스트 실행, 로그 처리는 costs 문서 "Delegate verbose operations"의 예와 같고, 자료 조사 탐색은 sub-agents 문서의 대량 탐색 용도와 같다. aria-label이 SVG와 일치. 캡션 "(에이전트 제품 문서를 바탕으로 이 책이 정리)" | 비용 띠에 "Agent SDK" 한정을 넣을지는 선택. 1번 지적(포크)을 반영할 때 함께 손보면 됨 |
| 17 | 참고 | 33행 "이 책은 하위 에이전트만 다룹니다" | 책의 범위 선언 | 사실 문장이 아님(판정 대상 아님) | 조치 없음 |
| 18 | 참고 | 참고 자료 항목 ref-anthropic-2026 | 형식 | 일치 | 문서 4개(Create custom subagents, How the agent loop works, Manage costs effectively, Glossary)가 한 항목에 있고, 확인일 표기 "2026년 10월 20일"이다. URL은 없다(STYLE 4절은 id 링크만 요구). ref-young-2025 날짜 2025년 11월 26일은 원문과 일치 | 조치 없음 |

## 찾지 못한 범위
- sub-agents 문서의 끝 약 9.5천 자를 읽었다(예시와 다음 단계 절, 영향 없음). C6 기록의 "확인하지 못한 것"은 해소됨. How Claude Code works는 이번에도 열지 않았고 판정에 쓰지 않았다.
- check.py, 단위 테스트의 실행 결과는 확인하지 못했다(셸 없음). 12, 13번은 소스 읽기와 RUNLOG 기록에 기댄 판정이다.

## 재발 주의 항목 점검
- 사례 주체(제품 팀 vs 사용한 팀): 7번 참조(Young 글의 "Claude Code" 표기).
- 사용량 화면 금액은 정가 기준: ch06 본문에 금액 서술 없음. costs 문서는 `/usage` 금액을 정가 기준 추정치로 설명(확인 2026-10-20). 9장 쪽 주의 대상.
- 권한 모드 기본값, 승인 정책 값, 규칙 문서 대체 읽기: ch06 범위에 해당 문장 없음.


## 처리(메인 세션)
| 항목 | 처리 | 내용 |
|---|---|---|
| 1 필수(포크) | 반영 | 본문 29행 포크 예외 유지, 표 6-3 "(포크 방식은 예외)", 그림 6-2 머리 줄과 aria-label "(포크 제외)", 정할 것 "일반 하위 에이전트" |
| 2 권장 | 반영 | 비용 문단에 주체(비용 문서와 Agent SDK 문서)와 인용 |
| 4 권장 | 반영 | "Claude Code 용어집은 … 설명합니다" |
| 5 권장 | 반영 | "최종 응답만 요약으로" |
| 6 참고 | 유지 | 상한 초과 여유는 9장 몫 |
| 7 참고 | 작가 확인 | Q-039에 6장 16, 17행 추가 |
| 13 참고 | 유지 | RUNLOG 실패 목록에서 도출, 본문 문장 맞음 |
