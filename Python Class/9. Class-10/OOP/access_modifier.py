# Acess Modifier mean that define accessbility of class attribute and method

# Public as by default and access outside class

# class Employee:
#     pass
# a = Employee()
# a.name = "umar"
# print(a.name)


# Private is start with __ and access not outside class 

# class Employee:
#     def __init__(self):
#         self.__name = "umar"
# a = Employee()
# print(a.__name)
# print(a._Employee__name)

# Private is start with _ and access in class or subclass 

# class MyClass:
#     def __init__(self, value):
#         self._protected_value = value
    
#     def _protected_method(self):
#         return self._protected_value

# class SubClass(MyClass):
#     def access_protected(self):
#         return self._protected_method()

# obj = SubClass(20)
# print(obj._protected_value)  # Accessing protected attribute (not recommended)
# print(obj.access_protected())  # Accessing protected method via subclass

class Student:
    def __init__(self):
        self._name = "umar"
    def _fullName(self):
        return "Umar Hayat"
class Subject(Student):
    def accessProtect(self):
        return self._fullName()

obj1 = Student()
obj2 = Subject()
print(obj1._name)
print(obj1._fullName())
print(obj2._name)
print(obj2._fullName())
print(obj2.accessProtect())