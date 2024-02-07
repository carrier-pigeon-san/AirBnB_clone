#!/usr/bin/python3
"""
This module contains tests for the FileStorage class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

class TestFileStorage(unittest.TestCase):
    """
    """
    def setUp(self):
        """
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        """
        self.storage = FileStorage()


    def test_all_method_and_new_method(self):
        """
        """
        kwargs = {
            'id': 'test_id',
            'created_at': '2017-09-28T21:03:54.052298',
            'updated_at': '2017-09-28T21:03:54.052298',
            'test_attr': '89'
            }
        model = BaseModel(**kwargs)
        self.storage.new(model)
        result = self.storage.all()

        expected_key = "BaseModel."

        # Check if all keys in the result follow the expected format
        for key in result:
            self.assertTrue(key.startswith(expected_key))

        # Check if all values in the result are instances of BaseModel
        for value in result.values():
            self.assertIsInstance(value, BaseModel)

    def test_save_method(self):
        """
        Tests the save method
        """
        kwargs = {
            'id': 'test_id',
            'created_at': '2017-09-28T21:03:54.052298',
            'updated_at': '2017-09-28T21:03:54.052298',
            'test_attr': '89'
        }
        model = BaseModel(**kwargs)
        self.storage.new(model)
        self.storage.save()

        self.assertTrue(os.path.exists("file.json"))


if __name__ == '__main__':
    unittest.main()
