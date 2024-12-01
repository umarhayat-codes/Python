def find_GCD(num1,num2):
    if num1 > num2:
        mn = num1
    else:
        mn = num2 
    for i in range(1,mn + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    return gcd
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print(find_GCD(a,b)) 