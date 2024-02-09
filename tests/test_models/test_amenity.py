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
        amenity = Amenity()
        self.assertEqual(type(amenity.name), str)

        amenity.name = "Internet access"
        self.assertEqual(amenity.name, 'Internet access')

    def test_inherited_attributes(self):
        amenity = Amenity()
        amenity0 = Amenity()
        self.assertNotEqual(amenity.id, amenity0.id)
        self.assertGreaterEqual(datetime.now(), amenity.created_at)
        self.assertGreaterEqual(amenity.updated_at, amenity.created_at)

    def test_str_function(self):
        amenity = Amenity()
        amenity.name = "Internet access"
        amenity_str = amenity.__str__()
        self.assertEqual(amenity_str, f"[Amenity] ({amenity.id}) {amenity.__dict__}")

    def test_to_dict_function(self):
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

if __name__ == '__main__':
    unittest.main()
