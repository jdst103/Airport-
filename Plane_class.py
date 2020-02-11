from Aircraft_class import Aircraft


class Plane(Aircraft):

    plane_id_var = 1

    def __init__(self, model, capacity, serial_number, airline):
        super().__init__(capacity)
        self.model = model
        self.serial_number = serial_number
        self.airline = airline
        self.__id = Plane.plane_id_var
        Plane.plane_id_var += 1

    def get_counter_aircraft_id(self):
            return self.plane_id_var

    def get_aircraft_id(self):
            return self.__id
