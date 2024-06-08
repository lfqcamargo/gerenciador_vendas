"""
This module configures environment variables for the application using Pydantic's BaseSettings.
It facilitates the management of configuration settings through environment variables, ensuring
that sensitive information is not hard-coded in the source code.

The `Settings` class automatically loads these configurations from a .env file or the environment,
providing a single object that can be used throughout the application to access configuration data.
"""
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    """
    A configuration class that loads environment variables from a .env file or directly from
    the environment. This class defines all necessary database configuration parameters
    and provides them through class attributes.
    """
    DATABASE_URL: str = Field(..., env='DATABASE_URL')
    DATABASE_USER: str = Field(..., env='DATABASE_USER')
    DATABASE_PASSWORD: str = Field(..., env='DATABASE_PASSWORD')
    DATABASE_DB: str = Field(..., env='DATABASE_DB')
    DATABASE_PORT: str = Field(..., env='DATABASE_PORT')
    DATABASE_VOLUME: str = Field(..., env='DATABASE_VOLUME')
    DATABASE_CONTAINER_NAME: str = Field(..., env='DATABASE_CONTAINER_NAME')


    class Config:
        """
        Configuration class that specifies the source of environment variables.
        """
        env_file = '.env'

settings = Settings()
