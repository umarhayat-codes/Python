# 17. Write a program that continues to ask for a number until the correct number is guessed



correct_num = 7
while True:
    guess = int(input("Guess the number 1 to 10: ")) 
    if guess == correct_num:
        print("Congratulation! You guess correct number.")
        break
    else:
        print("Incorrect number! \n")