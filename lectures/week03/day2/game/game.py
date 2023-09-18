import time
import random
from os import system, name

from classes.event import *
from classes.bumperCar import *
from classes.monsterTruck import *
from classes.vehicle import *
from classes.player import *
from extras.messages import *
from extras.functions import *

playing = True


while playing:
    message = str(input(welcome))
    player = Player(message)
    message = input(f'\nWelcome, {player.name}!\nWould you like to play a game?\nY/N\n')
    message = message.split()
    if message[0] == 'n' or message[0] == 'N':
        message = print(noGame)
        playing = False
    else:
        message = input(f"\nThat great it's going to be fun!\nBy the way do you know where that line is from?\nY/N\n")
        if message[0] == 'n' or message[0] == 'N':
            message = print(noRef)
            playing = False
        else:
            message = print(yesRef)
            playing = False
