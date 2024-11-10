#  Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.

num = int(input("Enter number checks it’s divisible by 2, 3, or both: "))

if num % 2 == 0 and num % 3 == 0:
    divisible = "both 2 and 3"
elif num % 2 == 0:
    divisible = "2"
elif num % 3 == 0:
    divisible = "3"
else:
    print(f"{num} is not divisible by 2 and 3 ")
    
print(f"{num} is divisible by {divisible}")

    