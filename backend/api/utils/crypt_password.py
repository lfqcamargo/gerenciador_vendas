"""
This module provides functionality to hash passwords using bcrypt.

Functions:
hash_password(password: str) -> str: Hashes a password and returns the hashed value.
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
