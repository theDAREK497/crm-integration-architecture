from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_users_returns_typed_records() -> None:
    response = client.get("/users")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Иван Иванов", "email": "ivan@example.com"},
        {"id": 2, "name": "Мария Смирнова", "email": "maria@example.com"},
    ]


def test_openapi_is_available() -> None:
    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert response.json()["info"]["title"] == "CRM Integration Service"
