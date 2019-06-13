import re
from src.numerals.arabic import Arabic
from src.materials import discovery_material_sale
from src.errors.exception import InvalidQuestion


def answer(question, galaxy_algarisms, materials):
    type_question, values_question = __get_values_from_question(question)
    if type_question == 'how much':
        arabic = Arabic('galaxy', values_question, galaxy_algarisms)
        return '>>>>>>>' + ' '.join(values_question) + f' is {arabic.value}'
    if type_question == 'how many credits':
        galaxy_numbers = values_question[:-1]
        material_name = values_question[-1]
        material = materials.get(material_name)
        arabic = Arabic('galaxy', galaxy_numbers, galaxy_algarisms)
        value_sale = discovery_material_sale(arabic.value, material.price)
        return '>>>>>>>' + ' '.join(values_question) + f' is {value_sale}'
    raise InvalidQuestion('I dont understand your question')


def __get_values_from_question(question):
    question = re.sub(r'\s*\?', '', question)
    splitted_message = question.split(' is ')
    type_question = splitted_message[0]
    values_question = splitted_message[1].split(' ')
    return type_question, values_question
