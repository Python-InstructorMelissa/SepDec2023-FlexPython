from .vehicle import *

class MonsterTruck(Vehicle):
    def __init__(self, name, doorCount, fuelType, color, tireSize):
        super().__init__(color, tireSize)
        self.name = name
        self.doorCount = doorCount
        self.fuelType = fuelType

    def printTruckInfo(self):
        print(f'{self.name}:\nColor: {self.color}\nFuel Type: {self.fuelType}\nNumber of Doors: {self.doorCount}\nTireSize: {self.tireSize}\nFuel Level: {self.fuelLevel}')

    def fuelUp(self):
        if self.fuelLevel == 100:
            print(f'{self.name} your tank is full move on out')
        else:
            self.fuelLevel = 100
            print(f'{self.name}, you are now full head on out')
        return self
    
    def useFuel(self, num):
        if self.fuelLevel > 0:
            self.fuelLevel = self.fuelLevel - num
            if self.fuelLevel < 0:
                self.fuelLevel == 0
                print(f'{self.name} sorry dude your all out of fuel better go fuel up')
            else:
                print(f'{self.name} you are now at a fuel level of {self.fuelLevel}')
        else:
            print(f'Error Will Robinson {self.name} is already empty')
        return self