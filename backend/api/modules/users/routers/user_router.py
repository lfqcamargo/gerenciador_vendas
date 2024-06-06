from api.modules.users.models.User import User
from api.shared.database.dependencies import get_session

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select




router = APIRouter()

@router.get('/')
async def find_user(db: AsyncSession = Depends(get_session)):
    
    query = select(User)
    results = await db.execute(query)
    users = results.scalars().all()
    
    return users