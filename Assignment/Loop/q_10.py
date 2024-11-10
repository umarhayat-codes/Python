# Use a loop to count the number of digits in an integer.

# num = 123
# count = 0
# for _ in str(num):
#     count += 1
# print(count)


num = 1234
count = 0
while num > 0:
    num //= 10
    count += 1