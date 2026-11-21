from typing import Any
from urllib.parse import urljoin, urlsplit

import requests

BASE_URL = "http://127.0.0.1:8000"
TIMEOUT = 5.0

def resolve_url(path: str, base_url: str = BASE_URL) -> str:
    if urlsplit(path).scheme:
        return path
    return urljoin(base_url.rstrip("/") + "/", path.lstrip("/"))


def request(method: str, path: str, **kw: Any) -> requests.Response:
    kw.setdefault("timeout", TIMEOUT)
    response = requests.request(method, resolve_url(path), **kw)
    return response

def main() -> None:
    todos = request("GET", "/todos", params={"limit": 3}).json()
    print(f"list: {todos}")

    created = request("POST", "/todos", json={"title": "learn urllib"}).json()
    print(f"created: {created}")

    patched = request("PATCH", f"/todos/{created['id']}", json={"done": True})
    print(f"patched: {patched}")

    request("DELETE", f"/todo/{created['id']}")
    print(f"deleted: {created['id']}")

main()