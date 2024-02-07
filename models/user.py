#!/user/bin/python3
"""
This module contains a class User that inherits from BaseModel
"""

from .base_model import BaseModel


class User(BaseModel):
    """
    User Class

    Attributes:
    - email (str): Email address of the user.
    - password (str): Password associated with the user's account.
    - first_name (str): First name of the user.
    - last_name (str): Last name of the user.

    Inherited Attributes from BaseModel:
    - id (str): Unique identifier for the user instance.
    - created_at (datetime): Date and time when the user instance was created.
    - updated_at (datetime): Date and time when the user instance was last
    updated.
    """
    email = ''
    password = ''
    first_name = ''
    last_name =''
