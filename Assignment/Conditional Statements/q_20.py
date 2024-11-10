# Create a program that evaluates if an inputted number is prime.

num = int(input("Enter number evaluates number is prime or not: "))

if num > 1:
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not prime number!")
            break
    else:
        print(f"{num} is prime number!")
else:
    print(f"{num} is not prime number")
    
