from Passengers_class import Passengers
class Flight():

    flight_id_var = 1

    def __init__(self, flight_number, origin, destination, date_time):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.date_time = date_time
        self.__id = Flight.flight_id_var
        Flight.flight_id_var += 1
        self.passengers_on_flight = []

    def counter_id(self):
        return self.flight_id_var

    def get_id(self):
        return self.__id


    def add_passenger_to_flight(self, passenger):
        if passenger not in self.passengers_on_flight:
            self.passengers_on_flight.append(passenger)

    def remove_passenger(self, passenger):
        if passenger in self.passengers_on_flight:
            self.passengers_on_flight.remove(passenger)


    def count_passengers_on_flight(self):
        return len(self.passengers_on_flight)

    def boarding_list(self):
        return self.passengers_on_flight
