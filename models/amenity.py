#!/usr/bin/python3
"""
This module contains the Amenity class, which inherits
from the BaseModel class.
"""

from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class
    Inherited Attributes from BaseModel:
    - id (str): Unique identifier for the user instance.
    - created_at (datetime): Date and time when the user instance was created.
    - updated_at (datetime): Date and time when the user instance was last
    """
    name = ''
