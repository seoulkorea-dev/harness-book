# ch11 fact-checker (2026-10-20, v1.0 보강)

범위: 주장 줄, 확인 방법(표 11-4), 원칙과 점검 질문. 대조: tools/check_all.py, .github/workflows/check.yml, verify-site.yml, tools/verify_site.py, DECISIONS.md, FAILURES.md, 같은 장 검증 세 단계 문단(2026-10-20). 외부 출처 없음.

| 발견 | 위치 | 근거 | 제안 | 확신 | 심각도 |
|---|---|---|---|---|---|
| book-check(PR과 main push에서 check_all.py --ci)와 verify-site(Pages 배포 뒤)는 따로 도는 워크플로이며 시점이 다름 | 표 11-4 2행 | check.yml, verify-site.yml | 두 워크플로와 시점을 나눠 씀 | 높음 | 필수(반영) |
| 본문 "저장소에 반영하면 GitHub Actions가 같은 검사와 사이트 검증을 다시 실행합니다"도 같은 이유로 부정확 | 이 책 저장소의 하네스 절(기존 본문) | check.yml, verify-site.yml | v1.1에서 본문 수정 | 높음 | 필수(보류: 기존 본문, v1.1) |
| 검사 요약 항목(빌드, 금칙어, 번호, 구조, 문체, 그림 안 이름)과 lint 4종은 일치. 재빌드 일치는 --ci에만 있음 | 표 11-4 1행 | check_all.py | 2행에 CI 항목임을 밝힘(반영) | 중간 | 권장(2행 수정으로 해소) |
| DECISIONS.md의 대체 열은 번호가 아닌 문장인 행도 있음 | 표 11-4 3행 | DECISIONS.md | "번호 또는 대체된 내용" | 중간 | 권장 |
| FAILURES.md의 F-13, F-14는 첫 발생 기록, F-09는 진행 중 | 표 11-4 4행 | FAILURES.md | 작가 판단(PR에 기록) | 중간 | 권장 |
| 저장소 루트 실행, 원칙과 점검 질문, 주장 줄 내용, 참고 자료 불필요 | check 도입, principle | check_all.py, 표 11-1 | 없음 | 높음 | 참고 |

필수 2(반영 1, 보류 1), 권장 2(+1 해소), 참고 4, 확인한 사실 문장 9개
