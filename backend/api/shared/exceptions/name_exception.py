"""
This module defines custom exceptions for handling name validation errors 
within a FastAPI application.
It includes the `NameValidationException` class, which extends FastAPI's `HTTPException` 
to provide a specific 
exception for handling invalid name entries. This exception is used to
enforce data integrity by ensuring 
that all name values meet standards for format and validity 
before being processed or stored.
"""
from fastapi import HTTPException, status

class NameValidationException(HTTPException):
    """
    A custom exception for handling invalid names in FastAPI routes.

    This exception is raised when a name fails validation checks, indicating that
    the input data does not conform to the expected format or validity. It automatically
    sets the HTTP status code to 422 Unprocessable Entity, which is appropriate for situations
    where the client submits data that the server recognizes as structurally correct but 
    semantically incorrect.

    Attributes:
        detail (str): A human-readable description of the error.
    """
    def __init__(self, detail: str):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)
