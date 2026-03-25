from fastapi import APIRouter, Depends
from app.schemas.cep_data import CepData
from app.services.api_service import get_cep

router = APIRouter()


@router.get("/cep/{cep}")
def get_cep_data(cep: str, service: CepData = Depends(get_cep)) -> CepData:
    return service
