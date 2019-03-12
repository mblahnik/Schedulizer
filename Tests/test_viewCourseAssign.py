import unittest
from Commands import viewCourseAssign
from instructor import instructor

class test_ViewCourseAssign(unittest.TestCase):

    def setUp(self):
        self.view = viewCourseAssign(self)

    def test_instructor_can_view(self):
        self.assertTrue(self.view in instructor.displayCourses())


if __name__ == '__main__':
    unittest.main()
