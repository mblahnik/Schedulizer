from unittest import TestCase

class test_sendOutNotification(TestCase):


  def setup(self):

   """
   When the user type the command sendOutNotification
   It will ask you the password first
    Once you successfully login
   It takes 2-3 arguments

   sendNotification -a
   To send notification to all users.

sendNotification userNames -s
 To send notification to specific users.
 UserNames can be written as userName, userName form.

sendNotification  userName

to send notification to one person
   """

def test_command_password_was_correct
       self.assertEquals(self.ui.command("password"), "You have just entered sendOutNotification system")


def test_command_password_was_incorrect
    self.assertEquals(self.ui.command("password"), "Password is incorrect, there are 3 more chances to type it")


 def test_command_nofitication_was_not_sent

         self.assertEquals(self.ui.command("sendNotification userName"), "We weren't able to send a notification")
         

 def test_command_nofitication_was_not_sent_all

         self.assertEquals(self.ui.command("sendNotification userName -a"), "We weren't able to send a notification")

 def test_command_nofitication_was_not_sent_specific

         self.assertEquals(self.ui.command("sendNotification userNames -s"), "We weren't able to send a notification")

def test_command_no_argument
            self.assertEquals(self.ui.command("sendNotification"), "Please type the email that you want to sent")
