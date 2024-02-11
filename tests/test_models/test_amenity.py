#!/usr/bin/python3
"""
Defines TestAmenity class that contains methods to test Amenity class
"""

from datetime import datetime
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """
    defines methods that test attributes and methods of object of class Amenity
    """

    def test_amenity_name(self):
        """
        Tests the data type and initialization of local variable - 'name'
        """
        amenity = Amenity()
        self.assertEqual(type(amenity.name), str)
        self.assertRaises(TypeError, amenity.name, 3)

        amenity.name = "Internet access"
        self.assertEqual(amenity.name, 'Internet access')

    def test_inherited_attributes(self):
        """Tests the initialization and values of inherited attributes"""
        amenity = Amenity()
        amenity0 = Amenity()
        self.assertNotEqual(amenity.id, amenity0.id)
        self.assertGreaterEqual(datetime.now(), amenity.created_at)
        self.assertGreaterEqual(amenity.updated_at, amenity.created_at)

    def test_str_function(self):
        """Tests the output value of inherited '__str__' function"""
        amenity = Amenity()
        amenity.name = "Internet access"
        amenity_str = amenity.__str__()
        self.assertEqual(amenity_str,
                         f"[Amenity] ({amenity.id}) {amenity.__dict__}")

    def test_to_dict_function(self):
        """Tests the output value of inherited 'to_dict' function"""
        amenity = Amenity()
        amenity.name = "Internet access"
        self.assertEqual(amenity.to_dict(),
                         {
                             '__class__': 'Amenity',
                             'id': amenity.id,
                             'created_at': amenity.created_at.isoformat(),
                             'updated_at': amenity.updated_at.isoformat(),
                             'name': 'Internet access'
                             }
                         )

    def test_class_amenity_with_kwargs(self):
        """
        Tests the initialization of Amenity class attributes with **kwargs
        """
        kwargs = {
                '__class__': 'MyModel',
                'id': '12121212',
                'created_at': '2019-06-27T09:17:08.031275',
                'updated_at': '2019-06-27T09:17:08.031275',
                'name': 'Internet access'
                }
        amenity = Amenity(**kwargs)
        self.assertEqual(amenity.to_dict()['__class__'], 'Amenity')
        self.assertEqual(amenity.id, '12121212')
        self.assertEqual(
                amenity.created_at, datetime(2019, 6, 27, 9, 17, 8, 31275)
                )
        self.assertEqual(
                amenity.updated_at, datetime(2019, 6, 27, 9, 17, 8, 31275)
                )
        self.assertEqual(amenity.name, 'Internet access')


if __name__ == '__main__':
    unittest.main()
