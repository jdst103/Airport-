from Building_class import Building

class Runway(Building):
    def __init__(self, runway_name, location):
        super().__init__(location)
        self.runway_name = runway_name
