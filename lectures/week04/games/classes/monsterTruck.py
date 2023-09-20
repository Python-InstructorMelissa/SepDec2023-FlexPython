from .vehicle import *

class MonsterTruck(Vehicle):
    def __init__(self, name, doorCount, fuelType, color, tireSize):
        super().__init__(color, tireSize)
        self.name = name
        self.doorCount = doorCount
        self.fuelType = fuelType

    def printTruckInfo(self):
        print(f'{self.name}:\nFuel Type: {self.fuelType}\nNumber of Doors: {self.doorCount}\n')
        self.printVehicleInfo()
        return self
