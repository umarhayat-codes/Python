# person and student
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"Hey my name is {self.name} and i am {self.age} year old. ")

# class Student(Person):
#     def __init__(self,name,age,studentId):
#         super().__init__(name,age) 
#         self.studentId = studentId
#     def introduce(self):
#         super().introduce()
#         print(f"My class ID is: {self.studentId}")

# stud1 = Student("umar",18,4)
# stud1.introduce()
        
# vehicle and car      
# class vehicle:
#     def __init__(self,model,make):
#         self.model = model
#         self.make = make
#     def detail(self):
#         print(f"Vehicle: {self.model} and {self.make}")
# class Car(vehicle):
#     def __init__(self,model,make,doors):
#         super().__init__(model,make)
#         self.doors = doors
#     def detail(self):
#         super().detail()
#         print(f"The no.of door {self.doors}")
# kar = Car("Honda","Carmy",5)
# kar.detail()
        
        
# Employee and manager
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def show(self):
#         print(f"Employee:Name is  {self.name} and salary is {self.salary}")

# class Manager(Employee):
#     def __init__(self,name,salary,department):
#         super().__init__(name,salary)
#         self.department = department
#     def show(self):
#         super().show()
#         print(f"Department: {self.department}")
# e1 = Manager("umar",100,"IT")
# e1.show()


# class Account:
#     def __init__(self,account_holder,balance):
#         self.account_holder = account_holder
#         self.balance = balance
#     def display(self):
#         print(f"account holder: {self.account_holder} and balance {self.balance}")
#     def deposit(self,amount):
#         self.balance -= amount
#         print(f"Total Balance: {self.balance}")
# class SavingAcount(Account):
#     def __init__(self, account_holder, balance,interestRate):
#         super().__init__(account_holder, balance)
#         self.interestRate = interestRate
#     def display(self):
#         super().display()
#         print(f"Interest Rate: {self.interestRate}")
#     def calculateInterest(self):
#         interest = self.balance * self.interestRate / 100
#         self.deposit(interest)
    
# acc1 = SavingAcount("umar",100,4)
# acc1.display()
# acc1.calculateInterest()


class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def display(self):
        print(f"Product of {self.name} in {self.price}")
    def calculateDiscount(self,discount):
        self.price -= self.price * discount / 100
        print(f"New Price after discount: {self.price}")
class DiscountProduct(Product):
    def __init__(self, name, price,discount):
        super().__init__(name, price)
        self.discount = discount
    def display(self):
        super().display()
        print(f"Discount: {self.discount}")
    def calculateDiscount(self):
        super().calculateDiscount(self.discount)
product = DiscountProduct("laptop",100,20)
product.display()
product.calculateDiscount()

