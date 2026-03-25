from unittest.mock import patch

from fastapi.testclient import TestClient

from app.exceptions.cep_service_error import CepServiceError
from app.main import app

client = TestClient(app)


@patch("app.api.routes.cep.get_cep")
def test_should_return_200_and_cep_data_when_request_is_valid(mock_get_cep):
    mock_get_cep.return_value = {
        "cep": "03535-000",
        "logradouro": "Av Dr Bernardino Brito Fonseca De Carvalho",
    }

    response = client.get("/cep/03535000")

    assert response.status_code == 200
    assert response.json() == {
        "cep": "03535-000",
        "logradouro": "Av Dr Bernardino Brito Fonseca De Carvalho",
    }


@patch("app.api.routes.cep.get_cep")
def test_should_return_400_when_cep_is_invalid(mock_get_cep):
    mock_get_cep.side_effect = CepServiceError("CEP inválido")

    response = client.get("/cep/abc12345")

    assert response.status_code == 400
    assert response.json() == {"detail": "CEP inválido"}
