# Different b/w while and for 
# 1. Syntax
# list1=[10,20,30,40,50]
# i=0
# while i<len(list1):
#     print("while-loop: ",list1[i],"and i = ",i)
#     i+=1


# for is use for list iterate only 
# for is closed than while   
# list1=[10,20,30,40,50]   
# for item in list1:
#     print(item)

fruits = ["apple", "banana","mango", "cherry"]
for i in fruits:
    print(i)   
    if (i == "mango"):
        break

# for i in range(5):
#     print(i)

# for i in range(3):
#     print("Hello, World: ")

# if not list then while use but we use for 
# list1=list(range(0,10,2))
# for item in list1:
#     print(item)
    
# for item in range(0,10,2):
#     print(item)

# display index
list1=["umar","hayat","zain","ashfaq","1234"]
# for item in range(0,len(list1)):
#     print("index: ",item,"value: ",list1[item])

# enumerte is use for display index with value
# for index, item in enumerate(list1):
#     print(index,item)

# it execute all item in list1
# for index, item in enumerate(list1):
#     print(item,index)
#     if item=="zain":
#         print("find: ")

# if we use break then it's stop after zain
for index, item in enumerate(list1):
    print(item,index)
    if item=="zain":
        print("find: ")
        break
    
        