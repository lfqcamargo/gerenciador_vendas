"""
This module sets up the SQLAlchemy engine and sessionmaker for asynchronous database interaction.
It utilizes the application settings to configure the database connection URL and initializes
the declarative base for ORM models.

The module configures an asynchronous engine and session factory which are used throughout
the application to interact with the database in an asynchronous manner.

Globals:
    Base (declarative_base): A base class for declarative class definitions.
    engine (create_async_engine): The SQLAlchemy engine configured for async communication.
    async_session (sessionmaker): A configured sessionmaker for creating asynchronous ORM sessions.
"""
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from api.shared.configs.settings import settings

DATABASE_URL = settings.DATABASE_URL

Base = declarative_base()

engine = create_async_engine(DATABASE_URL, echo=False)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
