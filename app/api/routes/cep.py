from fastapi import APIRouter, HTTPException
from app.exceptions.cep_service_error import CepServiceError
from app.services.api_service import get_cep

router = APIRouter()


@router.get("/cep/{cep}")
def get_cep_data(cep: str) -> dict:
    return get_cep(cep)
