import time
data = [0,6,12,9,5,14,7,10,2,-4]
moreData = [
    {'name': 'Melissa'},
    {'name': 'Corey'},
    {'name': 'Keith'},
    {'name': 'George'},
    {'name': 'Eric'}
]
print(moreData[0]['name'])
print(data[3])

testing = True
dataCount = 0
moreDataCount = 0
newList = []
loop1Count = 0
loop2Count = 0

while testing:
    for i in data:
        loop1Count = loop1Count+1
        message = print(f'loop1count = {loop1Count}')
        if i > 5:
            newList.append(i)
            # message = print(f'i = {i} and now newList = {newList}')
            # time.sleep(2)
        else:
            dataCount = dataCount+1
            # message = print(f'i = {i} failing the if condition so dataCount = {dataCount}')
            # time.sleep(2)
        for j in moreData:
            loop2Count = loop2Count+1
            print(j['name'])
            # message = print(f'loop2count = {loop2Count}')
            if j['name'] == 'Melissa' or j['name'] == 'Keith':
                newList.append(j['name'])
                # message = print(f'j = {j} and now newList = {newList}')
                # time.sleep(2)
            if j['name'] == 'Melissa':
                newList.append('Geoffrey')
                # message = print(f'j = {j} and now newList = {newList}')
                # time.sleep(2)
            else:
                moreDataCount = moreDataCount+1
                # message = print(f'j = {j} failing the if condition so dataCount = {moreDataCount}')
                # time.sleep(2)
    message = print(f'Final Results: loop1Count: {loop1Count}, loop2Count: {loop2Count}, newList: {newList}')
    testing = False