from fastapi import APIRouter, HTTPException
from app.exceptions.cep_service_error import CepServiceError
from app.services.api_service import get_cep

router = APIRouter()


@router.get("/cep/{cep}")
def get_cep_data(cep: str) -> dict:
    try:
        return get_cep(cep)
    except CepServiceError as exc:
        if str(exc) == "CEP inválido":
            raise HTTPException(status_code=400, detail=str(exc)) from exc

        raise HTTPException(status_code=502, detail=str(exc)) from exc
