# 16. Create a program to calculate the sum of the digits of an inputted integer.

num = int(input("Enter number to calculate the sum of the digits: "))
sum = 0
while num > 0:
    last_digit = num % 10
    sum += last_digit
    num //= 10
print(f"Sum of Digit is {sum}")
