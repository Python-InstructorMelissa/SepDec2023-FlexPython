data = [0,6,12,9,5,14,7,10,2,-4]
# print(len(data))
even = []   # creating a list called even
for i in data: # for loop of the dataset
    if i % 2 == 0: # if current value is even (num / 2 has no remainder)
        even.append(i) # take even list add current value to it

grades = [90,70,80,90]

def avg():
    sum = 0
    count = len(grades)
    for i in grades:
        sum = sum + i
    answer = sum/count
    print(answer)

avg()
# line 10 function start called avg
# line 11 var sum set to 0
# line 12 var count = number of grades
# line 13 start of for loop through grades
# line 14 adding each grade to the previous value of sum
# line 15 var answer is sum / number of grades
# line 16 printing answer
# line 18 calling the function

moreData = [
    {'name': 'John'},
    {'name': 'Jane'},
    {'name': 'Mary'},
    {'name': 'Mike'},
    {'name': 'Bob'},
    {'name': 'Britney'}
]
# print(len(moreData))



evenMoreData = [
    {
        'Stack': 'WebFundamentals',
        'Topic': [
            'HTML', 'CSS', 'JS'
        ]
    },
    {
        'Stack': 'Python',
        'Topic': [
            'Fundamentals', 'OOP', 'SQL', 'Flask noDB', 'Flask DBnoLogReg', 'FullStackFlask', 'Deployment'
        ]
    },
    {
        'Stack': "P&A",
        'Topic': [
            'Solo or Group Project', 'Algos'
        ]
    }
]
print('Version 1',evenMoreData)  # step one to finding the word Deployment is printing whole dataset 
print('Version 2',evenMoreData[1]) # then we move 1 layer in since it is [] we need to use a integer
print('Version 3',evenMoreData[1]['Topic']) # moving another layer in by calling the key because it is {}
print('Version 4',evenMoreData[1]['Topic'][6]) # moving the final layer in and printing Deployment
# [] call the item by it's index
# {} call the item by it's key
for i in evenMoreData:  # looping through same data
    print('This will print the same as Version 2 but all the dict:', i) # prints each dict
    print('all the stack name:', i['Stack']) # prints the value of each Stack (key)
    # print(i['Topic'][1]) # printed all the words at index 1 in the list of topic not just deployment
    # print([0]['Topic'][1]) # errors out because it doesn't know what its looking at
    if i['Stack'] == 'WebFundamentals': # digging in another layer by asking if the stack name is web fun
        print(i['Topic'][1]) # if yes printing CSS but below is best
        for j in i['Topic']: # looping through all the values in topic list
            if j == 'CSS': # if it = CSS
                print(j) # print away