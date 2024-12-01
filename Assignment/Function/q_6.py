def count_vowel(s):
    vowel = ["a","A","e","E","i","I","o","O",'u','U']
    count = 0
    for i in s:
        if i in vowel:
            count += 1
    return count
s = input("Enter the string to count vowel: ")
print(count_vowel(s))