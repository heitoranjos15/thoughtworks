import unittest
from src.logic.galaxy import new_galaxy_number


class TestGalaxyLogic(unittest.TestCase):
    def test_new_galaxy_number(self):
        galaxy_number = new_galaxy_number('glob is M')
        self.assertIsNotNone(galaxy_number.get('glob'))
        galaxy_number = galaxy_number.get('glob')
        self.assertEqual(galaxy_number.name, 'glob')
        self.assertEqual(galaxy_number.roman_value, 'M')

    def test_invalid_new_galaxy_number(self):
        with self.assertRaises(IndexError):
            new_galaxy_number('glob M')
