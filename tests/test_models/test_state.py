#!/usr/bin/python3
"""
Defines TestState class that contains methods to test State class
"""

from datetime import datetime
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """
    defines methods that test attributes and methods of object of class State
    """

    def test_state_name(self):
        """Tests initialization and data type of 'name' class attribute"""
        state = State()
        self.assertEqual(type(state.name), str)
        self.assertRaises(TypeError, state.name, 3)

        state.name = "Washington"
        self.assertEqual(state.name, 'Washington')

    def test_inherited_attributes(self):
        """Tests initialization and values of inherited attributes"""
        state = State()
        state0 = State()
        self.assertNotEqual(state.id, state0.id)
        self.assertGreaterEqual(datetime.now(), state.created_at)
        self.assertGreaterEqual(state.updated_at, state.created_at)

    def test_str_function(self):
        """Tests the output value of inherited '__str__' method"""
        state = State()
        state.name = "Washington"
        state_str = state.__str__()
        self.assertEqual(state_str, f"[State] ({state.id}) {state.__dict__}")

    def test_to_dict_function(self):
        """Tests the output value of inherited 'to_dict' method"""
        state = State()
        state.name = "Washington"
        self.assertEqual(state.to_dict(),
                         {
                             '__class__': 'State',
                             'id': state.id,
                             'created_at': state.created_at.isoformat(),
                             'updated_at': state.updated_at.isoformat(),
                             'name': 'Washington'
                             }
                         )

    def test_class_state_with_kwargs(self):
        """Tests initialization of State class attributes with kwargs"""
        kwargs = {
                '__class__': 'MyModel',
                'id': '12121212',
                'created_at': '2019-06-27T09:17:08.031275',
                'updated_at': '2019-06-27T09:17:08.031275',
                'name': 'Washington'
                }
        state = State(**kwargs)
        self.assertEqual(state.to_dict()['__class__'], 'State')
        self.assertEqual(state.id, '12121212')
        self.assertEqual(
                state.created_at, datetime(2019, 6, 27, 9, 17, 8, 31275)
                )
        self.assertEqual(
                state.updated_at, datetime(2019, 6, 27, 9, 17, 8, 31275)
                )
        self.assertEqual(state.name, 'Washington')


if __name__ == '__main__':
    unittest.main()
