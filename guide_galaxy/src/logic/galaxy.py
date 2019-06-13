from src.numerals.galaxy import Galaxy


def new_galaxy_number(message):
    splitted_message = message.split(' is ')
    galaxy_name = splitted_message[0]
    roman_value = splitted_message[1]
    galaxy = Galaxy(galaxy_name, roman_value)
    return {galaxy.name: galaxy}