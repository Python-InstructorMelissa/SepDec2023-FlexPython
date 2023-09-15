from .bumperCar import *
from .monsterTruck import *

class Event:
    def __init__(self, eventName):
        self.eventName = eventName

    def eventAgenda(self, player1, player2):
        print(f'For tonights agenda {player1.name} will be going against {player2.name} in a winner takes all match')
        return self

    def theMatch(self, player1, player2):
        if player1.tireSize > player2.tireSize:
            print(f"{player1.name} crushes {player2.name}")
        if player2.tireSize > player1.tireSize:
            print(f"{player2.name} crushes {player1.name}")
        if player1.tireSize == player2.tireSize:
            if player1.fuelLevel > player2.fuelLevel:
                print(f'{player1.name} wins by default for lack of foresite and lack of fuel on {player2.name} side')
            if player2.fuelLevel > player1.fuelLevel:
                print(f'{player2.name} wins by default for lack of foresite and lack of fuel on {player1.name} side')
        return self