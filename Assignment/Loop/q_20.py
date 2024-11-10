#  Create a program that simulates a countdown timer starting from a given number down to zero.
import time

start_number = int(input("Enter the starting number for the countdown: "))

for i in range(start_number, -1, -1):
    print(i)
    time.sleep(1)  

print("Countdown complete!")
