import random

def generate_password(upp, lower, num, sym, length):
    all_chars = upp + lower + num + sym
    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()"

print(generate_password(uppercase, lowercase, numbers, symbols, 5))
