# import all classes
from Passengers_class import Passengers
from Plane_class import Plane
from Flight_class import Flight

#start empty list of passenger
passengers = []

# initialize 6 passengers (append to list)
passenger_1 = Passengers('David', '576198')
passenger_2 = Passengers('Sam', '585434')
passenger_3 = Passengers('Eric', '786475')
passenger_4 = Passengers('Hugh', '298754')
passenger_5 = Passengers('Zoe', '953523')
passenger_6 = Passengers('Tyrese', '987427')

#adding each passenger to list
passengers.append(passenger_1)
passengers.append(passenger_2)
passengers.append(passenger_3)
passengers.append(passenger_4)
passengers.append(passenger_5)
passengers.append(passenger_6)

# iterate passengers to show name and passport
for passenger in passengers:
    print(f'Name: {passenger.name} | Passport number: {passenger.get_passport()}')

############################################################################
#start empty list of what I want to track
    #   airplanes
planes = []

# # intialize 3 planes (append to list)
plane_1 = Plane('747',600, '435435A', 'Air Jamaica')
plane_2 = Plane('700', 350, 'T3453', 'British Airways')
plane_3 = Plane('707', 520, 'VA3687', 'Virgin Atlantic')

# adding plane to planes list
planes.append(plane_1)
planes.append(plane_2)
planes.append(plane_3)

for plane in planes:
    print(f'| Model: {plane.model} | Capacity: {plane.capacity}')

############################################################################
# create 3 flights (append to list)
flights = []

flight_1 = Flight('4657', 'London', 'Stockholm', '21/04/19')
flight_2 = Flight('3465', 'London', 'Kingston', '12/07/20')
flight_3 = Flight('6432', 'London', 'Sydney', '05/10/21')
flight_NewYork = Flight('2452', 'London', 'New York', '11/02/20')

#adding flight to list
flights.append(flight_1)
flights.append(flight_2)
flights.append(flight_3)
flights.append(flight_NewYork)

#   flights - this one i will always need - need to list all flights
for flight in flights:
    print(f'\n{flight.get_id()} - Flight Number:{flight.flight_number} | Origin:{flight.origin} | Destination:{flight.destination} | Date:{flight.date_time}')

#passengers to select one and add to flight
# add 2 passengers to each flight
flight_1.add_passenger(passenger_1.name)
flight_3.add_passenger(passenger_4.name)

#count passenger on particular flight
no_passengers_flight1 = flight_1.count_passengers_on_flight()


# list passengers in one flight
#save it as a variable
flight_1_passenger_list = flight_1.passengers_on_flight

# iteraitate
for person in flight_1_passenger_list:
    # displayu each passeneger
    print(person)