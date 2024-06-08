"""
This module provides a decorator for handling database exceptions consistently.
"""
from functools import wraps
from api.shared.exceptions.database_exception import DataBaseTransactionException
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError, DataError

def handle_database_exceptions(func):
    """
    Decorator to handle database exceptions and raise a custom exception.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function with exception handling.
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except (IntegrityError, OperationalError, DataError, SQLAlchemyError) as e:
            raise DataBaseTransactionException(e) from e
    return wrapper
