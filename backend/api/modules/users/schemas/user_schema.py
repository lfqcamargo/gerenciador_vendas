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
from api.shared.validators.phone_validator import validate_and_format_number
from api.shared.validators.name_validator import validate_format_name
from api.shared.validators.password_validator import validate_password
from api.shared.validators.sex_validator import validate_sex
from api.shared.validators.birthdate_validator import validate_birthdate

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

    @field_validator('whatsapp')
    def whatsapp_validator(cls, value: str) -> str: # pylint: disable=E0213
        """
        Validates whether the input is a valid phone number.
        
        Args:
            value (str): The phone number to validate.
        
        Returns:
            str: The validated phone number.
        
        Raises:
            PhoneNumberException: If the phone number is invalid.
        """
        return validate_and_format_number(value)

    @field_validator('name')
    def name_validator(cls, value: str) -> str: # pylint: disable=E0213
        """
        Validates whether the input is a valid name.

        Args:
            value (str): The name to validate.

        Returns:
            str: The validated and formatted name.

        Raises:
            NameValidationException: If the name is invalid.
        """
        return validate_format_name(value)

    @field_validator('password')
    def password_validator(cls, value: str) -> str: # pylint: disable=E0213
        """
        Validates whether the input is a valid password.

        Args:
            value (str): The password to validate.

        Returns:
            str: The validated password if it meets the criteria.

        Raises:
            PasswordValidationException: If the password does not meet security standards.
        """
        return validate_password(value)

    @field_validator('sex')
    def sex_validator(cls, value: str) -> str: # pylint: disable=E0213
        """
        Validates whether the input is a valid gender code.

        Args:
            value (str): The gender code to validate. Expected values are 'M' for male, 
            'F' for female, or 'O' for other.

        Returns:
            str: The validated gender code if it meets the criteria.

        Raises:
            GenderValidationException: If the gender code does not meet the required standards.
        """
        return validate_sex(value)

    @field_validator('date_birthday')
    def birthday_validator(cls, value: date) -> date: # pylint: disable=E0213
        """
        Validates whether the input is a 
        valid birth date and checks if the user is at least 14 years old.

        Args:
            value (date): The birth date to validate.

        Returns:
            date: The validated birth date if it meets the criteria.

        Raises:
            BirthdateValidationException: If the user is 
            not at least 14 years old based on the given birth date.
        """
        return validate_birthdate(value)

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
    