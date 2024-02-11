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
        """
        Tests initialization and data type of 'state_id' class attribute
        """
        city = City()
        state = State()
        state.name = "Washington"
        city.state_id = state.id
        self.assertEqual(city.state_id, state.id)
        self.assertEqual(type(city.state_id), str)

    def test_city_name(self):
        """Tests initialization and data type of 'name' class attribute"""
        city = City()
        self.assertEqual(type(city.name), str)
        self.assertRaises(TypeError, city.name, 3)

        city.name = "Seattle"
        self.assertEqual(city.name, 'Seattle')

    def test_inherited_attributes(self):
        """Tests initialization and values of inherited attributes"""
        city = City()
        city0 = City()
        self.assertNotEqual(city.id, city0.id)
        self.assertGreaterEqual(datetime.now(), city.created_at)
        self.assertGreaterEqual(city.updated_at, city.created_at)

    def test_str_function(self):
        """Tests output value of inherited '__str__' method"""
        city = City()
        state = State()
        city.state_id = state.id
        city.name = "Seattle"
        city_str = city.__str__()
        self.assertEqual(city_str, f"[City] ({city.id}) {city.__dict__}")

    def test_to_dict_function(self):
        """Tests output value of inherited method, 'to_dict'"""
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

    def test_class_city_with_kwargs(self):
        """Tests initialization of City class attributes using kwargs"""
        state = State()
        kwargs = {
                '__class__': 'MyModel',
                'id': '12121212',
                'created_at': '2019-06-27T09:17:08.031275',
                'updated_at': '2019-06-27T09:17:08.031275',
                'state_id': state.id,
                'name': 'Seattle'
                }
        city = City(**kwargs)
        self.assertEqual(city.id, '12121212')
        self.assertEqual(city.to_dict()['__class__'], 'City')
        self.assertEqual(
                city.created_at, datetime(2019, 6, 27, 9, 17, 8, 31275)
                )
        self.assertEqual(
                city.updated_at, datetime(2019, 6, 27, 9, 17, 8, 31275)
                )
        self.assertEqual(city.state_id, state.id)
        self.assertEqual(city.name, 'Seattle')


if __name__ == '__main__':
    unittest.main()
