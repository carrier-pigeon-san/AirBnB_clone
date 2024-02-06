#!/usr/bin/python3
"""
This module contains tests for the base_model class
"""

from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """
    Class to test the BaseModel class.
    """
    def test_base_model_attributes(self):
        """
        Test the attributes of the BaseModel class.
        """
        model = BaseModel()
        model1 = BaseModel()

        self.assertNotEqual(model.id, model1.id)
        self.assertIsInstance(model, BaseModel)

    def test_base_model_methods(self):
        """
        Test the methods of the BaseModel class.
        """
        model2 = BaseModel()
        model2.name = 'first model'
        model2.my_number = 89
        model2.save()
        model2_json = model2.to_dict()
        string_rep = model2.__str__()

        self.assertEqual(model2_json, {'my_number': 89, 'name': 'first model',
                                       '__class__': 'BaseModel', 'updated_at':
                                       model2.updated_at, 'id':
                                       model2.id,
                                       'created_at': model2.created_at})
        self.assertEqual(string_rep, f"[BaseModel] ({model2.id}) {model2.__dict__()}")
