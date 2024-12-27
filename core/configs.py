from typing import List, ClassVar

from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'mysql+aiomysql://root:root@localhost:3306/faculdade'
    DBBaseModel: ClassVar = declarative_base()

    JWT_SECRET: str = '814wS5FOfvV9Wkyue2SjIoIIBCAfkwZiyPBAUYvoIaI'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings: Settings = Settings()