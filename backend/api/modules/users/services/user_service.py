from api.modules.users.models.User import User
from api.modules.users.schemas.user_schema import UserCreateRequest, UserResponse

from datetime import datetime, timezone

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def create_new_user(self, data_user: UserCreateRequest):
        user_data = data_user.model_dump()
        user_data['date_created'] = datetime.now(timezone.utc)
        user_data['status'] = 1
        print(user_data)
        new_user = None
        try:
            new_user = User(**user_data)
            self.session.add(new_user)
            await self.session.commit()
            await self.session.refresh(new_user)
        except Exception as e:            
            print(f"An error occurred: {e}")
            await self.session.rollback() 
            return None

        print(new_user)
        return new_user