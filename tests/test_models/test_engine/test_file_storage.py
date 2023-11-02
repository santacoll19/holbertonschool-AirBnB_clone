import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.temp_file_path = "test_file.json"
        FileStorage._FileStorage__file_path = self.temp_file_path

    def tearDown(self):
        if os.path.exists(self.temp_file_path):
            os.remove(self.temp_file_path)
        FileStorage._FileStorage__file_path = self.temp_file_path

    def test_file_storage_attributes(self):
        """Test FileStorage class attributes"""
        file_storage = FileStorage()
        self.assertTrue(hasattr(file_storage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(file_storage, '_FileStorage__objects'))

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
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertTrue(key in FileStorage._FileStorage__objects)

    def test_save_method(self):
        """Test the save method"""
        file_storage = FileStorage()
        base_model = BaseModel()
        base_model.name = "Test Model"
        file_storage.new(base_model)
        file_storage.save()

        with open(self.temp_file_path, 'r') as f:
            saved_data = json.load(f)
            key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
            self.assertTrue(key in saved_data)

    def test_reload_method(self):
        """Test the reload method"""
        file_storage = FileStorage()
        base_model = BaseModel()
        base_model.name = "Test Model"
        file_storage.new(base_model)
        file_storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertTrue(key in new_storage.all())

if __name__ == '__main__':
    unittest.main()
