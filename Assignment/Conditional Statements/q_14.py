# Check if a year input by the user is a century year.
year = int(input("Enter year: "))
if year % 100 == 0:
    print(f"{year} is century year")
else:
    print(f"{year} is not century year")