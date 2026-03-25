from pydantic import BaseModel


class CepData(BaseModel):
    cep: str
    logradouro: str
