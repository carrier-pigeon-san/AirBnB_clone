#!/usr/bin/python3
"""
This module contains tests for the base_model class
"""

from models.base_model import BaseModel
import unittest
from datetime import datetime


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

        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model1.id)
        self.assertNotEqual(model.id, model1.id)
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model1, BaseModel)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertIsInstance(model1.created_at, datetime)
        self.assertIsInstance(model1.updated_at, datetime)

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

        self.assertEqual(
            model2_json,
            {
                '__class__': 'BaseModel',
                'id': model2.id,
                'created_at': model2_json['created_at'],
                'updated_at': model2_json['updated_at'],
                'name': 'first model',
                'my_number': 89
            }
        )
        self.assertEqual(
            string_rep, f"[BaseModel] ({model2.id}) {model2.__dict__}"
        )
        self.assertGreaterEqual(model2.updated_at, model2.created_at)

    def test_base_model_with_kwargs(self):
        """
        tests basemodel with kwargs present
        """
        kwargs = {
            'id': 'test_id',
            'created_at': '2017-09-28T21:03:54.052298',
            'updated_at': '2017-09-28T21:03:54.052298',
            'test_attr': '89'
            }
        model3 = BaseModel(**kwargs)

        self.assertEqual(model3.id, 'test_id')
        self.assertEqual(
            model3.created_at, datetime(2017, 9, 28, 21, 3, 54, 52298)
        )
        self.assertEqual(
            model3.updated_at, datetime(2017, 9, 28, 21, 3, 54, 52298)
        )
        self.assertEqual(model3.test_attr, '89')


if __name__ == '__main__':
    unittest.main()
