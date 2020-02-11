# import all classes
from Passengers_class import Passengers
from Plane_class import Plane
from Flight_class import Flight
from Employees_class import Employees

# intializing employees
employee_1 = Employees('Johnson', 34000)
employee_2 = Employees('Dennis', 400000)

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

# SHOWS ALL PASSENGERS
# for passenger in passengers:
#     print(f'Name: {passenger.name} | Passport number: {passenger.get_passport()}')

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

# PRINT PLANES:
for plane in planes:
    print(f' {plane.get_aircraft_id()}| Model: {plane.model} | Capacity: {plane.capacity}')

############################################################################
# create 3 flights (append to list)
flights = []

flight_stockholm = Flight('SA4657', 'London', 'Stockholm', '21/04/19')
flight_kingston = Flight('AJ3465', 'London', 'Kingston', '12/07/20')
flight_Sydney = Flight('AA6432', 'London', 'Sydney', '05/10/21')
flight_NewYork = Flight('VA2452', 'London', 'New York', '11/02/20')

#adding flight to list
flights.append(flight_stockholm)
flights.append(flight_kingston)
flights.append(flight_Sydney)
flights.append(flight_NewYork)

#  SHOWS ALL FLIGHTS
# for flight in flights:
#     print(f'\n{flight.get_id()} - Flight Number:{flight.flight_number} | Origin:{flight.origin} | Destination:{flight.destination} | Date:{flight.date_time}')

#############################################################################

#passengers to select one and add to flight
# add 2 passengers to each flight

flight_stockholm.add_passenger_to_flight(passenger_1.name)
flight_Sydney.add_passenger_to_flight(passenger_4.name)
flight_Sydney.add_passenger_to_flight(passenger_6.name)
flight_kingston.add_passenger_to_flight(passenger_2.name)


# PRINT COUNT FOR PASSENGER ON FLIGHT
print('\nnumber of passengers on flight to Sydney:', flight_Sydney.count_passengers_on_flight())

##### print Passenger list
print('Passengers to sydney:')
for passenger in flight_Sydney.boarding_list():
    print(passenger)

###########

for flight in flights:
    print(f'\n{flight.get_id()} - Flight Number:{flight.flight_number} | Origin:{flight.origin} | Destination:{flight.destination}\n Passengers:')
    for passenger in flight.passengers_on_flight:
        print(passenger)



