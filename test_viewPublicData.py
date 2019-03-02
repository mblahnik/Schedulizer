from unittest import TestCase


class TestViewPublicData(TestCase):

    def setUp(self):
        self.ui.command("createAccount accountName")

    """
         When the vpd command is entered is takes one argument 
         -account Name
         If the name entered does not match one in the database an error is displayed
         other wise all of the account information that is public will be displayed
    """
    def test_command_vpd_success(self):
        self.assertEquals(self.ui.command("vpd accountName"), "Name: accountName"
                                                              "email: accountEmail"
                                                              "add more information later")
        
    def test_command_vps_no_account(self):
        self.assertEqual(self.ui.command("vpd invalidAccount"), "Account does not exist")

    def test_command_vps_no_args(self):
        self.assertEqual(self.ui.command("vpd"), "Please specify and account name")



