total=0
count=0
while(True):
    inp=input("Enter a number: ")
    if inp == 'done':break
    value = float(inp)
    total = total + value
    count = count + 1
    average=total/count
print("AVERAGE: ",average)


#METHOD2
print("**************************")
myList=list()
while(True):
    inp=input("ENTER A NUMBER: ")
    if inp == 'done':break
    value = float(inp)
    myList.append(value)
    tot=sum(myList)
    cou=len(myList)
    avg = tot/cou
print("AVERAGE: ",avg)