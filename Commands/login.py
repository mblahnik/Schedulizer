from account import account
from Directory import Directory

"""
This method will need access to the directory as well. It will return the account upon a successful
log in or None if the account wasn't found or the password was incorrect. That way the Current user 
and user title can be updated. 
"""


def login(account, password, Directory):
    tempaccount = Directory.getAccount(account)
    if password == tempaccount.accountInfo["password"] == password:
        return account
    else:
        raise ValueError("incorrect password")
