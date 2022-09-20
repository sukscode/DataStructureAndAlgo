from array import *

arr1 = array('i',[0,1,2,3,4,9])

def searchInArray(array,value):
    for i in array:              #O(n)
        if i == value:           #O(1)
            return array.index(value)   #O(n)
    return 'Value not exist'            #O(1)
print(searchInArray(arr1,9)) 

arr1.remove(3)
print(arr1)