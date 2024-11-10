# Check if a string input is uppercase, lowercase, or a mix.



string = input("Enter alphabet check input is uppercase, lowercase, or a mix: ")

if string.isalpha():
    if string.isupper():
        print("Upper Case!")
    elif string.islower():
        print("lower Case!")
    else:
        print("Both upper and lower Case!")
else:
    print("Please Enter Alphabet!")
        
    