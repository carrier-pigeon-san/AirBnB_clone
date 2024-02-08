#!/usr/bin/python3
"""
This module contains State class that ing=herits from BaseModel
"""

from .base_model import BaseModel


class State(BaseModel):
    """
    State Class

    Inherited Attributes from BaseModel:
    - id (str): Unique identifier for the user instance.
    - created_at (datetime): Date and time when the user instance was created.
    - updated_at (datetime): Date and time when the user instance was last
    """
    name = ''
