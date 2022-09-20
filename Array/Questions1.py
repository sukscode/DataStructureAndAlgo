#1.create an array and traverse
from array import *
print("***Step1***")
arr1 = array('i',[1,2,3,4,5,6,7,8,9,10])
print(arr1)
def traverse(array):
    for i in array:
        print(i)

traverse(arr1)

#2.Access individual elements
print("***Step2***")
def access(array,index):
    if index > len(array):
        return 'Array out of bound'
    else:
        print(array[index])
access(arr1,2)            

#Append
print("****Step3***")
arr1.append(0)
print(arr1)

#Insert
print("***Step4***")
arr1.insert(10,11)
arr1.insert(11,12)
print(arr1)

#Extend
print("***Step5***")
arr2=array('i',[13,14,15])
arr1.extend(arr2)
print(arr1)

#Fromlist
print("***Step6***")
temp = [11,18,19]
arr1.fromlist(temp)
print(arr1)

#remove
print("***Step7***")
arr1.remove(18)
print(arr1)

#Pop
print("***Step8***")
arr1.pop()
print(arr1)

#Index
print("***Step9***")
print(arr1.index(0))

#Reverse
print("***Step10***")
arr1.reverse()
print(arr1)

#Memory info
print("***Step11***")
print(arr1.buffer_info())

#Count(occurence of particular element)
print("***Step12***")
print(arr1.count(11))

#array to List
print("***Step13***")
temp1 = arr1.tolist()
print(temp1)

#Slice
print("***Step14***")
print(arr1[0:5])