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
        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']
            created_at = kwargs.get('created_at', datetime.now().isoformat())
            updated_at = kwargs.get('updated_at', datetime.now().isoformat())
            kwargs['created_at'] = datetime.strptime(created_at,
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs['updated_at'] = datetime.strptime(updated_at,
                                                     "%Y-%m-%dT%H:%M:%S.%f")

            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        returns a str represenation of class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates updated_at with current date time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
         Returns a dictionary containing all keys/values of
         __dict__ of the instance, including the class name.
        """
        instance_dict = {'__class__': self.__class__.__name__}
        instance_dict.update(self.__dict__)
        created_at = instance_dict.get('created_at')
        updated_at = instance_dict.get('updated_at')
        if created_at is not None:
            instance_dict['created_at'] = created_at.isoformat()

        if updated_at is not None:
            instance_dict['updated_at'] = updated_at.isoformat()
        return instance_dict
