# A decorator in Python is a design pattern that allows you to modify the behavior of a function

# def decorator(func):
#     def wrapper():
#         print("Good Morning: ")
#         func()
#         print("Thank you for using this function: ")
#     return wrapper

# @decorator
# def hello():
#     print("Hello World: ")
# hello()
# decorator(hello)()


#add

# def decorator(func):
#     def wrapper(*args,**kwards):
#         print(args)
#         print("Good Morning: ")
#         func(*args,**kwards)
#         print(args)
#         print("Thank you for using this function: ")
#     return wrapper

# @decorator
# add = decorator(add)
# def add(a,b):
#     print(a + b)

# # add(1,2)

# decorator(add)(1,2)




# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"{func.__name__} is call")
#         func(*args, **kwargs)
#         print("Thank you for using this function")
#     return wrapper

# @decorator
# def userName(name):
#     print(f"successful login: {name}")

# userName("Umar")


# def decorator(func):
#     def wrapper(*args, **kwards):
#         print(f"We calling {func.__name__} with parameter {args} and {kwards}")
#         print(f"Add: {func(*args, **kwards)}")
#         print("Thank you for using function: ")
#     return wrapper

# # add = decorator(add)
# @decorator
# def add(a,b):
#     return a + b

# add(1,2)

# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwards):
#             for _ in range(n):
#                 func(*args, **kwards)
#         return wrapper
#     return decorator
# # userName = repeat(3)(userName)
# @repeat(3)
# def userName(name):
#     print("Name: ", name)

# userName("umar")



def decorator(func):
    def wrapper(*args, **kwards):
        print("Good Morning: ")
        result = func(*args, **kwards)
        result.upper()
    return wrapper

@decorator
def upper(name):
    print(f"Name: {name}")

upper("umar")
