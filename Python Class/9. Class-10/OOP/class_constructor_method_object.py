# class Student:
#     def __init__(self,name):
#         self.name = name
#         self.age = 0
#         self.rollNo = 0 
        
#     def showDetail(self,age,rollNo,father):
#         self.age = age
#         self.rollNo = rollNo
#         print(f"The Student Detail: Name {self.name}, Age {self.age},RollNo {self.rollNo}, Father Name {father}")
    
    
#     def result(self,grade,age,rollNo):
#         self.age = age
#         self.rollNo = rollNo
#         print(f"Result: rollNo {self.rollNo}")



# class Student:
#     def __init__(self,name,age,rollNo):
#         self.name = name
#         self.age = age
#         self.rollNo = rollNo
    
#     def showDetail(self):
#         print(f"Name: {self.name}, Age: {self.age}, RollNo : {self.rollNo}")
    
# name = input("Enter Your Name: ")
# age = int(input("AGE: "))
# rollNo = int(input("RollNo: "))
# student1 = Student(name,age,rollNo)
# student1.showDetail()


# instance variable
# instance variable are variable which is unique of all instance of class and it is define in constructor and profix with self

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# a = Student("umar",20)
# b = Student("hayat",20)
# print(a.name, a.age)
# print(b.name, b.age)

# class variable
# class variable are variable which is same of all instance of class and it is define in outside method and inside class

# class Student:
#     rollNo = 4
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# a = Student("umar",20)
# b = Student("hayat",20)
# print(a.name, a.age, a.rollNo)
# print(b.name, b.age, b.rollNo)




# example 
class Employee:
    totalEmp = 0
    def __init__(self,name,id):
        self.name = name
        self.name = name

