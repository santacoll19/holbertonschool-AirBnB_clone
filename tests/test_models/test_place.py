import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.place = Place()

    def test_init(self):
        """Test the initialization"""
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        """Test the attributes"""
        self.place.city_id = "0001"
        self.place.user_id = "0002"
        self.place.name = "My place"
        self.place.description = "A lovely place"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 37.7749
        self.place.longitude = -122.4194
        self.assertEqual(self.place.city_id, "0001")
        self.assertEqual(self.place.user_id, "0002")
        self.assertEqual(self.place.name, "My place")
        self.assertEqual(self.place.description, "A lovely place")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 37.7749)
        self.assertEqual(self.place.longitude, -122.4194)

if __name__ == '__main__':
    unittest.main()
