def is_prime(num):
    if num <= 1:
        return "Not Prime"
    if num <= 3:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

num = int(input("Enter number to check is prime or not: "))
print(is_prime(num))