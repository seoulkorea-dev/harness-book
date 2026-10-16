"""정산 요청 등록 규칙."""
from expense import store

REQUIRED = ("requester", "date", "amount", "purpose")


def validate(form):
    errors = []
    for field in REQUIRED:
        if not str(form.get(field, "")).strip():
            errors.append(f"{field} 항목이 비어 있습니다.")
    amount = str(form.get("amount", "")).strip()
    if amount and not amount.isdigit():
        errors.append("amount 항목은 숫자로 입력합니다.")
    return errors


def register(data_dir, form):
    errors = validate(form)
    if errors:
        return False, errors
    requests = store.load_requests(data_dir)
    number = f"REQ-{len(requests) + 1:03d}"
    requests.append({
        "number": number,
        "requester": form["requester"].strip(),
        "date": form["date"].strip(),
        "amount": int(form["amount"]),
        "purpose": form["purpose"].strip(),
        "status": "요청",
    })
    store.save_requests(data_dir, requests)
    return True, []
