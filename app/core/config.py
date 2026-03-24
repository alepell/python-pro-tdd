from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    VIA_CEP_BASE_URL: str = os.getenv("VIA_CEP_BASE_URL", "https://viacep.com.br/ws")


settings = Settings()
