from unittest import TestCase
from account import account


class TestAccount(TestCase):

    def setUp(self):
        self.Account1 = account()
        self.Account1.accountName = "Mr.Sparkle"
        self.Account1.accountInfo["Home Phone"] = "555-0113"
        self.Account1.accountInfo["eMail"] = "chunkylover53@aol.com"
        self.Account1.accountInfo["address"] = "123 Fake Street"


    def test_getName(self):
        self.assertEqual(self.Account1.getName(), "Mr.Sparkle")

    def test_setName(self):
        self.assertEqual(self.Account1.accountName, "Mr.Sparkle")
        self.Account1.setName("Homer")
        self.assertEqual(self.Account1.accountName, "Homer")

    def test_setInfo(self):
        self.assertEqual(self.Account1.accountInfo["address"], "123 Fake Street")
        self.Account1.setInfo("address", "742 Evergreen Terrace")
        self.assertEqual(self.Account1.accountInfo["address"], "742 Evergreen Terrace")

        self.assertEqual(self.Account1.accountInfo["address"], "123 Fake Street")
        self.Account1.setInfo("address", "742 Evergreen Terrace")
        self.assertEqual(self.Account1.accountInfo["address"], "742 Evergreen Terrace")

    def test_getInfo(self):
        self.assertEqual(self.Account1.getInfo("address"), "123 Fake Street")


