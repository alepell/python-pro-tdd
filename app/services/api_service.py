import requests
from app.core.config import settings
from app.exceptions.cep_service_error import CepServiceError
from typing import Any


def build_cep_url(cep: str) -> str:
    return f"{settings.VIA_CEP_BASE_URL}/{cep}/json/"


def get_cep(cep: str) -> dict[str, Any]:
    validate_cep(cep)

    url = build_cep_url(cep)

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.Timeout as exc:
        raise CepServiceError("Timeout ao buscar CEP") from exc

    if response.status_code != 200:
        raise CepServiceError("Erro ao buscar CEP")

    return response.json()


def validate_cep(cep: str) -> None:
    if not cep.isdigit() or len(cep) != 8:
        raise CepServiceError("CEP inválido")
