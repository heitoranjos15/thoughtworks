import unittest
from src.numerals.galaxy import Galaxy
from src.materials import Material
from src.logic.answer import answer
from src.errors.exception import InvalidQuestion


class TestAnswerLogic(unittest.TestCase):
    def test_question_how_much(self):
        galaxy_algarisms = {'glob': Galaxy('glob', 'I'), 'prok': Galaxy('prok', 'V')}
        answer_response = answer('how much is glob prok ?', galaxy_algarisms, {})
        self.assertEqual(answer_response, 4)

    def test_question_how_many(self):
        galaxy_algarisms = {'glob': Galaxy('glob', 'I'), 'prok': Galaxy('prok', 'V')}
        materials = {'silver': Material('silver', 16)}
        answer_response = answer('how many credits is glob prok silver ?', galaxy_algarisms, materials)
        self.assertEqual(answer_response, 68)

    def test_question_invalid(self):
        with self.assertRaises(InvalidQuestion):
            answer('how is are you ?', {}, {})
