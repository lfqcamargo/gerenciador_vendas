"""
This module contains the UserService class, which provides methods for managing user-related
database operations. It includes functionality to create new users based on data validated
by pydantic models, handle database transactions, and apply business logic such as setting
the user's creation date and status.
"""
from sqlalchemy.ext.asyncio import AsyncSession

from api.modules.users.models.User import User
from api.modules.users.schemas.user_schema import UserCreateRequest, UserResponse
from api.shared.handlers.database_handler import handle_database_exceptions

class UserService:
    """
    A service class for handling user-related database operations.

    Attributes:
        session (AsyncSession): An instance of AsyncSession for database transactions.
    """
    def __init__(self, session: AsyncSession):
        self.session = session

    @handle_database_exceptions
    async def create_new_user(self, data_user: UserCreateRequest) -> UserResponse:
        """
        Creates a new user in the database from the provided user data.

        Args:
            data_user (UserCreateRequest): The user data validated by pydantic, 
            used to create a new user.

        Returns:
            UserResponse: A model representing the newly created user, 
            validated through pydantic.

        Raises:
            Exception: Captures any exceptions during the transaction, 
            rolls back the session, and logs the error.
        """
        user_data = data_user.model_dump()
        new_user = None

        new_user = User(**user_data)
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)

        return new_user
