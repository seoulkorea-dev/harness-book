# 부록 사실 점검(fact-checker)

## 1. 결론(필수 24, 권고 32)

점검 대상은 브랜치 appendix-playbook의 bbf1459 시점 src/appendix/terms.html과 practice.html입니다. 작업 중에 bbf1459(check.py 요약 줄 순서, 실행 날짜, 인계 항목 위치 수정)가 반영되어 practice.html은 그 뒤 문안으로 다시 맞췄습니다. 원고와 파일은 고치지 않았습니다.

**용어 풀이(terms.html)**
- 정의가 본문과 다른 항목이 있습니다. 프롬프트는 본문이 "사람이 이번 작업에 입력하는 요청"으로 좁혀 정의했는데 용어 풀이는 일반 의미로 썼습니다. 저장소와 CI도 정의가 다릅니다. 하네스는 핵심 정의(BOOK_SPEC 4절)와 문구가 다릅니다.
- "(Chapter n)" 링크 가운데 처음 정의한 장이 아닌 것이 있습니다. 장이 다른 경우는 세션, 권한 규칙, 훅, 승인 지점, 완료 기준, 규칙 문서, 검사 스크립트, CI, 저장소 아홉 건(필수)입니다. 같은 장의 다른 절인 경우는 수용 기준, 지시와 강제, 자동 메모리, 격리, 컨텍스트 네 건(권고)입니다.
- 근거 없는 설명이 한 건 있습니다. Skill 항목의 "Chapter 11은 … 하는 일을 드러내려고 절차 묶음이라고 부릅니다"는 ch11에 그 이유가 없습니다.
- 본문에서 정의한 용어가 빠져 있습니다. BOOK_SPEC 4절과 5절에 있는 11개(실행 장치, 설정, 다섯 구성 요소, 세 설계 층, 에이전트 루프, 턴, 영역, 하네스 설정 파일, 역할, 기록, 검증)는 필수입니다. "…라고 합니다"로 정의한 용어 중 빠진 것 19개는 권고입니다.
- 본문에 없는 용어는 없습니다. 50개 항목이 모두 본문에 나옵니다. 저장소는 ch01#request에 정의가 있어 본문 용어가 맞습니다.
- 모든 href와 앵커는 실제로 존재합니다. 링크 문구(절 제목)도 일치합니다.
- 용어 풀이 안에서 구별이 흐린 짝은 프롬프트/컨텍스트(필수 1번으로 해소), 하네스/실행 장치/설정(필수 12, 13, 14번으로 해소), 수용 기준/검증 기준(권고 25, 34번으로 해소)입니다. 승인 정책/권한 모드, 규칙 파일/규칙 문서, 격리/샌드박스는 정의로 구별됩니다.

**실습(practice.html)**
- 공식 문서와 대조해 틀린 제품 설명은 없습니다. 확인한 사실은 다음과 같습니다.
  - 무료 요금제 미포함, Pro·Max·Team·Enterprise·Console 계정 사용
  - 설치 명령 두 줄
  - Git for Windows가 있으면 Git Bash를 쓰고 PowerShell 도구도 함께 켜질 수 있다는 설명
  - Bash 금지 규칙이 있으면 PowerShell 도구가 꺼진다는 설명
  - 신뢰 화면
  - /permissions, /hooks, /memory, /usage, /exit, claude --continue
  - 자동 메모리 기본값과 보관 위치
  - /usage 금액이 정가 기준 추정치라는 설명
- 인용 불일치는 1건입니다(필수 24번). /context의 Memory files 문장이 context-window를 인용하는데 그 문서에는 "Memory files"라는 표시 이름이 없습니다.
- Chapter 9, 10과의 정합: 샌드박스 기본 꺼짐과 "금지 규칙은 문자열만 대조" 설명은 같습니다. 다만 ch10은 v2.1.283 이상의 터미널이 auto로 시작한다고 쓰는데, 실습은 "버전과 권한 모드에 따라"라고만 썼습니다(권고 51번).
- 실행 확인(R8): 실습 1의 복사, git init, commit, 단위 테스트, check.py를 2026-10-24 Linux에서 실행했습니다. 설명과 같았고, check.py 요약 줄 순서(tests → FAILED → acceptance)는 bbf1459 이후 문안과 일치합니다. 출력 원문은 3절에 있습니다.
- 클론 URL(github.com/seoulkorea-dev/harness-book)은 열리고, 기본 브랜치 main에 examples/expense-app/이 있습니다.

**작가 확인 필요(AUTHOR_QUEUE 후보)**
- 요청 단위 이름: BOOK_SPEC 5절은 "하나의 요청"이고 "한 요청"은 쓰지 않는다고 하는데, ch03·ch04·ch05는 "요청 한 건"을 15회 씁니다. 용어 풀이 완료 기준 항목도 "요청 한 건"입니다. 용어 풀이만 고치지 않고 작가 판단을 받아야 합니다.
- Skill과 절차 묶음: ch05는 Skill, ch11은 절차 묶음(Skill)로 한 개념에 두 이름을 씁니다(플레이북 5장 "한 개념에는 한 이름").
- 괄호 속 풀이(빌드, 피드백 루프, 시스템 프롬프트, 승인 피로, XML 태그, 컨테이너, 가상 머신 등)를 용어 풀이에 넣을지는 기준이 없어 하나씩 판정하지 않았습니다. 포함 기준을 작가가 정해야 합니다(미확인).

## 2. 지적 표

가나다순 삽입 위치 요약(기존 항목 뒤에 새 항목을 이 순서로 넣음):
- 검수 문서 뒤: 검증, 검증 기준
- 규칙 파일 뒤: 기록, 기준표, 다섯 구성 요소
- 독립 검수 뒤: 변환, 빌드
- 샌드박스(Sandbox) 뒤: 설정, 세 설계 층
- 승인 지점 뒤: 승인자
- 실행 로그 뒤: 실행 장치, 압축, 업무 항목, 에이전트 루프
- 에이전트 명세서 뒤: 에이전트 제품
- 에이전트(Agent) 뒤: 역할, 영역, 예시 답안
- 워크플로(Workflow) 뒤: 원본 자료
- 작업 단위 뒤: 작업 단위 분할
- 저장소 뒤: 종료 코드, 주 에이전트, 지속적 통합
- 진행 기록 뒤: 채점
- 컨텍스트(Context) 뒤: 턴
- 토큰(Token) 뒤: 편집 뒤 훅
- 프롬프트 엔지니어링(Prompt Engineering) 뒤: 하네스 설정 파일
- 영어 절 CLAUDE.md 뒤: commit, commit 확인

### 2-1. 기존 항목의 정의와 링크

| 번호 | 등급 | 위치 | 문제와 근거 | 원문 | 고친 문안 |
|---|---|---|---|---|---|
| 1 | 필수 | terms, 프롬프트 | 본문 정의와 다릅니다. ch01#layers는 프롬프트를 "사람이 이번 작업에 입력하는 요청"으로 좁히고 시스템 프롬프트는 컨텍스트로 분류합니다(BOOK_SPEC 5절도 같음). 풀이의 "모델에 주는 지시문"은 같은 풀이의 컨텍스트 항목("프롬프트는 그 일부")과도 충돌합니다. 영문 병기도 빠졌습니다(프롬프트 엔지니어링 항목은 있음). | `<dt>프롬프트</dt><dd>모델에 보내는 요청, 곧 모델에 주는 지시문입니다. <a href="../chapters/ch01.html#layers">(Chapter 1)</a></dd>` | `<dt>프롬프트(Prompt)</dt><dd>사람이 이번 작업에 입력하는 요청입니다. 컨텍스트의 일부이며, 제품이 미리 포함하는 시스템 프롬프트는 컨텍스트로 분류합니다. <a href="../chapters/ch01.html#layers">(Chapter 1)</a></dd>` |
| 2 | 필수 | terms, 저장소 | 정의가 다르고 링크가 본문이 아닙니다. 본문 정의는 ch01#request와 ch08 도입의 "코드와 문서를 변경 이력과 함께 보관하는 곳"입니다. 풀이는 "Git으로 관리하는 폴더"라고 새로 정의하고 부록 실습으로 연결합니다. | `<dt>저장소</dt><dd>파일과 그 변경 이력을 Git으로 관리하는 폴더입니다. 변경을 이력에 남기는 일을 commit이라고 합니다. <a href="practice.html#lab-1">(부록 실습 1)</a></dd>` | `<dt>저장소</dt><dd>코드와 문서를 변경 이력과 함께 보관하는 곳입니다. <a href="../chapters/ch01.html#request">(Chapter 1)</a></dd>` |
| 3 | 필수 | terms, CI(영어 절) | 정의와 링크가 어긋납니다. ch01#loop가 먼저 "지속적 통합(Continuous Integration, CI)은 저장소에 변경이 올라올 때 자동으로 검사를 실행하는 장치"라고 정의합니다. 풀이는 "방식"이라 쓰고 빌드까지 넣었으며, ch07#report는 재사용 위치입니다. 본문 표기도 한글 먼저입니다(영문 병기 규칙). 이 항목은 영어 절에서 지우고 한국어 절(저장소 뒤)로 옮깁니다. 빌드 풀이는 권고 40번으로 따로 둡니다. | `<dt>CI(Continuous Integration)</dt><dd>저장소에 변경을 반영할 때마다 빌드(원고나 코드로 결과물을 만드는 일)와 검사를 자동으로 실행하는 방식입니다. <a href="../chapters/ch07.html#report">(Chapter 7)</a></dd>` | `<dt>지속적 통합(Continuous Integration, CI)</dt><dd>저장소에 변경이 올라올 때 자동으로 검사를 실행하는 장치입니다. <a href="../chapters/ch01.html#loop">(Chapter 1)</a></dd>` |
| 4 | 필수 | terms, 세션 | 처음 정의한 곳은 ch01#agent-harness("세션은 에이전트와 한 번 대화를 시작해 끝낼 때까지")이고 ch08은 이후 장입니다. | `<dt>세션</dt><dd>에이전트와 한 번 대화를 시작해 끝낼 때까지입니다. 새 세션은 이전 세션의 대화를 알지 못합니다. <a href="../chapters/ch08.html#session">(Chapter 8)</a></dd>` | `<dt>세션</dt><dd>에이전트와 한 번 대화를 시작해 끝낼 때까지입니다. 새 세션은 이전 세션의 대화를 알지 못합니다. <a href="../chapters/ch01.html#agent-harness">(Chapter 1)</a> <a href="../chapters/ch08.html#session">(Chapter 8)</a></dd>` |
| 5 | 필수 | terms, 권한 규칙 | 처음 정의한 곳은 ch01#background("권한 규칙(Permission Rule)은 도구 호출을 허용, 확인 요청, 금지로 나눠 정한 규칙")입니다. 평가 순서 문장은 ch02#tool-scope와 공식 문서(permissions, Manage permissions 절)로 확인되므로 ch02 링크는 유지합니다. | `<dt>권한 규칙(Permission Rule)</dt><dd>Claude Code에서 도구 사용을 허용(allow), 확인 요청(ask), 금지(deny)하는 규칙입니다. 금지, 확인 요청, 허용의 순서로 평가합니다. <a href="../chapters/ch02.html#tool-scope">(Chapter 2)</a></dd>` | `<dt>권한 규칙(Permission Rule)</dt><dd>Claude Code에서 도구 사용을 허용(allow), 확인 요청(ask), 금지(deny)하는 규칙입니다. 금지, 확인 요청, 허용의 순서로 평가합니다. <a href="../chapters/ch01.html#background">(Chapter 1)</a> <a href="../chapters/ch02.html#tool-scope">(Chapter 2)</a></dd>` |
| 6 | 필수 | terms, 훅 | 처음 정의한 곳은 ch01#loop("훅(Hook)은 정해진 시점에 자동으로 실행되는 명령입니다")이고 ch02#components가 아닙니다. | `<dt>훅(Hook)</dt><dd>파일 수정 직후처럼 정해진 시점에 자동으로 실행되는 셸 명령입니다. 예를 들어 파일을 수정할 때마다 테스트를 실행하게 할 수 있으며, 에이전트의 판단과 관계없이 적용됩니다. 제품에는 다른 형식의 훅도 있지만, 본문은 셸 명령을 실행하는 훅만 다룹니다. <a href="../chapters/ch02.html#components">(Chapter 2)</a></dd>` | `<dt>훅(Hook)</dt><dd>파일 수정 직후처럼 정해진 시점에 자동으로 실행되는 셸 명령입니다. 예를 들어 파일을 수정할 때마다 테스트를 실행하게 할 수 있으며, 에이전트의 판단과 관계없이 적용됩니다. 제품에는 다른 형식의 훅도 있지만, 본문은 셸 명령을 실행하는 훅만 다룹니다. <a href="../chapters/ch01.html#loop">(Chapter 1)</a> <a href="../chapters/ch02.html#components">(Chapter 2)</a></dd>` |
| 7 | 필수 | terms, 승인 지점 | 처음 정의한 곳은 ch01#loop("승인 지점은 되돌리기 어려운 동작에서 사람이 개입하는 자리입니다")입니다. 링크가 ch03, ch09만 있습니다. | `<a href="../chapters/ch03.html#spec">(Chapter 3)</a> <a href="../chapters/ch09.html#approval">(Chapter 9)</a></dd>` | `<a href="../chapters/ch01.html#loop">(Chapter 1)</a> <a href="../chapters/ch03.html#spec">(Chapter 3)</a> <a href="../chapters/ch09.html#approval">(Chapter 9)</a></dd>` |
| 8 | 필수 | terms, 완료 기준 | 처음 정의한 곳은 ch01#request이고 정의 문구는 "작업이 끝났다고 판정하는 조건"입니다(BOOK_SPEC 5절도 같음). 풀이는 "받아들여지기 위해 충족해야 하는 조건"이라 쓰고 링크도 ch04, ch07만 있습니다. 풀이가 쓰는 "요청 한 건"은 작가 확인 필요(결론의 작가 확인 항목)이므로 이번 고침에서는 그대로 둡니다. | `<dt>완료 기준</dt><dd>요청 한 건이나 작업 단위 하나가 받아들여지기 위해 충족해야 하는 조건입니다. 요청의 네 요소 가운데 하나이며, 작업 단위 목록에서는 작업을 맡기기 전에 검사할 수 있는 형태로 변환합니다. 완료 기준 가운데 사람이 정한 것이 수용 기준입니다. <a href="../chapters/ch04.html#elements">(Chapter 4)</a> <a href="../chapters/ch07.html#criteria">(Chapter 7)</a></dd>` | `<dt>완료 기준</dt><dd>요청 한 건이나 작업 단위 하나가 끝났다고 판정하는 조건입니다. 요청의 네 요소 가운데 하나이며, 작업 단위 목록에서는 작업을 맡기기 전에 검사할 수 있는 형태로 변환합니다. 완료 기준 가운데 사람이 정한 것이 수용 기준입니다. <a href="../chapters/ch01.html#request">(Chapter 1)</a> <a href="../chapters/ch04.html#elements">(Chapter 4)</a> <a href="../chapters/ch07.html#criteria">(Chapter 7)</a></dd>` |
| 9 | 필수 | terms, 규칙 문서 | 처음 정의한 곳은 ch01#request("규칙 문서는 작업 규칙을 적어 프로젝트에 두는 파일로, Claude Code에서는 CLAUDE.md, Codex에서는 AGENTS.md")입니다. | `<dt>규칙 문서</dt><dd>에이전트가 세션마다 읽는 프로젝트 지침입니다. CLAUDE.md와 AGENTS.md가 해당합니다. <a href="../chapters/ch05.html#rule-doc">(Chapter 5)</a></dd>` | `<dt>규칙 문서</dt><dd>에이전트가 세션마다 읽는 프로젝트 지침입니다. CLAUDE.md와 AGENTS.md가 해당합니다. <a href="../chapters/ch01.html#request">(Chapter 1)</a> <a href="../chapters/ch05.html#rule-doc">(Chapter 5)</a></dd>` |
| 10 | 필수 | terms, 검사 스크립트 | ch02#example이 "검사 스크립트: 단위 테스트와 수용 시험을 한 번에 실행해 결과를 출력하는 파일(check.py)"로 먼저 정의합니다. 링크가 ch03뿐입니다. | `<dt>검사 스크립트</dt><dd>단위 테스트와 수용 시험을 한 번에 실행하는 파일입니다. 예제에서는 check.py입니다. <a href="../chapters/ch03.html#example">(Chapter 3)</a></dd>` | `<dt>검사 스크립트</dt><dd>단위 테스트와 수용 시험을 한 번에 실행하는 파일입니다. 예제에서는 check.py입니다. <a href="../chapters/ch02.html#example">(Chapter 2)</a> <a href="../chapters/ch03.html#example">(Chapter 3)</a></dd>` |
| 11 | 필수 | terms, Skill | R4 근거 없는 서술입니다. "Chapter 11은 … 하는 일을 드러내려고 절차 묶음이라고 부릅니다"의 이유는 ch11에 없습니다. ch11#this-book-now는 "절차 묶음(Skill)은 필요할 때만 읽히는 절차"라고만 씁니다. ch05#kinds의 정의는 "Skill(필요할 때 읽히는 지침 묶음)", 기본 설정에서는 이름과 설명만 컨텍스트에 상시 있다는 설명도 ch05에 있습니다. 두 이름 문제는 작가 확인 필요(결론 참조). | `<dt>Skill</dt><dd>필요할 때만 읽히는 지침과 자료의 묶음입니다. 상시 규칙 문서를 짧게 유지하려고 사용하며, Chapter 11은 Claude Code의 기능 이름 대신 하는 일을 드러내려고 절차 묶음이라고 부릅니다. <a href="../chapters/ch05.html#kinds">(Chapter 5)</a></dd>` | `<dt>Skill</dt><dd>필요할 때 읽히는 지침 묶음입니다. 상시 규칙 문서를 짧게 유지하려고 사용하며, 기본 설정에서는 이름과 설명만 늘 컨텍스트에 있고 본문은 필요할 때 읽힙니다. Chapter 11은 같은 대상을 절차 묶음(Skill)이라고 부릅니다. <a href="../chapters/ch05.html#kinds">(Chapter 5)</a> <a href="../chapters/ch11.html#this-book-now">(Chapter 11)</a></dd>` |
| 12 | 필수 | terms, 하네스 | BOOK_SPEC 4절 핵심 정의("모델이 에이전트로 일할 수 있게 하는 모델 바깥의 실행 체계 전체", "바꾸지 않음")와 문구가 다릅니다. 또 풀이는 하네스가 "기록, 검증을 맡습니다"라고 하는데, ch01#agent-harness는 기록과 검증을 설정이 정하는 구성 요소로, 실행 장치는 루프 실행, 도구 제공, 컨텍스트 관리, 권한 확인, 세션 기록으로 나눕니다. 괄호 속 구분도 달라 실행 장치와 설정이 구별되지 않습니다. | `<dt>하네스(Harness)</dt><dd>모델을 에이전트로 동작하게 하는 모델 바깥의 실행 체계입니다. 루프 실행, 도구 제공, 컨텍스트 관리, 권한, 기록, 검증을 맡습니다. 제품이 제공하는 실행 장치(루프, 도구 실행)와 사용자와 팀이 정하는 설정(규칙 문서, 권한 규칙, 훅)으로 나뉩니다. <a href="../chapters/ch01.html#agent-harness">(Chapter 1)</a></dd>` | `<dt>하네스(Harness)</dt><dd>모델이 에이전트로 일할 수 있게 하는 모델 바깥의 실행 체계 전체입니다. 제품이 제공하는 실행 장치(루프 실행, 도구 제공, 컨텍스트 관리, 권한 확인, 세션 기록)와 사용자와 팀이 정하는 설정(규칙 문서, 권한 설정, 자동 검사, 역할 분담)으로 나뉩니다. <a href="../chapters/ch01.html#agent-harness">(Chapter 1)</a></dd>` |
| 25 | 권고 | terms, 수용 기준 | 같은 장(ch03)이지만 정의 문장은 #spec에 있습니다. 정의는 "완료 기준 가운데 사람이 업무의 요구로 정한 것"입니다. 풀이의 "변경 요청 문서"는 BOOK_SPEC 6절의 "변경 요청 사항 문서(docs/CR.md)"와 다른 이름입니다. 완료 기준과의 관계가 이 항목에 없습니다. | `<dt>수용 기준</dt><dd>사람이 정한 완료 조건으로, 결과물이 받아들여지기 위해 충족해야 하는 조건입니다. 변경 요청 문서에 적습니다. <a href="../chapters/ch03.html#example">(Chapter 3)</a></dd>` | `<dt>수용 기준</dt><dd>완료 기준 가운데 사람이 업무의 요구로 정한 것으로, 충족해야 할 조건입니다. 예제에서는 변경 요청 사항 문서(docs/CR.md)에 적습니다. <a href="../chapters/ch03.html#spec">(Chapter 3)</a></dd>` |
| 26 | 권고 | terms, 지시와 강제 | 정의 문장은 ch02#components에 있고(#instruct-enforce는 규칙 처리 절차를 다루는 뒤 절), 문구는 본문과 같습니다. | `<a href="../chapters/ch02.html#instruct-enforce">(Chapter 2)</a></dd>` (지시와 강제 항목 끝) | `<a href="../chapters/ch02.html#components">(Chapter 2)</a></dd>` |
| 27 | 권고 | terms, 자동 메모리 | ch02에서 자동 메모리가 나오는 곳은 #example(표 2-4 아래 문단) 한 곳뿐이고 #components에는 없습니다. 정의 문구는 같습니다. 보관 위치(컴퓨터마다 따로)는 ch08#session이고 공식 문서(memory, Auto memory 절)로 확인했습니다. | `<dt>자동 메모리</dt><dd>Claude Code가 작업 중에 알게 된 내용을 기기 안의 파일에 스스로 기록하고 다음 세션에 읽는 기능입니다. <a href="../chapters/ch02.html#components">(Chapter 2)</a></dd>` | `<dt>자동 메모리</dt><dd>Claude Code가 작업 중에 알게 된 내용을 기기 안의 파일에 스스로 기록하고 다음 세션에 읽는 기능입니다. <a href="../chapters/ch02.html#example">(Chapter 2)</a> <a href="../chapters/ch08.html#session">(Chapter 8)</a></dd>` |
| 28 | 권고 | terms, 격리 | 격리의 정의 문장은 ch09#kinds("격리는 에이전트가 실행한 명령이 정한 범위 밖의 파일과 네트워크에 닿지 못하게, 에이전트 프로그램 바깥의 운영 체제가 막는 일")에 있습니다. 컨테이너와 가상 머신 설명은 #isolation이므로 둘 다 연결합니다. | `<dt>격리</dt><dd>접근 범위를 운영 체제 수준에서, 곧 에이전트 프로그램이 아니라 컴퓨터의 운영 체제가 막는 방식으로 제한하는 일입니다. 샌드박스와 격리된 실행 환경(컨테이너나 가상 머신)이 해당합니다. <a href="../chapters/ch09.html#isolation">(Chapter 9)</a></dd>` | `<dt>격리</dt><dd>접근 범위를 운영 체제 수준에서, 곧 에이전트 프로그램이 아니라 컴퓨터의 운영 체제가 막는 방식으로 제한하는 일입니다. 샌드박스와 격리된 실행 환경(컨테이너나 가상 머신)이 해당합니다. <a href="../chapters/ch09.html#kinds">(Chapter 9)</a> <a href="../chapters/ch09.html#isolation">(Chapter 9)</a></dd>` |
| 29 | 권고 | terms, 샌드박스 | ch01#background가 "격리 환경, 곧 샌드박스(Sandbox)"로 먼저 소개합니다(범위는 폴더 밖 파일과 네트워크). 풀이는 ch09의 구체 정의를 씁니다. 공식 문서(sandboxing)로 기본 꺼짐, 셸 명령과 하위 프로세스만 대상, 파일 도구 제외를 확인했으므로 정의 문구는 맞습니다. 첫 소개 장을 병기합니다. | `Claude Code에서는 기본으로 꺼져 있고, 파일 편집 도구는 대상이 아닙니다. <a href="../chapters/ch09.html#isolation">(Chapter 9)</a></dd>` | `Claude Code에서는 기본으로 꺼져 있고, 파일 편집 도구는 대상이 아닙니다. <a href="../chapters/ch01.html#background">(Chapter 1)</a> <a href="../chapters/ch09.html#isolation">(Chapter 9)</a></dd>` |
| 30 | 권고 | terms, 컨텍스트 | 정의 문장은 ch01#background에 있습니다. #layers는 프롬프트와의 관계를 다루는 절입니다. | `<dt>컨텍스트(Context)</dt><dd>모델이 응답을 생성할 때 입력되는 정보 전체입니다. 프롬프트는 그 일부입니다. <a href="../chapters/ch01.html#layers">(Chapter 1)</a></dd>` | `<dt>컨텍스트(Context)</dt><dd>모델이 응답을 생성할 때 입력되는 정보 전체입니다. 프롬프트는 그 일부입니다. <a href="../chapters/ch01.html#background">(Chapter 1)</a> <a href="../chapters/ch01.html#layers">(Chapter 1)</a></dd>` |
| 31 | 권고 | terms, 컨텍스트 윈도 | 연결한 ch01#background에 /context 설명이 없습니다(ch01#check 표 1-9, ch05#resource에 있음). 명령은 공식 문서(commands, /context)로 확인됩니다. 본문에서 정의한 뜻만 싣는 풀이 원칙에 맞춰 문장을 뺍니다. | `<dt>컨텍스트 윈도(Context Window)</dt><dd>모델이 한 번에 처리할 수 있는 토큰의 범위입니다. Claude Code에서는 /context 명령으로 사용 현황을 확인합니다. <a href="../chapters/ch01.html#background">(Chapter 1)</a></dd>` | `<dt>컨텍스트 윈도(Context Window)</dt><dd>모델이 한 번에 처리할 수 있는 토큰의 범위입니다. <a href="../chapters/ch01.html#background">(Chapter 1)</a></dd>` |
| 32 | 권고 | terms, 토큰 | 연결한 ch01#background에 /usage 설명이 없습니다(ch01#check, ch08#logs에 있음). 공식 문서(costs)로 /usage의 세션 금액은 API 사용자용이고 구독 사용자는 요금제 사용량 막대가 보입니다. 이 문장은 "사용량" 한 단어로는 부정확해질 수 있어 뺍니다. | `<dt>토큰(Token)</dt><dd>모델이 텍스트를 나누어 처리하는 단위입니다. Claude Code는 /usage 명령으로 사용량을 확인합니다. <a href="../chapters/ch01.html#background">(Chapter 1)</a></dd>` | `<dt>토큰(Token)</dt><dd>모델이 텍스트를 나누어 처리하는 단위입니다. <a href="../chapters/ch01.html#background">(Chapter 1)</a></dd>` |
| 33 | 권고 | terms, MCP | ch02#tool-scope는 "외부 시스템의 기능을 에이전트의 도구로 연결하는 개방형 표준"이라고 정의하고 "이를 구현한 프로그램을 MCP 서버"라고 합니다. 풀이의 "규약"은 본문에 없는 낱말이고, 연결한 ch01#agent-harness에는 "표준 방식"만 있습니다. | `<dt>MCP(Model Context Protocol)</dt><dd>외부 시스템의 기능을 에이전트의 도구로 연결하는 규약입니다.` (뒤 문장은 유지) | `<dt>MCP(Model Context Protocol)</dt><dd>외부 시스템의 기능을 에이전트의 도구로 연결하는 개방형 표준입니다.` (끝의 링크에 `<a href="../chapters/ch02.html#tool-scope">(Chapter 2)</a>` 병기) |
| 34 | 권고 | terms, 에이전트 | BOOK_SPEC 4절 핵심 정의 문구("인공지능 모델이 루프 안에서 …")와 ch01의 문구에서 "인공지능"을 뺐고, "루프(작업을 반복하는 실행 흐름)"는 본문 풀이("루프는 판단, 도구 실행, 결과 확인의 반복")와 다릅니다. 작가가 확정한 문안이면 그대로 두고 AUTHOR_QUEUE에 올립니다. | `<dt>에이전트(Agent)</dt><dd>모델이 루프(작업을 반복하는 실행 흐름) 안에서 도구를 사용해 다음 행동을 스스로 정하고, 결과를 확인하며, 목표를 이룰 때까지 반복하는 시스템입니다. 모델과 하네스로 이루어집니다. <a href="../chapters/ch01.html#agent-harness">(Chapter 1)</a></dd>` | `<dt>에이전트(Agent)</dt><dd>인공지능 모델이 루프(Loop) 안에서 도구를 사용해 다음 행동을 스스로 정하고, 결과를 확인하며, 목표를 이룰 때까지 이 과정을 반복하는 시스템입니다. 루프는 판단, 도구 실행, 결과 확인의 반복입니다. 에이전트는 모델과 하네스로 이루어집니다. <a href="../chapters/ch01.html#agent-harness">(Chapter 1)</a></dd>` |
| 35 | 권고 | terms, 정렬 | 정렬 기준 안내(가나다순)와 맞지 않는 곳이 있습니다. 짧은 항목이 앞인 항목(도구/도구 호출, 프롬프트/프롬프트 엔지니어링)과 달리 컨텍스트, 하네스, 에이전트(Agent)는 긴 항목 뒤에 있습니다. 컨텍스트는 `컨텍스트 엔지니어링` 앞으로, 하네스는 `하네스 엔지니어링` 앞으로, 에이전트(Agent)는 `에이전트 명세서` 앞(에이전트 루프 뒤)으로 옮기는 것을 권합니다. 삽입 위치 요약은 이 순서를 전제하지 않고 현재 순서 기준입니다. | `<dt>컨텍스트 엔지니어링(Context Engineering)</dt>` (현재 컨텍스트보다 앞) | (문안 변경 없음. 위치만 이동) |

### 2-2. 필수 누락 용어(BOOK_SPEC 4절, 5절에 있고 본문이 정의한 용어)

| 번호 | 등급 | 위치(앞에 올 기존 항목) | 문제와 근거 | 원문 | 고친 문안 |
|---|---|---|---|---|---|
| 13 | 필수 | 용어 추가: 실행 장치 | ch01#agent-harness가 정의하고 prologue도 설명합니다. 하네스(핵심 정의)의 두 층 중 하나입니다. | `<dt>실행 로그</dt>` | `<dt>실행 장치</dt><dd>하네스 가운데 제품이 제공하는 층입니다. 루프 실행, 도구 제공, 컨텍스트 관리, 권한 확인, 세션 기록처럼 에이전트가 움직이는 데 필요한 기본 기능입니다. <a href="../chapters/ch01.html#agent-harness">(Chapter 1)</a></dd>` |
| 14 | 필수 | 용어 추가: 설정 | ch01#agent-harness가 정의합니다. 실행 장치와 짝으로 구별해야 하며, 설정이 없어도 에이전트는 제품 기본값으로 동작한다는 문장이 ch01에 있습니다. | `<dt>샌드박스(Sandbox)</dt>` | `<dt>설정</dt><dd>하네스 가운데 사용자와 팀이 맡길 업무에 맞춰 정하는 층입니다. 규칙 문서, 권한 설정, 자동 검사, 역할 분담처럼 정하는 값이며, 설정이 없어도 에이전트는 제품의 기본값으로 동작합니다. <a href="../chapters/ch01.html#agent-harness">(Chapter 1)</a></dd>` |
| 15 | 필수 | 용어 추가: 다섯 구성 요소 | ch01#agent-harness가 정의합니다. 핵심 정의입니다. | `<dt>규칙 파일</dt>` (기록, 기준표 다음) | `<dt>다섯 구성 요소</dt><dd>설정에서 정하는 항목을 다섯으로 정리한 것으로, 역할, 도구, 권한, 기록, 검증입니다. <a href="../chapters/ch01.html#agent-harness">(Chapter 1)</a></dd>` |
| 16 | 필수 | 용어 추가: 세 설계 층 | ch01#layers와 prologue가 정의합니다. 핵심 정의입니다. | `<dt>샌드박스(Sandbox)</dt>` (설정 다음) | `<dt>세 설계 층</dt><dd>프롬프트, 컨텍스트, 하네스를 묶어 이르는 말입니다. 제품이 정한 기본값 위에서 사용자와 팀이 설계합니다. <a href="../chapters/ch01.html#layers">(Chapter 1)</a></dd>` |
| 17 | 필수 | 용어 추가: 에이전트 루프 | ch01#loop가 정의합니다. BOOK_SPEC 5절의 용어입니다(다섯 단계 이름은 장마다 바꾸지 않음). | `<dt>실행 로그</dt>` (실행 장치, 압축, 업무 항목 다음) | `<dt>에이전트 루프</dt><dd>하네스가 판단과 실행을 반복하는 순서로, 컨텍스트 구성, 판단과 응답, 권한 확인, 도구 실행, 최종 응답의 다섯 단계입니다. <a href="../chapters/ch01.html#loop">(Chapter 1)</a></dd>` |
| 18 | 필수 | 용어 추가: 턴 | BOOK_SPEC 5절에서 턴은 "문서마다 범위가 다르므로 어느 문서 기준인지 밝힘"이라고 합니다. ch01#loop("Agent SDK 문서는 이 왕복 한 번을 턴이라고 부릅니다"), ch03, ch08("Agent SDK 문서 기준으로 도구 호출을 주고받은 횟수")과 맞춘 문안입니다. | `<dt>컨텍스트(Context)</dt>` | `<dt>턴</dt><dd>Agent SDK 문서가 에이전트 루프에서 도구 호출을 주고받는 왕복 한 번을 이르는 말입니다. 문서마다 범위가 달라 쓸 때는 어느 문서 기준인지 밝힙니다. <a href="../chapters/ch01.html#loop">(Chapter 1)</a></dd>` |
| 19 | 필수 | 용어 추가: 영역 | ch02#components가 정의합니다. BOOK_SPEC 5절의 용어입니다(지시, 실행 수단, 강제). | `<dt>에이전트(Agent)</dt>` (역할 다음) | `<dt>영역</dt><dd>다섯 구성 요소를 모델의 판단을 기준으로 나눈 지시 영역(역할, 기록), 실행 수단 영역(도구), 강제 영역(권한, 검증)입니다. <a href="../chapters/ch02.html#components">(Chapter 2)</a></dd>` |
| 20 | 필수 | 용어 추가: 하네스 설정 파일 | ch03#spec이 정의합니다. BOOK_SPEC 5절의 용어입니다("제품 파일"은 쓰지 않음). 설정과는 "층"과 "파일"로 구별됩니다. | `<dt>프롬프트 엔지니어링(Prompt Engineering)</dt>` | `<dt>하네스 설정 파일</dt><dd>에이전트 명세서의 값을 옮겨, Claude Code가 정해진 위치에서 자동으로 읽어 들이는 파일입니다. 규칙 문서(CLAUDE.md), 권한 규칙과 훅을 담는 설정 파일(.claude/settings.json), 하위 에이전트 정의가 해당합니다. <a href="../chapters/ch03.html#spec">(Chapter 3)</a></dd>` |
| 21 | 필수 | 용어 추가: 역할 | ch01#agent-harness가 정의합니다. BOOK_SPEC 5절의 용어입니다. | `<dt>에이전트(Agent)</dt>` | `<dt>역할</dt><dd>에이전트가 할 작업과 사람이 할 작업의 경계입니다. 다섯 구성 요소의 하나이며, 주로 규칙 문서에 적습니다. <a href="../chapters/ch01.html#agent-harness">(Chapter 1)</a></dd>` |
| 22 | 필수 | 용어 추가: 기록 | BOOK_SPEC 5절은 "설정에서는 결정 기록과 진행 기록, 실행 장치에서는 세션 기록. 범위는 Chapter 8 기준"이라고 합니다. ch01#agent-harness와 ch08#kinds로 맞춘 문안입니다. | `<dt>규칙 파일</dt>` | `<dt>기록</dt><dd>설정에서 정하는 구성 요소로, 무엇을 왜 정했는지 남긴 결정 기록과 작업이 어디까지 진행되었는지 남긴 진행 기록입니다. 실행 장치의 세션 기록과는 대상이 다릅니다. Chapter 8은 여기에 규칙 문서를 더해 기록을 세 종류로 나눕니다. <a href="../chapters/ch01.html#agent-harness">(Chapter 1)</a> <a href="../chapters/ch08.html#kinds">(Chapter 8)</a></dd>` |
| 23 | 필수 | 용어 추가: 검증 | ch01#agent-harness가 정의합니다. BOOK_SPEC 5절의 용어입니다. | `<dt>검수 문서</dt>` | `<dt>검증</dt><dd>결과를 받아들이기 전에 확인하는 방법과 기준입니다. 다섯 구성 요소의 하나입니다. <a href="../chapters/ch01.html#agent-harness">(Chapter 1)</a></dd>` |

### 2-3. 권고 누락 용어(본문이 "…라고 합니다" 등으로 정의한 용어)

| 번호 | 등급 | 위치(앞에 올 기존 항목) | 문제와 근거 | 원문 | 고친 문안 |
|---|---|---|---|---|---|
| 36 | 권고 | 용어 추가: 검증 기준 | 수용 기준과 짝으로 구별해야 하는 용어입니다. ch03#spec에 정의가 있습니다. | `<dt>검증</dt>` (위 23번 추가분 다음) | `<dt>검증 기준</dt><dd>수용 기준을 자동으로 판정하는 시험과 그 시험을 실행하는 작은 프로그램(스크립트)을 묶어 이르는 말입니다. 수용 기준은 충족해야 할 조건이고, 검증 기준은 그 조건의 충족 여부를 판정하는 파일입니다. <a href="../chapters/ch03.html#spec">(Chapter 3)</a></dd>` |
| 37 | 권고 | 용어 추가: 편집 뒤 훅 | ch02#instruct-enforce가 정의합니다. 공식 문서(hooks 계열)와 research/ch02-sources.md로 PostToolUse의 종료 코드 2가 stderr를 모델에 전달하고 이미 실행된 도구는 되돌리지 못함을 확인했습니다. | `<dt>토큰(Token)</dt>` | `<dt>편집 뒤 훅</dt><dd>도구 실행 뒤에 실행되는 PostToolUse 훅을 편집할 때마다 검사가 실행되게 하는 데 쓸 때의 이름입니다. 이미 실행된 편집은 되돌리지 못하고, 종료 코드 2로 끝나면 오류 출력을 모델에 전달합니다. <a href="../chapters/ch02.html#instruct-enforce">(Chapter 2)</a></dd>` |
| 38 | 권고 | 용어 추가: 종료 코드 | ch02#instruct-enforce가 처음 정의하고 ch03, ch07이 반복합니다. 실습 확인 방법에서 쓰입니다. | `<dt>저장소</dt>` | `<dt>종료 코드</dt><dd>명령이 끝나면서 성공이나 실패를 알리려고 돌려주는 숫자입니다. 0은 성공, 0이 아닌 값은 실패를 뜻합니다. <a href="../chapters/ch02.html#instruct-enforce">(Chapter 2)</a></dd>` |
| 39 | 권고 | 용어 추가: 업무 항목 | ch03#spec이 정의합니다. 에이전트 명세서 항목 아홉 개 중 구성 요소 다섯과 구별됩니다. | `<dt>실행 로그</dt>` | `<dt>업무 항목</dt><dd>에이전트 명세서의 아홉 항목 가운데 맡기는 업무 자체를 정하는 목적, 입력, 종료 조건, 승인 지점입니다. 나머지 다섯은 다섯 구성 요소인 역할, 도구, 권한, 기록, 검증입니다. <a href="../chapters/ch03.html#spec">(Chapter 3)</a></dd>` |
| 40 | 권고 | 용어 추가: 빌드 | CI 항목에서 빠지는 괄호 풀이이며 ch07#report에 정의가 있습니다. | `<dt>독립 검수</dt>` (변환 다음) | `<dt>빌드</dt><dd>원고나 코드로 결과물을 만드는 일입니다. <a href="../chapters/ch07.html#report">(Chapter 7)</a></dd>` |
| 41 | 권고 | 용어 추가: 원본 자료 | ch02#components가 먼저 "에이전트가 읽기만 하고 변경하면 안 되는 입력 자료"로 정의하고, ch03#example이 data/projects.csv를 원본 자료라고 합니다. | `<dt>워크플로(Workflow)</dt>` | `<dt>원본 자료</dt><dd>에이전트가 읽기만 하고 변경하면 안 되는 입력 자료입니다. 예제에서는 data/projects.csv입니다. <a href="../chapters/ch02.html#components">(Chapter 2)</a> <a href="../chapters/ch03.html#example">(Chapter 3)</a></dd>` |
| 42 | 권고 | 용어 추가: commit | ch03#example이 정의합니다("commit은 바뀐 파일을 저장소의 기록으로 남기는 명령"). 저장소 항목에서 이 문장을 빼므로 풀이로 옮깁니다. ch01, ch02에는 "변경 확정(git commit)"만 있어 정의 문장은 없음을 확인했습니다. | `<dt>CLAUDE.md</dt>` | `<dt>commit</dt><dd>바뀐 파일을 저장소의 기록으로 남기는 명령입니다. <a href="../chapters/ch03.html#example">(Chapter 3)</a></dd>` |
| 43 | 권고 | 용어 추가: commit 확인 | ch03#example이 정의합니다. | `<dt>CLAUDE.md</dt>` (commit 다음) | `<dt>commit 확인</dt><dd>사람이 commit을 승인하기 전에 바뀐 파일을 보는 일입니다. <a href="../chapters/ch03.html#example">(Chapter 3)</a></dd>` |
| 44 | 권고 | 용어 추가: 압축 | ch05#resource가 정의합니다. ch08 도입에서도 씁니다. | `<dt>실행 로그</dt>` (실행 장치 다음) | `<dt>압축</dt><dd>대화를 요약해 공간을 확보하는 일입니다. <a href="../chapters/ch05.html#resource">(Chapter 5)</a></dd>` |
| 45 | 권고 | 용어 추가: 작업 단위 분할 | ch06 도입 문단이 정의합니다(앵커가 있는 절 이전이라 장 링크만). | `<dt>작업 단위</dt>` | `<dt>작업 단위 분할</dt><dd>맡길 업무를 작업 단위로 나누는 일입니다. <a href="../chapters/ch06.html">(Chapter 6)</a></dd>` |
| 46 | 권고 | 용어 추가: 승인자 | ch06#split이 정의하고 ch09#approval이 재사용합니다. 승인 지점 항목과 짝입니다. | `<dt>승인 지점</dt>` | `<dt>승인자</dt><dd>사람 가운데 되돌리기 어려운 동작과 작업 단위의 완료를 승인하는 사람입니다. <a href="../chapters/ch06.html#split">(Chapter 6)</a></dd>` |
| 47 | 권고 | 용어 추가: 주 에이전트 | ch06#multi-agent가 정의합니다. 하위 에이전트와 짝입니다. | `<dt>저장소</dt>` (종료 코드 다음) | `<dt>주 에이전트</dt><dd>하위 에이전트에게 일을 맡기는 쪽으로, 주 대화에서 사람과 일하는 에이전트입니다. <a href="../chapters/ch06.html#multi-agent">(Chapter 6)</a></dd>` |
| 48 | 권고 | 용어 추가: 변환 | ch07#criteria가 "완료 기준을 이런 검사로 만드는 일을 이 장에서는 변환이라고 합니다"로 정의합니다. | `<dt>독립 검수</dt>` | `<dt>변환</dt><dd>완료 기준을 통과나 실패로 가르는 검사로 만드는 일입니다. <a href="../chapters/ch07.html#criteria">(Chapter 7)</a></dd>` |
| 49 | 권고 | 용어 추가: 채점 | ch07#rubric이 정의합니다. | `<dt>진행 기록</dt>` | `<dt>채점</dt><dd>기준 하나를 정답, 오답이나 점수 같은 판정값으로 만드는 일입니다. 방법은 코드 기반, 대규모 언어 모델 기반, 사람의 세 가지입니다. <a href="../chapters/ch07.html#rubric">(Chapter 7)</a></dd>` |
| 50 | 권고 | 용어 추가: 기준표 | ch07#rubric이 정의합니다. | `<dt>규칙 파일</dt>` (기록 다음) | `<dt>기준표(Rubric)</dt><dd>채점할 때 항목마다 무엇을 보고 어떻게 판정할지 적은 표입니다. <a href="../chapters/ch07.html#rubric">(Chapter 7)</a></dd>` |
| 51 | 권고 | 용어 추가: 예시 답안 | ch07#rubric이 정의합니다. | `<dt>에이전트(Agent)</dt>` (역할, 영역 다음) | `<dt>예시 답안</dt><dd>채점하는 쪽이 결과와 비교할, 기준이 되는 답입니다. <a href="../chapters/ch07.html#rubric">(Chapter 7)</a></dd>` |
| 52 | 권고 | 용어 추가: 에이전트 제품 | prologue(시작하며)가 "모델을 에이전트로 사용할 수 있게 만든 소프트웨어"로 정의하고 ch01도 씁니다. | `<dt>에이전트 명세서</dt>` | `<dt>에이전트 제품</dt><dd>모델을 에이전트로 사용할 수 있게 만든 소프트웨어입니다. OpenAI의 Codex와 Anthropic의 Claude Code가 예입니다. <a href="../chapters/prologue.html">(시작하며)</a></dd>` |

### 2-4. 실습(practice.html)

| 번호 | 등급 | 위치(파일, 절) | 문제와 근거 | 원문 | 고친 문안 |
|---|---|---|---|---|---|
| 24 | 필수 | practice, 실습 2 따라 하기 5단계 | R4, R11 인용 불일치입니다. 인용한 context-window 문서(Check your own session 절)는 /context가 어떤 CLAUDE.md와 자동 메모리 파일이 적재됐는지 보여 준다고만 씁니다. "Memory files"라는 표시 이름과 "그 목록에서 확인하라"는 안내는 memory 문서의 Troubleshoot memory issues 절("Run /context and check the list under Memory files")에 있습니다. 문장 자체는 사실이고 ch05도 memory로 인용합니다. | `<li>/context를 입력해 Memory files 항목(Claude Code가 규칙 문서를 표시하는 이름)에 CLAUDE.md가 있는지 확인합니다<sup class="cite" data-ref="context-window"></sup>.</li>` | `<li>/context를 입력해 Memory files 항목(Claude Code가 규칙 문서를 표시하는 이름)에 CLAUDE.md가 있는지 확인합니다<sup class="cite" data-ref="memory"></sup>.</li>` |
| 53 | 권고 | practice, 실습 2 따라 하기 6단계 | Chapter 10 버전 주석과 정합이 필요합니다. 공식 문서(permission-modes, Which mode a session starts in)로 v2.1.283 이상의 터미널과 VS Code는 auto로 시작하고 claude -p는 Manual(default)로 시작함을 확인했습니다. ch10은 수동 모드로 보려면 `claude --permission-mode default`라고 씁니다. 실습은 "버전과 권한 모드에 따라"라고만 써서, 최신 버전 독자가 2~5단계의 "확인 화면"을 보지 못하는 이유를 알기 어렵습니다. 실습 4 4단계의 같은 취지 문장("권한 모드에 따라 확인 화면 없이 바로 적용될 수도 있습니다.")에도 같은 안내를 맞추는 것을 권합니다. | `Claude Code의 버전과 권한 모드에 따라 확인 화면 없이 수정이 적용될 수도 있으며, 이때는 확인 방법의 git restore로 되돌립니다(<a href="../chapters/ch10.html#perm-claude">Chapter 10의 Claude Code: 도구별 권한 규칙과 추가로 켜는 샌드박스</a>)<sup class="cite" data-ref="permission-modes"></sup>.` | `Claude Code v2.1.283 이상의 터미널은 auto 모드로 시작하므로 확인 화면 없이 수정이 적용될 수도 있으며, 이때는 확인 방법의 git restore로 되돌립니다. 확인 화면을 보려면 claude --permission-mode default로 시작합니다(<a href="../chapters/ch10.html#perm-claude">Chapter 10의 Claude Code: 도구별 권한 규칙과 추가로 켜는 샌드박스</a>)<sup class="cite" data-ref="permission-modes"></sup>.` |
| 54 | 권고 | practice, 실습 준비 | R4 인용 누락입니다. 로그인 안내 문장에 인용이 없습니다. 공식 문서(setup, Authenticate 절)는 "claude를 실행하고 브라우저 안내를 따라 로그인"이라고 합니다. | `claude 명령을 처음 실행하면 로그인 화면이 열리므로, 사용할 요금제의 계정이나 Console 계정으로 로그인합니다.` | `claude 명령을 처음 실행하면 로그인 화면이 열리므로, 사용할 요금제의 계정이나 Console 계정으로 로그인합니다<sup class="cite" data-ref="cc-setup"></sup>.` |
| 55 | 권고 | practice, 실습 준비 | 공식 문서(setup, Authenticate 절)의 표현은 "Pro, Max, Team, Enterprise, or Console account"입니다. 풀이 문장의 "Console의 API 키"는 같은 문단 뒤쪽의 "Console 계정"과도 다릅니다. | `Anthropic 문서는 Claude Code를 Pro 이상의 유료 요금제나 Claude Console의 API 키로 사용하며, 무료 요금제에는 포함되지 않는다고 안내합니다` | `Anthropic 문서는 Claude Code를 Pro 이상의 유료 요금제나 Claude Console 계정으로 사용하며, 무료 요금제에는 포함되지 않는다고 안내합니다` |
| 56 | 권고 | practice, 실습 준비 | 비용과 한도 주의점이 빠졌습니다. 공식 문서(costs, Add usage credits to your subscription 절)는 사용 크레딧(usage credits)을 켜면 요금제 한도를 넘어 계속 쓸 수 있다고 합니다. 한도에 닿았을 때 거동은 이 부록이 안내하지 않습니다. 확인은 문서까지만 했고 화면 문구와 청구 시점은 미확인입니다. | `구독 요금제에서는 Claude Code 사용량이 요금제의 사용 한도 안에 포함됩니다<sup class="cite" data-ref="costs"></sup>.` | `구독 요금제에서는 Claude Code 사용량이 요금제의 사용 한도 안에 포함됩니다. 한도에 이르면 한도가 풀릴 때까지 기다려야 하고, 사용 크레딧(usage credits)을 켠 계정은 한도를 넘는 사용량이 크레딧으로 계산됩니다<sup class="cite" data-ref="costs"></sup>.` |
| 57 | 권고 | practice, 실습 6 따라 하기 5단계 | 공식 문서(costs, Using the /usage command 절)는 /usage의 세션 금액 블록이 API 사용자용이고 Pro, Max 구독자는 금액 대신 요금제 사용량 막대를 본다고 합니다. 구독으로 실습하는 독자(실습 준비의 기본 경로)는 금액을 못 찾을 수 있습니다. 정가 기준 추정치라는 설명은 맞습니다. | `/usage를 입력해 세션의 사용량을 확인합니다. 금액은 정가 기준의 추정치이며<sup class="cite" data-ref="costs"></sup>, 실제 청구액은 요금 화면에서 확인합니다` | `/usage를 입력해 세션의 사용량을 확인합니다. 세션 금액은 API 사용자용 정가 기준의 추정치이며, 구독 사용자는 금액 대신 요금제 사용량이 함께 보입니다<sup class="cite" data-ref="costs"></sup>. 실제 청구액은 요금 화면에서 확인합니다` |
| 58 | 권고 | practice, 실습 준비 | 터미널 열기 안내에 Linux가 없습니다. 이 부록은 "macOS와 Linux의 터미널" 기준이라고 하는데 Linux 방법은 없습니다. 공식 문서(terminal-guide, Install on macOS or Linux 1단계)는 Linux에서 Ctrl+Alt+T 또는 응용 프로그램 메뉴의 Terminal이라고 합니다. | `Anthropic의 터미널 안내에 따르면 Windows에서는 Win+X 메뉴에서 PowerShell을, macOS에서는 Cmd+Space로 Spotlight를 열어 Terminal을 찾아 엽니다<sup class="cite" data-ref="cc-terminal-guide"></sup>.` | `Anthropic의 터미널 안내에 따르면 Windows에서는 Win+X 메뉴에서 PowerShell을, macOS에서는 Cmd+Space로 Spotlight를 열어 Terminal을 찾아 열고, Linux에서는 대부분의 배포판에서 Ctrl+Alt+T를 누르거나 응용 프로그램 메뉴에서 Terminal을 찾아 엽니다<sup class="cite" data-ref="cc-terminal-guide"></sup>.` |

번호는 필수와 권고를 구분해 이어서 매겼으므로 2-1 표의 번호가 중간에 비어 있습니다(필수 1~12, 13~23, 24, 권고 25~58). 필수는 1~24 전부이며, 총 필수 24건입니다. 권고는 25~58 가운데 필수가 아닌 34건이 아니라 25~35(2-1), 36~52(2-3), 53~58(2-4)의 합계 11+17+6=34건에서 22건을 뺀 것이 아니라 그대로 34건입니다.

## 3. research 기록 문안

위 번호 계산 정정: 표의 권고는 25~35(11건), 36~52(17건), 53~58(6건)로 모두 34건입니다. 마지막 줄의 집계는 이 숫자를 따릅니다. 결론 절 맨 위의 "권고 32"는 "권고 34"로 읽어 주세요.

```
## 2026-10-24 fact-checker 재확인(부록)

범위: src/appendix/terms.html(용어 풀이), src/appendix/practice.html(실습). 브랜치 appendix-playbook, bbf1459 이후 문안. 확인 날짜는 모두 2026-10-24. 게시일은 공식 문서가 게시일을 표시하지 않아 "표시 없음"으로 적고 확인일만 남긴다.

- S-AP-1. Set up Claude Code(Advanced setup). https://code.claude.com/docs/en/setup . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: Authenticate 절에 "Pro, Max, Team, Enterprise, or Console account가 필요하고 무료 claude.ai 요금제는 Claude Code를 포함하지 않는다". 설치 명령은 macOS, Linux, WSL이 `curl -fsSL https://claude.ai/install.sh | bash`, Windows PowerShell이 `irm https://claude.ai/install.ps1 | iex`(CMD용 install.cmd도 있음). Verify your installation 절에 `claude --version`이 버전 번호를 출력. Windows에서 Git for Windows가 있으면 Bash 도구가 Git Bash를 쓰고, 없으면 PowerShell 도구를 쓴다. Git for Windows가 있을 때 PowerShell 도구는 claude.ai와 Console 계정에서 기본 켜짐. 로그인은 claude 실행 후 브라우저 안내.
- S-AP-2. Plans & pricing. https://claude.com/pricing . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: Free는 Claude Code 미포함("No"), Pro, Max(5x, 20x), Team, Enterprise는 포함. FAQ에 "Claude Code is included in all paid plans".
- S-AP-3. Manage costs effectively. https://code.claude.com/docs/en/costs . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: Using the /usage command 절에서 Session 블록의 금액은 로컬에서 정가(list price)로 계산한 추정치이며 API 사용자용이고, Pro와 Max 구독자는 사용량이 구독에 포함되어 요금제 사용량 막대를 본다. 실제 청구는 Claude Console Usage 페이지. Add usage credits to your subscription 절에서 사용 크레딧으로 요금제 한도를 넘어 계속 사용 가능. /cost는 /usage의 별칭(commands 문서).
- S-AP-4. Terminal guide for new users. https://code.claude.com/docs/en/terminal-guide . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: macOS는 Cmd+Space로 Spotlight에서 Terminal, Linux는 Ctrl+Alt+T 또는 응용 프로그램 메뉴, Windows는 Win+X에서 Windows PowerShell(또는 Terminal). Git for Windows는 선택 사항.
- S-AP-5. Tools reference(PowerShell tool 절, Bash deny rules also turn off the PowerShell tool 절). https://code.claude.com/docs/en/tools-reference . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: Windows에서 Git Bash가 있으면 PowerShell 도구는 claude.ai와 Console 계정에서 기본 켜짐. Windows에서 Git Bash가 있을 때 `Bash(git push *)` 같은 범위 지정 규칙을 포함한 Bash 금지 규칙은 그 세션에서 PowerShell 도구를 끈다(CLAUDE_CODE_USE_POWERSHELL_TOOL=1이나 PowerShell 규칙으로 유지 가능). 실습 준비의 해당 문장과 일치.
- S-AP-6. Security. https://code.claude.com/docs/en/security . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: Trust verification 항목에 신뢰하지 않은 폴더에서 대화형 세션을 시작하면 workspace trust 대화상자가 나온다. 홈 디렉터리에서 시작하면 신뢰가 디스크에 저장되지 않는다(실습은 expense-practice에서 시작하므로 해당 없음). Manual mode는 파일 수정과 명령 실행 전에 묻는다.
- S-AP-7. Explore the context window. https://code.claude.com/docs/en/context-window . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: Check your own session 절에 /context가 어떤 CLAUDE.md와 자동 메모리 파일이 적재됐는지 포함한 범주별 내역을 보여 준다. "Memory files" 표시 이름은 이 문서에 없음. 실습 2의 해당 인용은 memory 문서로 바꾸는 것을 제안(지적 24번).
- S-AP-8. How Claude remembers your project. https://code.claude.com/docs/en/memory . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: Troubleshoot memory issues 절에 "/context를 실행하고 Memory files 아래 목록을 확인". Auto memory 절에 로컬 세션에서 기본 켜짐, 보관 위치 ~/.claude/projects/<project>/memory/, 컴퓨터 간에 공유되지 않음("machine-local"). View and edit with /memory 절에 /memory가 CLAUDE.md 목록, 자동 메모리 토글, 메모리 폴더 열기를 제공. AGENTS.md 절에 기본으로 작업 폴더와 그 위에 CLAUDE.md, .claude/CLAUDE.md, CLAUDE.local.md가 없을 때만 AGENTS.md를 읽고, 직접 읽기는 v2.1.277 이상.
- S-AP-9. Permission modes. https://code.claude.com/docs/en/permission-modes . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: 모드는 default(Manual), acceptEdits, plan, auto, dontAsk, bypassPermissions. default는 읽기만 묻지 않음. v2.1.283 이상의 터미널과 VS Code 세션 시작 모드는 auto, claude -p와 Agent SDK는 Manual. 금지 규칙은 모든 모드에서 적용.
- S-AP-10. Configure permissions. https://code.claude.com/docs/en/permissions (Manage permissions 절). 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: 규칙은 deny, ask, allow 순서로 평가하고 처음 일치한 것이 결과를 정한다.
- S-AP-11. Sandboxing. https://code.claude.com/docs/en/sandboxing . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24. (문서 끝 약 3,000자는 읽지 못함)
  - 사용한 내용: 샌드박스는 기본 꺼짐이고 /sandbox 또는 sandbox.enabled로 켠다. 셸 명령과 그 하위 프로세스가 대상이며 Read, Edit, Write 같은 내장 파일 도구는 권한 규칙을 따른다. 네이티브 Windows는 미지원이고 macOS, Linux, WSL2에서 동작.
- S-AP-12. Automate actions with hooks. https://code.claude.com/docs/en/hooks-guide . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: /hooks가 hooks 브라우저를 연다. 성공한 훅은 아무것도 보이지 않는다(Ctrl+O 대화 기록 보기에서 결과 확인). exit 2는 stderr를 사유로 쓰며 이벤트에 따라 Claude가 피드백으로 받는다. PostToolUse의 세부(도구는 이미 실행됨)는 research/ch02-sources.md의 기존 기록을 따랐고 이번에 hooks 레퍼런스 문서를 다시 열지는 않음.
- S-AP-13. Commands, CLI reference. https://code.claude.com/docs/en/commands , https://code.claude.com/docs/en/cli-reference . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: /permissions(허용, 확인 요청, 금지 규칙 관리), /hooks, /memory, /context [all], /usage(별칭 /cost, /stats), /exit(별칭 /quit), /clear 모두 존재. `claude -c`는 현재 디렉터리의 가장 최근 대화를 이어 감. --permission-mode 플래그 존재.
- S-AP-14. 실행 기록(R8). 환경 Linux, Python 3.13.16, git 2.43.0, 2026-10-24. examples/expense-app을 스크래치 폴더에 복사해 실습 1을 실행(원본 저장소 변경 없음).
  - 명령과 출력 원문(요약):
    $ cp -r harness-book/examples/expense-app expense-practice && cd expense-practice && git init && git add -A && git commit -m "실습 시작 상태"
    $ git log --oneline
    573a937 실습 시작 상태
    $ ls -a  -> .gitignore DECISIONS.md README.md RUNLOG.md acceptance app.py check.py data docs expense reference tests (.claude 폴더와 CLAUDE.md 없음)
    $ python3 -m unittest discover tests -q
    Ran 3 tests in 0.003s
    OK
    $ python3 check.py ; echo exit=$?
    tests: 실행 3건, 실패 0건, 건너뜀 0건, project_code 시험 0건   (출력 앞쪽, 6번째 줄 부근)
    FAIL: test_1_form_offers_project_codes / test_2_unknown_code_rejected_with_reason / test_3_list_shows_project_code
    Ran 5 tests in 0.006s
    FAILED (failures=3)
    acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)
    exit=1
  - 판정: bbf1459 이후 practice.html의 요약 줄 순서(tests → FAILED → acceptance)와 "2026년 10월 24일 Linux에서 실행"이 실제와 일치. reference/tasks.example.json은 작업 1 true, 작업 2~5 false. reference/settings.example.json의 deny에 Edit(./data/**), Edit(./acceptance/**), Edit(./check.py), Edit(./CLAUDE.md), Edit(./DECISIONS.md), Edit(./.claude/**), Bash(git push *), WebFetch, WebSearch가 있음(실습 3, 4 설명과 일치). app.py는 localhost:8000과 /new 경로를 사용. https://github.com/seoulkorea-dev/harness-book.git 은 열리고 기본 브랜치 main에 examples/expense-app이 있음.
  - 실행하지 못한 것: 실습 2~6의 Claude Code 화면(로그인과 요금제가 필요). 해당 문장의 확인은 공식 문서 대조까지이며 화면 문구는 미확인(부록이 "예상"이라고 밝힌 부분).
- S-AP-15. 본문 대조(R7, 용어 풀이). src/chapters/ch01~ch11, prologue, epilogue에서 "…라고 합니다" 정의 문장과 절 앵커를 대조. terms.html과 practice.html의 모든 내부 링크(href, 앵커)가 실제로 존재하고 링크 문구가 해당 절 제목과 일치함을 스크립트로 확인.
```

## 지적 번호 안내

표의 번호는 필수 1~24와 권고 25~58을 한 줄로 이어 매겼습니다. 2-1 표에는 1~12와 25~35가, 2-2 표에는 13~23이, 2-3 표에는 36~52가, 2-4 표에는 24와 53~58이 있습니다.

필수 24, 권고 34, 확인 필요(작가 판단) 3, 확인한 사실 문장 98개

(위 결론 절 맨 위의 "필수 24, 권고 32"에서 권고는 34가 맞습니다. 표의 권고는 25~58의 34건입니다.)

관련 파일 경로
- /home/user/harness-book/src/appendix/terms.html
- /home/user/harness-book/src/appendix/practice.html
- /home/user/harness-book/BOOK_SPEC.md (4절 핵심 정의, 5절 용어표)
- /home/user/harness-book/research/bibliography.json (practice의 위첨자 KEY 10개 모두 존재)
