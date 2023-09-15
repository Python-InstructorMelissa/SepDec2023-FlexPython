from classes.bumperCar import *
from classes.event import *
from classes.monsterTruck import *
from classes.vehicle import *


# ======== Instance Creations ========

# Create Monster Truck
graveDigger = MonsterTruck("Grave Digger", 2, 'Diesel', "Green", 10)
tomater = MonsterTruck("Tomater", 2, "Diesel", "Rust Red", 10)


# Create Bumper Car
bilbo = BumperCar("Bilbo", "2 hours", "Wood", 1)

# Create Event

ralley = Event("Motor Mayhem")




# ======== Method Calling ========
# graveDigger.printTruckInfo()
# bilbo.printCarInfo()
# tomater.userFuel(50).printTruckInfo()
graveDigger.useFuel(50).printTruckInfo()
graveDigger.useFuel(50).printTruckInfo()
graveDigger.useFuel(50).printTruckInfo()

# ralley.eventAgenda(graveDigger, bilbo)
# ralley.theMatch(graveDigger, bilbo)
ralley.eventAgenda(graveDigger, tomater)
ralley.theMatch(graveDigger, tomater)