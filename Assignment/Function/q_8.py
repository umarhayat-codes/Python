def find_fibonacci(num):
    if num <= 0:
        return "Not Fibocanni!"
    if num == 1:
        return 0
    if num == 2:
        return 1
    return find_fibonacci(num - 1) + find_fibonacci(num - 2)
num = int(input("Enter number to calculate fibocanni: "))    
print(find_fibonacci(num))