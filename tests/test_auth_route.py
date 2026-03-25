from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_should_return_200_with_access_token_and_token_type():

    response = client.post(
        "/auth/token", data={"username": "teste", "password": "teste"}
    )

    body = response.json()

    assert response.status_code == 200
    assert "access_token" in body
    assert body["token_type"] == "bearer"


def test_should_return_401_when_credentials_are_invalid():
    response = client.post(
        "/auth/token", data={"username": "admin", "password": "errada"}
    )
    assert response.status_code == 401
