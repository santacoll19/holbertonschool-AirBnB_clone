import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    def setUp(self):
        """ Setup values for testing """
        self.review1 = Review()
        self.review2 = Review()
        self.review2.place_id = "123456"
        self.review2.user_id = "7890"
        self.review2.text = "A great place to stay!"

    def test_id(self):
        """ Test id """
        self.assertNotEqual(self.review1.id, self.review2.id)

    def test_attributes(self):
        """ Test attributes for Review"""
        self.assertTrue(hasattr(self.review1, "place_id"))
        self.assertTrue(hasattr(self.review1, "user_id"))
        self.assertTrue(hasattr(self.review1, "text"))

    def test_attributes_default(self):
        """ Test attributes default for Review """
        self.assertEqual(self.review1.place_id, "")
        self.assertEqual(self.review1.user_id, "")
        self.assertEqual(self.review1.text, "")

    def test_inheritance(self):
        """ Test inheritance from BaseModel """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_to_dict(self):
        """ Test to_dict for Review """
        expected = {
            "id": self.review2.id,
            "__class__": type(self.review2).__name__,
            "place_id": "123456",
            "user_id": "7890",
            "text": "A great place to stay!",
            "created_at": self.review2.created_at.isoformat(),
            "updated_at": self.review2.updated_at.isoformat()
        }
        self.assertDictEqual(self.review2.to_dict(), expected)

    def test_str(self):
        """ Test str for the Review """
        expected = "[Review] ({}) {}".format(self.review2.id, self.review2.__dict__)
        self.assertEqual(str(self.review2), expected)

    def test_save(self):
        """ Test save for the Review """
        created_at = self.review1.created_at
        updated_at = self.review1.updated_at
        self.review1.save()
        self.assertEqual(created_at, self.review1.created_at)
        self.assertNotEqual(updated_at, self.review1.updated_at)

if __name__ == '__main__':
    unittest.main()
