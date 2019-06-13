import unittest
import mock
import random
from faker import Faker
from guide_galaxy import GuideGalaxyProgram
from src.errors.exception import InvalidRomanAlgarism

@mock.patch('builtins.print', return_value='')
class TestProgramGuideGalaxy(unittest.TestCase):
    def setUp(self):
        self.faker = Faker()
        self.roman_algarism = ['i', 'v', 'x', 'l', 'c', 'd', 'm']
        self.materials = ['silver', 'iron', 'gold']
        self.program = GuideGalaxyProgram()

    def test_save_only_galaxy_algarism(self, print):
        algarism_to_be_save = random.randint(0, 10)
        for _ in range(algarism_to_be_save):
            roman_algarism = random.choice(self.roman_algarism)
            galaxy_name = self.faker.first_name().lower()
            self.program.flow_tree(f'{galaxy_name} is {roman_algarism}')
            self.assertIsNotNone(self.program.galaxy_algarisms.get(galaxy_name))
            galaxy_algarism = self.program.galaxy_algarisms.get(galaxy_name)
            self.assertEqual(galaxy_algarism.name, galaxy_name)
            self.assertEqual(galaxy_algarism.roman_value, roman_algarism.upper())

    def test_save_materials_purchase(self, print):
        material_name = random.choice(self.materials)
        self.program.flow_tree('glob is i')
        self.program.flow_tree(f'glob glob {material_name} is 34 credits')
        self.assertIsNotNone(self.program.materials.get(material_name))
        material = self.program.materials.get(material_name)
        self.assertEqual(material.name, material_name)
        self.assertEqual(material.price, 16)

    def test_send_question_how_much(self, print):
        material_name = random.choice(self.materials)
        self.program.flow_tree('glob is i')
        self.program.flow_tree(f'how much is glob glob glob')

    def test_send_question_how_many(self, print):
        material_name = random.choice(self.materials)
        self.program.flow_tree('glob is i')
        self.program.flow_tree(f'glob glob silver is 34 credits')
        self.program.flow_tree(f'how many credits is glob silver ?')

    def test_send_incorret_message(self, print):
        self.program.flow_tree(self.faker.sentence())
        self.assertEqual(self.program.galaxy_algarisms, {})
        self.assertEqual(self.program.materials, {})
