# Write a program that checks if a given number is positive, negative, or zero.

number = int(input("Enter the number: "))
if number:
    
    if number < 0:
        is_number = "negative"
    elif number > 0:
        is_number = "positive"
    else:
        is_number = "zero"
else:
    print("Please Enter Number: ")
print(f"User Enter Number is '{is_number}'")


    