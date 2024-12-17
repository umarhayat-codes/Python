import random 
import string

def generateRandomPassword(upper,lower,number,symbol,lenght):
    character = ""
    if (upper):
        character = string.ascii_uppercase
    if (lower):
        character += string.ascii_lowercase
    if (number):
        character += string.digits
    if (symbol):
        character += string.punctuation
    
    if(not character):
        print("Enter character minimum one: ")
        return
    
    password = ''.join(random.choice(character) for _ in range(lenght))
    return password
    
def main():
    print("Generate Password: ")
    upper = input("enter upper letter: {y/n}").lower() == 'y'
    lower = input("enter lower letter: {y/n}").lower() == 'y'
    symbol = input("enter symbol letter: {y/n}").lower() == 'y'
    puntuation = input("enter puntuation letter: {y/n}").lower() == 'y'
    lenght = int(input("Enter the length: "))
    password = generateRandomPassword(upper,lower,symbol,puntuation,lenght)
    print(f"The password: {password}")

if __name__ == '__main__':
    main()
    
