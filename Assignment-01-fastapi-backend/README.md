# Assignment 01: FastAPI Users API

A small, production-style REST API that manages users in memory. It demonstrates modular FastAPI routing, Pydantic validation, appropriate HTTP status codes, and automatic OpenAPI documentation.

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
| POST | `/users` | Create a user | 201 |
| GET | `/users` | List users | 200 |
| GET | `/users/{user_id}` | Fetch a user | 200 |
| PUT | `/users/{user_id}` | Fully replace a user | 200 |
| DELETE | `/users/{user_id}` | Delete a user | 204 |

`name` must contain at least two characters, `email` must be valid, and `age`, when provided, must be positive. Missing users return `404`.

## Test

```bash
pytest
```
