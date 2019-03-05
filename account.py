from abc import ABC, abstractmethod


class account(ABC):

    def __init__(self,accountname,title):
        self.accountName = accountname
        self.title = title
        self.eEmail = ""
        self.address = ""
        self.passWord = ""


