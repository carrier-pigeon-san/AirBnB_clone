#!/usr/bin/python3
"""
FileStorage Module

This module defines the FileStorage class responsible for
serializing instances to a JSON file and deserializing
JSON files to instances.
"""

import json


class FileStorage:
    """
    FileStorage Class
    Handles storage and retrieval of instances using JSON files.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
         serializes __objects to the JSON file (path: __file_path
        """
        # __objects is an key: value clasname:instance
        serialised_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialised_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(serialised_objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """

        from ..base_model import BaseModel
        from ..user import User
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..place import Place

        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8')\
                 as f:
                file_contents = json.load(f)

                for key, obj in file_contents.items():
                    class_name, obj_id = key.split('.')
                    class_instance = eval(class_name)
                    instance_obj = class_instance(**obj)
                    FileStorage.__objects[key] = instance_obj
        except FileNotFoundError:
            pass
