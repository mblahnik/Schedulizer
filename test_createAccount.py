from unittest import TestCase


class TestCreateAccount(TestCase):

    def setUp(self):
        self.ui.command("createAccount accountName")
    """
        When the createAccount command is entered, it takes two arguments:
        -Account name
        -title
        If the account being created already exists in the database an error message is displayed
    """
    def test_command_createAccount_success(self):
        self.assertEquals(self.ui.command("createAccount accountName  title"), "Account successfully created")

    def test_command_createAccount_no_title(self):
        self.assertEquals(self.ui.command("createAccount accountName "), "Need to specify a title")

    def test_command_createAccount_invalidTitle(self):
        self.assertEqual(self.ui.command("createAccount accountName cashier"), "Please enter a valid title")

    def test_command_createAccount_no_name(self):
        self.assertEquals(self.ui.command("createAccount title"), "Need to specify a name")

    def test_command_createAccount_no_args(self):
        self.assertEquals(self.ui.command("createAccount"), "Please enter a name and title")

    def test_command_createAccount_already_exists(self):
        self.assertEquals(self.ui.command("createAccount accountName title "), "Account already exists")






