from fastapi import FastAPI
from app.api.routes.cep import router as cep_router

app = FastAPI()
app.include_router(cep_router)
