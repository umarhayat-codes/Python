# import re

# users = []

# def is_valid_email(email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     return re.match(pattern, email) is not None

# def is_valid_password(password):
#     if len(password) <= 6:
#         return False
#     else:
#         return True

# def register():
#     print("Register! ")
#     userName = input("Enter Your Name: ")
#     password = input("Enter Your Password: ")
#     email = input("Enter Your email: ")
    
#     if not userName or not password or not email:
#         print("Please Fill all Field: ")
#         return
    
#     if not is_valid_email(email):
#         print("Invalid Email: ")
#         return
    
#     if not is_valid_password(password):
#         print("Invalid Password: ")
#         return
    
#     for user in users:
#         if user['userName'] == userName or user['email'] == email:
#             print("user or email already register! ")
#             return
        
#     user = {
#         "userName" : userName,
#         "email" : email,
#         "password" : password
#     }
    
#     users.append(user)
#     print("user Successfully Register! ")

    
# def login():
#     print("Login! ")
#     userName = input("Enter Your Name: ")
#     password = input("Enter Your Password: ")
#     email = input("Enter Your email: ")
    
#     userFound = None
#     for user in users:
#         if user['userName'] == userName and user['email'] == email and user['password'] == password:
#             userFound = user
#             print("Welcome Back! ", {user['userName']})
#             break
    
#     if not userFound:
#         print("user not found! ")
#         return
    
    
# def main():
#     while True:
#         print('Welome to login and register System')
#         print('1. Register')
#         print('2. login')
#         print('3. Exit')
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             register()
#         if choice == "2":
#             login()
#         if choice == "3":
#             print("Exit the program: ")
#             break
        

# if __name__ == "__main__":
#     main()
    


# import re

# users = []

# def is_valid_email(email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     return bool(re.match(pattern,email))

# def validate_registration_input(userName,email,password):
#     if len(userName.strip()) < 3:
#         return 'Incorrect name'
#     if len(password) < 3:
#         return 'Incorrect password'
#     if not is_valid_email(email) < 3:
#         return 'Incorrect email'
    

    
# def register():
#     print("\n Register")
#     userName = input("Name: ")    
#     email = input("Email: ")
#     password = input("Password: ")
#     error_msg = validate_registration_input(userName,email,password)
#     print(error_msg)
#     for user in users:
#         if user['email'] == email:
#             print(f"User {userName} already exit!")
#             return
#     users.append({'userName' : userName, 'email' : email, 'password' : password})
#     print(f"User {email} Successfully Register!")

# def login():
#     print("\n Login")
#     email = input("Email: ")
#     password = input("Password: ")
#     if not is_valid_email(email):
#         print("Invalid Email!")
#         return
#     if len(password) <= 5:
#         print("Password at least 6 characters!")
#         return
#     for user in users:
#         if user['email'] == email and user['password'] == password:
#             print(f"Welcome back! {email} Successfully Login")

# def main():
#     while True:
#         print("1. Register")        
#         print("2. Login")        
#         print("3. Exit")        
#         choice = input("Type your choice: ")
#         if choice == '1':
#             register()
#         elif choice == '2':
#             login()
#         elif choice == '3':
#             print("Exit Execution! ")
#             break
# if __name__ == '__main__':
#     main()
        
