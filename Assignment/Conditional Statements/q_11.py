# Check if a given number is a multiple of both 3 and 5.

num = int(input("Enter a number to find is multiple of both 3 and 5: "))

if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is a multiple of both 3 and 5")
else:
    print(f"{num} is not multiple of both 3 and 5")