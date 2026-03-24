import requests
import logging
from app.core.config import settings
from app.exceptions.cep_service_error import CepServiceError
from typing import Any

from app.schemas.cep_data import CepData

logger = logging.getLogger(__name__)


def build_cep_url(cep: str) -> str:
    return f"{settings.VIA_CEP_BASE_URL}/{cep}/json/"


def get_cep(cep: str) -> CepData:
    validate_cep(cep)

    url = build_cep_url(cep)

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.Timeout as exc:
        logger.error("Timeout ao buscar CEP")
        raise CepServiceError("Timeout ao buscar CEP") from exc

    if response.status_code != 200:
        raise CepServiceError("Erro ao buscar CEP")
    data = response.json()
    return parse_cep_response(data)


def validate_cep(cep: str) -> None:
    if not cep.isdigit() or len(cep) != 8:
        raise CepServiceError("CEP inválido")


def parse_cep_response(data: Any) -> CepData:
    if not isinstance(data, dict):
        raise CepServiceError("Resposta inválida ao buscar CEP")

    if "cep" not in data or "logradouro" not in data:
        raise CepServiceError("Resposta inválida ao buscar CEP")

    return {
        "cep": data["cep"],
        "logradouro": data["logradouro"],
    }
