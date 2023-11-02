import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.user = User()

    def test_init(self):
        """Test the initialization"""
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Test the attributes"""
        self.user.email = "test@example.com"
        self.user.password = "test_password"
        self.user.first_name = "Test"
        self.user.last_name = "User"
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "test_password")
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")

if __name__ == '__main__':
    unittest.main()
