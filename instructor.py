from account import account


class instructor(account):

    def __init__(self,name,title):
        super().__init__(self,name,title)
        self.courses = []
        self.accountInfo["Courses"] = self.courses

    def addcourse(self, newCourse):
        self.accountInfo["Courses"] = self.courses.append(newCourse)

