"""
Make two functions one for register and one for login to the system. Then ask user for choice and call the function.If user choice is 1 then call the register function and if user choice is 2 then call the login function else you have entered wrong choice. Allow user to register and login to the system only if password and name is correct.
"""
# data = dict()

# while(True):
#     print("WELCOME TO THE SYSTEM")

#     print("1-->Sign Up")
#     print("2-->Login")
#     print("3-->Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         def Register():
#             name = input("Enter your name: ")
#             pw = input("Enter your password: ")
#             print("---------------------------")
#             print("Your UserName is: ",name)
#             print("Your Password is: ",pw)
#             data.setdefault(name,pw)
#         Register()

#         print("You are successfully registered".center(50,"*"))
#         print()
#         # print(data)
    
#     elif choice == 2:
#         def Login():
#             name = input("Enter your name: ")
#             pw = input("Enter your password: ")
#             print()
#             print("---------------------------")
#             print()
#             if name in data.keys():
#                 if pw == data.get(name):
#                     print("Login Successful".center(50,"*"))
#                     print()
#                 else:
#                     print("Wrong Password".center(50,"*"))
#                     print()
#             else:
#                 print("User not found".center(50,"*"))
#                 print()
#         Login()

#     elif choice == 3:
#         break

#     else:
#         print("Wrong Choice")
#         continue

# print("Thank you for using the system".center(50,"*"))

