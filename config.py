from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    EMAIL_SENDER: str
    SENDER_PASSWORD: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()