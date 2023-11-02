import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.amenity = Amenity()

    def test_init(self):
        """Test the initialization"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        """Test the attributes"""
        self.amenity.name = "Pool"
        self.assertEqual(self.amenity.name, "Pool")

if __name__ == '__main__':
    unittest.main()
