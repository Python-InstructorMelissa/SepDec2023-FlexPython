from .vehicle import *

class BumperCar(Vehicle):
    def __init__(self, name, batteryType, color, tireSize):
        super().__init__(color, tireSize)
        self.name = name
        self.batteryType = batteryType

    def printCarInfo(self):
        print(f'{self.name}:\nBattery Life: {self.batteryType}\n')
        self.printVehicleInfo()
        return self