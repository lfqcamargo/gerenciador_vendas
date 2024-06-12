"""
This module provides functionalities for validating and formatting phone numbers using
the 'phonenumbers' library. It includes a function to validate phone numbers based on
international standards and format them into an international format. The module
demonstrates handling of phone numbers with consideration to country-specific formats,
ensuring they meet the validation criteria set by the Google libphonenumber library.

Functions:
- validate_and_format_number(phone_number: str, country_code: str) -> str
"""

import phonenumbers
from phonenumbers import NumberParseException
from api.shared.exceptions.phone_number_exceptions import PhoneNumberException

def validate_and_format_number(phone_number: str, country_code: str = 'BR') -> str:
    """
    Validates and formats a phone number to international format using the phonenumbers library.

    Args:
        phone_number (str): The phone number as a string.
        country_code (str): The ISO 3166-1 two-letter country code.

    Returns:
        str: The phone number in E.164 format if valid.

    Raises:
        PhoneNumberException: If the phone number is not valid.
    """
    try:
        number = phonenumbers.parse(phone_number, country_code)

        if not phonenumbers.is_valid_number(number):
            raise PhoneNumberException("The phone number is not valid.")

        return str(phone_number)

    except NumberParseException as exc:
        raise PhoneNumberException("The phone number is not valid.") from exc
