from account import account

"""
Administrators can:
-Create courses
-Create Accounts 
-Edit accounts
-Delete Accounts 
-Send out notifications to users 
-Access all data
"""

class administrator(account):

    def __init__(self, name = ""):
        super.__init__(name)
        self.accountInfo["title"] = 3
