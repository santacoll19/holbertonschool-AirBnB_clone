#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.file_storage = FileStorage()

    def test_all(self):
        """Test the all method"""
        result = self.file_storage.all()
        self.assertIsInstance(result, dict)

    def test_new(self):
        """Test the new method"""
        obj = BaseModel()
        self.file_storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.file_storage.all())

    def test_save(self):
        """Test the save method"""
        obj = BaseModel()
        self.file_storage.new(obj)
        self.file_storage.save()
        with open("file.json", "r") as file:
            self.assertIn(obj.id, file.read())

if __name__ == '__main__':
    unittest.main()
