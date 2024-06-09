"""
This module contains the Pydantic schemas for user-related data validation and handling,
and a utility function for CPF/CNPJ validation.
"""
from pycpfcnpj import cpf, cnpj

from api.shared.exceptions.cpf_cnpj_excpetion import CpfCnpjException

def validate_cpf_cnpj(value: str) -> str:
    """
    Validates whether the input is a valid CPF or CNPJ.
    
    Args:
        value (str): The CPF or CNPJ value to validate.
    
    Returns:
        str: The validated CPF or CNPJ value.
    
    Raises:
        ValueError: If the CPF or CNPJ is invalid.
    """
    if len(value) == 11:
        if not cpf.validate(value):
            raise CpfCnpjException(detail='Invalid CPF')
        return value
    if len(value) == 14:
        if not cnpj.validate(value):
            raise CpfCnpjException(detail='Invalid CNPJ')
        return value

    raise CpfCnpjException(detail='Invalid CPF/CNPJ length')
