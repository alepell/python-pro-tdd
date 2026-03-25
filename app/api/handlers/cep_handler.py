from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.cep_service_error import CepServiceError


def cep_service_exception_handler(request: Request, exc: CepServiceError):
    message = str(exc)

    if message == "CEP inválido":
        status_code = 400
    elif message == "Timeout ao buscar CEP":
        status_code = 504
    else:
        status_code = 502

    return JSONResponse(
        status_code=status_code,
        content={"detail": message},
    )
