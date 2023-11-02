#!/usr/bin/python3

import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    def setUp(self):
        """ Setup values for testing """
        self.state1 = State()
        self.state2 = State()
        self.state2.name = "California"
        self.state2.save()

    def test_id(self):
        """ Test id """
        self.assertNotEqual(self.state1.id, self.state2.id)

    def test_attributes(self):
        """ Test attributes for State"""
        self.assertTrue(hasattr(self.state1, "name"))

    def test_attributes_default(self):
        """ Test attributes default for State """
        self.assertEqual(self.state1.name, "")

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_to_dict(self):
        """ Test dict for State """
        expected = {
            "id": self.state2.id,
            "__class__": type(self.state2).__name__,
            "name": "California",
            "created_at": self.state2.created_at.isoformat(),
            "updated_at": self.state2.updated_at.isoformat()
        }
        self.assertDictEqual(self.state2.to_dict(), expected)

    def test_str(self):
        """ Test str for the State """
        expected = "[State] ({}) {}".format(self.state2.id, self.state2.__dict__)
        self.assertEqual(str(self.state2), expected)

    def test_save(self):
        """ Test save for the State"""
        created_at = self.state1.created_at
        updated_at = self.state1.updated_at
        self.state1.save()
        self.assertEqual(created_at, self.state1.created_at)
        self.assertNotEqual(updated_at, self.state1.updated_at)


if __name__ == '__main__':
    unittest.main()
