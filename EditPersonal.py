import unittest

class findaccounts(unittest.TestCase):
    def setUp(self):
        self.ui.command("change username phone newPhoneNumber")
        self.ui.command("change username Hphone newHPhoneNumber")
        self.ui.command("change username adress newAdress")
        self.ui.command("change username emailadress NewEmailAdress")

    def test_change_phone_command_correct(self):
        self.assertEqual(self.ui.command("change my phone newPhoneNumber"), "phone number has been changed")

    def test_change_phone_command_no_number(self):
        self.assertEqual(self.ui.command("change my phone"), "Error changing number")

    def test_change_phone_command_wrong_number_format(self):
        self.assertEqual(self.ui.command("change my phone IncorectNumberFormat"), "Error changing number"

    def test_change_phone_command_no_username(self):
        self.assertEqual(self.ui.command("change phone NewPhoneNumber "), "Error changing number")


    def test_change_adress_command_correct(self):
        self.assertEqual(self.ui.command("change my adress NewAdress"), "adress has been changed")

    def test_change_adress_command_no_adress(self):
        self.assertEqual(self.ui.command("change my adress"), "Error changing adress")

    def test_change_adress_command_no_username(self):
        self.assertEqual(self.ui.command("change adress NewAdress "), "Error changing adress")



    def test_change_Hphone_command_correct(self):
        self.assertEqual(self.ui.command("change my Hphone newPhoneNumber"), "Hphone number has been changed")

    def test_change_Hphone_command_no_number(self):
        self.assertEqual(self.ui.command("change my Hphone"), "Error changing Hnumber")

    def test_change_Hphone_command_no_username(self):
        self.assertEqual(self.ui.command("change Hphone NewPhoneNumber "), "Error changing Hnumber")

    def test_change_Hphone_command_wrong_number_format(self):
        self.assertEqual(self.ui.command("change my Hphone IncorectNumberFormat"), "Error changing Hnumber")


    def test_change_Eadress_command_correct(self):
        self.assertEqual(self.ui.command("change my emailadress NewEmailAdress"), "emailadress has been changed")

    def test_change_Eadress_command_no_adress(self):
        self.assertEqual(self.ui.command("change my emailadress"), "Error changing emailadress")

    def test_change_Eadress_command_no_username(self):
        self.assertEqual(self.ui.command("change emailadress NewEmailAdress "), "Error changing emailadress")
