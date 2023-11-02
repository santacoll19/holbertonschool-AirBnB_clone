#!/usr/bin/python3

import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.user = User()
        self.user.email = "test@example.com"
        self.user.password = "test_password"
        self.user.first_name = "Test"
        self.user.last_name = "User"

    def test_init(self):
        """Test the initialization"""
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Test the attributes"""
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "test_password")
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")

    def test_attribute_types(self):
        """Test the type of the attributes"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_inheritance(self):
        """Test if User class is correctly inheriting from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_to_dict(self):
        """Test the to_dict method"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["email"], "test@example.com")
        self.assertEqual(user_dict["password"], "test_password")
        self.assertEqual(user_dict["first_name"], "Test")
        self.assertEqual(user_dict["last_name"], "User")


if __name__ == '__main__':
    unittest.main()
