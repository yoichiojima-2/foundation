import pytest
from api_requests.fake_api import app
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    with TestClient(app) as c:
        c.post("/reset")
        yield c


def test_health(client):
    assert client.get("/health").json() == {"status": "ok"}


def test_list_todos_total(client):
    assert client.get("/todos").json()["total"] == 5


def test_list_todos_last_page(client):
    page = client.get("/todos", params={"limit": 2, "offset": 4}).json()
    assert len(page["items"]) == 1
    assert page["total"] == 5


def test_filter_done(client):
    assert len(client.get("/todos", params={"done": "true"}).json()["items"]) == 2


def test_missing_todo(client):
    assert client.get("/todos/999").status_code == 404


def test_create_todo(client):
    r = client.post("/todos", json={"title": "x"})
    assert r.status_code == 201
    assert r.json()["id"] == 6


def test_secret_requires_token(client):
    assert client.get("/secret").status_code == 401
    r = client.get("/secret", headers={"Authorization": "Bearer secret-token"})
    assert r.status_code == 200


def test_flaky(client):
    assert client.get("/flaky", params={"fail_rate": 1}).status_code == 500
    assert client.get("/flaky", params={"fail_rate": 0}).status_code == 200


def test_status_code(client):
    assert client.get("/status/503").status_code == 503
