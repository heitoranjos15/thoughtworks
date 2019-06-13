import unittest
from src.materials import Material, discovery_material_price
from src.errors.exception import InvalidRomanAlgarism


class TestMaterials(unittest.TestCase):
    def test_discovery_material_price(self):
        galaxy_value = discovery_material_price(4, 68)
        self.assertEqual(galaxy_value, 16)

    def test_send_invalid_params_for_discovery(self):
        with self.assertRaises(ValueError):
            discovery_material_price('asd', 68)
        with self.assertRaises(ValueError):
            discovery_material_price(4, 'po')

    def test_material(self):
        material = Material('silver', 15.90)
        self.assertEqual(material.name, 'silver')
        self.assertEqual(material.price, 15.90)
        material = Material('silver', '18.21')
        self.assertEqual(material.price, 18.21)

    def test_invalid_material(self):
        with self.assertRaises(ValueError):
            material = Material('Silver', 'asd')
        with self.assertRaises(ValueError):
            material = Material('H20', '18.21')
