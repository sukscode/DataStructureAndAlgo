shoppingList = ['Milk','Cheese','Butter']
print(shoppingList[0])
print(shoppingList[1])
print(shoppingList[2])

#PRINT IN REVERSE ORDER
print("**************************")
print(shoppingList[-1])
print(shoppingList[-2])
print(shoppingList[-3])

#FIND
print("**************************")
print('Milk' in shoppingList)
print('milk' in shoppingList)

#TRAVERSE
print("**************************")
def travese(list):
    for i in list:
        print(i)
travese(shoppingList)

#UPDATE
print("**************************")
shoppingList[2] = 'COFFEE'
print(shoppingList)