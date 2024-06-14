"""
This test module contains various tests for user creation functionalities within the application.
It tests the API's ability to handle user creation requests correctly, 
ensuring that the data is validated,
the user is correctly added to the database, and the appropriate response is returned.
"""
from datetime import datetime, timedelta, timezone
import pytest
from httpx import AsyncClient
from fastapi import status
from sqlalchemy.future import select

from api.modules.users.models.User import User
from api.utils.crypt_password import verify_password

@pytest.mark.asyncio
async def test_create_new_user(client: AsyncClient, setup_database) -> None:
    """
    Test the creation of a user.

    Ensures a 201 status code and correct user data is returned.
    """
    user_data = {
        "email": "user@example.com",
        "cpf_cnpj": "88877936037", 
        "whatsapp": "14991396707",
        "name": "UserExample",
        "password": "securepassword",
        "sex": "M",
        "date_birthday": "1990-01-01" 
    }

    response = await client.post("/users/", json=user_data)
    assert response.status_code == status.HTTP_201_CREATED

    body = response.json()
    assert body["email"] == user_data["email"]
    assert body["cpf_cnpj"] == user_data["cpf_cnpj"]
    assert body["whatsapp"] == user_data["whatsapp"]
    assert body["name"] == user_data["name"]
    assert body["sex"] == user_data["sex"]
    assert body["date_birthday"] == user_data["date_birthday"]

    async with setup_database.begin():
        user = await setup_database.execute(select(User).where(User.email == user_data["email"]))
        user = user.scalar_one()

    assert verify_password("securepassword", user.password)

    date_created_api = datetime.fromisoformat(
        body['date_created'].rstrip('Z')).replace(tzinfo=timezone.utc)

    date_now = datetime.now(timezone.utc)

    assert abs(date_now - date_created_api) <= timedelta(seconds=10)

@pytest.mark.asyncio
@pytest.mark.parametrize("email", [
    "plainaddress",
    "@missingusername.com",
    "email.example.com",
    "email@example@example.com",
    ".email@example.com",
    "email.@example.com",
    "email..email@example.com",
    "email@example.com (Lucas Camargo)",
    "email@example",
    "email@-example.com",
    "email@example..com",
    "Abc..123@example.com"
])
async def test_invalid_email(client: AsyncClient, email: str) -> None:
    """
    Test various invalid email formats.    
    """
    user_data = {
        "email": email,
        "cpf_cnpj": "88877936037", 
        "whatsapp": "14991000000",
        "name": "UserExample",
        "password": "securepassword",
        "sex": "M",
        "date_birthday": "1990-01-01" 
    }

    response = await client.post("/users/", json=user_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

@pytest.mark.asyncio
@pytest.mark.parametrize("cpf_cnpj", [
    "00000000000",
    "12345678901",
    "12345678901234",
    "11111111111",
    "22222222222222",
    "abcde12345",
    "00000000000000",
    "123",
    "abcdefghijk",
    "123456789012",
    "19283746582910"
])
async def test_invalid_cpf_cnpj(client: AsyncClient, cpf_cnpj: str) -> None:
    """
    Test various invalid cpf/cpnj formats.    
    """
    user_data = {
        "email": "user@example.com",
        "cpf_cnpj": cpf_cnpj, 
        "whatsapp": "14991000000",
        "name": "UserExample",
        "password": "securepassword",
        "sex": "M",
        "date_birthday": "1990-01-01" 
    }

    response = await client.post("/users/", json=user_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

@pytest.mark.asyncio
@pytest.mark.parametrize("whatsapp", [
    "149900000",       # Número muito curto
    "phone_number",    # Contém letras
    "+55149900000000", # Número muito longo
    "149900000000",    # Excede o tamanho máximo permitido
    "00000000000",     # Número não realista
    "1499-000-000",    # Formato incorreto com hífens
    "+1 (499) 000-000" # Formato internacional errado
])
async def test_invalid_whatsapp(client: AsyncClient, whatsapp: str) -> None:
    """
    Test various invalid WhatsApp number formats.
    """
    user_data = {
        "email": "user@example.com",
        "cpf_cnpj": "88877936037", 
        "whatsapp": whatsapp,
        "name": "UserExample",
        "password": "securepassword",
        "sex": "M",
        "date_birthday": "1990-01-01" 
    }

    response = await client.post("/users/", json=user_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
