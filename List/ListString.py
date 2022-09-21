a='spam'
b=list(a)
print("**************************")
print(b)

#SPLIT
print("**************************")
a='spam1 spam2 spam3'
b=a.split()
print(b)
print("**************************")
c='spam1-spam2-spam3'
delimiter='-'
d=c.split(delimiter)
print(d)
print("**************************")
e='spam1-spam2-spam3'
dem='s'
f=e.split(dem)
print(f)

#JOIN
print("**************************")
print(dem.join(f))

a=[1,2,3,4,5,6,7,8,9]
print(a[::2])
a=[1,2,3,4,5]
print(a[3:0:-1])