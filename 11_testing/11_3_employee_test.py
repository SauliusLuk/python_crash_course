import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test Employee class"""

    def setUp(self):
        """Make an employee"""
        self.saulius = Employee('saulius', 'lukosius', 10000)


    def test_give_default_raise(self):
        """test the raise"""