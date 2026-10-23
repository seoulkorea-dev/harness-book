# 6장 역할 검토: 실무자 1회 읽기(2026-10-23, 이슈 #66, D-139)

- 대상: src/chapters/ch06.html(브랜치 ch06-rework, 29dc5e0). 읽기만 함
- 대조: REVIEW_RULES.md(R1~R19), BOOK_STANDARD.md(4, 5, 7~12절), docs/example-facts.md, tasks.example.json, CLAUDE.example.md, settings.example.json, check.py, RUNLOG.md, acceptance/test_cr07.py, research/ch06-sources.md, bibliography.json, 이슈 #65, AUTHOR_QUEUE(Q-039, Q-101), 실습 1, 5, terms.html, ch02, ch03, ch07
- 실제 실행: git 2.55 임시 저장소에서 commit하지 않은 새 파일은 `git diff HEAD -- tasks.json`에 나오지 않음(종료 코드 0, `git status`에는 `?? tasks.json`). 스테이징 뒤 인자 없는 `git diff`는 비고 `git diff HEAD`에는 나옴
- 고칠 문장 비율: 47 ÷ 132 = 35.6%(필수 13문장 = 9.8%)
- 절별(N/고칠/필수): 도입 9/4/1, selection 11/1/0, split 35/12/4, multi-agent 27/12/2, example 36/12/4, fail 2/1/0, check 7/4/2, principle 5/1/0

## 총평
이슈 #65 대부분 반영. 남은 것은 실습에서 막히는 곳(확인 명령 실행 폴더, tasks.json을 commit하지 않으면 git diff HEAD가 빔, 작업 2, 3 동안 check.py 종료 코드 1)과 개념 경계(세 종류 경계 설명, multi-agent 절의 "작업 단위"가 하위 작업 뜻, "갱신 권한"이 강제처럼 읽힘 R16, 작업 5 완료 기준 문구). 내부 작업 이름("Chapter 3의 예제 정비")과 틀린 장 참조(중단 기준이 Chapter 7에 있다는 안내)는 필수.

## 필수(요약)
| 위치 | 발견 | 제안 요지 |
|---|---|---|
| lead, split | 작업 단위 정의 두 가지 | 하나로("한 세션 안에 끝내는 것을 목표로 하고 완료 기준과 확인 방법을 갖춘 업무의 조각") |
| split 3문단 | 발표 주체 | #65, Q-101대로 "Claude Code의 장기 실행 글" |
| split 6문단 | 세 종류 경계 | 누가 수행하는지와 누가 확인하는지 |
| split 끝 문단 | 중단 기준 Chapter 7(ch07에 "중단" 0건) | Chapter 3 예제의 중단 규칙 |
| multi-agent 1문단 | "작업 단위"가 하위 작업 뜻 | "작업 단위나 그 안의 하위 작업" |
| example | check.py 종료 코드 1 | 작업 4 전에는 종료 코드 1, 확인 방법의 시험 결과로 판단 |
| example 4문단, 표 6-4 | 작업 5 완료 기준 "초안" | 초안 작성(에이전트)과 승인(승인자) |
| example 5문단 | "Chapter 3의 예제 정비" | 내부 작업 이름 삭제, 공백을 메우는 방법으로 |
| example 6문단 | "갱신 권한"이 강제처럼 | 권한 규칙은 파일 단위라 통과 값만 고치도록 강제하지 못함, 지시와 변경 차이 검토 |
| check 1문단 | 실행 폴더 | 실습 1의 실습 폴더(expense-practice) |
| check 2문단 | tasks.json 미commit이면 diff가 빔 | 첫 단위 전에 tasks.json commit |

## 권고(요약)
lead의 컨텍스트 윈도 한계, 예제 정식 이름 첫 등장과 진행 기록, 요약 셋째 항목 네 이름, 협의 기준 "결재를 기다리지 않고", 사람 단위에서 멈춤, 공개 사례 단정 완화, 지시와 결과 구분, 검사 단위 정의, 하위 항목 "통과 값 변경" 통일, 꼬인 문장, 그림 읽는 법에 중단, 포크 기본값(v2.1.302, 확인 뒤), 위임 요청도 주 대화에 남음, 비용 증가 이유, 비용 상한은 SDK 설정, 에이전트 팀은 Claude Code 기능, 맡기는 방식 정의, 격리의 뜻, 보고 형식, 비용 상한 정할 것, 버전 주석 상한 초과 여유, 기준 적용 순서와 판정, 담당 열은 목록에 없음, test_5 설명, 공백 보완, 글 이름 통일, 운영 선택 이유, 예제 비용 상한, 표 6-5 소개, "보고가 아니라", HEAD 이유, 점검 질문 2

## 표, 그림(비율 밖)
표 6-1 협의 질문과 검증 조치, 표 6-2 첫째, 둘째 행 제약(R16, R17), 그림 6-1 중단 출구와 사람 단위, 그림 6-2 화살표 "맡길 작업과 필요한 정보"(필수), 표 6-3 제약 과장, 표 6-4 작업 5(필수)와 열 세트(작가 확인), 표 6-5 넷째 행과 설명 줄, 공백 행, 표 6-6 둘째~넷째 행

## 6장 밖
CLAUDE.example.md "통과하면"과 중단 규칙(종료 코드 1, PR #88), 실습 5 단계 1에 tasks.json commit 없음, commit 메시지 규칙 없음, 용어표와 terms.html의 작업 단위 정의(AUTHOR_QUEUE)
