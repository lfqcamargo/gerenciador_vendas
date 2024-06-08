"""
This module provides a utility function to yield database sessions. It is designed to be used
with FastAPI's dependency injection system to ensure that database sessions are handled
correctly within the context of asynchronous web requests.
"""
from typing import AsyncGenerator

from api.shared.database.connection import async_session

async def get_session() -> AsyncGenerator[AsyncGenerator, None]:
    """
    Provides an asynchronous generator that yields a database session.

    This generator is intended to be used as a dependency in FastAPI route handlers
    to manage the lifecycle of SQLAlchemy async sessions. It ensures that each session
    is contextually managed with proper transaction boundaries.
    """
    async with async_session() as session:
        yield session
        