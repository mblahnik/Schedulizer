from unittest import TestCase


class TestDeleteAccount(TestCase):
    pass

    def setUp(self):
        pass

    """
    When the deleteAccount command is entered, it takes two arguments, 
     -name 
     -title
    If a name or title is missing, an error message is displayed
    """

    def test_command_deleteAccount(self):
        self.assertEquals(self.ui.command("createAccount accountName  title"), "Account successfully deleted")

    def test_command_deleteAccount_no_title(self):
        self.assertEquals(self.ui.command("deleteAccount accountName "), "Need to specify a title")

    def test_command_deleteAccount_no_name(self):
        self.assertEquals(self.ui.command("deleteAccount title "), "Need to specify a name")

    def test_command_createAccount_no_args(self):
        self.assertEquals(self.ui.command("deleteAccount"), "Please enter a name and title")