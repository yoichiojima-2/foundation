from dataclasses import dataclass

import pytest
import requests
from api_requests.drill import count_by_priority, fetch_all, with_retry

# ---------------------------------------------------------------- fakes


class FakePager:
    def __init__(self, data: list[dict]) -> None:
        self.data = data
        self.offsets: list[int] = []

    def __call__(self, limit: int, offset: int) -> dict:
        self.offsets.append(offset)
        return {
            "items": self.data[offset : offset + limit],
            "total": len(self.data),
            "limit": limit,
            "offset": offset,
        }


@dataclass
class FakeResponse:
    status_code: int


class FakeCall:
    def __init__(self, codes: list[int]) -> None:
        self.codes = codes
        self.calls = 0

    def __call__(self) -> FakeResponse:
        code = self.codes[min(self.calls, len(self.codes) - 1)]
        self.calls += 1
        return FakeResponse(code)


# ---------------------------------------------------------------- fetch_all


def test_fetch_all_collects_every_page_in_order():
    data = [{"id": i} for i in range(1, 6)]
    pager = FakePager(data)
    assert fetch_all(pager, limit=2) == data
    assert pager.offsets == [0, 2, 4]


def test_fetch_all_empty():
    assert fetch_all(FakePager([]), limit=2) == []


# ---------------------------------------------------------------- with_retry


def test_with_retry_success_first_try():
    call = FakeCall([200])
    response = with_retry(call)
    assert response.status_code == 200
    assert call.calls == 1


def test_with_retry_recovers_after_failures():
    call = FakeCall([500, 500, 200])
    response = with_retry(call, max_attempts=3)
    assert response.status_code == 200
    assert call.calls == 3


def test_with_retry_gives_up():
    call = FakeCall([500])
    with pytest.raises(requests.HTTPError):
        with_retry(call, max_attempts=3)
    assert call.calls == 3


# ---------------------------------------------------------------- count_by_priority


def test_count_by_priority_seed():
    todos = [
        {"title": "buy milk", "priority": "low"},
        {"title": "write report", "priority": "high"},
        {"title": "call mom", "priority": "medium"},
        {"title": "fix bug #42", "priority": "high"},
        {"title": "water plants", "priority": "low"},
    ]
    assert count_by_priority(todos) == {"low": 2, "medium": 1, "high": 2}


def test_count_by_priority_empty():
    assert count_by_priority([]) == {}
