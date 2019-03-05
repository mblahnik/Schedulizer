from unittest import TestCase

class TestAssignTALab(TestCase):
    def setup(self):
        self.ui.command("createAccount name title")
        self.ui.command("createLab")

        """
            When AssignTALab command is entered, it takes two arguments:
                --TA username
                --Lab number
            Assignment may fail if:
                --Scheduling conflict for TA
                --TA already scheduled to lab
                --TA username is invalid or missing
                --Lab number is invalid or missing
                --No arguments
        """

    def test_command_AssignTALab_success(self):
        self.assertEqual(self.ui.command("AssignTACourse accountName  labNumber"), "Assignment successful")

    def test_command_AssignTALab_missingTA(self):
        self.assertEqual(self.ui.command("AssignTACourse labNumber"), "Missing TA Username.")

    def test_command_AssignTALab_invalidTA(self):
        self.assertEqual(self.ui.command("AssignTACourse accountName  labNumber"), "Invalid TA username.")

    def test_command_AssignTALab_missingLab(self):
        self.assertEqual(self.ui.command("AssignTACourse accountName"), "Missing lab number.")

    def test_command_AssignTALab_invalidLab(self):
        self.assertEqual(self.ui.command("AssignTACourse accountName  labNumber"), "Invalid lab number.")

    def test_command_AssignTALab_Maximum(self):
        self.assertEqual(self.ui.command("AssignTACourse accountName  labNumber"), "TA already assigned to this lab.")

    def test_command_AssignTALab_schedulingConflict(self):
        self.assertEqual(self.ui.command("AssignTACourse accountName  labNumber"), "Scheduling conflict.")

    def test_command_AssignTALab_noArgs(self):
        self.assertEqual(self.ui.command("AssignTACourse"), "Missing TA username and lab number.")
