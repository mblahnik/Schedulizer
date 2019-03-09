from account import account


class instructor(account):

    def __init__(self, name=""):
        super().__init__(name)
        self.accountInfo["title"] = 1
        self.courses = []
        self.accountInfo["Courses"] = self.courses

    def addcourse(self, newCourse):
        self.accountInfo["Courses"] = self.courses.append(newCourse)

    def displayCourses(self):
        for entry in self.courses:
            print(entry)


