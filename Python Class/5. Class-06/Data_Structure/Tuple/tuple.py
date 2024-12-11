userName=("umar","xain","ashfaq","mahad","ali")
i=userName[0]
print(i)
print(userName[3])
print(userName[-3])
# Slicing
user=userName[2:4]
print(user)
print(userName[-5,-2])
print(userName[:])
# update
y=list(userName)
y[1]="ahmad"
userName=tuple(y)
print(userName)
# add
a=list(userName)
a.append("jhon")
userName=tuple(a)
print(userName)
b=list(userName)
b.insert(1,"ali")
userName=tuple(b)
print(userName)
# remove
c=list(userName)
c.pop(2)
c.remove("ali")
c.clear()
del c["ali"]
userName=tuple(c)
print(userName)
#packing
userName=("umar","xain","ashfaq")
#unpacking
(a,b,c)=userName
print(a,b,c)        #a="umer",b="zain",c="ashfaq"
userName=("umar","xain","ashfaq","mahad","ali")
(a,b,c*)=userName
pass(a,b,c)         #a="umer",b="zain",c=["ashfaq",mahad,"ali"]

