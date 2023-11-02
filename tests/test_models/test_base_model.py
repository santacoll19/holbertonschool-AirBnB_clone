import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_base_model_attributes(self):
        """Test BaseModel class attributes"""
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertIsInstance(base_model.id, str)
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertTrue(hasattr(base_model, 'updated_at'))
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_base_model_str(self):
        """Test the __str__ method"""
        base_model = BaseModel()
        expected_str = f"[{base_model.__class__.__name__}] ({base_model.id})"
        self.assertIn(expected_str, str(base_model))

    def test_base_model_save(self):
        """Test the save method"""
        base_model = BaseModel()
        original_updated_at = base_model.updated_at
        base_model.save()
        new_updated_at = base_model.updated_at
        self.assertGreater(new_updated_at, original_updated_at)

    def test_base_model_to_dict(self):
        """Test the to_dict method"""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIsInstance(base_model_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
