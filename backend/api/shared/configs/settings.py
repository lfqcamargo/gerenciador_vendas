from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    DATABASE_URL: str = Field(..., env='DATABASE_URL')
    DATABASE_USER: str = Field(..., env='DATABASE_USER')
    DATABASE_PASSWORD: str = Field(..., env='DATABASE_PASSWORD')
    DATABASE_DB: str = Field(..., env='DATABASE_DB')
    DATABASE_PORT: str = Field(..., env='DATABASE_PORT')
    DATABASE_VOLUME: str = Field(..., env='DATABASE_VOLUME')
    DATABASE_CONTAINER_NAME: str = Field(..., env='DATABASE_CONTAINER_NAME')

       
    class Config:
        env_file = '.env'
        
settings = Settings()