import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.city = City()

    def test_init(self):
        """Test the initialization"""
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        """Test the attributes"""
        self.city.name = "San Francisco"
        self.city.state_id = "CA"
        self.assertEqual(self.city.name, "San Francisco")
        self.assertEqual(self.city.state_id, "CA")

if __name__ == '__main__':
    unittest.main()
