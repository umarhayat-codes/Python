# file=open("example.txt","r")
# text=file.read()
# text=file.readline()
# text=file.readlines()
# print(text)
# file.close()

# with open("example.txt","w") as file:
#     text=file.write("We are learning C++ language and python languages: ")
    
    
# with open("example.txt","a") as file:
#     text=file.write("We are interest in C++ language and python languages: ")
    
    
# file = open("example.txt",'r')
# text = file.read()
# print(text)
# file.close()
# file = open("example.txt","r")
# text = file.readlines()
# print(f"We read other file: {text}")
# file.close()


# with open("example.txt",'w') as file:
#     text = file.write("We are writing in  another file using file handling: ")


# with open("example.txt",'r') as file:
#     print(file.read())


with open("example.txt",'a') as file:
    file.write("We are writing using another file: ")

