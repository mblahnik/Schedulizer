import unittest
from Commands import viewInfo
from instructor import instructor

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.Instructor = instructor()
        self.Instructor.accountName = "Mr.Sparkle"
        self.Instructor.accountInfo["Home Phone"] = "555-0113"
        self.Instructor.accountInfo["Email"] = "chunkylover53@aol.com"
        self.Instructor.accountInfo["address"] = "123 Fake Street"
        self.Instructor.accountInfo["Office Phone"] = "555-5555"
        self.Instructor.accountInfo["Office hours"] = "All day everyday"

    def test_viewInfo(self):
        self.assertEqual(viewInfo(self.Instructor), "Name: Mr.Sparkle"
                                                    "Email: chumnkylover53@aol.com"
                                                    "Office Phone: 555-5555"
                                                    "Office hours: All day everyday")

if __name__ == '__main__':
    unittest.main()
