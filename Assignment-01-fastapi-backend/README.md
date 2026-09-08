# Assignment A1: In-Memory Task API

A small FastAPI task API that keeps data in memory. Restarting the service clears all tasks by design; Assignment A2 moves the same API contract to SQLite.

## Run locally

```bash
cd Assignment-01-fastapi-backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API runs at `http://127.0.0.1:8000`. Interactive documentation is available at `/docs` and `/redoc`.

## Endpoints

| Method | Endpoint | Description | Success code |
| --- | --- | --- | --- |
| GET | `/health` | Service health check | 200 |
| GET | `/` | API information | 200 |
| POST | `/tasks` | Create a task | 201 |
| GET | `/tasks` | List tasks | 200 |
| GET | `/tasks/{task_id}` | Fetch a task | 200 |
| PUT | `/tasks/{task_id}` | Update title and/or completion | 200 |
| DELETE | `/tasks/{task_id}` | Delete a task | 204 |

`title` is required. Missing tasks return `404`; invalid payloads return `422` through FastAPI validation.

## Test

```bash
pytest
```
