class Aircraft():

    aircraft_id_var = 1

    def __init__(self, capacity):
        self.capacity = capacity
        self.__id = Aircraft.aircraft_id_var
        Aircraft.aircraft_id_var += 1

    def get_counter_aircraft_id(self):
        return self.aircraft_id_var

    def get_aircraft_id(self):
        return self.__id








