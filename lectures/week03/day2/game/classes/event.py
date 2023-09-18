from .bumperCar import *
from .monsterTruck import *

class Event:
    def __init__(self, eventName):
        self.eventName = eventName

    def eventAgenda(self, player1, player2):
        print(f'For tonights agenda {player1.name} will be going against {player2.name} in a winner takes all match')
        return self

    def theMatch(self, player1, player2):
        self.tireCheck(player1, player2)
        self.fuelCheck(player1, player2)