# api-requests

Practice making HTTP requests against a local fake API.

```sh
uv run fake-api            # starts http://127.0.0.1:8000  (Swagger UI at /docs)
```

| Endpoint | What to practice |
|---|---|
| `GET /todos?done=false&priority=high&q=bug&limit=2&offset=0` | query params, pagination |
| `GET /todos/{id}` | 404 handling |
| `POST /todos` `{"title": "...", "priority": "high"}` | JSON body, 201, 422 validation errors |
| `PUT` / `PATCH` / `DELETE /todos/{id}` | full vs partial update, 204 no content |
| `GET /secret` with `Authorization: Bearer secret-token` | auth headers, 401 |
| `GET /echo` with `X-Custom: hi` | sending/reading headers |
| `GET /slow?seconds=5` | timeouts |
| `GET /flaky?fail_rate=0.7` | retries on 500 |
| `GET /ratelimited` (3 per 10s) | 429 + `Retry-After` |
| `GET /status/503` | any status code |
| `POST /reset` | restore seed data |
