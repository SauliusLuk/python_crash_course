import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Tests for 11 1 city country.py"""

    def test_city_country(self):
        """Should be Kaunas, Lithuania"""
        formatted_city_and_country = city_country('kaunas', 'lithuania')
        self.assertEqual(formatted_city_and_country, 'Kaunas, Lithuania')

    def test_city_country_pop(self):
        """Should be Kaunas, Lithuania, 400"""
        formatted_city_country_pop = city_country('kaunas', 'lithuania', '400')
        self.assertEqual(formatted_city_country_pop, 'Kaunas, Lithuania, 400')

if __name__ == '__main__':
    unittest.main()