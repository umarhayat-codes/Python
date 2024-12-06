# print("line 1")
# print("line 2")
# def hide():
#     print("line 3")
#     print("line 4")
# print("line 5")
# def show():
#     print("line 6")
# hide()
# print("line 7")
# show()

# def add():
#     a=3
#     b=4
#     rexult=a+b
#     print(rexult)
# add()

# Postion Argument or require
# def add(a,b):
#     result=a+b
#     print(result)
# add(4,5,6)
# add(3)

# Default argument
# def add(a,b=2,c=4):
#     result=a+b+c
#     print(result)
# add(3,4)

# return keyword
# def sum(a,b):
#     c=a+b
#     # print(c)
#     return c
# result=sum(2,4)
# output=sum(result,3)
# output=sum(sum(2,4),3)
# print(output)
# print(sum(sum(2,4),3))
# print(sum(sum(2,sum(2,3)),3))
# # print(result)


# local & global scope variable

# user="umar"
# user="hayat"
# def add(a,b):
#     c=a+b
#     c=19
#     print(c)
# print(c)
# add(3,4)
# print(user)
# def sum(a,b):
#     c=a+b
#     print(c)

# c=15
# def sum(a,b):
#     print(c)        # error
#     c=a+b
#     print(c)        # print value 7
#     return c
# d=sum(3,4)
# print(c)        # print value 15

user="umar"
def add():
    print(user)
   
add()