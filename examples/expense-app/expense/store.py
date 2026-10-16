"""정산 요청과 프로젝트 코드 자료를 읽고 쓰는 모듈."""
import csv
import json
from pathlib import Path

REQUESTS_FILE = "expenses.json"
PROJECTS_FILE = "projects.csv"


def load_requests(data_dir):
    path = Path(data_dir) / REQUESTS_FILE
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save_requests(data_dir, requests):
    path = Path(data_dir) / REQUESTS_FILE
    path.write_text(json.dumps(requests, ensure_ascii=False, indent=2), encoding="utf-8")


def load_projects(data_dir):
    path = Path(data_dir) / PROJECTS_FILE
    with path.open(encoding="utf-8", newline="") as f:
        return [row for row in csv.DictReader(f)]
