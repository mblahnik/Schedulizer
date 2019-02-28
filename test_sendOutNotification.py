from unittest import TestCase

class sendOutNotification(TestCase):


  def setup(self):

   """
   When the user type the command sendOutNotification
   It will ask you the password first
    Once you successfully login
   It takes 2-4 arguments

   sendNotification -a
   To send notification to all users.

sendNotification userName. -s
for the list of username parts name the username as many as you want to type

sendNotification  username

sendNotification -a

   -a to all users
   """

def test_command_password_was_correct
       self.assertEquals(self.ui.command("password"), "You have just entered sendOutNotification system")


def test_command_password_was_incorrect
    self.assertEquals(self.ui.command("password"), "Password is incorrect, there are 3 more chances to type it")


 def test_command_nofitication_was_not_sent

         self.assertEquals(self.ui.command("sendNotification"), "type the username")

def test_command_no_argument
            self.assertEquals(self.ui.command("sendNotification"), "Please type the email that you want to sent")

 def test_command_nofitication
            self.assertEquals(self.ui.command("sendNotification"), "notification was succesfully sent")
