from .kingdom import *
class Animal(AnimalKingdom):
    def __init__(self, name, appendages, size, classification):
        super().__init__(classification)
        self.name = name
        self.appendages = appendages
        self.size = size
