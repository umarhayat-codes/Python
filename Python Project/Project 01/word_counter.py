def countWord(text):
    wordCount = {}
    words = text.split()
    for word in words:
        word = word.lower()
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    return wordCount

def main():
    print("Word Counter: ")
    print("1. Text Manually")
    print("2. Another File: ")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        text = input("Enter Some Text: ")
        wordCounter = countWord(text)
    elif choice == 2:
        try: 
            fileName = input("Enter Your File Name: ")
            fileName += ".txt"
            with open(fileName,'r') as file:
                text = file.read()
                wordCounter = countWord(text)            
        except Exception as e:
            print(f"Error: {e}")
            return
    else:    
        print(f"Invalid Input: ")
        return
    for count,word in wordCounter.items():
        print(f"{count} {word}")


if __name__ == '__main__':
    main()
    




# wordCount = {}
# def count_word(text):
#     words = text.split()
#     for word in words:
#         word = word.lower().strip('.?!@')
#         if word in wordCount:
#             wordCount[word] += 1
#         else:
#             wordCount[word] = 1
#     # return wordCount

# def display_count_word():
#     for word, count in wordCount.items():
#         print(f"{word} {count}")
    
    
# def process_manually_input():
#     text = input("Enter Your Text Manually: ")
#     count_word(text)
#     display_count_word()

# def process_file_input():
#     fileName = input("Enter File Name {with or without extension .txt}")
#     if not fileName.endswith('.txt'):
#         fileName += '.txt'
#     try:
#         with open(fileName,'r') as file:
#             text = file.read()
#             count_word(text)
#             display_count_word()
#     except Exception as e:
#         print(f"Error: {e}")
        
# def main():
#     while True:
#         print("\n Count Word")
#         print("1. text manuallly")
#         print("2. from file")
#         print("3. Exit")
#         choice = input("Enter You Choice: ")
#         if choice == '1':
#             process_manually_input()
#         elif choice == '2':
#             process_file_input()
#         elif choice == '3':
#             print("Exit Program")
#             break
# if __name__ == '__main__':
#     main()
        
            
