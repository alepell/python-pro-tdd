from fastapi import FastAPI
from app.api.handlers.cep_handler import cep_service_exception_handler
from app.api.routes.cep import router as cep_router
from app.api.routes.auth import router as auth_router
from app.exceptions.cep_service_error import CepServiceError

app = FastAPI()
app.include_router(cep_router)
app.include_router(auth_router)
app.add_exception_handler(CepServiceError, cep_service_exception_handler)
