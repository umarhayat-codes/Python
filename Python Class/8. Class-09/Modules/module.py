# from generatetext import userName
# print("Generatetext :",userName)


# from generatetext import firstName 
# print("Funtion call from generatetext",firstName())

# import generatetext
# print("user name: ",generatetext.userName)
# print("function: ",generatetext.firstName())


# import generatetext as gt
# print("user name",gt.userName)
# print("user name function: ",gt.userName())


# Built in module
# from time import time           # for use one function use
# current=time()
# print("the current time: ",current)

# import time
# current=time.sleep(4)
# print("stop execution for 4sec: ",current)


# datetime
# import datetime
# current=datetime.datetime(2024,2,20)
# current=datetime.datetime.now()
# print(current.year,current.second,current.month)
# current=datetime.date.today()
# delta=current+datetime.timedelta(days=5,hours=3,minutes=30,seconds=15)
# delta=current-datetime.timedelta(days=5,hours=3,minutes=30,seconds=15)
# print(delta)
# current=datetime.datetime.now().strftime("%Y-%d-%m-%H-%M-%S")
# print(current)
# date_str="2024-2-20"
# current=datetime.datetime.strptime(date_str,"%y-%m-%d")
# print("date time: ",current)

# from os import getcwd
# currentWorkingDirectory=getcwd()
# print(currentWorkingDirectory)
# from os import listdir
# listDirectory=listdir(currentWorkingDirectory)
# print(listDirectory)
# from os import mkdir
# createDirectory=mkdir("creatDirBy")
# print(createDirectory)
# import os
# new__dir_path=os.path.join(currentWorkingDirectory,"example.txt")
# os.mkdir(new__dir_path)
# print(new__dir_path)

# newFile=os.path.join("example.txt","creatDirBy")
# print(newFile)
# creatFile=os.remove("creatDirByOS")
# print(creatFile)

# Math
# import math
# factorial=math.factorial(4)
# print(factorial)
# sine=math.sin(0)
# print(sine,math.cos(0))
# print(math.sqrt(25),math.log(1))

# random
import random
# float=random.random()
# print(float)
# print(random.randint(100,1000))
seq=[2,3,4,56,7]
# print(random.choice(seq))
print(random.shuffle(seq))