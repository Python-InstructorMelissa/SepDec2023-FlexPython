task = [
    {'id': 1, 'name': 'wash dishes'},
    {'id': 2, 'name': 'vacuum'},
    {'id': 3, 'name': 'fold clothes'},
    {'id': 4, 'name': 'clean fish tank'},
]

user = [
    {'id': 1, 'firstName': 'Jane', 'lastName': 'Doe'},
    {'id': 2, 'firstName': 'Bob', 'lastName': 'Ross'},
    {'id': 3, 'firstName': 'Artie', 'lastName': 'Smith'},
    {'id': 4, 'firstName': 'Zoe', 'lastName': 'Heart'},
]

class Task:
    def __init__(self,id, name):
        self.id = id
        self.name = name

    def printTask(self):
        print(f'the name of the task is {self.name}')


class User:
    def __init__(self, id, firstName, lastName):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
    
    def printUser(self):
        print(f'{self.firstName} {self.lastName}')

    def sayHi(self, other):
        print(f"{self.firstName} say's hi to {other.firstName}")

    def drives(self, other, another):
        print(f"{self.firstName} drives {other.firstName}'s car into the river, but {another.firstName} buys {other.firstName} a Motorcycle instead")



clean = Task(1,'clean dishes')
eric = User(1, 'Eric', 'Perrigo')
corey = User(2, 'Corey', 'W')
rod = User(3, 'Max', 'Rodriguez')

clean.printTask()
eric.printUser()
eric.sayHi(corey)
corey.drives(eric, rod)