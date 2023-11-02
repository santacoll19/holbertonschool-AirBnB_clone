#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Sets up testing environment"""
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def tearDown(self):
        """Tears down testing environment"""
        del self.my_model

    def test_str(self):
        """Tests str method of BaseModel"""
        my_model_str = self.my_model.__str__()
        self.assertEqual(my_model_str,
                         "[BaseModel] ({}) {}".format(self.my_model.id,
                                                      self.my_model.__dict__))

    def test_init_no_kwargs(self):
        """Test initialization without kwargs"""
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_init_with_kwargs(self):
        """Test initialization with kwargs"""
        kwargs = {
            "id": "1234-5678-9012",
            "created_at": "2022-02-22T22:22:22.222222",
            "updated_at": "2022-02-22T22:22:22.222222",
            "name": "Test"
        }
        bm = BaseModel(**kwargs)
        self.assertEqual(bm.id, "1234-5678-9012")
        self.assertEqual(bm.created_at, datetime.strptime(
            "2022-02-22T22:22:22.222222", "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(bm.updated_at, datetime.strptime(
            "2022-02-22T22:22:22.222222", "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(bm.name, "Test")

    def test_to_dict(self):
        """Tests to_dict method of BaseModel"""
        my_model_dict = self.my_model.to_dict()
        self.assertEqual(type(my_model_dict), dict)
        self.assertEqual(my_model_dict['name'], "My First Model")
        self.assertEqual(my_model_dict['my_number'], 89)
        self.assertEqual(my_model_dict['__class__'], "BaseModel")
        self.assertEqual(my_model_dict['created_at'],
                         self.my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'],
                         self.my_model.updated_at.isoformat())

    def test_save(self):
        """Tests save method of BaseModel"""
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(old_updated_at, self.my_model.updated_at)

    def test_id(self):
        """Tests id attribute of BaseModel"""
        self.assertEqual(type(self.my_model.id), str)

    def test_created_at(self):
        """Tests created_at attribute of BaseModel"""
        self.assertEqual(type(self.my_model.created_at), datetime)

    def test_updated_at(self):
        """Tests updated_at attribute of BaseModel"""
        self.assertEqual(type(self.my_model.updated_at), datetime)

    if __name__ == '__main__':
        unittest.main()
