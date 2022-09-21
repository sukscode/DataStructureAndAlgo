myList=['a','b','c','d','e','f','g']
print("**************************")
print(myList)
print(myList[0:2])
print(myList[:2])
print(myList[1:])
print(myList[:])
myList[0:2] = ['x','y']
print(myList)

#POP
print("**************************")
print(myList.pop(1))
print(myList)
print(myList.pop())
print(myList)

#DELETE
print("**************************")
newList=['a','b','c','d','e','f','g']
del newList[2]
print(newList)
del newList[2:4]

#REMOVE
print("**************************")
nList=['a','b','c','d','e','f','g']
nList.remove('b')
print(nList)
