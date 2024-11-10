# 15. Print the sum of even and odd numbers separately up to a given number.

num = 123456789
str_num = str(num)
even_sum = 0
odd_sum = 0
print(f"Sum Odd and Even number separate of {num}")
for i in str_num:
    i = int(i)
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"Even Number is {even_sum}")
print(f"Odd Number is {odd_sum}")

        
