from Aircraft_class import Aircraft


class Plane(Aircraft):


    def __init__(self, model, capacity, serial_number, airline):
        super().__init__(capacity)
        self.model = model
        self.serial_number = serial_number
        self.airline = airline

    def get_counter_aircraft_id(self):
            super().get_counter_aircraft_id()
            #return self.aircraft_id_var

    def get_aircraft_id(self):
            super().get_aircraft_id()
            #return self.__id
