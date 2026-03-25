import requests
import logging
from app.core.config import settings
from app.exceptions.cep_service_error import CepServiceError
from typing import Any

from app.schemas.cep_data import CepData

TIMEOUT_ERROR_MESSAGE = "Timeout ao buscar CEP"
GENERIC_ERROR_MESSAGE = "Erro ao buscar CEP"
INVALID_CEP_MESSAGE = "CEP inválido"
INVALID_RESPONSE_MESSAGE = "Resposta inválida ao buscar CEP"

logger = logging.getLogger(__name__)


def build_cep_url(cep: str) -> str:
    return f"{settings.VIA_CEP_BASE_URL}/{cep}/json/"


def get_cep(cep: str) -> CepData:
    validate_cep(cep)

    url = build_cep_url(cep)

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.Timeout as exc:
        logger.error(TIMEOUT_ERROR_MESSAGE)
        raise CepServiceError(TIMEOUT_ERROR_MESSAGE) from exc

    if response.status_code != 200:
        logger.error(GENERIC_ERROR_MESSAGE)
        raise CepServiceError(GENERIC_ERROR_MESSAGE)
    data = response.json()
    return parse_cep_response(data)


def validate_cep(cep: str) -> None:
    if not cep.isdigit() or len(cep) != 8:
        raise CepServiceError(INVALID_CEP_MESSAGE)


def parse_cep_response(data: Any) -> CepData:
    if not isinstance(data, dict):
        logger.error(INVALID_RESPONSE_MESSAGE)
        raise CepServiceError(INVALID_RESPONSE_MESSAGE)

    if "cep" not in data or "logradouro" not in data:
        logger.error(INVALID_RESPONSE_MESSAGE)
        raise CepServiceError(INVALID_RESPONSE_MESSAGE)

    return {
        "cep": data["cep"],
        "logradouro": data["logradouro"],
    }
