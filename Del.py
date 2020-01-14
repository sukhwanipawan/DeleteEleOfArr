from array import *
Arr = array('i', [])
l = int(input('What will be the length of Arr'))
for i in range(l):
    x=int(input('Enter a value to append in Arr'))
    Arr.append(x)
print(Arr)
tempArr = array('i', [])
d = int(input('Enter a index number from which you want to delete value of Arr'))
k=0
for i in Arr:
    if k == d:
        pass
    else:
        tempArr.append(i)
    k+=1
print('The new Arr is',tempArr)