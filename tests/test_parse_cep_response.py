import pytest
from app.services.api_service import parse_cep_response
from app.exceptions.cep_service_error import CepServiceError


def test_should_parse_valid_response():
    data = {"cep": "03535-000", "logradouro": "Rua X"}

    result = parse_cep_response(data)

    assert result["cep"] == "03535-000"
    assert result["logradouro"] == "Rua X"


def test_should_raise_error_when_missing_fields():
    data = {"cep": "03535-000"}

    with pytest.raises(CepServiceError, match="Resposta inválida ao buscar CEP"):
        parse_cep_response(data)


def test_should_raise_error_when_data_is_not_dict():
    data = []

    with pytest.raises(CepServiceError, match="Resposta inválida ao buscar CEP"):
        parse_cep_response(data)
