def sum_even(arr):
    sum = 0
    for i in arr:
        if i % 2 == 0:
            sum += i
    return sum
arr = [1,2,3,4,5,6,7,9,10]
print(sum_even(arr))