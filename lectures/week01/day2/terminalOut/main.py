import time

x = 9
y = 21
z = -5
count = 0

leave =  False

while not leave:
    message  = print('Hello there sports fan.  Welcome to town')
    count = count+1
    time.sleep(2)
    message = print(f'Loop count is {count}')
    time.sleep(2)
    message = print('I do hope that you are doing well today')
    time.sleep(2)
    message = print('Lets play a quick game...to see if you can understand my code')
    time.sleep(2)
    if x <= 10:
        message = print(f'Sorry x seems to be smaller than 10: x = {x}')
        time.sleep(2)
    if y >= 20:
        message = print(f'Looks like y is greater than or equal to 20: y = {y}')
        time.sleep(2)
        if z > 5:
            message = print(f'z is greater than 5: z = {z}')
            time.sleep(2)
            message = print('Oh no the boss lady is hear I must leave now..')
            time.sleep(2)
            leave = True
        else:
            message = print(f'z failed the if condition: z = {z}')
            z = z + 5
            time.sleep(2)
            message = print(f'because z failed the if condition, increasing its value by 5: z = {z}')
            time.sleep(2)