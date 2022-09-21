myList = [1,2,3,4,5,6,7]
print(myList)

#INSERT
print("**************************")
myList.insert(0,11)
myList.insert(4,44)
myList.insert(6,66)
print(myList)

#APPEND
print("**************************")
myList.append(99)
print(myList)

#EXTEND
print("**************************")
new=[8,9,10,11,12,13]
myList.extend(new)
print(myList)