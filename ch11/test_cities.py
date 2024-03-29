# Create a file called test_cities.py that tests the function you just wrote
# (remember that you need to import unittest and the function you want to
# test). Write a method called test_city_country() to verify that calling
# your function with values such as 'santiago' and 'chile' results in the
# correct string. Run test_cities.py, and make sure test_city_country()
# passes.

import unittest
from city_functions import format_city_info

class CityInfoTestCase(unittest.TestCase):
    """Tests for 'get_city_info'."""

    def test_format_city_info_without_population(self):
        """Do cities like Paris, France work?"""
        formatted_city = format_city_info('paris', 'france')
        self.assertEqual(formatted_city, 'Paris, France')

    def test_format_city_info_with_population(self):
        """Do cities like Paris, France work?"""
        formatted_city = format_city_info('paris', 'france', 2000000)
        self.assertEqual(formatted_city, 'Paris, France - population 2000000')

unittest.main()

