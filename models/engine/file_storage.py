#!/usr/bin/python3
"""
"""

import json


class FileStorage:
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
        self.__objects.update(
            {obj.__class__.__name__ + '.' + obj.id : obj.to_dict()}
        )

    def save(self):
        """
         serializes __objects to the JSON file (path: __file_path
        """
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                self.__objects = json.load(f)
                return self.__objects
        except:
            pass
