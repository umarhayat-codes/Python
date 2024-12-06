# # it execute top to bottom
# print("line 1")
# print("line 2")
# print("line 3")
# print("line 4")
# print("line 5")

# # Break by default execution and execute again  & again 
# # control flow of execution 
# # so we learn new control is called def mean funtion
# # we use indention to make block of control
# # if we use no indention then we remove control
# # we can make block using tab
# # main reson  to make reuseability
# print("line 1")
# print("line 2")
# def hide():                         # def is control in which down tab is add it stat cannot exe normal flow
#     print("line 3")                 # it is part of control
#     print("line 4")             
# print("line 5")                     # it no under control
#     # print("line 6")                 # it control end if indentation is use after remove indentation so we use now make def
# hide()                      # it return def and is use to call control if all stat exe then it will remain return
# print("line 7")
# def show():
#     print("line 8")
#     print("line 8")
#     print("line 8")
# show()                   # it return def and is use to call control if all stat exe then it will remain return
# print("line 9")

# function calling up we called function defination
# def add():
#     a=4
#     b=5   
#     result=a+b
#     print(result)      # it can exe if no call def
# add()              # we cannot use it again and again
# #  we want to sum deff no
# # so leaun nwe thing 
# add(3,4)            # so add() can carry out value and it cannot exe because it cannot receieve

# # posittional argument or require argument

# def add(a,b):          # Which is recieve value called parameter
#     print("a->",a,"b->",b)
#     result=a+b
#     print(result)
# add(20,25)             # Which is carry out value called argument
# add(13,26)  
# # if parameter 2 then argument is 2
# # if argumenet is less or greater than parameter then erroe is coming
# #  is called posittional argument or require argument

# # Default Argument 
# # if parament is add after default then is coming erroe
# def add(a,b,c=4,d):          # if argument is less than paramenter then get default value
#     print("a->",a,"b->",b)
#     result=a+b+c+d
#     print(result)
# add(20,25,4)             
# add(13,26,3)                # if argumetn is pass then it is not carry out default value



# Return keyword in function
# Return keyword can be return any data type

def add(a,b):
    c=a+b
    # print(c)      # I want to print it where i am function call
    # return "no date"      # Now it return no data
    return c        
# if we not use return then it print none
# return is keyword which is use in fnuction so that value send or print in function calling or value store in function calling
result=add(10,20)
print(result)
# we can also write it
print(add(10,20))       # it which value return i am not store it variable i am print directly
print(add(add(10,20),10))
print(add(add(10,add(10,5)),10))        # 55 answer
#if we use not result variable
output=add(add(10,20),10)
# return keyword is used for further calculate value
output=add(result,100)
print(output)
# one functuon only return value only one because konsi value print ho
def sum(a,b):
    c=a+b
    return c
    d=a+b/c         # now it isno access able
    return d
print(sum(10,20))

# use of return 
# we can use return in variable and use for store in vari for further calculation
# we can use anyfunction for give input


def sum(a,b):
    c=a+b   # if we not use return then value cannot return in function calling
print(sum(2,4))
print(sum())     

# Local and Global scope variable
# whish variablae we is make inside body of function is called local scope variable
 
def sum(a,b):
    c=a+b
# if we print variable then error caming that variable cannot define
print(c)
