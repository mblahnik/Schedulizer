from unittest import TestCase
from Directory import Directory
from account import account


class TestDirectory(TestCase):

    def setUp(self):
        self.Directory1 = Directory()
        self.Directory2 = Directory()
        self.Directory2.data.append("firstAccount")
        self.Directory2.data.append("secondAccount")
        self.Directory2.data.append("lastAccount")
        self.Directory2.manyItems = 3
        self.Account1 = account()

    def test_insert(self):
        self.assertEqual(len(self.Directory1.data), 0)
        self.assertEqual(self.Directory1.manyItems, 0)

        self.Direcotry1.insert("newAccount")

        self.assertEqual(self.Directory1.data[0], "newAccount")
        self.assertEqual(self.Directory1.manyItems, 1)

        self.Directory1.insert("nextAccount")

        self.assertEqual(self.Directory1.data[1], "nextAccount")
        self.assertEqual(self.Directory1.manyItems, 2)
        self.assertEqual(self.Directory1.data[0], "newAccount")

        self.Directory1.insert("lastAccount")

        self.assertEqual(self.Directory1.data[2], "lastAccount")
        self.assertEqual(self.Directory1.manyItems, 3)
        self.assertEqual(self.Directory1.data[0], "newAccount")
        self.assertEqual(self.Directory1.data[1], "nextAccount")

        #Should not be able to insert an account that already exists
        with self.assertRaises(ValueError):
            self.Directory1.insert("newAccount")
            self.Directory1.insert("nextAccount")
            self.Directory1.insert("lastAccount")

    def test_remove(self):
        self.assertEqual(len(self.Directory2.data), 3)
        self.assertEqual(self.Directory2.manyItems, 3)
        self.assertEqual(self.Directory2.data[1], "secondAccount")

        self.Directory2.remove("secondAccount")

        self.assertEqual(self.Directory2.manyItems, 2)
        self.assertEqual(self.Directory2.data[0], "firstAccount")
        self.assertEqual(self.Directory2.data[1], "lastAccount")

        self.Directory2.remove("firstAccount")

        self.assertEqual(self.Directory2.manyItems, 1)
        self.assertEqual(self.Directory2.data[0], "lastAccount")

        self.Directory2.remove("lastAccount")

        self.assertEqual(self.Directory2.manyItems, 0)
        self.assertEqual(len(self.Directory2.data), 0)

        #Should raise and exception if remove is called on something that isnt in the directory
        with self.assertRaises(ValueError):
            self.Directory2.remove("firstAccount")

    def test_isEmpty(self):
        self.assertTrue(self.Directory1.isEmpty())
        self.assertFalse(self.Directory2.isEmpty())

    def test_getAccount(self):
        #should not be able to get an account that doesn't exist
        with self.assertRaises(ValueError):
            self.account1 = self.Directory1.getAccount("firstAccount")

        self.assertEqual(self.Directory2.manyItems, 3)

        self.account1 = self.Directory2.getAccount("firstAccount")

        self.assertEqual(self.account1.accoutName, "firstAccount")

        self.assertEqual(self.Directory2.manyItems, 3)

    def test_size(self):
        self.assertEqual(self.Directory1.size(), 0)
        self.assertEqual(self.Directory2.size(), 3)
