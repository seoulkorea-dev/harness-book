# ch09 fact-checker (2026-10-20, v1.0 보강)

범위: 주장 줄, CR 이름 문장, 표 9-4, 9-5, 원칙과 점검 질문. 문서: Configure permissions, Manage costs effectively, Configure the sandboxed Bash tool, Choose a permission mode(2026-10-20). 대조: 부록 실습 3, settings.example.json, research S22.

| 발견 | 위치 | 근거 | 제안 | 확신 | 심각도 |
|---|---|---|---|---|---|
| Edit deny는 내장 도구와 인식되는 Bash 파일 명령은 막지만 Python 같은 스크립트의 간접 쓰기는 막지 못함(샌드박스 필요) | 표 9-4 1행 | permissions 문서 Read and Edit 절 | 막는 장치에 샌드박스 보완 추가 | 높음 | 필수(반영) |
| git -C . push 불일치와 샌드박스 보완은 일치. 표에 발표 주체와 링크 없음 | 표 9-4 2행 | permissions 문서 | 도입 문장에 주체와 ref-anthropic-2026b | 중간 | 권장 |
| 승인자가 검토 없이 승인한다는 일반화의 1차 출처 없음 | 표 9-4 3행 | permission modes 문서(prompt fatigue 한 줄) | 설계 판단 표현으로 낮춤 | 중간 | 권장(미확인) |
| 샌드박스는 macOS, Linux, WSL2에서만 동작, 네이티브 Windows에서는 샌드박스 없이 실행. 예제 설정에 샌드박스 없음 | 표 9-4 2행 | sandboxing 문서 | v1.1 보강 | 중간 | 참고 |
| 작업 단위 분할이 재실행 비용을 줄인다는 문장은 비용 문서에 없음(6장 링크로 충분) | 표 9-4 4행 | costs 문서 | 지출 한도는 총량 상한임을 정리 | 중간 | 참고 |
| /permissions 화면, 실습 3 요청과 거부, /usage Session과 정가 기준 추정치, 지출 한도 결정 | 표 9-5, 점검 질문 3 | permissions, costs 문서, 실습 3 | 유지(modelPricing 예외는 v1.1) | 높음 | 일치 |
| auto 모드 기본 시작은 v2.1.283 이상(범위 밖 기록) | 권한 모드 | permission modes 문서 | 기록만 | 중간 | 참고 |

필수 1, 권장 2, 참고 5, 확인한 사실 문장 11개
