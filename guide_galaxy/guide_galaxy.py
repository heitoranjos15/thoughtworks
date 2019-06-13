import time
import re
from src.logic.galaxy import new_galaxy_number
from src.logic.materials import new_material
from src.logic.answer import answer
from src.errors.exception import InvalidRomanAlgarism, InvalidGalaxyAlgarism, InvalidQuestion


class GuideGalaxyProgram():
    def __init__(self):
        self.galaxy_algarisms = dict()
        self.materials = dict()
        self.resp = 1

    def run_program(self):
        self.__welcomeMessages()
        while(self.resp > 0):
            message = str(input()).lower()
            self.resp = self.flow_tree(message)

    def flow_tree(self, message):
        if message == 'end':
            return -1
        elif re.match(r'[a-z]\w*\s(is)\s([a-z])\w*', message):
            try:
                self.galaxy_algarisms.update(
                    new_galaxy_number(message))
            except IndexError:
                self.__invalidMessages('You dont typed all values')
            except InvalidRomanAlgarism as error:
                self.__invalidMessages(error)
        elif re.match(r'[\w\s]*is\s\d*\scredits', message):
            try:
                self.materials.update(new_material(
                    message, self.galaxy_algarisms))
            except (IndexError, ValueError):
                self.__invalidMessages('You dont typed all values')
            except InvalidGalaxyAlgarism as error:
                self.__invalidMessages(error)
        elif re.match(r'how\smany\scredits\sis[\s\w]*', message) or re.match(r'how\smuch\sis[\s\w]*', message):
            try:
                print(answer(message, self.galaxy_algarisms, self.materials))
            except IndexError:
                self.__invalidMessages('You dont typed all values')
            except (InvalidGalaxyAlgarism, InvalidQuestion) as error:
                self.__invalidMessages(error)
        else:
            self.__invalidMessages('I have no idea what you are talking about')
        return 1

    def __welcomeMessages(self):
        print('Welcome to Guide Galaxy program!\n')
        time.sleep(0.5)
        print('To get out of Guide Galaxy, type end\n')
        time.sleep(0.5)
        print('If you type like this : glob is I\nGlob will be equals to I (roman) and 1(arabic)\n')
        print('If you type like this : glob glob Silver is 34 Credits\nThe program will save this'
              ' purchase and discovery the value from Material\n')
        print('If you type like this : how much is glob prok ?\nThe program will respond you')
        print('If you type like this : how many credits is glob prok silver ?\nThe program will respond you')
        time.sleep(0.5)

    def __invalidMessages(self, error_message):
        print(f'\n{error_message}\n')
        print('Try Again\n')

program = GuideGalaxyProgram()
program.run_program()
