from unittest import TestCase

class test_ViewCourseAssignments(TestCase):

    def setUp(self):



"""
   When the user type the command viewCourseAssignments,
   User needs to enter the password to see the schedule
       The command for view my schedule :viewMySchedule
    For searching the the assignments for other professors;
    It takes 2 arguments to search;
    search accountName
   """

def test_command_password_was_correct(self):
    self.assertEquals(self.ui.command("password"), "You have just entered sendOutNotification system")

def test_command_password_was_incorrect(self):
    self.assertEquals(self.ui.command("password"), "Password is incorrected, there are 3 more chances to type it")

def test_command_password_was_incorrect_3times(self):
    self.assertEquals(self.ui.command("password"), "Passwrod is incorrected for 3 times contact to administrator")

def test_command_can_not_view_my_schedule(self):
    self.assertEquals(self.ui.command("viewMySchedule"), "The schedule hasn't been uploaded yet")

def test_command_cannot_find_name(self):
    self.assertEquals(self.ui.command("search accountName"), "Can't fine the name of the professor, retype it")


def test_command_username_not_typed(self):
    self.assertEquals(self.ui.command("search"), "Type the username")
