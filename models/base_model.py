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
    def __init__(self, *arg, **kwargs):
        """
        initialises instaces of the base class
        """
        self.id = str(uuid.uuid4())
        self.created_at = "{:%Y-%m-%dT%H:%M:%S.%f}".format(datetime.now())
        self.updated_at = self.created_at

        if kwargs:
            del kwargs['__class__']
            created_at = kwargs['created_at']
            updated_at = kwargs['updated_at']
            kwargs['created_at'] = datetime.strptime(created_at,
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs['updated_at'] = datetime.strptime(updated_at,
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        returns a str represenation of class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

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
