#!/usr/bin/python3
"""
Defines TestPlace class that contains methods to test Place class
"""

from datetime import datetime
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
import unittest


class TestPlace(unittest.TestCase):
    """
    defines methods that test attributes and methods of object of class Place
    """

    def test_city_id(self):
        """tests class attribute 'city_id', initiialization and type"""
        place = Place()
        city = City()
        place.city_id = city.id
        self.assertEqual(place.city_id, city.id)
        self.assertEqual(type(place.city_id), str)

    def test_user_id(self):
        """tests class attribute 'user_id', initialization and type"""
        place = Place()
        user = User()
        place.user_id = user.id
        self.assertEqual(place.user_id, user.id)
        self.assertEqual(type(place.user_id), str)

    def test_place_name(self):
        """tests class attribute 'name', initialization and type"""
        place = Place()
        self.assertEqual(type(place.name), str)
        self.assertRaises(TypeError, place.name, 3)

        place.name = "Holberton"
        self.assertEqual(place.name, 'Holberton')

    def test_place_description(self):
        """tests class attribute 'description', initialization and type"""
        place = Place()
        self.assertEqual(type(place.description), str)
        self.assertRaises(TypeError, place.description, 3)

        place.description = "Highway A2"
        self.assertEqual(place.description, 'Highway A2')

    def test_number_rooms(self):
        """
        tests class attribute 'number_rooms' initialization and value type
        """
        place = Place()
        self.assertEqual(type(place.number_rooms), int)
        self.assertRaises(TypeError, place.number_rooms, 'three')

        place.number_rooms = 3
        self.assertEqual(place.number_rooms, 3)

    def test_number_bathrooms(self):
        """
        tests class attribute 'number_bathrooms' initialization and value type
        """
        place = Place()
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertRaises(TypeError, place.number_bathrooms, 'three')

        place.number_bathrooms = 3
        self.assertEqual(place.number_bathrooms, 3)

    def test_max_guest(self):
        """tests class attribute 'max_guest' initialization and value type"""
        place = Place()
        self.assertEqual(type(place.max_guest), int)
        self.assertRaises(TypeError, place.max_guest, 'three')

        place.max_guest = 3
        self.assertEqual(place.max_guest, 3)

    def test_price_by_night(self):
        """
        tests class attribute 'price_by_night' initialization and value type
        """
        place = Place()
        self.assertEqual(type(place.price_by_night), int)
        self.assertRaises(TypeError, place.price_by_night, 'three thousand')

        place.price_by_night = 3000
        self.assertEqual(place.price_by_night, 3000)

    def test_latitude(self):
        """tests class attribute 'latitude' initialization and value type"""
        place = Place()
        self.assertEqual(type(place.latitude), float)
        self.assertRaises(TypeError, place.latitude, 'three')

        place.latitude = -0.0391144916628642
        self.assertEqual(place.latitude, -0.0391144916628642)

    def test_longitude(self):
        """tests class attribute 'longitude' initialization and value type"""
        place = Place()
        self.assertEqual(type(place.longitude), float)
        self.assertRaises(TypeError, place.longitude, 'three')

        place.longitude = 76.3271279631721
        self.assertEqual(place.longitude, 76.3271279631721)

    def test_amenity(self):
        """tests class attribute 'amenity_ids' initialization and type"""
        place = Place()
        self.assertEqual(type(place.amenity_ids), list)
        self.assertRaises(TypeError, place.amenity_ids, 'swimming pool')

        amenity = Amenity()
        amenity0 = Amenity()
        amenities = [amenity.id, amenity0.id]
        place.amenity_ids = amenities
        self.assertEqual(place.amenity_ids, [amenity.id, amenity0.id])

    def test_inherited_attributes(self):
        """tests inherited attributes, initialization and attribute value"""
        place = Place()
        place0 = Place()
        self.assertNotEqual(place.id, place0.id)
        self.assertGreaterEqual(datetime.now(), place.created_at)
        self.assertGreaterEqual(place.updated_at, place.created_at)

    def test_str_function(self):
        """tests inherited '__str__' method output value"""
        place = Place()
        city = City()
        user = User()
        place.city_id = city.id
        place.user_id = user.id
        place.name = 'Holberton'
        place.description = "Highway A2"
        place_str = place.__str__()
        self.assertEqual(place_str, f"[Place] ({place.id}) {place.__dict__}")

    def test_to_dict_function(self):
        """tests inherited 'to_dict' method output value"""
        place = Place()
        city = City()
        user = User()
        amenity = Amenity()
        amenity0 = Amenity()
        amenities = [amenity.id, amenity0.id]
        place.city_id = city.id
        place.user_id = user.id
        place.name = 'Holberton'
        place.description = "Highway A2"
        place.number_rooms = 3
        place.number_bathrooms = 4
        place.max_guest = 3
        place.price_by_night = 3000
        place.latitude = -0.0391144916628642
        place.longitude = 76.3271279631721
        place.amenity_ids = amenities
        self.assertEqual(place.to_dict(),
                         {
                             '__class__': 'Place',
                             'id': place.id,
                             'created_at': place.created_at.isoformat(),
                             'updated_at': place.updated_at.isoformat(),
                             'city_id': city.id,
                             'user_id': user.id,
                             'name': 'Holberton',
                             'description': 'Highway A2',
                             'number_rooms': 3,
                             'number_bathrooms': 4,
                             'max_guest': 3,
                             'price_by_night': 3000,
                             'latitude': -0.0391144916628642,
                             'longitude': 76.3271279631721,
                             'amenity_ids': amenities
                             }
                         )

    def test_class_place_with_kwargs(self):
        """tests initialization of Place class attributes with kwargs"""
        city = City()
        user = User()
        amenity = Amenity()
        amenity0 = Amenity()
        amenities = [amenity.id, amenity0.id]
        kwargs = {
                '__class__': 'MyModel',
                'id': '12121212',
                'created_at': '2019-06-27T09:17:08.031275',
                'updated_at': '2019-06-27T09:17:08.031275',
                'city_id': city.id,
                'user_id': user.id,
                'name': 'Holberton',
                'description': 'Highway A2',
                'number_rooms': 3,
                'number_bathrooms': 4,
                'max_guest': 3,
                'price_by_night': 3000,
                'latitude': -0.0391144916628642,
                'longitude': 76.3271279631721,
                'amenity_ids': amenities
                }
        place = Place(**kwargs)
        self.assertEqual(place.to_dict()['__class__'], 'Place')
        self.assertEqual(place.id, '12121212')
        self.assertEqual(place.created_at,
                         datetime(2019, 6, 27, 9, 17, 8, 31275))
        self.assertEqual(place.updated_at,
                         datetime(2019, 6, 27, 9, 17, 8, 31275))
        self.assertEqual(place.city_id, city.id)
        self.assertEqual(place.user_id, user.id)
        self.assertEqual(place.name, 'Holberton')
        self.assertEqual(place.description, 'Highway A2')
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 4)
        self.assertEqual(place.max_guest, 3)
        self.assertEqual(place.price_by_night, 3000)
        self.assertEqual(place.latitude, -0.0391144916628642)
        self.assertEqual(place.longitude, 76.3271279631721)


if __name__ == '__main__':
    unittest.main()
