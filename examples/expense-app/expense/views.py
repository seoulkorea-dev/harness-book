"""화면 HTML 생성."""
from html import escape


def render_list(requests):
    rows = "".join(
        f"<tr><td>{escape(r['number'])}</td><td>{escape(r['requester'])}</td>"
        f"<td>{escape(r['date'])}</td><td>{r['amount']}</td>"
        f"<td>{escape(r['purpose'])}</td><td>{escape(r['status'])}</td></tr>"
        for r in requests
    )
    return (
        "<h1>정산 요청 목록</h1><table><tr><th>번호</th><th>요청자</th><th>날짜</th>"
        f"<th>금액</th><th>사용처</th><th>상태</th></tr>{rows}</table>"
        '<p><a href="/new">새 요청 등록</a></p>'
    )


def render_form(projects, errors=()):
    messages = "".join(f"<li>{escape(e)}</li>" for e in errors)
    return (
        "<h1>정산 요청 등록</h1>"
        f"<ul class='errors'>{messages}</ul>"
        '<form method="post" action="/new">'
        '<label>요청자 <input name="requester"></label>'
        '<label>날짜 <input name="date" type="date"></label>'
        '<label>금액 <input name="amount"></label>'
        '<label>사용처 <input name="purpose"></label>'
        "<button>등록</button></form>"
    )
