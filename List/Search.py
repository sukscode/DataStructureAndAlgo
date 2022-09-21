myList=[10,20,30,40,50,60,70,80,90]

#IN OPERATOR
print("**************************")
if 20 in myList:
    print(myList.index(20))
else:
    print("NOT FOUND")  

print("**************************")
if 100 in myList:
    print(myList.index(100))
else:
    print("NOT FOUND")    

#LINEAR SEARCH
print("**************************")
def search(list,value):
    for i in list:
        if i == value:
         return list.index(value)
    return 'NOT FOUND'
print(search(myList,90))
print(search(myList,1000))
       
