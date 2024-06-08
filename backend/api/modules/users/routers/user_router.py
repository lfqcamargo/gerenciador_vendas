from api.shared.database.dependencies import get_session
from api.modules.users.services.user_service import UserService
from api.modules.users.schemas.user_schema import UserCreateRequest, UserResponse

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()


@router.post('/',
             response_model=UserResponse,
             status_code=status.HTTP_201_CREATED,
             summary='Create new user',
             tags=['users'])
async def create_new_user(data_user: UserCreateRequest,
                          db: AsyncSession = Depends(get_session)
                          ) -> UserResponse:
    
    user_service = UserService(db)
    new_user = await user_service.create_new_user(data_user)
    return UserResponse.model_validate(new_user)