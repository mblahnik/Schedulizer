from account import account

"""
Supervisors can:
-Create courses
-Create new accounts 
-Edit accounts 
-Delete accounts 
-Send out notifications 
-Access all data
-Assign Instructors to classes 
-Assign TAs to courses 
-Assign TAs to lab sections 
"""

class supervisor(account):

    def __inti__(self, name = ""):
        super.__init__(name)
        self.accountInfo["title = 4"]

