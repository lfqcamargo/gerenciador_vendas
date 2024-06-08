"""
This module provides a base schema class that extends Pydantic's BaseModel.
It's designed to be a foundation for all schema classes, applying common configurations
across all derived classes such as automatic attribute population from model fields.
"""
from pydantic import BaseModel, ConfigDict

class BaseSchema(BaseModel):
    """
    Base schema class that extends BaseModel from Pydantic.

    This base class configures common settings for all derived schema classes,
    enabling automatic population from attributes among other configurations.

    Attributes:
        model_config (ConfigDict): Configuration dict for Pydantic models,
                                   set to populate model fields from attributes.
    """
    model_config = ConfigDict(from_attributes=True)
    