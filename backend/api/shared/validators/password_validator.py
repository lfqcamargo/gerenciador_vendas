"""
This module provides functionalities for validating 
passwords to ensure they meet security standards. 
It uses regular expressions to validate passwords, ensuring they contain the required characters for 
adequate security, such as a mix of uppercase, lowercase, numbers, and special characters.

Functions:
- validate_password(password: str) -> str
"""

import re
from api.shared.exceptions.password_exception import PasswordValidationException

def validate_password(password: str) -> str:
    """
    Validates a password to ensure it is strong enough by checking for a combination of 
    uppercase, lowercase, numbers, and special characters.

    Args:
        password (str): The password as a string.

    Returns:
        str: The password if it is valid.

    Raises:
        PasswordValidationException: If the password is not strong enough.
    """
    # Regex to check the validity of the password
    if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
                    password):
        raise PasswordValidationException(f"Key (password)=({password})"
            "The password is not strong enough. It must be at least 8 chars"
            "long and include at least one uppercase letter, "
            "one lowercase letter, one number, and one special character.")
    return password
