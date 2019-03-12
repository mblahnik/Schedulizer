from Account import Account
from Directory import Directory

"""
This method will need access to the directory as well. It will return the account upon a successful
log in or None if the account wasn't found or the password was incorrect. That way the Current user 
and user title can be updated. 
"""
def login(account, password, Directory):
    return Account