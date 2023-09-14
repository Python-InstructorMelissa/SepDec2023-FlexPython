# class is always lower case class Name is always Upper case
class Park:
    def __init__(self, parkName, location):
        self.parkName = parkName
        self.location = location


class Animal(Park):
    # AKA Constructor - Attributes - Describe the instance that we will create
    # in the __init__() goes the required attributes
    def __init__(self, name, species, appendages, classification, diet, parkName, location):
        super().__init__(parkName, location)
        self.name = name
        self.species = species
        self.appendages = appendages
        self.classification = classification
        self.diet = diet
        # These are  not added to the declaration because they are predetermined
        self.willToLive = True
        self.sound = ''
        self.isDead = False

    def printAnimal(self):
        print(f'{self.name} is a {self.species} of the class {self.classification}.\n{self.name} has {self.appendages} Appendages and eats {self.diet}.\n{self.name} is currently living at the {self.parkName} in {self.location}\nWill to live: {self.willToLive}\nIs Dead: {self.isDead}')
        return self

    def feedAnimal(self):
        if self.isDead == False:
            print(f'{self.name}, ate, {self.diet}, and has lived to see another day')
        else:
            print(f'{self.name} has passed away')
        return self
    
    def refusedToEat(self):
        if self.isDead == False:
            print(f'{self.name} has refused to eat {self.diet} and thusly has passed away\n{self.name} has officially canceled their subscription to the game of life')
            self.willToLive = False
            self.isDead = True
            return self
        else:
            print(f"{self.name} is already dead so how can they refuse to eat...oh wait it's a zombie")
            return self
    
    def makeNoise(self, noise):
        if self.isDead == False:
            self.sound = noise
            print(f'{self.name} loves to {self.sound}')
        else:
            print(f'{self.name} has passed away')
        return self
    
    def playDate(self, other, confirmation):
        print(f'{self.name} wants to go on a play date with {other.name}')
        if self.location != other.location:
            print(f'They live at different parks and can not play at this time')
            return self
        if self.isDead == True:
            print(f'However {self.name}, has passed away so this can not be their request')
            return self
        if other.isDead == True:
            print(f'However {self.name} is saddened to learn that {other.name} has passed away')
            return self
        else:
            if self.classification != other.classification:
                print(f'However {self.classification} and {other.classification} are unable to play together safely')
            if self.species != other.species:
                if self.species == "Canine" or other.species == "Canine":
                    if confirmation == "Yes":
                        print(f'They will play a nice game but only once')
                if self.species == "Feline" or other.species == "Feline":
                    if confirmation == "Yes":
                        print(f'Someone is going to get scratched up')
                if self.species == "Panda" or other.species == "Panda":
                    if confirmation == "Yes":
                        print(f'No playing will happen but they will both get drunk on Bamboo') 
            if confirmation == "Yes":
                if self.classification == "Insect":
                    self.isDead = True
                    print(f'They chose to play anyways and tragedy has struck, and {self.name} has passed away')
                    return self
                if other.classification == "Insect":
                    other.isDead = True
                    print(f'They chose to play anyways and tragedy has struck, and {other.name} has passed away')
                    return self
            else:
                print(f'They have a great time')
                return self


class Product:
    def __init__(self, prodName, cost, producer):
        self.prodName = prodName
        self.cost = cost
        self.producer = producer

    def printProd(self):
        print(f'{self.prodName} is {self.cost}\nThis is produced by {self.producer.name}')
        return self


# Creating Park Instances
# bronx = Park("Bronx Zoo", "NYC, NY")
# sd = Park("San Diego Zoo", "San Diego, CA")

# Creating Instances of Animals
cat = Animal("Whiskers", "Feline", 5, "Mammal", "Cat Food", "Bronx Zoo", "NYC, NY")
bee = Animal("Lily", "HoneyBee", 6, "Insect", "Nectar", "Bronx Zoo", "NYC, NY")
panda = Animal("Jason", "Panda", 4, "Mammal", "Bamboo", "Bronx Zoo", "NYC, NY")
tom = Animal("Tom", "HoneyBee", 6, "Insect", "Nectar", "Bronx Zoo", "NYC, NY")
dog = Animal("Rocky", "Canine", 5, "Mammal", "Dog Food", "San Diego Zoo", "San Diego, CA")
koala = Animal("Fito", "Koala", 4, "Mammal", "Leaves",  "San Diego Zoo", "San Diego, CA")

# Creating Product
honey = Product("Honey", 20, bee)

honey.printProd()


# cat.printAnimal().feedAnimal()
# tom.printAnimal().refusedToEat().printAnimal()
# panda.playDate(cat, "Yes")
# cat.feedAnimal()
# cat.makeNoise("Purr")
# cat.feedAnimal().makeNoise("Purr")

# cat.playDate(bee, "Yes")
# panda.playDate(bee, "Yes")
# bee.playDate(cat, "Yes")


# 1:1 = one user has one ssn  - one wife one husband
# 1:M = one husband many wives = cheater
# M:M = swingers club