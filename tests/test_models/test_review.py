import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.review = Review()

    def test_init(self):
        """Test the initialization"""
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """Test the attributes"""
        self.review.place_id = "0001"
        self.review.user_id = "0002"
        self.review.text = "Great place!"
        self.assertEqual(self.review.place_id, "0001")
        self.assertEqual(self.review.user_id, "0002")
        self.assertEqual(self.review.text, "Great place!")

if __name__ == '__main__':
    unittest.main()
