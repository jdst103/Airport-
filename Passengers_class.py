from People_class import People

class Passengers(People):

    def __init__(self, name, passport_no):
        super().__init__(name)
        self.__passport = passport_no

    def set_passport(self, passport_no):
        self.__passport = passport_no

    def get_passport(self):
        return self.__passport















