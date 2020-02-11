from Aircraft_class import Aircraft


class Helicopter(Aircraft):

    heli_id_var = 1

    def __init__(self, capacity, no_rotors):
        super().__init__(capacity)
        self.no_rotors = no_rotors

    def get_counter_aircraft_id(self):
        return self.heli_id_var

    def get_aircraft_id(self):
        return self.__id