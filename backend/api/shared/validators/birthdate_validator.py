"""
This module provides functionalities for validating 
user birth dates to ensure they are at least 14 years old from the current date. 

Functions:
- validate_birthdate(date_birthday: date) -> date
"""

from datetime import date
from api.shared.exceptions.birthdate_exception import BirthdateValidationException

def validate_birthdate(date_birthday: date) -> date:
    """
    Validates a birth date to ensure the user is at least 14 years old.

    Args:
        date_birthday (date): The birth date to validate.

    Returns:
        date: The birth date if it is valid.

    Raises:
        BirthdateValidationException: If the user is not at least 14 years old.
    """
    today = date.today()
    age = today.year - date_birthday.year - (
        (today.month, today.day) < (date_birthday.month, date_birthday.day))
    if age < 14:
        raise BirthdateValidationException(f"Key (date_birthday)=({date_birthday}) User must be at least 14 years old.")
    return date_birthday
