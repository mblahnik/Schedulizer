from instructor import instructor


class taAccount(instructor):

    def __init__(self, name=""):
        super().__init__(name)
        self.accountInfo["title"] = 1
        self.labs = []
        self.accountInfo["Labs"] = self.courses

    def addlab(self, newLab):
        self.accountInfo["Labs"] = self.courses.append(newLab)

    def displayCourses(self):
        for entry in self.labs:
            print(entry)


