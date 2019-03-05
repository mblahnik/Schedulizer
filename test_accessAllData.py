from unittest import TestCase


class TestAccessAllData(TestCase):
    pass

    def setUp(self):
        self.ui.command("createAccount name")

    """
    When the AccessAllData command is entered, it takes one argument, 
    - name
    
    If no name is entered, an error is displayed 
    If user does not exist, an error is displayed
    Alex - I believe AccessAllData should print all of the data for an account - the password
    rather than just saying "account found" it should probably print off all of the data in an easy to read format 
    """

    def test_command_AccessAllData_success(self):
        self.assertEqual(self.ui.command("AccessAllData name"), "Account found!")

    def test_command_AccessAllData_noname(self):
        self.asserEqual(self.ui.command("AccessAllData"), "No name was entered, error")

    def test_command_AccessAllData_no_such_user(self):
        self.assertEqual(self.ui.command("AccessAllData name"), "User does not exist")

