"""경비 정산 미니 웹 앱 실행: python app.py 뒤 http://localhost:8000"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs

from expense import service, store, views

DATA_DIR = Path(__file__).parent / "data"


class Handler(BaseHTTPRequestHandler):
    def _send(self, body, status=200):
        data = f"<!doctype html><meta charset='utf-8'>{body}".encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/new":
            self._send(views.render_form(store.load_projects(DATA_DIR)))
        else:
            self._send(views.render_list(store.load_requests(DATA_DIR)))

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = parse_qs(self.rfile.read(length).decode("utf-8"))
        form = {k: v[0] for k, v in raw.items()}
        ok, errors = service.register(DATA_DIR, form)
        if ok:
            self.send_response(303)
            self.send_header("Location", "/")
            self.end_headers()
        else:
            self._send(views.render_form(store.load_projects(DATA_DIR), errors), 400)


if __name__ == "__main__":
    print("http://localhost:8000")
    HTTPServer(("localhost", 8000), Handler).serve_forever()
