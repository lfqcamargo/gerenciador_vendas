"""
This module defines the Pydantic schemas for user-related operations. These schemas are used
for validating the data sent to the API endpoints for creating and responding with user data.
"""
import uuid
from datetime import datetime, date
from typing import Annotated, Optional
from pydantic import Field, EmailStr, field_validator

from api.shared.configs.base_schema import BaseSchema
from api.shared.validators.cpf_cnpj_validator import validate_cpf_cnpj

class UserCreateRequest(BaseSchema):
    """
    A schema for user creation requests. Validates and describes user information required
    to create a new user in the system.
    """
    email: Annotated[
        EmailStr,
        Field(..., max_length=50, description='Email must be at most 50 characters.')]
    cpf_cnpj: Annotated[
        str,
        Field(..., min_length=11, max_length=14,
              description='CPF must be 11 characters or CNPJ must be 14 characters.')]
    whatsapp: Annotated[
        str,
        Field(..., min_length=8, max_length= 14,
              description='WhatsApp number with a minimum 8 characters and maximum 14 characters')]
    name: Annotated[
        str,
        Field(..., min_length=7, max_length= 100,
              description='Name must be between 7 and 100 characters.')]
    password: Annotated[
        str,
        Field(..., min_length=8, max_length=20,
              description='Password must be between 8 and 20 characters.')]
    sex: Annotated[
        str,
        Field(..., min_length=1, max_length= 1,
              description='The user gender (M for male, F for female, O for other).')]
    date_birthday: Annotated[
        date,
        Field(..., description='The user date of birth.')]

    @field_validator('cpf_cnpj')
    def cpf_cnpj_validator(cls, value: str) -> str: # pylint: disable=E0213
        """
        Validates whether the input is a valid CPF or CNPJ.
        
        Args:
            value (str): The CPF or CNPJ value to validate.
        
        Returns:
            str: The validated CPF or CNPJ value.
        
        Raises:
            CpfCnpjException: If the CPF or CNPJ is invalid.
        """
        return validate_cpf_cnpj(value)

class UserResponse(BaseSchema):
    """
    A schema for responding with user data. Provides a secure way to present user information
    after operations such as creation or update.
    """
    id: Annotated[
        uuid.UUID,
        Field(description='The unique identifier for the user.')]
    email: Annotated[
        EmailStr,
        Field(description='The email address of the user.')]
    cpf_cnpj: Annotated[
        str,
        Field(description='The CPF or CNPJ the user')]
    whatsapp: Annotated[
        str,
        Field(description='Whatsapp the user')]
    name: Annotated[
        str,
        Field(description='The full name of the user.')]
    sex: Annotated[
        str,
        Field(description='The gender of the user (M for male, F for female, O for other).')]
    date_birthday: Annotated[
        date,
        Field(description='The date of birth of the user.')]
    status: Annotated[
        int,
        Field(description='Status the user(1 for Activate, 2 for Inatived, 99 for Suspende).')]
    date_created: Annotated[
        datetime,
        Field(description='The date and time when the user account was created.')]
    profile_photo: Annotated[
        Optional[bytes],
        Field(description='Profile photo the user')]
    date_login: Annotated[
        Optional[datetime],
        Field(description='The last date and time the user logged in, may be null.')]
    