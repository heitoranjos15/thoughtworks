import re
from src.materials import discovery_material_price, Material
from src.numerals.arabic import Arabic
from src.numerals.galaxy import Galaxy


def new_material(message, galaxy_algarisms):
    sum_values, result_values = __get_values_from_message(message)
    algarisms = sum_values[:-1]

    arabic = Arabic('galaxy', algarisms, galaxy_algarisms)

    material_name = sum_values[-1]
    material_price = discovery_material_price(arabic.value, result_values)

    material = Material(material_name, material_price)
    return {material.name: material}


def __get_values_from_message(message):
    splitted_message = message.split(' is ')
    sum_values = splitted_message[0].split(' ')
    result_values = float(re.sub(r'\s(credits)', '', splitted_message[1]))
    return sum_values, result_values
