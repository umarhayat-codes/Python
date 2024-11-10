# Write a program to determine if a given character is a vowel or consonant.

char = input("Enter a single character: ").lower()
vowel = ['a','e','i','o','u','s']

# if len(char) == 1 and char.isalpha():
#     for i in vowel:
#         if char == i:
#             print(f"{char} is vowel! ")
#     else:
#             print(f"{char} is not vowel! ")
# else:
#     print("Please Enter single character! ")


if len(char) == 1 and char.isalpha():
    if char in vowel:
        print(f"{char} is vowel! ")
    else:
        print(f"{char} is not vowel! ")
        
else:
    print("Please Enter single character! ")
        
            

            
 