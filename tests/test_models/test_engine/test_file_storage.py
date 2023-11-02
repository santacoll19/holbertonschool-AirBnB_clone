#!/usr/bin/python3
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.temp_file_path = "test_file.json"
        FileStorage._FileStorage__file_path = self.temp_file_path
        FileStorage._FileStorage__objects = {}  # Clear __objects for testing
        self.storage = FileStorage()
        self.obj = BaseModel()

def tearDown(self):
    if hasattr(self, 'temp_file_path') and os.path.exists(self.temp_file_path):
        os.remove(self.temp_file_path)
    FileStorage._FileStorage__file_path = "file.json"
    FileStorage._FileStorage__objects = {}

    def test_file_storage_attributes(self):
        """Test FileStorage class attributes"""
        file_storage = FileStorage()
        self.assertTrue(hasattr(file_storage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(file_storage, '_FileStorage__objects'))
        self.assertTrue(hasattr(file_storage, 'CLASS_DICT'))

    def test_class_dict(self):
        """Test CLASS_DICT attribute"""
        file_storage = FileStorage()
        self.assertIsInstance(file_storage.CLASS_DICT, dict)
        self.assertEqual(file_storage.CLASS_DICT, {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "Amenity": Amenity
        })

    def test_all_method(self):
        """Test the all method"""
        file_storage = FileStorage()
        objects = file_storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(objects, FileStorage._FileStorage__objects)

    def test_new_method(self):
        """Test the new method"""
        file_storage = FileStorage()
        base_model = BaseModel()
        file_storage.new(base_model)
        self.assertIn(f"BaseModel.{base_model.id}", FileStorage._FileStorage__objects)

    def test_save_method_for_model(self):
        """Test the save method for a specific model instance"""
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()
        key = f"BaseModel.{base_model.id}"
        with open(self.temp_file_path, "r") as file:
            data = json.load(file)
            self.assertTrue(key in data)

    def test_reload_method(self):
        """Test the reload method"""
        file_storage = FileStorage()
        base_model = BaseModel()
        base_model.save()
        file_storage.reload()
        key = f"BaseModel.{base_model.id}"
        self.assertTrue(key in FileStorage._FileStorage__objects)

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.obj.id = "123"

    def test_all(self):
        """Test all method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test new method"""
        self.storage.new(self.obj)
        key = self.obj.__class__.__name__ + "." + self.obj.id
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test save method"""
        self.storage.new(self.obj)
        self.storage.save()
        key = self.obj.__class__.__name__ + "." + self.obj.id
        with open(self.storage._FileStorage__file_path, "r") as f:
            self.assertIn(key, f.read())

    def test_reload(self):
        """Test reload method"""
        self.storage.new(self.obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = self.obj.__class__.__name__ + "." + self.obj.id
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
