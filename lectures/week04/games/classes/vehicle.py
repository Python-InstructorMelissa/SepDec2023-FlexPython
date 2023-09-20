class Vehicle:
    def __init__(self, color, tireSize):
        self.color = color
        self.tireSize = tireSize
        self.fuelLevel = 100
        self.damage = 0

    def printVehicleInfo(self):
        print(f'Color: {self.color}\nTireSize: {self.tireSize}\nFuel Level: {self.fuelLevel}\nDamage Level: {self.damage}')
        return self

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
    
    def takeDamage(self, num):
        if self.damage < 100:
            self.damage = self.damage + num
            if self.damage > 99:
                self.damage = 100
                print(f'{self.name} has sustained Maximum Damage and is no longer able to fight. Please head to medical tent for healing')
            else:
                print(f'{self.name} has sustained damage and is now at {self.damage}')
        else:
            print(f"I'm sorry {self.name} but you are already at maximum damage please head to the medical tent immediately")
        return self
    
    def tireCheck(self, other):
        if self.tireSize > other.tireSize:
            self.useFuel(20)
            other.useFuel(10)
            other.takeDamage(50)
        if other.tireSize > self.tireSize:
            self.useFuel(10)
            other.useFuel(20)
            self.takeDamage(50)
        else:
            self.useFuel(10)
            other.useFuel(10)
            self.takeDamage(10)
            other.takeDamage(10)
        return self

    def fuelCheck(self, other):
        if self.fuelLevel < 0:
            other.useFuel(20)
            self.takeDamage(30)
        if other.fuelLevel < 0:
            self.useFuel(20)
            other.takeDamage(30)
        else:
            self.useFuel(10)
            other.useFuel(10)
            self.takeDamage(10)
            other.takeDamage(10)
        return self