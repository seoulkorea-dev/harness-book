"""CR-07 수용 시험(사람이 작성, 에이전트는 수정하지 않음)."""
import hashlib
import shutil
import tempfile
import unittest
from pathlib import Path

from expense import service, store, views

DATA = Path(__file__).resolve().parent.parent / "data"
FORM = {"requester": "최하늘", "date": "2026-10-06", "amount": "5000", "purpose": "택시"}


class CR07AcceptanceTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        for name in ("expenses.json", "projects.csv"):
            shutil.copy(DATA / name, self.tmp / name)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_1_form_offers_project_codes(self):
        html = views.render_form(store.load_projects(self.tmp))
        self.assertIn('name="project_code"', html)
        for code in ("PRJ-2601", "PRJ-2602", "PRJ-2603"):
            self.assertIn(code, html)

    def test_2_unknown_code_rejected_with_reason(self):
        ok, errors = service.register(self.tmp, dict(FORM, project_code="PRJ-9999"))
        self.assertFalse(ok)
        self.assertTrue(any("PRJ-9999" in e for e in errors))

    def test_3_list_shows_project_code(self):
        ok, errors = service.register(self.tmp, dict(FORM, project_code="PRJ-2602"))
        self.assertTrue(ok, errors)
        html = views.render_list(store.load_requests(self.tmp))
        self.assertIn("PRJ-2602", html)

    def test_4_existing_requests_still_listed(self):
        html = views.render_list(store.load_requests(self.tmp))
        for number in ("REQ-001", "REQ-002", "REQ-003"):
            self.assertIn(number, html)

    def test_5_project_source_unchanged(self):
        before = hashlib.sha256((self.tmp / "projects.csv").read_bytes()).hexdigest()
        service.register(self.tmp, dict(FORM, project_code="PRJ-2601"))
        after = hashlib.sha256((self.tmp / "projects.csv").read_bytes()).hexdigest()
        self.assertEqual(before, after)
