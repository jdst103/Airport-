from People_class import People


#employees inherited from People class

class Employees(People):
    def __init__(self, name):
        super().__init__(name)
