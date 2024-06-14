"""
This module defines custom exceptions for handling 
gender validation errors within a FastAPI application.
It includes the `GenderValidationException` class, which extends FastAPI's `HTTPException` 
to provide a specific exception for handling invalid gender entries. This exception is used to 
enforce data integrity by ensuring that all gender values meet the accepted standards before 
being processed or stored.
"""
from fastapi import HTTPException, status

class SexValidationException(HTTPException):
    """
    A custom exception for handling invalid gender codes in FastAPI routes.

    This exception is raised when a gender code fails validation checks, indicating that
    the input data does not conform to the expected validity. It automatically
    sets the HTTP status code to 422 Unprocessable Entity, which is appropriate for situations
    where the client submits data that the server recognizes as structurally correct but 
    semantically incorrect.

    Attributes:
        detail (str): A human-readable description of the error.
    """
    def __init__(self, detail: str):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)
