from .bumperCar import *
from .monsterTruck import *
from games.extras.functions import *

class Event:
    def __init__(self, eventName):
        self.eventName = eventName
    
    # player01 and player02 - determined before game choice
    # players can chose or make characters
    # Universal Methods
    def eventAgenda(self, player01, player02):
        print(f'For tonights agenda {player01.name} will be going against {player02.name} in a winner takes all match')
        delay(1)
        print(f'A test of wills where {player01.name} as {player01.char.name} faces {player02.name} as {player02.char.name}.')
        return self


    # MTvsBC Game Methods


    
    # Animal Mayhem Methods