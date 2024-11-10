# Write a program that checks if a given year is a leap year.

year = int(input("Enter year find given year is a leap or not year: "))
if (year >= 0):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        is_leap = "leap"
    else:
        is_leap = "not leap"
    print(f"{year} is {is_leap} year")
else:
    print("Please Enter Correct Year!")
    
    
    
    
    