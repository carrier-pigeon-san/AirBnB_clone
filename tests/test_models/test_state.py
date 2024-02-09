#!/usr/bin/python3
"""
Defines TestState class that contains methods to test State class
"""

from datetime import datetime
from models.state import State
import unittest


class TestCity(unittest.TestCase):
    """
    defines methods that test attributes and methods of object of class State
    """

    def test_city_name(self):
        state = State()
        self.assertEqual(type(state.name), str)

        state.name = "Washington"
        self.assertEqual(state.name, 'Washington')

    def test_inherited_attributes(self):
        state = State()
        state0 = State()
        self.assertNotEqual(state.id, state0.id)
        self.assertGreaterEqual(datetime.now(), state.created_at)
        self.assertGreaterEqual(state.updated_at, state.created_at)

    def test_str_function(self):
        state = State()
        state.name = "Washington"
        state_str = state.__str__()
        self.assertEqual(state_str, f"[State] ({state.id}) {state.__dict__}")

    def test_to_dict_function(self):
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

if __name__ == '__main__':
    unittest.main()
