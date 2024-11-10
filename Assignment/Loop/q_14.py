# 14. Write a program that breaks the loop when a certain condition is met.


for i in range(1,21):
    if i % 7 == 0:
        print(f"number is divisible by 7. Break the loop!")
        break
    
    print(i)