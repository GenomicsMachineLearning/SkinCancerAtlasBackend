from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Lambda Service"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # CORS
    ALLOWED_HOSTS: List[str] = ["*"]

    # AWS
    AWS_REGION: str = "ap-southeast-2"

    # Database (if needed)
    DATABASE_URL: str = ""

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()