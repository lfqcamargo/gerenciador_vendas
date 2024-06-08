"""
This module configures environment variables for the application using Pydantic's BaseSettings.
It facilitates the management of configuration settings through environment variables, ensuring
that sensitive information is not hard-coded in the source code.

The `Settings` class automatically loads these configurations from a .env file or the environment,
providing a single object that can be used throughout the application to access configuration data.
"""
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """
    A configuration class that loads environment variables from a .env file or directly from
    the environment. This class defines all necessary database configuration parameters
    and provides them through class attributes.
    """
    DATABASE_URL: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_DB: str
    DATABASE_PORT: str
    DATABASE_VOLUME: str
    DATABASE_CONTAINER_NAME: str

    class ConfigDict:
        """
        Configuration class that specifies the source of environment variables.
        """
        env_file = '.env'

    def __init__(self, **values):
        super().__init__(**values)
        if os.getenv('TEST_ENV'):
            self.DATABASE_URL = os.getenv('DATABASE_URL_TEST') # pylint: disable=invalid-name
            self.DATABASE_USER = os.getenv('DATABASE_USER_TEST') # pylint: disable=invalid-name
            self.DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD_TEST') # pylint: disable=invalid-name
            self.DATABASE_DB = os.getenv('DATABASE_DB_TEST') # pylint: disable=invalid-name
            self.DATABASE_PORT = os.getenv('DATABASE_PORT_TEST') # pylint: disable=invalid-name
            self.DATABASE_VOLUME = os.getenv('DATABASE_VOLUME_TEST') # pylint: disable=invalid-name
            self.DATABASE_CONTAINER_NAME = os.getenv('DATABASE_CONTAINER_NAME_TEST') # pylint: disable=invalid-name

settings = Settings()
