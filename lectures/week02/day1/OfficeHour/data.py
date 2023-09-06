# Reminders
# [] call the item by it's index - [0] or [i]
# {} call the item by it's key - ['keyName']

school = [
    {
        id: 1,
        "class": "Web Fundamentals",
        "instructor": "Stephanie",
        "students": [
            {
                id: 1,
                "firstName": "Jane",
                "lastName": "Doe",
                "grades": [
                    {
                        "quarter": 90
                    },
                    {
                        "quarter": 60
                    },
                    {
                        "quarter": 95
                    },
                    {
                        "quarter": 80
                    },
                ]
            },
            {
                id: 2,
                "firstName": "Bob",
                "lastName": "Ross",
                "grades": [
                    {
                        "quarter": 70
                    },
                    {
                        "quarter": 80
                    },
                    {
                        "quarter": 65
                    },
                    {
                        "quarter": 80
                    },
                ]
            },
            {
                id: 3,
                "firstName": "John",
                "lastName": "Smith",
                "grades": [
                    {
                        "quarter": 90
                    },
                    {
                        "quarter": 75
                    },
                    {
                        "quarter": 100
                    },
                    {
                        "quarter": 80
                    },
                ]
            }
        ],
        "languagesFrameworks": [
            "HTML",
            "CSS",
            "JavaScript",
            "LESS",
            "Python",
            "Java",
            "Django",
            "Flask"
        ],
        "family": [
            {
                "spouse": "Josh",
                "children": {
                    "biological": [
                        {
                            "name": "Josh JR",
                            "info": [
                                {
                                    "age": 16,
                                    "grade": "10th",
                                }
                            ]
                        }
                    ],
                    "Step": [
                    ]
                }
            }
        ]
    },
    {
        id: 2,
        "class": "Python",
        "instructor": "Melissa",
        "students": [
            {
                id: 4,
                "firstName": "Barbara",
                "lastName": "Doe",
                "grades": [
                    {
                        "quarter": 70
                    },
                    {
                        "quarter": 70
                    },
                    {
                        "quarter": 75
                    },
                    {
                        "quarter": 80
                    },
                ]
            },
            {
                id: 5,
                "firstName": "James",
                "lastName": "Ross",
                "grades": [
                    {
                        "quarter": 50
                    },
                    {
                        "quarter": 90
                    },
                    {
                        "quarter": 85
                    },
                    {
                        "quarter": 80
                    },
                ]
            }
        ],
        "languagesFrameworks": [
            "HTML",
            "CSS",
            "JavaScript",
            "LESS",
            "Python",
            "Java",
            "React",
            "Express",
            "Pug",
            "Vite",
            "Django",
            "Flask"
        ],
        "family": [
            {
                "spouse": "Nick",
                "children": {
                    "biological": [
                        {
                            "name": "Shannon",
                            "info": [
                                {
                                    "age": 20,
                                    "grade": "College",
                                }
                            ]
                        },
                        {
                            "name": "Aiden",
                            "info": [
                                {
                                    "age": 16,
                                    "grade": "JR"
                                }
                            ]
                        }
                    ],
                    "Step": [
                        {
                            "name": "Nathan", 
                            "info": [
                                {
                                    "age": 17,
                                    "grade": "JR"
                                }
                            ]
                        },
                        {
                            "name": "Hayden",
                            "info": [
                                {
                                    "age": 15,
                                    "grade": "9th"
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
]

# Test prints start with the whole list, then go 1 layer in, then another, till you reach the inner most layer
# print(school)
# print(school[0])
# print(school[0]['class'])
# print(school[0]['students'])
# print(school[0]['students'][1])
# print(school[0]['students'][1]['firstName'])
# print(school[0]['students'][1]['grades'])
# print(school[0]['students'][1]['grades'][1])
# print(school[0]['students'][1]['grades'][1]['quarter2'])


# Print a Student from Stephanie's class
for s in school:
    if s['instructor'] == "Stephanie":
        print("Stephanie's student name", s['students'][1]['firstName'])


# Print the grades for a student in Melissa's class
for s in school:
    if s['instructor'] == "Melissa":
        print("Melissa's students' grades", s['students'][1]['grades'])


# Calculate and print the GPA for a Student in Stephanie's class
for s in school:
    if s['instructor'] == "Stephanie":
        theGrades = s['students'][1]['grades']
        sum = 0
        dividend = len(theGrades)
        for g in theGrades:
            sum = sum + g['quarter']
            print(sum)
        avg = sum/dividend
        print("gpa for a student in Stephanie's class", avg)
# line 1 = looping through the school list
# line 2 = finding stephanie's class
# line 3 = pulling just the list of grades for her students
# line 4 = creating var for sum
# line 5 = creating var for number of grades to divide by
# line 6 = looping though all the grades
# line 7 = pulling each grade value and adding it to sum
# line 8 = printing sum to check it is adding
# line 9 =  outside loop finding average by diving the total sum by the length
# line 10 = printing the final value of avg


# Calculate and print the GPA for all of the students in Melissa's class



# Print the 3rd language that Stephanie knows
for s in school:
    if s['instructor'] == "Stephanie":
        print(s['languagesFrameworks'][2])


# Print the names of Melissa's Children
for s in school:
    if s['instructor'] == "Melissa":
        names = []
        bio = s['family'][0]['children']['biological']
        step = s['family'][0]['children']['Step']
        print(s['family'][0]['children'])
        print(s['family'][0]['children']['biological'][0]['name'])
        for b in bio:
            print(b['name'])
            # names.append(b['name'])
            names += [b['name']]
        for s in step:
            names.append(s['name'])


# Print the names and ages of Stephanie's children
for s in school:
    if s['instructor'] == "Stephanie":
        names = []
        bio = s['family'][0]['children']['biological']
        step = s['family'][0]['children']['Step']
        print(s['family'][0]['children'])
        print(s['family'][0]['children']['biological'][0]['name'])
        if bio:
            for b in bio:
                print(b['name'])
                # names.append(b['name'])
                names += [b['name']]
        else: 
            print('no biological kids')
        if step:
            for s in step:
                names.append(s['name'])
        # else:
        #     print('no step kids')
# line 1 = looping through school data
# line 2 = if the instructor is stephanie continue
# line 3 = creating a list to contain the names of children
# line 4/5 = since there are 2 dictionaries inside stephanies children dictionary we made to vars for us to loop through
# line 7/11 = if data is returned for the biological/step  list the move to the directions
# if there was data then loop through each of the lists created in line 4/5 and then append the names to the list