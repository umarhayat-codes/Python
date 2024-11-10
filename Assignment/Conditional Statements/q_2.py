# Take a user’s age as input and display whether they are a minor, adult, or senior citizen.


age = int(input("Please Enter Your Age: "))
if age > 0:
    
    if age < 18:
        citizen_is = 'minor'
    elif age >= 18 and age <= 45:
        citizen_is = "adult"
    else:
        citizen_is = "senior"
        
    print(f"You are {citizen_is} citizen.")
else:
    print(f"Please Enter Correct Age! ")
