#!/usr/bin/python3
"""
FileStorage Module

This module defines the FileStorage class responsible for serializing instances
to a JSON file and deserializing JSON files to instances.
"""

import json
import importlib

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
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
         serializes __objects to the JSON file (path: __file_path
        """
        #__objects is an key: value clasname:instance
        serialised_objects = {}
        for key, obj in self.__objects.items():
            serialised_objects[key] = obj.to_dict()

        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(serialised_objects, f)

    def reload(self):
        base_model = importlib.import_module("..base_model", __package__)
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                file_contents = json.load(f)
                for key, obj_dict in file_contents.items():
                    class_name = obj_dict.get('__class__')
                    if class_name:
                        class_instance = getattr(base_model, class_name)
                        obj_instance = class_instance(**obj_dict)
                        self.__objects[key] = obj_instance
        except:
            pass
