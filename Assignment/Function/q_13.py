def remove_duplicate(lis):
    l = 0
    r = 1
    while r < len(lis):
        if lis[l] == lis[r]:
            lis.pop(r)
        else:
            r += 1
            l += 1
    return lis
print(remove_duplicate([0,0,1,1,2,3,4,4]))
