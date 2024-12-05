# print("Hello, World:")      # i want to print many time
# While loop
# n=1
# print("Before while")
# while n<=5:
#     print("Hollo ,World:")
#     n+=1
# print("Before while")

# n = 1
# print("Before While Loop")
# while n <= 5:
#     print("Hello, World: ")
#     n += 1
# print("Before While Loop")

# n = 1
# while n < 10:
#     print(n)
#     n += 1

fruits = ["apple", "banana", "cherry"]

i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


# Table printing

# num=int(input("ENter a number for table printing: "))
# n=1
# while n<=20:
#     print(num, "*",n,"=",n*num)
#     n+=1


# num=int(input("ENter a number for table printing: "))
# length=int(input("Enter the lenght: "))
# n=int(input("Enter start point: "))
# while n<=length:
#     print(num, "*",n,"=",n*num)
#     n+=1


# chapter 06

# print 1 to 10
# n=1
# while n<=10:
#     print("n is: ",n)
#     n+=1


# sum five number
# n=1
# sum=0
# while n<=5:
#     print(n)
#     sum=sum+n
#     n+=1
# print("sum is: ",sum)

# display square of five digit
# n=1
# while n<=5:
#     print(n,"square of n is: ",n*n)
#     n+=1
    
# add three digit number    
# sumOfdigit=0
# num=int(input("ENter the three digit number: "))
# while num!=0:
#     digit=num%10
#     sumOfdigit=sumOfdigit+digit
#     num=num//10
# print("The sum of digit iss: ",sumOfdigit)


# list1=[10,20,30,40,50]
# list2=[]
# i=0
# while i<len(list1):
     
#     list2.append(list1[i]*2)
#     i+=1
# print(list2)


list1=[2,3,4,5,6,7,8,43,54,65,73,97,51]
# i=0
# while i<len(list1):
#     if list1[i]%2==0:
#         print("even: ",list1[i])
#     else:
#         print("odd",list1[i])
#     i+=1
    
    
# evenCount=0
# oddCount=0
# i=0
# while i<len(list1):
#     if list1[i]%2==0:
#         evenCount+=1
#     else:
#         oddCount=oddCount+1
#     i+=1
# print("the even number is: ",evenCount)
# print("the odd number is: ",oddCount)

evenSum=0
oddSum=0
i=0
while i<len(list1):
    if list1[i]%2==0:
        evenSum=evenSum+list1[i]
    else:
        oddSum=oddSum+list1[i]
    i+=1
print("sum of even isS:",evenSum)
print("sum of odd isS:",oddSum)


    
