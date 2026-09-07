from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_user_lifecycle() -> None:
    create_response = client.post(
        "/users",
        json={"name": "Ada Lovelace", "email": "ada@example.com", "age": 36},
    )
    assert create_response.status_code == 201
    user_id = create_response.json()["id"]

    assert client.get(f"/users/{user_id}").status_code == 200
    assert client.put(
        f"/users/{user_id}",
        json={"name": "Ada Byron", "email": "ada@example.com", "age": 36},
    ).status_code == 200
    assert client.delete(f"/users/{user_id}").status_code == 204
    assert client.get(f"/users/{user_id}").status_code == 404


def test_health_check() -> None:
    assert client.get("/health").json() == {"status": "ok"}
