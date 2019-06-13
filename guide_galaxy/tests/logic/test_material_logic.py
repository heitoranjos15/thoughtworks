import unittest
from src.logic.materials import new_material
from src.numerals.galaxy import Galaxy
from src.errors.exception import InvalidGalaxyAlgarism


class TestMaterialLogic(unittest.TestCase):
    def test_new_material(self):
        galaxy_algarisms = {'glob': Galaxy('glob', 'I'), 'prok': Galaxy('prok', 'V')}
        material = new_material('glob prok gold is 57800 credits', galaxy_algarisms)
        self.assertIsNotNone(material.get('gold'))
        material = material.get('gold')
        self.assertEqual(material.name, 'gold')
        self.assertEqual(material.price, 14449)

    def test_invalid_new_material(self):
        with self.assertRaises(InvalidGalaxyAlgarism):
            new_material('glob prok gold is 57800 credits', {})
        with self.assertRaises(IndexError):
            new_material('glob prok gold', {})
