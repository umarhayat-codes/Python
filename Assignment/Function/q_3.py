def factorial(num):
    if num < 0:
        return "Not Find Factorial of Negative number!"
    if num == 1:
        return 1
    return num * factorial(num - 1)
num = int(input("Enter number to find factorial: "))
print(factorial(num))
    















