"""
This module defines custom exceptions for handling password 
validation errors within a FastAPI application.
It includes the `PasswordValidationException` class, 
which extends FastAPI's `HTTPException` to provide a specific
exception for handling inadequate password strength entries. 
This exception is used to enforce data integrity by ensuring
that all password values meet security standards before being processed or stored.
"""
from fastapi import HTTPException, status

class PasswordValidationException(HTTPException):
    """
    A custom exception for handling inadequate passwords in FastAPI routes.

    This exception is raised when a password fails security checks, indicating that
    the input data does not conform to the expected security standards. It automatically
    sets the HTTP status code to 422 Unprocessable Entity, which is appropriate for situations
    where the client submits data that the server recognizes as structurally correct but 
    semantically inadequate for security.

    Attributes:
        detail (str): A human-readable description of the error.
    """
    def __init__(self, detail: str):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)
