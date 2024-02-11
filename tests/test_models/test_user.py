#!/usr/bin/python3
"""
defines TestUser class that contains methods to test the User class
"""

from datetime import datetime
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """
    defines methods that test the attributes and methods of objects of
    class User
    """

    def test_user_email(self):
        """
        Tests initialization and data type of the class attribute 'email'
        """
        user = User()
        self.assertEqual(type(user.email), str)
        self.assertRaises(TypeError, user.email, 3)

        user.name = "john@mail.com"
        self.assertEqual(user.name, "john@mail.com")

    def test_user_password(self):
        """
        Tests the initialization and data type of class attribute 'password'
        """
        user = User()
        self.assertEqual(type(user.password), str)
        self.assertRaises(TypeError, user.password, 3)

        user.password = "P@ssw0rd"
        self.assertEqual(user.password, "P@ssw0rd")

    def test_first_name(self):
        """
        Tests the initialization and data type of class attribute 'first_name'
        """
        user = User()
        self.assertEqual(type(user.first_name), str)
        self.assertRaises(TypeError, user.first_name, 3)

        user.first_name = "John"
        self.assertEqual(user.first_name, "John")

    def test_last_name(self):
        """
        Tests the initialization and the data type of class attribute
        'last_name'
        """
        user = User()
        self.assertEqual(type(user.last_name), str)
        self.assertRaises(TypeError, user.last_name, 3)

        user.last_name = "Doe"
        self.assertEqual(user.last_name, "Doe")

    def test_inherited_attributes(self):
        """Tests the initialization and values of inherited attributes"""
        user = User()
        user0 = User()
        self.assertNotEqual(user.id, user0.id)
        self.assertGreaterEqual(datetime.now(), user.created_at)
        self.assertGreaterEqual(datetime.now(), user.updated_at)
        self.assertGreaterEqual(user.updated_at, user.created_at)

    def test_str_function(self):
        """Tests the output value of inherited '__str__' function"""
        user = User()
        user.email = "john@email.com"
        user.password = "P@ssw0rd"
        user.first_name = "John"
        user.last_name = "Doe"
        user_str = user.__str__()
        self.assertEqual(user_str, f"[User] ({user.id}) {user.__dict__}")

    def test_to_dict_function(self):
        """Tests the output value of inherited 'to_dict' function"""
        user = User()
        user.email = "john@mail.com"
        user.password = "P@ssw0rd"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.to_dict(),
                         {
                             '__class__': 'User',
                             'id': user.id,
                             'created_at': user.created_at.isoformat(),
                             'updated_at': user.updated_at.isoformat(),
                             'email': 'john@mail.com',
                             'password': 'P@ssw0rd',
                             'first_name': 'John',
                             'last_name': 'Doe'
                             }
                         )

    def test_class_user_with_kwargs(self):
        """Tests creation of User class with kwargs present"""
        kwargs = {
                '__class__': 'MyModel',
                'id': '12121212',
                'created_at': '2019-06-27T09:17:08.031275',
                'updated_at': '2019-06-27T09:17:08.031275',
                'email': 'smith@mail.com',
                'password': 'p@55word',
                'first_name': 'Jane',
                'last_name': 'Smith'
                }
        user = User(**kwargs)
        self.assertEqual(user.id, '12121212')
        self.assertEqual(user.to_dict()['__class__'], 'User')
        self.assertEqual(user.created_at,
                         datetime(2019, 6, 27, 9, 17, 8, 31275))
        self.assertEqual(user.updated_at,
                         datetime(2019, 6, 27, 9, 17, 8, 31275))
        self.assertEqual(user.email, 'smith@mail.com')
        self.assertEqual(user.password, 'p@55word')
        self.assertEqual(user.first_name, 'Jane')
        self.assertEqual(user.last_name, 'Smith')


if __name__ == '__main__':
    unittest.main()
