
"""
This module sets up fixtures for testing the API. It includes fixtures to manage the
event loop, set up the database for tests, and create a test client using HTTPX with ASGI support.
These fixtures help manage database state between tests and ensure that each test
has a fresh database and can run asynchronously.
"""
import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from api.app import app
from api.shared.database.connection import Base
from api.shared.configs.settings import settings

DATABASE_URL = settings.DATABASE_URL


@pytest.fixture(scope='function', autouse=True)
async def setup_database():
    """ Sets up the database for each test function by creating and dropping tables. """
    engine = create_async_engine(DATABASE_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )

    async with async_session() as session:
        yield session

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()

@pytest.fixture
async def client():
    """ Creates an asynchronous HTTP client to test the application. """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url='http://test') as ac:
        yield ac
        