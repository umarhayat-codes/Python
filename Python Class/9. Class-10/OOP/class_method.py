# Class Method
# first parameter cls and  allows it to access and modify class state that applies across all instances of the class 
# they can access and modify class-level attributes and methods


# class Employee:
#     company = "Apple"           # class variable
#     def show(self):
#         print(f"The name is {self.name} and {self.company}") 
#     @classmethod       
#     def changeCompany(cls, changeCompany):     # 1 para is cls and access it with class variable
#         cls.company = changeCompany

    
# e1 = Employee()
# e1.name = "umar"
# e1.show()
# print(Employee.company)
# Employee.changeCompany("Tesla")   # call with class name or object 
# e1.show()
# print(Employee.company)


# class MyClass:
#     class_attribute = 'class_attr'

#     def __init__(self, instance_attribute):
#         self.instance_attribute = instance_attribute

#     def regular_method(self):
#         return f'Regular method: instance attribute = {self.instance_attribute}'

#     @classmethod
#     def class_method(cls):
#         return f'Class method: class attribute = {cls.class_attribute}'

# # Create an instance of MyClass
# obj = MyClass('instance_attr')

# # Calling regular method
# print(obj.regular_method())

# # Calling class method
# print(MyClass.class_method())


# example

# class Employee:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#     @classmethod
#     def fromString(cls, empValue):
#         name,age,salary = empValue.split("-")
#         return cls(name,age,salary)

# emp = Employee.fromString("umar-20-2000")
# print(emp.name,emp.salary,emp.age)




# class Employee:
#     company = "apple"
#     def show(self):
#         print(f"Employee is {self.name} by {self.company}")
#     @classmethod
#     def changeCompany(cls,name):
#         cls.company = name
    
# e1 = Employee()
# e1.name = "umar"
# e1.show()
# print(e1.company)
# print(Employee.company)
# e1.changeCompany("Tesla")
# e1.show()
# print(e1.company)
# print(Employee.company)


# class Student:
#     totalStudent = 0
#     def __init__(self,name, age):
#         self.name = name    
#         self.age = age    
#         Student.totalStudent += 1
#     @classmethod    
#     def noOfStudent(cls):
#         return cls.totalStudent

# stu1 = Student("umar", 23)
# stu2 = Student("hayat", 20)
# print(stu2.totalStudent)
# print(Student.totalStudent)
# print(stu1.noOfStudent())


# class Employee:
#     minAge = 10
#     @classmethod
#     def isValidAge(cls,age):
#         return age > cls.minAge
    
# print(Employee.isValidAge(29))
# print(Employee.isValidAge(9))


class Config:
    debug = False
    # @classmethod
    def enable(cls):
        cls.debug = True
    # @classmethod
    def disable(cls):
        cls.debug = False

c1 = Config()
print(Config.debug)
c1.enable()
print(Config.debug)
c1.disable()
print(Config.debug)


