import unittest
from src.numerals.arabic import Arabic
from src.errors.exception import InvalidRomanAlgarism


class TestArabicNumeral(unittest.TestCase):
    def test_roman_to_arabic(self):
        arabic_value = Arabic('roman', ['I', 'X'])
        self.assertEqual(arabic_value.value, 9)

    def test_invalid_roman_to_arabic(self):
        with self.assertRaises(InvalidRomanAlgarism):
            Arabic('roman', ['V', 'X'])
        with self.assertRaises(InvalidRomanAlgarism):
            Arabic('roman', ['I', 'I', 'I', 'I', 'X'])
        with self.assertRaises(InvalidRomanAlgarism):
            Arabic('roman', ['D', 'D', 'X'])
