# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# base class


class Vehicle:
    pass

# inherits from Vehicle


class GroundVehicle(Vehicle):
    pass

# inherits from GroundVehicle


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass

# inherits from Vehicle


class FlightVehicle(Vehicle):
    pass

# inherits from FlightVehicle


class Airplane(FlightVehicle):
    pass


class Starship(FlightVehicle):
    pass
