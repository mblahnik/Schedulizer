from unittest import TestCase

class test_sendOutNotification(TestCase):

    def setUp(self):
        self.ui.command("createAccount accountName")


"""
   When the user type the command sendOutNotification
   It will ask you the password first
    Once you successfully login
   It takes 2-3 arguments

   sendNotification -a
   To send notification to all users.

sendNotification accountNames -s
 To send notification to specific users.
 UserNames can be written as userName, userName form.

sendNotification  accountName

to send notification to one person
   """

def test_command_password_was_correct(self):
       self.assertEquals(self.ui.command("password"), "You have just entered sendOutNotification system")


def test_command_password_was_incorrect(self):
    self.assertEquals(self.ui.command("password"), "Password is incorrect, there are 3 more chances to type it")


 def test_command_nofitication_was_not_sent(self):

         self.assertEquals(self.ui.command("sendNotification accountName"), "We weren't able to send a notification")


 def test_command_nofitication_was_not_sent_all(self):

         self.assertEquals(self.ui.command("sendNotification accountName -a"), "We weren't able to send a notification")

 def test_command_nofitication_was_not_sent_specific(self):

         self.assertEquals(self.ui.command("sendNotification accountNames -s"), "We weren't able to send a notification")

def test_command_no_argument(self):
            self.assertEquals(self.ui.command("sendNotification"), "Please type the email that you want to sent")
