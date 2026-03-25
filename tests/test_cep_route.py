import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.exceptions.cep_service_error import CepServiceError
from app.schemas.cep_data import CepData
from app.services.api_service import get_cep


def make_client(override):
    app.dependency_overrides[get_cep] = override
    client = TestClient(app)
    return client


def teardown():
    app.dependency_overrides.clear()


def test_should_return_200_and_cep_data_when_request_is_valid():
    def mock_get_cep(cep: str):
        return CepData(cep="03535-000", logradouro="Av Dr Bernardino Brito Fonseca De Carvalho")

    client = make_client(mock_get_cep)
    response = client.get("/cep/03535000")
    app.dependency_overrides.clear()

    assert response.status_code == 200
    assert response.json() == {
        "cep": "03535-000",
        "logradouro": "Av Dr Bernardino Brito Fonseca De Carvalho",
    }


def test_should_return_400_when_cep_is_invalid():
    def mock_get_cep(cep: str):
        raise CepServiceError("CEP inválido")

    client = make_client(mock_get_cep)
    response = client.get("/cep/abc12345")
    app.dependency_overrides.clear()

    assert response.status_code == 400
    assert response.json() == {"detail": "CEP inválido"}


def test_should_return_502_when_external_service_fails():
    def mock_get_cep(cep: str):
        raise CepServiceError("Erro ao buscar CEP")

    client = make_client(mock_get_cep)
    response = client.get("/cep/03535000")
    app.dependency_overrides.clear()

    assert response.status_code == 502
    assert response.json() == {"detail": "Erro ao buscar CEP"}


def test_should_use_global_handler_for_cep_service_error():
    def mock_get_cep(cep: str):
        raise CepServiceError("CEP inválido")

    client = make_client(mock_get_cep)
    response = client.get("/cep/abc12345")
    app.dependency_overrides.clear()

    assert response.status_code == 400
    assert response.json() == {"detail": "CEP inválido"}
