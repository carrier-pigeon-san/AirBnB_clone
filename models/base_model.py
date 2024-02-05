#!/usr/bin/python3
"""
This module contains:
BaseModel that defines all common attributes/methods for other classes
"""

from datetime import datetime
import uuid


class BaseModel:
    """
    This is the base class!
    """
    def __init__(self):
        """
        initialises instaces of the base class
        """
        self.id = str(uuid.uuid4())
        self.create_at = "{:%Y-%m-%dT%H:%M:%S.%f}".format(datetime.now())
        self.updated_at = self.create_at

    def __str__(self):
        """
        returns a str represenation of class
        """
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """
        updates updated_at with current date time
        """
        self.updated_at = "{:%Y-%m-%dT%H:%M:%S.%f}".format(datetime.now())

    def to_dict(self):
        """
         Returns a dictionary containing all keys/values of
         __dict__ of the instance, including the class name.
        """
        instance_dict = {'__class__': self.__class__.__name__}
        instance_dict.update(self.__dict__)
        return instance_dict
