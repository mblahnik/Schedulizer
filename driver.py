from account import account
from Directory import Directory
from instructor import instructor

directory = Directory()

"""
This is my fake command prompt to maybe work with until we get a real one. Since Accounts that are
created won't be saved just login with the command "login admin password". None if this works yet

"""
admin = instructor()
admin.accountName = admin
admin.accountInfo["password"] = "password"
directory.data.append(admin)

currentUser = account()
currentUserTitle = 0

userInput = input("Please enter a command: ")

command = userInput.split(' ')


if(command[0].lower() == "login"):
    print("got here")
elif(command[0].lower() == "logout"):
    print("now here")
elif(command[0].lower() == "createaccount"):

elif(command[0].lower() == "createlab"):

elif(command[0].lower() == "createlab"):

