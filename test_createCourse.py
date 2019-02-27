from unittest import TestCase


class TestCreateCourse(TestCase):

    def setUp(self):
        self.ui.command("Put a course in the database to check against")
    """
        When the createCourse command is entered, it takes one argument:
        -Course Name 
        If the course name matches a database entry a then the course is not created 
        and an error message is displayed and some other stuff
    """
    def test_command_createCourse_success(self):
        self.assertEquals(self.ui.command("createCourse courseName"), "Course successfully created")

    def test_command_createCourse_no_args(self):
        self.assertEquals(self.ui.command("createCourse "), "Please specify a course name")

    def test_command_createCourse_course_exists(self):
        self.assertEqual(self.ui.command("createCourse courseName"), "Course already exists")


