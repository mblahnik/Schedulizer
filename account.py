from abc import ABC, abstractmethod


class account(ABC):

    def __init__(self,accountname,title):
        self.accountName = accountname
        self.title = title
        self.eEmail = ""
        self.address = ""
        self.passWord = ""

    def getName(self):
        return self.accountName

    def setName(self,newName):
        self.accountName = newName

    def setEmail(self):
        pass

    def getEmail(self):
        pass

    def setAddress(self):
        pass

    def getAddress(self):
        pass

    def setPassWord(self):
        pass

    def getPassWord(self):
        pass

