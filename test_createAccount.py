from unittest import TestCase


class TestCreateAccount(TestCase):


    def test_command_create_success(self):
        self.assertEquals(self.ui.command("createAccount TA"), "TA account successfully created")
        

    def test_command_create_fail(self):


    def test_command_creat_no_args(self):


