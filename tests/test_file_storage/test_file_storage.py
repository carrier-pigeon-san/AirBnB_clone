#!/usr/bin/python3
"""
This module contains tests for the FileStorage class
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """
        Set up a clean instance of FileStorage before each test.
        """
        self.storage = FileStorage()

    def test_new_method_with_valid_object(self):
        """
        Test if new method adds valid objects to the storage correctly.
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

        for key in result:
            self.assertTrue(key.startswith(expected_key))

        for value in result.values():
            self.assertIsInstance(value, BaseModel)

    def test_save_method(self):
        """
        Test if save method creates a non-empty 'file.json'.
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
        self.assertGreater(os.path.getsize("file.json"), 0)

    def test_reload_method(self):
        """
        Test if reload method loads objects correctly from 'file.json'.
        """
        self.storage.reload()
        result = self.storage.all()
        expected_key = 'BaseModel.'

        for key in result:
            self.assertTrue(key.startswith(expected_key))
            self.assertIsInstance(result[key], BaseModel)


if __name__ == '__main__':
    unittest.main()
