import unittest
import random
from faker import Faker
from src.numerals.galaxy import Galaxy
from src.numerals import roman_conversor
from src.errors.exception import InvalidRomanAlgarism


class TestGalaxyNumeral(unittest.TestCase):
    def setUp(self):
        self.faker = Faker()

    def test_roman_to_galaxy(self):
        roman_algarism = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        algarism = random.choice(roman_algarism)
        galaxy = self.faker.name()

        random_value = Galaxy(galaxy, algarism)
        self.assertEqual(random_value.name, galaxy)
        self.assertEqual(random_value.roman_value, algarism)

    def test_invalid_algarism_roman_to_galaxy(self):
        invalids_algarism = ['A', 'B', '1', '45', '^', 'Ç', '-']
        algarism = random.choice(invalids_algarism)
        with self.assertRaises(InvalidRomanAlgarism):
            Galaxy('glob', algarism)
