from os import system, name
import time
from .messages import *

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def delay(a):
    time.sleep(a)
    return

def exitGame(a):
    delay(a)

def loading(a):
    delay(a)
    delay(a)
    print(stillLoading)
    delay(a)
    delay(a)

def badEntry(a):
    print(badInput)
    delay(a)
    print(badInputExit)
    exitGame(a)

def gameTesting(a):
    print(goodChoice)
    delay(a)
    print(gameNotReady)
    delay(a)
    print(exitGame)
    exitGame(a)