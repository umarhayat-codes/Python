# userName="Umar Hayat"
# print("userName: ",userName)

# lenght
# lenght=len(userName)
# print("count the character: ",lenght)

# str
# integer=12345
# string=str(integer)
# print("the count of integer: ",len(string))

# contatenation string
# firstName="Umar"
# lastName="Hayat"
# space=" "
# contatenate=firstName+space+lastName
# print(contatenate)
# print(firstName,lastName)

# multiple value
# userName="umar hayat " * 2
# print(userName*2)

# Access
# a=userName[1]
# print(a)
# print(userName[1:8])
# print(userName[::2])
# print(userName[::-2])

# Method String
# userName=" Umar Hayat Zain Ashfaq "
# method=userName.upper()
# print(method)
# print("lower: ",userName.lower())
# print("Capitalize: ",userName.capitalize())
# print("Title: ",userName.title())
# print("remove whitespace or right and left: ",userName.strip())
# print("remove left space",userName.lstrip())
# print("remove right space",userName.rstrip())
# userName=" Umar Hayat Zain Ashfaq "
# convertList=userName.split()            # ['Umar', 'Hayat', 'Zain', 'Ashfaq']
# userName=" Umar:Hayat:Zain:Ashfaq "
# convertList=userName.split(":")
# print("convert string into list: ",convertList)
# userName=["Umar","Hayat", "Zain", "Ashfaq "]
# listIntoString= "--".join(userName)
# print("Convert list into string: ",listIntoString)      # Umar--Hayat--Zain--Ashfaq
# userName="ashfaq  "
# print("check the alphabet: ",userName.isalpha())    #   return false if is space or digit otherwise true 
# rollNo="10233"
# print("check the digit: ",rollNo.isnum())    #   return false if is space or alphabet otherwise true 
# nameOrRollNo="umar1234"
# return true if is only alpha or digit or both and false if is space
# print("check the digit or alphabet: ",nameOrRollNo.isalnum())   
# userName="--umar"
# print("check starting point:",userName.startswith("--"))
# userName="--umar--"
# print("check starting point:",userName.endswith("--"))
# isspace

# replace 
# userName="umar"
# replaces=userName.replace("umar","hayat")
# print("replace: ",replaces)
# index
# userName="umar"
# print("find the index of m",userName.index("m"))
# count