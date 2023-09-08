trainingSchool = [
    {
        'id': 1,
        "className": "Eating right with Jane",
        "trainer": {
            'id': 1,
            "firstName": "Jane",
            "lastName": "Doe",
            "skills": [
                {
                    'id': 1,
                    "skillName": "Nutrition"
                },
                {
                    'id': 2,
                    "skillName": "Agility"
                }
            ]
        },
        "petsInClass": [
            {
                'id': 2,
                "name": "Bear",
                "breed": "Mixed",
                "species": "Dog",
                "gender": "Male",
                "age": 7,
                "owner": {
                    'id': 1,
                    "firstName": "Melissa",
                    "lastName": "Longenberger"
                }
            },
            {
                'id': 3,
                "name": "Copper Tone",
                "breed": "Beagle",
                "species": "Dog",
                "gender": "Male",
                "age": 1,
                "owner": {
                    'id': 1,
                    "firstName": "Melissa",
                    "lastName": "Longenberger"
                }
            }
        ]
    },
    {
        'id': 2,
        "className": "Jumping Basics",
        "trainer": {
            'id': 2,
            "firstName": "John",
            "lastName": "Smith",
            "skills": [
                {
                    'id': 2,
                    "skillName": "Agility"
                }
            ]
        },
        "petsInClass": [
            {
                'id': 1,
                "name": "Butch",
                "breed": "Boxer",
                "species": "Dog",
                "gender": "Male",
                "age": 3,
                "owner": {
                    'id': 2,
                    "firstName": "Bob",
                    "lastName": "Ross"
                }
            }
        ]
    },
    {
        'id': 3,
        "className": "Advanced Jumping",
                "trainer": {
            'id': 2,
            "firstName": "John",
            "lastName": "Smith",
            "skills": [
                {
                    'id': 2,
                    "skillName": "Agility"
                }
            ]
        },
        "petsInClass": [

        ]
    },
    {
        'id': 4,
        "className": "Kruisin Kaninies",
        "trainer": {
            'id': 1,
            "firstName": "Jane",
            "lastName": "Doe",
            "skills": [
                {
                    'id': 1,
                    "skillName": "Nutrition"
                },
                {
                    'id': 2,
                    "skillName": "Agility"
                }
            ]
        },
        "petsInClass": [
            {
                'id': 3,
                "name": "Copper Tone",
                "breed": "Beagle",
                "species": "Dog",
                "gender": "Male",
                "age": 1,
                "owner": {
                    'id': 1,
                    "firstName": "Melissa",
                    "lastName": "Longenberger"
                }
            },
            {
                'id': 4,
                "name": "Lady",
                "breed": "Mixed",
                "species": "Dog",
                "gender": "Female",
                "age": 2,
                "owner": {
                    'id': 3,
                    "firstName": "Bill",
                    "lastName": "Ross"
                }
            }
        ]
    }
]


# Reminders
# [] call the item by it's index - [0] or [i]
# {} call the item by it's key - ['keyName']


# print('#1: Whole List:', trainingSchool)

# print('#2: 1 Dictionary inside the list:', trainingSchool[0])
two = trainingSchool[0]

# print('#3: 1 key containing Dictionary:', two['trainer'])

three = two['trainer']

# print('#3a: 1 key containing list:', two['petsInClass'])

threeA = two['petsInClass']

# print('#4: 1 key containing list:', three['skills'])

four = three['skills']

# print('#4a: 1 dictionary in list:', threeA[1])

fourA = threeA[1]

# print('#5: 1 dictionary inside list:', four[1])

five = four[1]

# print('#5a: 1 key in containing Dictionary:', fourA['owner'])

fiveA = fourA['owner']

# print('#6: 1 key in dictionary:', five['skillName'])

six = five['skillName']

# print('#6a: 1 key in dictionary:', fiveA['lastName'])

sixA = fiveA['lastName']


# I want to print the class names that 1 trainer teaches (John Smith)

janesStudentsByClass = []
# whole school
for s in trainingSchool:
    # print('each loop in school', s)
    if 'Jane' in s['trainer']['firstName']:
        # print('yes')
        if 'Doe' in s['trainer']['lastName']:
            # print('yes')
            print('class name', s['className'])

for s in trainingSchool:
    # print('each loop in school', s)
    if 'Jane' in s['trainer']['firstName']:
        # print('yes')
        if 'Doe' in s['trainer']['lastName']:
            # print('pets', s['petsInClass'])
            for p in s['petsInClass']:
                print('p', p['name'])
                c = {s['className']: p['name']}
                janesStudentsByClass.append(c)
print(janesStudentsByClass)
