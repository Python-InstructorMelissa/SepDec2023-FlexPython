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
player01 = False
player02 = False

while playing:
    answer = input(welcome)
    player01 = Player(answer)
    message = print(f'\nWelcome, {player01.name}!')
    delay(2)
    message = input(altPlayer)
    if message[0] == 'n' or message[0] == 'N':
        message = print(noAltPlayer)
        delay(1)
        message = print(ai)
        delay(1)
        message = input(gameQuestion)
    else:
        answer = input(welcome2)
        player02 = Player(answer)
        message = print(f'\nWelcome, {player02.name}!')
        delay(1)
        message = print(ai)
        delay(1)
        message = print(f'{player01.name} and {player02.name} I have another question for you')
        message = input(gameQuestion)
    if message[0] == 'n' or message[0] == 'N':
        message = print(noGame)
        exitGame(1)
        playing = False
    else:
        message = input(yesGame)
        if message[0] == 'n' or message[0] == 'N':
            print(noRef)
            exitGame(1)
            playing = False
        else:
            print(yesRef)
            delay(1)
            print(loadGameMenu)
            delay(1)
            print(imLoading)
            loading(2)
        clear()
        if player02 == False:
            message = print(f'Welcome {player01.name}!!!')
        else:
            message = print(f'Welcome {player01.name} and {player02.name}!!!!')
        delay(2)
        message = input(gameMenu)
        if message[0] == '1':
            gameTesting(1)
        if message[0] == '2':
            gameTesting(1)
        if message[0] == '3':
            gameTesting(1)
        else:
            badEntry(1)
        playing = False
