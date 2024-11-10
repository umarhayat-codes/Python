#  Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.

temp = int(input("Enter a temperature in Celsius: "))
if temp <= 0:
    print(f"{temp} celsius point is freezing! ")
elif temp <= 25:
    print(f"{temp} celsius point is moderate! ")
else:
    print(f"{temp} celsius point is hot! ")