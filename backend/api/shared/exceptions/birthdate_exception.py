"""
This module defines custom exceptions for handling birth date validation 
errors within a FastAPI application.
It includes the `BirthdateValidationException` class, which extends FastAPI's `HTTPException`
to provide a specific exception for handling inadequate birth date entries. 
This exception is used to enforce data integrity by ensuring that all birth date values 
meet the minimum age requirement before being processed or stored.
"""
from fastapi import HTTPException, status

class BirthdateValidationException(HTTPException):
    """
    A custom exception for handling inadequate birth dates in FastAPI routes.

    This exception is raised when a birth date fails validation checks, indicating that
    the user is not old enough according to the specified criteria. It automatically
    sets the HTTP status code to 422 Unprocessable Entity, which is appropriate for situations
    where the client submits data that the server recognizes as structurally correct but 
    semantically incorrect.

    Attributes:
        detail (str): A human-readable description of the error.
    """
    def __init__(self, detail: str):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)
