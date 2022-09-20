import numpy as np 

twoArray = np.array([[11,15,10,19],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoArray)


newArray = np.insert(twoArray,0,[1,2,3,10])
newArray = np.insert(twoArray,0,[4,5,6,10])
print("##############################")
print(newArray)

print("##############################")
def acessElement(array,row,col):
    if row >= len(array) and col >= len(array[0]):
        print("Incorrect index")
    else:
        print(array[row][col])  
acessElement(twoArray,0,1)

print("##############################")
def Travese(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
Travese(twoArray)

print("##############################")
def search(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return (i,j)
    return "Not found"
print(search(twoArray,11))

print("##############################")
newtd = np.delete(newArray,0)
print(newtd)