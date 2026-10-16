"""단위 테스트와 수용 시험을 함께 실행하는 검사 스크립트(에이전트는 수정하지 않음)."""
import sys
import unittest

results = {}
for folder in ("tests", "acceptance"):
    suite = unittest.TestLoader().discover(folder)
    run = unittest.TextTestRunner(verbosity=0).run(suite)
    results[folder] = (run.testsRun, len(run.failures) + len(run.errors))

for folder, (count, failed) in results.items():
    print(f"{folder}: 실행 {count}건, 실패 {failed}건")
sys.exit(0 if all(count > 0 and failed == 0 for count, failed in results.values()) else 1)
