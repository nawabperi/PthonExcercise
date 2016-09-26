
import re
#25
def make(i):
    if i.endswith('ie'):
        inputWord = i.rstrip('ie')
        p = inputWord+'y'+'ing'

    elif i.endswith('e'):
        inputWord = i[:-1]
        p = inputWord+'ing'

    elif i[-2] in 'aiou':
        print(i[-2])
        p = i + i[-1] + 'ing'
        print(p)

    print(str(p))

make('lie')
make('see')
make('move')
make('hug')

#26
list1=[1,2,7,3,4,]
def max_in_list(x):

    return reduce(max,x)
print(max_in_list(list1))

#27
strList=['ab','abc','ahkh','w']
def forloop(x):
    numList=[]
    for i in x:
        numList.append(len(i))
    return numList
print forloop(strList)

def funMAp(x):
