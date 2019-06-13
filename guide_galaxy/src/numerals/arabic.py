from src.numerals import roman_conversor
from src.errors.exception import InvalidRomanAlgarism, InvalidGalaxyAlgarism


class Arabic():
    def __init__(self, type_algarism, value, galaxy_algarisms=[]):
        if type_algarism == 'roman':
            self.value = self.__convert_roman_to_arabic(value)
            return
        elif type_algarism == 'galaxy':
            self.value = self.__convert_galaxy_to_arabic(value, galaxy_algarisms)
            return
        raise ValueError('type_algarism is not valid')

    def __convert_roman_to_arabic(self, roman):
        self.repeat = 0
        past_value, arabic_value = 0, 0
        for algarism in roman:
            try:
                arabic_algarism = self.__get_arabic_algarism(algarism, past_value)
                arabic_value = self.__sum(past_value, arabic_algarism, arabic_value)
                past_value = arabic_algarism
            except InvalidRomanAlgarism:
                raise InvalidRomanAlgarism(f'{roman} is not a valid algarism')
        return arabic_value

    def __get_arabic_algarism(self, algarism, past_value):
        arabic_algarism = roman_conversor.get(algarism)
        canRepeat = ['I', 'X', 'C', 'M']
        if arabic_algarism == past_value:
            if self.repeat >= 2 or algarism not in canRepeat:
                raise InvalidRomanAlgarism()
            self.repeat += 1
        return arabic_algarism

    def __sum(self, past_value, arabic_value, total):
        if past_value < arabic_value:
            if past_value == 5:
                raise InvalidRomanAlgarism()
            return arabic_value - total
        return total + arabic_value

    def __convert_galaxy_to_arabic(self, value, galaxy_algarisms):
        roman_values = self.__get_roman_algarism_from_galaxy_list(value, galaxy_algarisms)
        arabic_value = self.__convert_roman_to_arabic(roman_values)
        return arabic_value

    def __get_roman_algarism_from_galaxy_list(self, value, galaxy_algarisms):
        roman_values = list()
        for number in value:
            galaxy = galaxy_algarisms.get(number)
            if galaxy:
                roman_values.append(galaxy.roman_value)
            else:
                raise InvalidGalaxyAlgarism(f'The {number} is not a galaxy number')
        return roman_values
