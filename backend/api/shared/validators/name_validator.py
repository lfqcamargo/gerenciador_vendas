"""
This module provides functionalities for validating and formatting names to ensure they meet
common standards for personal names. It uses regular expressions to validate names and ensure
they are properly capitalized and free of numbers or special characters.

Functions:
- validate_and_format_name(name: str) -> str
"""

import re
from api.shared.exceptions.name_exception import NameValidationException

def validate_format_name(name: str) -> str:
    """
    Validates a name to ensure it is plausible as a personal name and formats it to capitalize
    each word properly.

    Args:
        name (str): The name as a string.

    Returns:
        str: The name properly formatted if valid.

    Raises:
        NameValidationException: If the name is not valid.
    """
    # Regex to check the validity of the name
    if not re.match(r"^(?!.*[!@#$%^&*0-9])(?!.*[_]{2,})(?!.*\s{2,})[A-Za-zéàëç \-']{2,50}$", name):
        raise NameValidationException("The name is not valid. It must start with a capital "
                                      "letter and only contain alphabetic characters and spaces.")
    return name
