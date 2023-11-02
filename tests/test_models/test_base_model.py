#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.base_model = BaseModel()

    def test_init(self):
        """Test the initialization"""
        self.assertIsInstance(self.base_model, BaseModel)

    def test_attributes(self):
        """Test the attributes"""
        self.assertTrue(hasattr(self.base_model, "id"))
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))

    def test_created_at(self):
        """Test the created_at attribute"""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        """Test the updated_at attribute"""
        self.assertIsInstance(self.base_model.updated_at, datetime)

def test_str(self):
    """Test the __str__ method"""
    expected_output = "[{}] ({}) {}".format(self.base_model.__class__.__name__, self.base_model.id, self.base_model.__dict__)
    expected_output = expected_output.replace("(", "").replace(")", "")  # Remove parentheses
    self.assertEqual(str(self.base_model), expected_output)


if __name__ == '__main__':
    unittest.main()
