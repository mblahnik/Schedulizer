from account import account


class instructor(account):


    def __init__(self,name,title):
        super().__init__(self,name,title)
        courseAssignments = []
