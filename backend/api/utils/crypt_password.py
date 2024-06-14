"""
This module uses bcrypt to provide secure hashing functionalities for passwords. 
It includes functions to hash passwords and verify hashed passwords against plaintext passwords.

Available Functions:
- hash_password(password: str) -> str: Hashes a plaintext password and returns the hashed value.
- verify_password(password: str, hashed_password: str) -> bool: 
Checks if a plaintext password matches a hashed password.
"""
import bcrypt

def has_password(password: str) -> str:
    """
    Hashes a password using bcrypt.

    Args:
    password (str): The password to be hashed.

    Returns:
    str: The hashed password.
    """
    password_bytes = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_password.decode('utf-8')

def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verifies a hashed password against a password provided by the user.

    Args:
        password (str): The plaintext password to verify.
        hashed_password (str): The hashed password to compare against.

    Returns:
        bool: True if the password matches the hashed password, False otherwise.
    """
    password_bytes = password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)
