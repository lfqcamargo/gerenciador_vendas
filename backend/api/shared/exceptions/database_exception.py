"""
This module defines custom exceptions for database transactions in a FastAPI application.
It includes a specific exception class for handling various SQLAlchemy errors and converting
them into HTTP responses with appropriate status codes and detailed error messages.
"""
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError, DataError

class DataBaseTransactionException(HTTPException):
    """
    Exception raised for errors that occur during database transactions.

    Attributes:
        status_code (int): The HTTP status code for the response.
        detail (str): A detailed error message.
    """
    def __init__(self, exception: Exception):
        if isinstance(exception, IntegrityError):
            error_message = f"Integrity constraint violated: {exception.orig}"
            status_code = status.HTTP_400_BAD_REQUEST
        elif isinstance(exception, DataError):
            error_message = f"Data formatting error in database operation: {exception.orig}"
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        elif isinstance(exception, OperationalError):
            error_message = f"Operational error in database transaction: {exception.orig}"
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif isinstance(exception, SQLAlchemyError):
            error_message = f"Database transaction failed: {str(exception)}"
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            error_message = "An unexpected error occurred in the database transaction."
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        super().__init__(status_code=status_code, detail=error_message)
