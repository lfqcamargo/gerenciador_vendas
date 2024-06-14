"""
This module provides functionalities for validating user gender entries to ensure they conform
to accepted values. It validates that the gender code is one of the specified valid options.

Functions:
- validate_sex(sex: str) -> str
"""

from api.shared.exceptions.sex_excpetion import SexValidationException

def validate_sex(sex: str) -> str:
    """
    Validates a gender code to ensure it is one of the accepted values (M, F, or O).

    Args:
        sex (str): The gender code to validate.

    Returns:
        str: The gender code if it is valid.

    Raises:
        GenderValidationException: If the gender code does not meet the specified criteria.
    """
    valid_sexes = {'M', 'F', 'O'}
    if sex not in valid_sexes:
        raise SexValidationException("Invalid gender code. Must be 'M' for male, "
                                        "'F' for female, or 'O' for other.")
    return sex
