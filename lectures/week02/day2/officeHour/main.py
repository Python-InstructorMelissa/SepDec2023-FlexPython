

x = 'the string'
def string(x):
    for i in x:
        print('theString',i)
string(x)

y = [1,2,3,4,5]
z = ['hello', 'out', 'there']

def thelist(x):
    for i in x:
        print('theList',i)
thelist(y)
thelist(z)

def alist(x):
    for i in x:
        string(i)
alist(z)