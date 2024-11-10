# 18. Use a loop to print numbers in reverse order within a given range.



num = 123
reverse_num = 0
print(f"before number is {num}")
while num > 0:
    last_digit = num % 10
    reverse_num = reverse_num * 10 + last_digit
    num //= 10

print(f"After number is {reverse_num}")