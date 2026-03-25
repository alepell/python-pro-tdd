from fastapi.testclient import TestClient
from app.main import app
from app.schemas.cep_data import CepData
from app.exceptions.cep_service_error import CepServiceError
from app.services.api_service import get_cep


def test_should_return_200_using_dependency_override():
    def mock_get_cep(cep: str) -> CepData:
        return CepData(cep="03535-000", logradouro="Rua Teste")

    app.dependency_overrides[get_cep] = mock_get_cep
    client = TestClient(app)

    response = client.get("/cep/03535000")

    app.dependency_overrides.clear()

    assert response.status_code == 200
    assert response.json() == {"cep": "03535-000", "logradouro": "Rua Teste"}
