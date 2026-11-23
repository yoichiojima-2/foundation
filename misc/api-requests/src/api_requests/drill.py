"""Practice drill: implement these three functions, then run `uv run pytest`."""

from collections.abc import Callable
from typing import Any


def fetch_all(get_page: Callable[[int, int], dict], limit: int = 2) -> list[dict]:
    """Collect every item from a paginated source.

    get_page(limit, offset) returns one page dict:
        {"items": [...], "total": int, "limit": int, "offset": int}

    Call it with increasing offsets (0, limit, 2*limit, ...) until all `total`
    items are collected. Return the items in order. An empty dataset
    (total == 0) returns [].
    """
    raise NotImplementedError


def with_retry(call: Callable[[], Any], max_attempts: int = 3) -> Any:
    """Call `call()` until it returns a non-5xx response.

    call() returns a response-like object with a .status_code attribute.
    Return the first response whose status_code < 500. If every attempt
    returns >= 500, raise requests.HTTPError after exactly max_attempts calls.
    """
    raise NotImplementedError


def count_by_priority(todos: list[dict]) -> dict[str, int]:
    """Count todo dicts (each has a "priority" key) by priority.

    Example: [{"priority": "low"}, {"priority": "low"}] -> {"low": 2}.
    An empty list returns {}.
    """
    raise NotImplementedError
