# Reminders
# [] call the item by it's index - [0] or [i]
# {} call the item by it's key - ['keyName']

grades =[
    {
        "quarter01": 90,
        "quarter02": 60
    },
    {
        "quarter01": 60,
        "quarter02": 90,
    },
    {
        "quarter01": 95,
        "quarter02": 80
    },
    {
        "quarter01": 80,
        "quarter02": 80
    },
]
print("#1", grades)
print("#2", grades[0])
print("#3a", grades[0]['quarter01'])
print("#3b", grades[0]['quarter02'])

for g in grades:
    print(g['quarter01'], g['quarter02'])