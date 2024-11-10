# Print the multiplication table of a given number.

num = int(input("Enter number to multiplication table: "))
if (num > 0):
    for i in range(1, 10 + 1):
        print(f"{num} * {i} = {num * i}")
else:
    print("Please Enter Correct number! ")
    
