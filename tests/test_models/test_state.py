import unittest
from models.state import State

class TestState(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.state = State()

    def test_init(self):
        """Test the initialization"""
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """Test the attributes"""
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

if __name__ == '__main__':
    unittest.main()
