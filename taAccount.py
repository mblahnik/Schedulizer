from account import account


class taAccount(account):

    def __init__(self, name, title):
        account.__init__(self, name, title)


x = taAccount("Bob", "TA")

print(x.accountName)
