def count_frequency(s):
    fre = {}
    count = 0
    for i in s:
        for j in s:
            if i == j:
                count += 1
        fre[i] = count
        count = 0
    return fre

print(count_frequency("abcabcabc")) 