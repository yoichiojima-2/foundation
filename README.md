# foundation

Personal practice repo. Each top-level directory is independent and gets its
own CI check (`test (<directory>)`).

| Directory | What it is | Run the tests |
|---|---|---|
| `dsa/` | Shared data structures and builders used by the other Python projects | `cd dsa && uv run pytest` |
| `dsa-skelton/` | Algorithm skeletons to implement; unimplemented ones fail on purpose | `cd dsa-skelton && uv run pytest` |
| `leetcode/` | One uv project per LeetCode problem | `cd leetcode/<problem> && uv run pytest` |
| `misc/` | Miscellaneous practice projects; `api-requests/` is HTTP client practice against a local fake API (FastAPI) | no tests; `cd misc/api-requests && uv run fake-api` starts the server |
| `rust-the-book/` | Projects from *The Rust Programming Language*; `minigrep/` is the `grep` clone | `cd rust-the-book/minigrep && cargo test` |

## Conventions

- Every leetcode project has the same layout: `src/<package>/solution.py` and
  `tests/test_solution.py`. `./init <problem-name>` scaffolds a new one.
- Lint and format from the repo root: `uvx ruff check .` and
  `uvx ruff format .` (config in `ruff.toml`; also wired into pre-commit).
- CI (`.github/workflows/test.yml`) discovers every top-level directory that
  contains a `pyproject.toml` or `Cargo.toml`, so a new directory is tested
  without editing the workflow.
