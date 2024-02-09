#!/usr/bin/python3
"""
Defines TestCity class that contains methods to test City class
"""

from datetime import datetime
from models.city import City
from models.state import State
import unittest


class TestCity(unittest.TestCase):
    """
    defines methods that test attributes and methods of object of class City
    """

    def test_state_id(self):
        city = City()
        state = State()
        state.name = "Washington"
        city.state_id = state.id
        self.assertEqual(city.state_id, state.id)
        self.assertEqual(type(city.state_id), str)

    def test_city_name(self):
        city = City()
        self.assertEqual(type(city.name), str)

        city.name = "Seattle"
        self.assertEqual(city.name, 'Seattle')

    def test_inherited_attributes(self):
        city = City()
        city0 = City()
        self.assertNotEqual(city.id, city0.id)
        self.assertGreaterEqual(datetime.now(), city.created_at)
        self.assertGreaterEqual(city.updated_at, city.created_at)

    def test_str_function(self):
        city = City()
        state = State()
        city.state_id = state.id
        city.name = "Seattle"
        city_str = city.__str__()
        self.assertEqual(city_str, f"[City] ({city.id}) {city.__dict__}")

    def test_to_dict_function(self):
        city = City()
        state = State()
        city.state_id = state.id
        city.name = "Seattle"
        self.assertEqual(city.to_dict(),
                {
                    '__class__': 'City',
                    'id': city.id,
                    'created_at': city.created_at.isoformat(),
                    'updated_at': city.updated_at.isoformat(),
                    'state_id': state.id,
                    'name': 'Seattle'
                    }
                )

if __name__ == '__main__':
    unittest.main()
