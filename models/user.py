#!/user/bin/python3
"""
This module contains a class User that inherits from BaseModel
"""

from .base_model import BaseModel


class User(BaseModel):
    """
    User Class

    Inherited Attributes from BaseModel:
    - id (str): Unique identifier for the user instance.
    - created_at (datetime): Date and time when the user instance was created.
    - updated_at (datetime): Date and time when the user instance was last
    updated.
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
