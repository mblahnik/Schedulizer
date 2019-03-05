from unittest import TestCase

class TestAssignTACourse(TestCase):

    def setup(self):
        self.ui.command("createAccount name title")
        self.ui.command("createCourse")

        """
            When AssignTACourse command is entered, it takes two arguments:
                --TA username
                --Course number
            Assignment may fail if:
                --Scheduling conflict for TA
                --Max TAs assigned to course
                --TA username is invalid or missing
                --Course number is invalid or missing
                --No arguments
        """

    def test_command_AssignTACourse_success(self):
        self.assertEqual(self.ui.command("AssignTACourse accountName  courseNumber"), "Assignment successful")

    def test_command_AssignTACourse_missingTA(self):
        self.assertEqual(self.ui.command("AssignTACourse courseNumber"), "Missing TA Username.")

    def test_command_AssignTACourse_invalidTA(self):
        self.assertEqual(self.ui.command("AssignTACourse accountName  courseNumber"), "Invalid TA username.")

    def test_command_AssignTACourse_missingCourse(self):
        self.assertEqual(self.ui.command("AssignTACourse accountName"), "Missing course number.")

    def test_command_AssignTACourse_invalidCourse(self):
        self.assertEqual(self.ui.command("AssignTACourse accountName  courseNumber"), "Invalid course number.")

    def test_command_AssignTACourse_Maximum(self):
        self.assertEqual(self.ui.command("AssignTACourse accountName  courseNumber"), "Maximum TAs assigned to course.")

    def test_command_AssignTACourse_schedulingConflict(self):
        self.assertEqual(self.ui.command("AssignTACourse accountName  courseNumber"), "Scheduling conflict.")

    def test_command_AssignTACourse_noArgs(self):
        self.assertEqual(self.ui.command("AssignTACourse"), "Missing TA username and course number.")
