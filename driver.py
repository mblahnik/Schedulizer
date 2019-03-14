from account import account
from Directory import Directory
from instructor import instructor
from Commands import login
directory = Directory()

"""
This is my fake command prompt to maybe work with until we get a real one. Since Accounts that are
created won't be saved just login with the command "login admin password". Login works if you
type it in correctly

"""
admin = instructor("admin")
admin.accountInfo["password"] = "password"
directory.data.append(admin)

currentUser = account
currentUserTitle = 0
mainMenu = True

while(mainMenu):
    userInput = input("Please enter a command: ")

    command = userInput.split(' ')

    if(command[0].lower() == "login"):
        currentUser = login.login(command[1], command[2], directory)
        print("currentuser is " + currentUser)
    elif(command[0].lower() == "logout"):
        print("now here")
    elif(command[0].lower() == "createaccount"):
        print("now here")
    elif(command[0].lower() == "createlab"):
        print("now here")
    elif(command[0].lower() == "createlab"):
        print("now here")
