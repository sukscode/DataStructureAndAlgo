from array import *

arr1 = array('i',[1,2,3,4,5])
print(arr1)
arr1.insert(4,4)
arr1.insert(2,2)
arr1.insert(9,9)
arr1.insert(0,0)
print(arr1)

def traversearray(array):
    for i in array:
        print(i)

#print(traversearray(arr1))

def accessElement(array,index):
    if index > len(array):
        print('out of bound')
    else:
        print(array[index])
accessElement(arr1,4)
