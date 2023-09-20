class Player:
    def __init__(self, name):
        self.name = name
        self.strength = 100
        self.health = 100
        self.inventory = []
        self.score = 0
        self.char = ''

    def printPlayer(self):
        print(f'{self.name}\nStrength: {self.strength}\nHealth: {self.health}\nScore: {self.score}')
        return self