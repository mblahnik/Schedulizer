from unittest import TestCase


class TestDeleteAccount(TestCase):
    pass

    def setUp(self):
        self.ui.command("deleteAccount name title")

    """
    When the deleteAccount command is entered, it takes two arguments, 
     -name 
     -title
    If a name or title is missing, an error message is displayed
    If the account that the user is trying to delete does not exist, an error 
    message is displayed. 
    
    """

    def test_command_deleteAccount(self):
        self.assertEquals(self.ui.command("deleteAccount name title"), "Account successfully deleted")

    def test_command_deleteAccount_no_title(self):
        self.assertEquals(self.ui.command("deleteAccount name"), "Need to specify a title")

    def test_command_deleteAccount_no_name(self):
        self.assertEquals(self.ui.command("deleteAccount title"), "Need to specify a name")

    def test_command_deleteAccount_no_args(self):
        self.assertEquals(self.ui.command("deleteAccount"), "Please enter a name and title")

    def test_command_deleteAccount_doesnotexist(self):
        self.assertEqual(self.ui.command("deleteAccount name title"), "Account does not exist")