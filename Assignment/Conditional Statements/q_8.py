# Create a program that checks if a given string is a palindrome.
text = input("Enter a string: ")
clean_text = text.replace(" ","").lower()
reverse_text = clean_text[::-1] 
if clean_text == reverse_text:
    print(f"{clean_text} string is palindrome! ")
else:
    print(f"{clean_text} != {reverse_text}.No palindrome! ")

