# Take an integer and check if it’s even or odd

number = int(input("Enter a number to find it even or odd: "))
if number > 0:
    if number % 2 == 0:
        is_number = "even"
    else:
        is_number = "odd"
    print(f"{number} is {is_number} number! ")
else:
    print("Please Enter the correct number! ")

        
