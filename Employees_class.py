from People_class import People

class Employees(People):
    def __init__(self, name, pay):
        super().__init__(name)
        self.pay = pay
        self.email = name + '@workmail.com'

