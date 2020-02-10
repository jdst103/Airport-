from Building_class import Building

class Terminal(Building):
     def __init__(self, floors, location, gate=[]):
         super().__init__(floors, location)
         self.gate = gate

