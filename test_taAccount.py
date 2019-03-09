from unittest import TestCase
from taAccount import taAccount

class TestTaAccount(TestCase):

    def setUp(self):
        self.TA1 = taAccount()

    def test_addlab(self):
        self.assertEqual(len(self.TA1.labs), 0)
        self.instructor1.addcourse("CPS361")
        self.assertEqual(len(self.TA1.labs), 1)
        self.instructor1.addcourse("CPS101")
        self.assertEqual(len(self.TA1.labs), 2)

    def test_displayCourses(self):
        pass
