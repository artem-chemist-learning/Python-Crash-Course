from city_functions import city
import unittest

class CityTestCase(unittest.TestCase):
    def test_city(self):
        city_return = city('Montreal', 'Canada')
        self.assertEqual(city_return, 'Montreal, Canada')
        
unittest.main()