"""기준 상태의 단위 테스트(에이전트가 CR-07에 맞춰 갱신할 수 있음)."""
import shutil
import tempfile
import unittest
from pathlib import Path

from expense import service, store, views

DATA = Path(__file__).resolve().parent.parent / "data"


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        for name in ("expenses.json", "projects.csv"):
            shutil.copy(DATA / name, self.tmp / name)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_register_valid(self):
        ok, errors = service.register(self.tmp, {"requester": "최하늘", "date": "2026-10-06", "amount": "5000", "purpose": "택시"})
        self.assertTrue(ok, errors)
        self.assertEqual(len(store.load_requests(self.tmp)), 4)

    def test_register_missing_field(self):
        ok, errors = service.register(self.tmp, {"requester": "", "date": "2026-10-06", "amount": "5000", "purpose": "택시"})
        self.assertFalse(ok)
        self.assertTrue(errors)

    def test_list_shows_requesters(self):
        html = views.render_list(store.load_requests(self.tmp))
        for name in ("이서연", "박준호", "김도윤"):
            self.assertIn(name, html)
