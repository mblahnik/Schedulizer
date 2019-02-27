from unittest import TestCase


class TestAccessAllData(TestCase):
    pass

    def setUp(self):
        pass

    """
    When the AccessAllData command is entered, it takes one argument, 
    - name
    
    """

    def test_command_AccessAllData_success(self):
        self.assertEqual(self.ui.command("AccessAllData name"), "Account found!")

    def test_command_AccessAllData_noname(self):
        self.asserEqual(self.ui.command("AccessAllData"), "No name was entered, error")

    def test_command_AccessAllData_no_such_user(self):
        self.assertEqual(self.ui.command("AccessAllData name"), "User does not exist")

