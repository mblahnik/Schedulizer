import unittest
from Commands import login
from instructor import instructor
from teachingAssistant import teachingAssistant
from Directory import Directory


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.Directory = Directory()
        self.Instructor = instructor("Mr.Sparkle")
        self.Instructor.accountInfo["password"] = "12345"
        self.TA = teachingAssistant("Myopic Myron")
        self.TA.accountInfo["password"] = "54321"
        self.Directory.data.append(self.Instructor)
        self.Directory.data.append(self.TA)

    def test_login(self):
        self.assertEqual(self.Instructor, login.login("Mr.Sparkle", "12345", self.Directory))
        self.assertEqual(self.TA, login.login("Myopic Myron", "54321", self.Directory))

        self.assertIsNone(login.login("Mr.Sparkle", "55555", self.Directory))

        self.assertIsNone(login.login("Bob", "12345", self.Directory))


if __name__ == '__main__':
    unittest.main()
