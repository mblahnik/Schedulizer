from account import account

class Directory():

    def __init__(self):
        self.data = [account]
        self.manyItems = 0

    def insert(self, newAccount):
        return None

    def remove(self, account):
        return None

    def isEmpty(self):
        return None

    def getAccount(self, account):
        for i in self.data:
            if i.accountName == account:
                return i
    def size(self):
        return None
