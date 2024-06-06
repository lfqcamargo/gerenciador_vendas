from typing import AsyncGenerator

from api.shared.database.connection import async_session

async def get_session() -> AsyncGenerator[AsyncGenerator, None]:
    async with async_session() as session:
        yield session