from src.errors.exception import InvalidRomanAlgarism


def get(algarism):
    roman_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    arabic_value = roman_values.get(algarism)
    if arabic_value:
        return arabic_value
    raise InvalidRomanAlgarism(f'{algarism} is not algarism roman')
