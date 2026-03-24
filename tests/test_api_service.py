import pytest
import requests
from unittest.mock import Mock, patch


from app.exceptions.cep_service_error import CepServiceError
from app.services.api_service import build_cep_url, get_cep


def test_should_build_cep_url_correctly():

    cep = "03535000"
    result = build_cep_url(cep)
    assert result == "https://viacep.com.br/ws/03535000/json/"


@patch("app.services.api_service.requests.get")
def test_should_return_json_when_api_respond_200(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "cep": "03535-000",
        "logradouro": "Av Dr Bernardino Brito Fonseca De Carvalho",
    }
    mock_get.return_value = mock_response
    result = get_cep("03535000")
    assert result["cep"] == "03535-000"
    assert result["logradouro"] == "Av Dr Bernardino Brito Fonseca De Carvalho"


@patch("app.services.api_service.requests.get")
def test_should_raise_cep_service_error_when_status_is_not_200(mock_get):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    with pytest.raises(CepServiceError, match="Erro ao buscar CEP"):
        get_cep("03535000")

    # try:
    #     get_cep("03535000")
    #     assert False
    # except Exception as e:
    #     assert str(e) == "Erro ao buscar CEP"


@patch("app.services.api_service.requests.get")
def test_should_return_timeout_error(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout()

    with pytest.raises(CepServiceError, match="Timeout ao buscar CEP"):
        get_cep("03535000")


def test_should_raise_error_when_cep_contains_non_digits():
    with pytest.raises(CepServiceError, match="CEP inválido"):
        get_cep("abc12345")


def test_should_raise_error_when_cep_length_is_not_8():
    with pytest.raises(CepServiceError, match="CEP inválido"):
        get_cep("123")


@patch("app.services.api_service.requests.get")
def test_should_not_call_requests_when_cep_is_invalid(mock_get):
    with pytest.raises(CepServiceError, match="CEP inválido"):
        get_cep("abc12345")

    mock_get.assert_not_called()


@patch("app.services.api_service.requests.get")
def test_should_return_expected_cep_data_structure(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "cep": "03535-000",
        "logradouro": "Av Dr Bernardino Brito Fonseca De Carvalho",
    }
    mock_get.return_value = mock_response

    result = get_cep("03535000")

    assert "cep" in result
    assert "logradouro" in result
    assert isinstance(result["cep"], str)
    assert isinstance(result["logradouro"], str)


@patch("app.services.api_service.requests.get")
def test_should_raise_error_when_response_data_is_invalid(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"asd": "asdasd"}
    mock_get.return_value = mock_response

    with pytest.raises(CepServiceError, match="Resposta inválida ao buscar CEP"):
        get_cep("03535000")
