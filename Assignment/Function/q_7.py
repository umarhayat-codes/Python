def find_largest_num(arr):
    max = 0
    for i in arr:
        for j in arr:
            if i > j:
                max = i
    return max

arr = [3,6,8,10,14]
print(find_largest_num(arr)) 