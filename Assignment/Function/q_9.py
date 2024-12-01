def is_palindrome(s):
    reverse = s[::-1]
    return s == reverse
s = input("Enter string to check is palindrome: ")   
print(is_palindrome(s))