from unittest import TestCase


class TestViewTAAssignments(TestCase):

    def setUp(self):
        self.ui.command("ViewTAAssignments classNumber")


    """
    When the ViewTAAssignments command is entered, it takes one argument
    - class Number 
    
    If the class Number is not entered, an error message is displayed
    If the class does not exist, an error message is displayed 
    
    """

    def test_command_ViewTAAssignments_success(self):
        self.assertEqual(self.ui.command("ViewTAAssignments classNumber"), "The TA Assignments are: ")

    def test_command_ViewTAAssignments_noClassNum(self):
        self.assertEqual(self.ui.command("ViewTAAssignments"), "Error, no class number entered")

    def test_command_ViewTAAssignments_classDoesNotExist(self):
        self.assertEqual(self.ui.command("ViewTAAssignments classNumber"), "Class does not exist")
