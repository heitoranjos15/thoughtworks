from src.numerals.arabic import roman_conversor


class Galaxy():
    def __init__(self, name, roman_value):
        if name:
            roman_value = roman_value.upper()
            roman_conversor.get(roman_value)
            self.name = name
            self.roman_value = roman_value
            return
        raise ValueError('name is not valid')
