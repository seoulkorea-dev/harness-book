"""단위 테스트와 수용 시험을 함께 실행하는 검사 스크립트(에이전트는 수정하지 않음).

통과 조건: 두 폴더 모두 실행 1건 이상, 실패 0건, 건너뜀 0건. 수용 시험은 정한 수만큼 실행되고,
단위 테스트에는 이름에 project_code가 든 시험이 1건 이상 있어야 한다(작업 3).
"""
import sys
import unittest

ACCEPTANCE_COUNT = 5  # docs/CR.md의 수용 기준 수
UNIT_KEYWORD = "project_code"


def test_ids(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from test_ids(item)
        else:
            yield item.id()


ok = True
for folder in ("tests", "acceptance"):
    suite = unittest.TestLoader().discover(folder)
    ids = list(test_ids(suite))
    run = unittest.TextTestRunner(verbosity=0).run(suite)
    failed, skipped = len(run.failures) + len(run.errors), len(run.skipped)
    line = f"{folder}: 실행 {run.testsRun}건, 실패 {failed}건, 건너뜀 {skipped}건"
    ok = ok and run.testsRun > 0 and failed == 0 and skipped == 0
    if folder == "tests":
        count = sum(1 for i in ids if UNIT_KEYWORD in i)
        line += f", {UNIT_KEYWORD} 시험 {count}건"
        ok = ok and count > 0
    else:
        line += f"(정한 수 {ACCEPTANCE_COUNT}건)"
        ok = ok and run.testsRun == ACCEPTANCE_COUNT
    print(line)
sys.exit(0 if ok else 1)
