#Find the factorial of a number using a while loop.

n = int(input("Enter the number to calculate facturial: "))
i = 1
fact = 1
while i <= n:
    fact *= i
    i += 1    
print(f"Factorial of {n} is {fact}")    

