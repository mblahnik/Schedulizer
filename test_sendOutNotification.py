from unittest import TestCase

class sendOutNotification(TestCase):


  def setup(self):

   """
   When the user type the command sendOutNotification
   It will ask the enter the login information first
    Once you successfully login
    You need to choose 3 options before you send the notification
   option 1.  to send email all
   option 2. to send email to specific group
   option 3. to send email to one
   Once you choose the option, you will type sendNotification
   You could type the command sendNotification just for all people
   type sendNotification "one email address or multiple addresses"

   """

def test_command_password_was_correct
       self.assertEquals(self.ui.command("password"), "You have just entered sendOutNotification system")


def test_command_password_was_incorrect
    self.assertEquals(self.ui.command("password"), "Password is incorrect, there are 3 more chances to type it")



def test_command_choose_option_to_send_specific
        self.assertEquals(self.ui.command("sendSpecific"), "Your notification will be send to specific people")


def test_command_choose_option_to_send_one
        self.assertEquals(self.ui.command("sendOne"), "notification was sent to one")

def test_command_choose_option_to_send_all
        self.assertEquals(self.ui.command("sendToAll"), "Your notification will be sent to all"

 def test_command_nofitication_was_sent

         self.assertEquals(self.ui.command("sendNotification"), "notification was succesffuly sent")

def test_command_no_argument
            self.assertEquals(self.ui.command("sendNotification"), "Please type the email that you want to sent")

 def test_command_nofitication
            self.assertEquals(self.ui.command("sendNotification"), "notification was succesfully sent")
