from unittest import TestCase

class sendOutNotification(TestCase):


  def setup(self):

   """
   When the user type the command sendOutNotification
   It will ask the enter the login information first
    Once you successfully login
   It takes 3 argument
   sendNotification userName sendOne|sendAll|sendSpecific

   """

def test_command_password_was_correct
       self.assertEquals(self.ui.command("password"), "You have just entered sendOutNotification system")


def test_command_password_was_incorrect
    self.assertEquals(self.ui.command("password"), "Password is incorrect, there are 3 more chances to type it")


 def test_command_nofitication_was_sent

         self.assertEquals(self.ui.command("sendNotification"), "notification was succesffuly sent")

def test_command_no_argument
            self.assertEquals(self.ui.command("sendNotification"), "Please type the email that you want to sent")

 def test_command_nofitication
            self.assertEquals(self.ui.command("sendNotification"), "notification was succesfully sent")
