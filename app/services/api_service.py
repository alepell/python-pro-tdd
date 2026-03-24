import requests

from app.exceptions.cep_service_error import CepServiceError


def build_cep_url(cep: str) -> str:
    return f"https://viacep.com.br/ws/{cep}/json/"


def get_cep(cep: str) -> str:
    url = build_cep_url(cep)

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.Timeout as exc:
        raise CepServiceError("Timeout ao buscar CEP") from exc

    if response.status_code != 200:
        raise CepServiceError("Erro ao buscar CEP")

    return response.json()
