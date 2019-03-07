from unittest import TestCase
from instructor import instructor


class TestInstructor(TestCase):

    def setUp(self):
        self.instructor1 = instructor("Bob", "Instructor")

    def test_getname(self):
        self.assertEqual(self.instructor1.getName(), "Bob")

    def test_setName(self):
        self.instructor1.setName("Joe")
        self.assertEqual(self.instructor1.getName(), "Joe")
