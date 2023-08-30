# JS comparing
print('I am the same as a console.log in javascript')

x = 'Whats up'
x = 'No really whats up'
print(x)


# Empty Function
def addMe():
    pass


# Data types
iAmBoolean = True

iAmNumber = 24

iAmString = "String"


# Tuples
iAmTuple = (24, 'Favorite Number', True)
print(iAmTuple[1])

# iAmTuple[1] = 'Testing'


# Lists
iAmList = ['Age', 'Old', True, 45]
print(iAmList[2])
iAmList[2] = 'Ancient'
# iAmList[4] = 'Halloween Baby'
iAmList.append('Halloween Baby') # append always adds to the end
iAmList.append('Ancient')
iAmList.pop() # pop always takes from the end
iAmList.insert(2, 'Hey Class') # inserting the string into the index indicated and pushes the rest up and index
iAmList.remove('Ancient') # removes the item listed in the ()


# Dictionaries

owner = {"name": "Melissa", "age": 45, "location": "Berwick, PA"}
print(owner['location'])

location = owner['location']
name = owner['name']
print('the owners location is', location)
print('the owners location is '+location)
print(f'The owners location is {location}')
print('the owners name is {} and the location is {}'.format(name, location))


x = 10
# x = 5
# x = 6
if (x < 5):
    print(True)
else:
    print(False)

y = 9

if (y < 10):
    print("y is less than 10") #if true print me
elif (y < 5):
    print("y is less than 5") # if above is false but i am true print me
else:
    print("no if statement was true") # if none are true then print me


for i in iAmList:
    print(i)