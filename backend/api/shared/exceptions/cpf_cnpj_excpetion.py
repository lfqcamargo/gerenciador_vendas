"""
This module defines custom exceptions for handling CPF and CNPJ 
validation errors within a FastAPI application.

It includes the `CpfCnpjException` class, which extends FastAPI's `HTTPException` 
to provide a specific exception
for handling invalid CPF or CNPJ entries. This exception is used to enforce data 
integrity by ensuring that all
CPF and CNPJ values meet Brazilian federal standards for format and validity 
before being processed or stored.
"""
from fastapi import HTTPException, status

class CpfCnpjException(HTTPException):
    """
    A custom exception for handling invalid CPF or CNPJ numbers in FastAPI routes.

    This exception is raised when a CPF or CNPJ fails validation checks, indicating that
    the input data is not conforming to the expected format or validity. It automatically
    sets the HTTP status code to 422 Unprocessable Entity, which is appropriate for situations
    where the client submits data that the server recognizes
    as structurally correct but semantically incorrect.

    Attributes:
        detail (str): A human-readable description of the error.
    """
    def __init__(self, detail: str):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)
