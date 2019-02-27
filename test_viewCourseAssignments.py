from unittest import TestCase

class viewCourseAssignments(TestCase):


  def setup(self):

   """
   When the user type the command viewCourseAssignments
   User need to enter the password to see the schedule
    For search the the assignments from other professors
    you need to type search "The name of professor"

    Takes 2 argument for search
    search UserName
   """

def test_command_password_was_correct
       self.assertEquals(self.ui.command("password"), "You have just entered sendOutNotification system")


def test_command_password_was_incorrect
    self.assertEquals(self.ui.command("password"), "Password is incorrect, there are 3 more chances to type it")



def test_command_can_not_view_my_schedule
        self.assertEquals(self.ui.command("viewOwnSchedule"), "The schedule hasn't been uploaded yet")


def test_command_can_find_name
        self.assertEquals(self.ui.command("search username"), "Can't fine the name of the professor, retype it")
