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
directory.insert(admin)

currentUser = account
mainMenu = True


while(mainMenu):
    userInput = input("Please enter a command: ")

    command = userInput.split(' ')

    if(command[0].lower() == "login"):
        try:
            currentUser = login.login(command[1], command[2], directory)
            print("Now logged in as " + currentUser)
        except ValueError as error:
            print(error)
    elif(command[0].lower() == "logout"):
        currentUser = account
        print("Succeffuly logged out")
    elif(command[0].lower() == "createaccount"):
        print("now here")
    elif(command[0].lower() == "createlab"):
        print("now here")
    elif(command[0].lower() == "createlab"):
        print("now here")
    elif (command[0].lower() == "exit"):
        print("Goodbye")
        mainMenu = False
    else:
        print(command[0] + " is an unsupported command")
