from pydantic_settings import BaseSettings
from typing import List
import os as os
import pathlib as pathlib


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Lambda Service"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # CORS
    ALLOWED_HOSTS: List[str] = ["*"]

    # AWS
    AWS_REGION: str = "ap-southeast-2"

    IMAGE_STORAGE_PATH: pathlib.Path = pathlib.Path("./data")

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()