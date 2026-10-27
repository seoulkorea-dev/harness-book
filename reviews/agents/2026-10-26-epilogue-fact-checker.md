## 1. 결론(필수 4, 권고 4)

범위는 src/chapters/epilogue.html의 머리 문단, `#hard`, `#worked`, `#future`, `#next`와 옮긴 절의 지시어입니다. 사실 문장은 33개를 확인했습니다. 참고(미확인)는 4건입니다.

- `#future`의 Anthropic 글 내용은 원문과 일치합니다. 2026-10-26에 두 원문을 직접 열어 확인했습니다. 근거는 아래 3절에 적었습니다.
- 위첨자 두 곳은 모두 문장 끝 마침표 앞에 있고, 인용 키 `harness-design-apps`, `long-running-harness`는 bibliography.json에 있습니다.
- Chapter 10 `#criteria` 절은 "규칙 문서, 권한, 격리, 설정 파일"의 네 가지 비교 기준을 둡니다. Chapter 1~10의 `#principle` 앵커와 `#components`, `#methods`, `#decisions`, `#manager` 앵커도 모두 있고, 표 1-8은 "증상별 원인 층"입니다.
- 불일치는 네 곳입니다.
  - 장별 수정 비율 범위가 맞지 않습니다.
  - 점검 에이전트와 재검수 서술이 D-129, D-130과 다릅니다.
  - 지난 책 정리 단위 수가 genai-book의 PR과 다릅니다.
  - 지시어 "앞의 원칙"이 새 배치에서 가리킬 대상을 잃었습니다.
- research 기록 문안(2026-10-26 마치며 항목)에는 고쳐야 할 오류가 둘 있습니다. D-137은 DECISIONS.md에 없는 번호이고, 비율 범위가 "24.0~55.2%"로 되어 있습니다. 3절에 정정문을 붙였습니다.

## 2. 지적 표

| 번호 | 등급 | 위치 | 문제와 근거 | 원문 | 고친 문안 |
|---|---|---|---|---|---|
| 1 | 필수 | src/chapters/epilogue.html, `#hard` 넷째 항목 | HANDOFF.md "지금 상태"의 편집장 1회 "고칠 문장" 줄은 2장 22.6%(20행), 3장 28.6%, 4장 24.0%, 5장 36.4%, 6장 41.8%, 7장 50.6%, 8장 45.2%, 9장 55.2%, 10장 49.3%, 11장 53.7%입니다. 범위는 22.6~55.2%인데 원문은 24%부터라 2장이 빠졌습니다. 확인일 2026-10-26. | `장마다 24~55%였습니다` | `장마다 23~55%였습니다` |
| 2 | 필수 | 같은 파일, `#hard` 둘째 항목 | D-129(2026-10-22)는 점검 에이전트 수를 8개로 유지하고 출판 역할에 맞췄으며, 장 PR마다 여섯 확인 표를 필수로 했습니다. D-130은 에이전트를 7개로 줄였고 "editor 재검수는 최대 2회"로 상한을 뒀습니다. D-139(2026-10-23)가 "시간 단축"을 목적으로 검토를 장마다 한 번으로 바꿨습니다. 따라서 "늘리고"와 "통과할 때까지"는 기록과 다릅니다. | `점검 에이전트를 늘리고 편집 검수를 통과할 때까지 다시 받게 하자` | `장 PR마다 여섯 가지 확인을 모두 받고 편집 검수도 최대 두 번 다시 받게 하자` |
| 3 | 필수 | 같은 파일, `#worked` 넷째 항목 | genai-book PR은 gh REST로 확인했습니다. #15~#26이 모두 2026-10-25에 병합되었고 개수는 12건입니다. 내용은 Chapter 1~8(8건), 시작하며(#23), 마치며(#24), 부록 1~3(#25), 책 전체 점검(#26)입니다. 시작하며부터 부록까지는 11단위이고 열두째는 책 전체 점검이라 "열두 단위"는 맞지 않습니다. "같은 순서"를 뒷받침하는 기록도 없습니다. 이번 책은 시작하며를 2026-10-23에 먼저 정리했고, genai-book은 시작하며를 Chapter 8 뒤에 정리했습니다. 저장소 밖 사실인데 출처 표시도 없습니다. 근거는 genai-book의 PR #15~#26, DECISIONS.md D-001, CLAUDE.md입니다. | `2026년 10월 25일 지난 책의 시작하며부터 부록까지 열두 단위를 같은 순서로 정리했습니다.` | `2026년 10월 25일 지난 책 저장소(seoulkorea-dev/genai-book)에서 Chapter 1~8, 시작하며, 마치며, 부록, 책 전체 점검의 정리 PR 열두 건이 병합되었습니다.` |
| 4 | 필수 | 같은 파일, `#next` 첫 문단 | 옛 Chapter 11에서는 "앞의 원칙"이 바로 앞 절의 개선 순서를 가리켰습니다. 새 배치에서는 바로 앞이 `#future`이고, 거기에는 원칙이 없습니다. `#future`는 "앞으로"를 다루는 절이라 지시 대상이 사라졌습니다. | `앞의 원칙은 한 번에 모두 적용할 필요가 없습니다` | `앞에서 정리한 장별 원칙과 개선 순서는 한 번에 모두 적용할 필요가 없습니다` |
| 5 | 권고 | 같은 파일, `#future` 셋째 항목 | 위첨자 `long-running-harness`의 문서는 Anthropic의 Justin Young, "Effective harnesses for long-running agents"(2025-11-26)입니다. 원문에 "each new session begins with no memory of what came before"가 있어 내용은 일치합니다(확인 2026-10-26). 그러나 이 문장에는 발표 주체가 없습니다. 앞 문단의 Anthropic은 다른 글(`harness-design-apps`)이고, 뒤의 "같은 하네스 설계 글"도 그 글입니다. BOOK_SPEC 7절에 따라 이 글의 주체를 밝혀야 합니다. 주체 표기는 Q-202(장기 실행 글 주체는 작가 결정 대기)와 같은 사안입니다. | `한 세션을 넘는 긴 작업에서는 새 세션이 이전 세션의 기억 없이 시작하므로` | `Anthropic의 장기 실행 에이전트 하네스 글은 새 세션이 이전 세션의 기억 없이 시작한다고 적으므로, 한 세션을 넘는 긴 작업에서는` |
| 6 | 권고 | 같은 파일, `#worked` 둘째 항목 | 10월 24일 하루 병합은 확인했습니다. PR #124~#133, #135, #136이 2026-10-24T00:53Z~06:02Z(한국 시간 같은 날 09:53~15:02)에 병합되었습니다. #134(11장 작가 사례)는 병합 기록이 없습니다. 다만 새 구성에서 Chapter 11이 마치며로 옮겨졌고 장은 Chapter 1~10이라, "마지막 장"이 독자에게는 Chapter 10으로 읽힙니다. 병합 당시의 11장이었음을 밝혀야 합니다. | `2장부터 마지막 장, 마치며, 부록까지의 정비가` | `2장부터 옛 Chapter 11, 마치며, 부록까지의 정비가` |
| 7 | 권고 | 같은 파일, `#worked` 넷째 항목 | genai-book에는 .claude/agents에 chief-editor, fact-checker, practice-checker, production-checker, researcher의 5개만 있습니다(이번 책은 7~8개). NEW_BOOK_PLAYBOOK.md와 HARNESS_SETUP.md는 harness-book 커밋 339749d의 문서를 옮겼다고 genai-book/CLAUDE.md에 적혀 있습니다. 따라서 "에이전트 구성을 그대로 적용"은 과합니다. | `이번 책에서 정리한 원칙 문서와 에이전트 구성은 원고와 따로 저장되어 있어, 지난 책의 정리판에도 그대로 적용할 수 있었습니다.` | `이번 책에서 정리한 원칙 문서와 점검 에이전트 일부(편집장, 사실, 실습, 제작 점검, 조사)는 원고와 따로 저장되어 있어, 지난 책의 정리판에도 옮겨 쓸 수 있었습니다.` |
| 8 | 권고 | 같은 파일, `#hard` 셋째 항목 | 2026-10-26에 gh로 확인한 이슈 조회 오류는 "GitHub GraphQL is not available from Claude Code sessions"이고, 이는 세션 도구의 제한입니다. 네트워크 정책으로 기록된 것은 wikidocs.net 차단과 참고 문헌 8개 미확인(HANDOFF.md, Q-235)입니다. openai.com은 research/ch01-sources.md 등에서 HTTP 403 또는 이름 해석 실패(ENOTFOUND)입니다. 원인을 모두 "네트워크 정책"으로 묶은 것은 부정확합니다. 나머지 서술(검색 요약으로만 확인, 작가 확인 목록: Q-030, Q-090)은 기록과 일치합니다. | `클라우드에서 실행한 세션에서는 네트워크 정책 때문에 GitHub 명령 일부와 일부 공식 문서 사이트에 접속하지 못했습니다.` | `클라우드에서 실행한 세션에서는 GitHub의 GraphQL 호출이 막혀 일부 GitHub 명령을 쓰지 못했고, 네트워크 정책과 접속 거부로 일부 공식 문서 사이트(openai.com 등)를 열지 못했습니다.` |

### 참고(미확인, 찾은 범위)
- `#hard` 첫째 항목의 "2026년 10월 22일까지 일주일 동안 완성된 장이 나오지 않았습니다"와 "원인 네 가지"(기준 변경, 합격선 없음, 역할 부재, 체계 변경)는 이슈 #66 본문이 저장소에 없어 원문으로 확인하지 못했습니다. gh 이슈 조회는 GraphQL 403입니다.
  - 부분 근거: D-129(출판 역할에 맞춰 점검 에이전트 개편, 체계 동결, 2026-10-22), D-131·D-132(기준서 BOOK_STANDARD.md 신설과 승인), HANDOFF.md 35행(1장 완성본 병합 2026-10-22, PR #81).
  - "일주일"의 시작일과 "합격선" 서술은 작가 확인이 필요합니다.
- "작가가 최종 검수의 목표로 정한 수정 비율 5%"는 근거를 확인했습니다.
  - NEW_BOOK_PLAYBOOK.md 733행("작가 최종 검수에서 수정할 문장이 5% 미만이면 완료"), 1002행("기본: 5% 미만"), BOOK_STANDARD.md 22행, HANDOFF.md 110행.
  - HARNESS_SETUP.md에는 5%가 없습니다.
- 비교 대상이 다릅니다. 5%는 작가 최종 검수의 수정 비율이고, 23~55%는 편집장 검토에서 고치기로 한 문장 비율입니다. 원문은 "크게 높았고"로 비교합니다. 같은 척도가 아니므로 필요하면 "편집장 검토의 비율은 작가 최종 검수의 목표 5%와 직접 비교할 수 없지만"을 더하는 것을 작가가 검토하면 됩니다.
- `#hard` 둘째 항목의 "작업 체계를 마지막으로 한 번 정비한 뒤 책이 끝날 때까지 변경하지 않기로"는 D-129로 일치합니다. 다만 D-138·D-139(2026-10-23)가 장별 정비 절차를 바꿨고, 원문의 "그래서 … 변경했습니다"가 이를 가리킵니다.

## 3. research 기록 문안

```
## 2026-10-26 fact-checker 재확인(마치며: 어려움, 잘된 점, 하네스의 앞으로, 다음 작업)
- Anthropic(Prithvi Rajasekaran), Harness design for long-running application development, https://www.anthropic.com/engineering/harness-design-long-running-apps, 게시 2026-03-24, 확인 2026-10-26. 원문 일치: "every component in a harness encodes an assumption about what the model can't do on its own", 새 모델이 나올 때 하네스를 다시 점검(re-examine)하는 것이 좋은 관행, "the space of interesting harness combinations doesn't shrink as models improve", "agents reliably skew positive when grading their own work". 사용처: 마치며 #future 첫 문단, 셋째 항목. 인용 키 harness-design-apps(bibliography.json에 있음, 정정 불필요).
- Anthropic(Justin Young), Effective harnesses for long-running agents, https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents, 게시 2025-11-26, 확인 2026-10-26. 원문: "each new session begins with no memory of what came before". 사용처: 마치며 #future 셋째 항목. 인용 키 long-running-harness(있음). 본문에 발표 주체 Anthropic을 문장에 밝힐 것(권고 5).
- seoulkorea-dev/harness-book 저장소 내부 대조, 확인 2026-10-26.
  - HANDOFF.md "지금 상태" 2~11장 줄의 편집장 고칠 문장 비율은 22.6%, 28.6%, 24.0%, 36.4%, 41.8%, 50.6%, 45.2%, 55.2%, 49.3%, 53.7%로 범위 22.6~55.2%입니다. 아래 앞서 기록한 "24.0~55.2%"는 2장(22.6%)이 빠진 오류입니다.
  - D-129, D-130: 점검 에이전트 개편과 재검수 최대 2회. D-139: 검토 장마다 한 번. D-131·D-132: 기준서와 동결.
  - GitHub PR #124~#136(2026-10-24T00:53Z~06:02Z 병합, #134만 병합 기록 없음).
  - FAILURES.md F-07.
  - BOOK_STANDARD.md 22행, NEW_BOOK_PLAYBOOK.md 733, 1002행의 5% 기준.
- seoulkorea-dev/genai-book PR #15~#26(gh REST, 병합 2026-10-25): Chapter 1~8, 시작하며(#23), 마치며(#24), 부록 1~3(#25), 책 전체 점검(#26)의 12건. .claude/agents 5개(chief-editor, fact-checker, practice-checker, production-checker, researcher).
- 클라우드 제약: gh issue view 66이 "GitHub GraphQL is not available from Claude Code sessions"(HTTP 403)로 실패했습니다. 이슈 #66 본문은 열람 못 했습니다. openai.com HTTP 403 또는 이름 해석 실패는 research/ch01-sources.md 등 기존 기록과 같습니다.
- 정정 요청(front-back-sources.md 끝, 2026-10-26 마치며 항목): (1) "D-137(클라우드 GraphQL 차단)"의 D-137은 DECISIONS.md에 없는 번호입니다(D-138 행: D-137은 열린 PR #92용으로 비워 둠). 근거를 "PR #92(클라우드용 gh 대체, 보류), 2026-10-26 gh GraphQL 403 확인, S-FB-28"로 바꿔야 합니다. (2) "24.0~55.2%"를 "22.6~55.2%"로 바꿔야 합니다.
```

새 인용 키는 필요 없습니다.

필수 4, 권고 4, 참고 4, 확인한 사실 문장 33개
