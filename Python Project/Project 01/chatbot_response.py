#ok
import random

patterns = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm doing well, thank you.", "I'm great, thanks for asking!"],
    "what's your name": ["I'm a chatbot.", "My name is ChatBot."],
    "default": ["I'm not sure what you're asking.", "Could you please clarify?"]
}

# def chatbotResponse(userInput):
#     for pattern, response in patterns.items():
#         if pattern == userInput.lower():
#             return random.choice(response)
#     return random.choice(patterns['default'])


# def main():
#     print("Welcome to the chatBot: ")
#     print("You can start chatting. Type 'quit' to end th cnverstion: " )
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == 'quit':
#             print("Goodbye Chatbot:")
#             break
        
#         response = chatbotResponse(user_input)
#         print("ChatBot: ",response)

# if __name__ == '__main__':
#     main()
    
def chatBotResponse(userInput):
    for k, v in patterns:
        if k == userInput:
            return random.choice(v)
    return random.choice(patterns["default"])

def main():
    while True:
        userInput = input("Enter Your Message: ")
        if userInput.lower() == "quit":
            break
        response = chatBotResponse(userInput)
        print("ChatBot: ",response)
if __name__ == '__main__':
    main()


