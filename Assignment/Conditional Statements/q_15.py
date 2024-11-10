# Write a program to check if a number is within a specified range.

number = int(input('Enter number to check within a specified range: '))
upper_limit = int(input('Enter upper range: '))
lower_limit = int(input('Enter lower range: '))

if upper_limit > lower_limit:
    if lower_limit <= number <= upper_limit:
        print(f"{number} within range of {lower_limit} and {upper_limit}")
    else:
        print(f"{number} is not within range of {lower_limit} and {upper_limit}")
else:
    print("Please Enter Correct Range!")