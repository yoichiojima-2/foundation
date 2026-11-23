"""A small fake REST API for practicing HTTP requests.

Run with:  uv run fake-api
Docs at:   http://127.0.0.1:8000/docs
"""

import random
import time
from typing import Literal

from fastapi import Depends, FastAPI, Header, HTTPException, Query, status
from pydantic import BaseModel, Field

app = FastAPI(title="Fake API", version="0.1.0")

API_TOKEN = "secret-token"

# ---------------------------------------------------------------- models


class TodoIn(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    done: bool = False
    priority: Literal["low", "medium", "high"] = "medium"


class TodoPatch(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    done: bool | None = None
    priority: Literal["low", "medium", "high"] | None = None


class Todo(TodoIn):
    id: int


class Page(BaseModel):
    items: list[Todo]
    total: int
    limit: int
    offset: int


# ---------------------------------------------------------------- state


def _seed() -> dict[int, Todo]:
    data = [
        ("buy milk", False, "low"),
        ("write report", False, "high"),
        ("call mom", True, "medium"),
        ("fix bug #42", False, "high"),
        ("water plants", True, "low"),
    ]
    return {
        i: Todo(id=i, title=t, done=d, priority=p)
        for i, (t, d, p) in enumerate(data, 1)
    }


DB: dict[int, Todo] = _seed()
_rate_hits: list[float] = []


def _next_id() -> int:
    return max(DB, default=0) + 1


def require_token(authorization: str | None = Header(default=None)) -> None:
    if authorization != f"Bearer {API_TOKEN}":
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED, "missing or invalid bearer token"
        )


# ---------------------------------------------------------------- basic


@app.get("/")
def root() -> dict:
    return {"message": "hello", "docs": "/docs"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/reset", status_code=status.HTTP_204_NO_CONTENT)
def reset() -> None:
    DB.clear()
    DB.update(_seed())


# ---------------------------------------------------------------- CRUD


@app.get("/todos")
def list_todos(
    done: bool | None = None,
    priority: Literal["low", "medium", "high"] | None = None,
    q: str | None = Query(default=None, description="substring match on title"),
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
) -> Page:
    items = list(DB.values())
    if done is not None:
        items = [t for t in items if t.done == done]
    if priority is not None:
        items = [t for t in items if t.priority == priority]
    if q:
        items = [t for t in items if q.lower() in t.title.lower()]
    return Page(
        items=items[offset : offset + limit],
        total=len(items),
        limit=limit,
        offset=offset,
    )


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int) -> Todo:
    if todo_id not in DB:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"todo {todo_id} not found")
    return DB[todo_id]


@app.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo(body: TodoIn) -> Todo:
    todo = Todo(id=_next_id(), **body.model_dump())
    DB[todo.id] = todo
    return todo


@app.put("/todos/{todo_id}")
def replace_todo(todo_id: int, body: TodoIn) -> Todo:
    if todo_id not in DB:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"todo {todo_id} not found")
    DB[todo_id] = Todo(id=todo_id, **body.model_dump())
    return DB[todo_id]


@app.patch("/todos/{todo_id}")
def update_todo(todo_id: int, body: TodoPatch) -> Todo:
    if todo_id not in DB:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"todo {todo_id} not found")
    DB[todo_id] = DB[todo_id].model_copy(update=body.model_dump(exclude_none=True))
    return DB[todo_id]


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int) -> None:
    if todo_id not in DB:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"todo {todo_id} not found")
    del DB[todo_id]


# ---------------------------------------------------------------- auth / headers


@app.get("/secret", dependencies=[Depends(require_token)])
def secret() -> dict:
    return {"secret": "the cake is a lie"}


@app.get("/echo")
def echo(
    x_custom: str | None = Header(default=None), user_agent: str = Header()
) -> dict:
    return {"x_custom": x_custom, "user_agent": user_agent}


# ---------------------------------------------------------------- errors / timing


@app.get("/slow")
def slow(seconds: float = Query(default=2.0, ge=0, le=30)) -> dict:
    """Useful for practicing timeouts."""
    time.sleep(seconds)
    return {"slept": seconds}


@app.get("/flaky")
def flaky(fail_rate: float = Query(default=0.5, ge=0, le=1)) -> dict:
    """Randomly returns 500. Useful for practicing retries."""
    if random.random() < fail_rate:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR, "random failure, try again"
        )
    return {"ok": True}


@app.get("/ratelimited")
def ratelimited() -> dict:
    """Allows 3 requests per 10 seconds, then returns 429 with Retry-After."""
    now = time.monotonic()
    _rate_hits[:] = [t for t in _rate_hits if now - t < 10]
    if len(_rate_hits) >= 3:
        retry = int(10 - (now - _rate_hits[0])) + 1
        raise HTTPException(
            status.HTTP_429_TOO_MANY_REQUESTS,
            "slow down",
            headers={"Retry-After": str(retry)},
        )
    _rate_hits.append(now)
    return {"ok": True, "remaining": 3 - len(_rate_hits)}


@app.get("/status/{code}")
def any_status(code: int) -> dict:
    """Return any status code you ask for, e.g. /status/503."""
    if code < 200 or code > 599:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "code must be 200-599")
    if code >= 400:
        raise HTTPException(code, f"you asked for {code}")
    return {"code": code}


def main() -> None:
    import uvicorn

    uvicorn.run("api_requests.fake_api:app", host="127.0.0.1", port=8000, reload=True)
