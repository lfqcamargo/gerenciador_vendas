from api.shared.configs.base_schema import BaseSchema

import uuid
from typing import Annotated, Optional
from pydantic import Field, EmailStr
from datetime import datetime, date


class UserCreateRequest(BaseSchema):
    email: Annotated[EmailStr, Field(..., max_length=50, description='Email must be at most 50 characters.')]
    cpf_cnpj: Annotated[str, Field(..., min_length=11, max_length=14, description='CPF must be exactly 11 characters or CNPJ must be exactly 14 characters.')]
    whatsapp: Annotated[str, Field(..., min_length=8, max_length= 14, description='WhatsApp number with a minimum 8 characters and maximum of 14 characters')]
    name: Annotated[str, Field(..., min_length=7, max_length= 100, description='Name must be between 7 and 100 characters.')]
    password: Annotated[str, Field(..., min_length=8, max_length=20, description='Password must be between 8 and 20 characters.')]
    sex: Annotated[str, Field(..., min_length=1, max_length= 1, description='The user gender (M for male, F for female, O for other).')]
    date_birthday: Annotated[date, Field(..., description='The user date of birth.')]
    
class UserResponse(BaseSchema):
    id: Annotated[uuid.UUID, Field(description='The unique identifier for the user.')]
    email: Annotated[EmailStr, Field(description='The email address of the user.')]
    cpf_cnpj: Annotated[str, Field(description='The CPF or CNPJ the user')]
    whatsapp: Annotated[str, Field(description='Whatsapp the user')]
    name: Annotated[str, Field(description='The full name of the user.')]
    sex: Annotated[str, Field(description='The gender of the user (M for male, F for female, O for other).')]
    date_birthday: Annotated[date, Field(description='The date of birth of the user.')]
    status: Annotated[int, Field(description='Status the user(1 for Activate, 2 for Inatived, 99 for Suspende).')]
    date_created: Annotated[datetime, Field(description='The date and time when the user account was created.')]
    profile_photo: Annotated[Optional[bytes], Field(description='Profile photo the user')]
    date_login: Annotated[Optional[datetime], Field(description='The last date and time the user logged in, may be null.')]