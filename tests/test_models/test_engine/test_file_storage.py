import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.file_storage = FileStorage()
        self.base_model = BaseModel()
        self.file_storage.new(self.base_model)

    def tearDown(self):
        """Tear down for the tests"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_all(self):
        """Test the all method"""
        self.assertIsInstance(self.file_storage.all(), dict)

    def test_new(self):
        """Test the new method"""
        self.assertIn("BaseModel.{}".format(self.base_model.id), self.file_storage.all())

    def test_save(self):
        """Test the save method"""
        self.file_storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test the reload method"""
        self.file_storage.save()
        self.file_storage.__objects = {}
        self.file_storage.reload()
        self.assertIn("BaseModel.{}".format(self.base_model.id), self.file_storage.all())

if __name__ == '__main__':
    unittest.main()
