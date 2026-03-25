import pytest
from app.core.security import create_access_token, verify_token


def test_should_create_a_valid_jwt_token():
    data = {"sub": "user123"}
    token = create_access_token(data)
    assert isinstance(token, str)
    assert len(token) > 0


def test_should_return_payload_when_token_is_valid():
    data = {"sub": "user123"}
    token = create_access_token(data)
    payload = verify_token(token)
    assert payload["sub"] == "user123"


def test_should_raise_error_when_token_is_invalid():
    with pytest.raises(Exception):
        verify_token("token.invalido.aqui")
