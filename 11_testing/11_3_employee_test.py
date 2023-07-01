import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test Employee class"""

    def setUp(self):
        """Make an employee"""
        self.saulius = Employee('saulius', 'lukosius', 10000)


    def test_give_default_raise(self):
        """test the raise"""
        self.saulius.give_raise()
        self.assertEqual(self.saulius.salary, 15000)

    def test_give_custom_raise(self):
        """test the raise"""
        self.saulius.give_raise(10000)
        self.assertEqual(self.saulius.salary, 20000)