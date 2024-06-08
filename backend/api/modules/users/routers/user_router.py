"""
This module defines the routing for user-related operations in the FastAPI application.
It utilizes dependencies from the shared database module and services from the user module
to perform operations such as creating a new user.
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.shared.database.dependencies import get_session
from api.modules.users.services.user_service import UserService
from api.modules.users.schemas.user_schema import UserCreateRequest, UserResponse

router = APIRouter()

@router.post('/',
             response_model=UserResponse,
             status_code=status.HTTP_201_CREATED,
             summary='Create new user',
             tags=['users'])
async def create_new_user(data_user: UserCreateRequest,
                          db: AsyncSession = Depends(get_session)
                          ) -> UserResponse:
    """
    Create a new user in the database.

    Args:
        data_user (UserCreateRequest): The user data received from the request, 
        validated by pydantic.
        db (AsyncSession): The database session dependency that allows 
        execution of database operations asynchronously.

    Returns:
        UserResponse: The response model that returns the created user's data after 
        validating through pydantic.

    Raises:
        HTTPException: An error response with appropriate status code and message 
        indicating what went wrong.
    """
    user_service = UserService(db)
    new_user = await user_service.create_new_user(data_user)
    return UserResponse.model_validate(new_user)
