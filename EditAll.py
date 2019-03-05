import unittest

class findaccounts(unittest.TestCase):
    def setUp(self):
        self.ui.command("create username Title Name Pawssowrd Phone Adress Email")
        self.ui.command("change username title newTitle")
        self.ui.command("find username")
        self.ui.command("change username name newName")
        self.ui.command("change username password newPassword")
        self.ui.command("change username phone newPhoneNumber")
        self.ui.command("change username Hphone newHPhoneNumber")
        self.ui.command("change username adress newAdress")
        self.ui.command("change username emailadress NewEmailAdress")
        self.ui.command("add class username classname")
        self.ui.command("remove class username classname")

    def test_find_command_correct(self):
        self.assertEqual(self.ui.command("find username"), "account exists")

    def test_find_command_no_username(self):
        self.assertEqual(self.ui.command("find "), "no such account exists")

    def test_find_command_invalid_username(self):
            self.assertEqual(self.ui.command("find InexistantAccount"), "no such account exists")


    def test_change_phone_command_correct(self):
        self.assertEqual(self.ui.command("change username phone newPhoneNumber"), "phone number has been changed")

    def test_change_phone_command_no_number(self):
        self.assertEqual(self.ui.command("change username phone"), "Error changing number")

    def test_change_phone_command_invalid_username(self):
        self.assertEqual(self.ui.command("change InexistantAccount phone newPhoneNumber "), "Error changing number")

    def test_change_phone_command_no_username(self):
        self.assertEqual(self.ui.command("change phone NewPhoneNumber "), "Error changing number")

    def test_change_phone_command_wrong_number_format(self):
        self.assertEqual(self.ui.command("change username phone IncorectNumberFormat"), "Error changing number")


    def test_change_adress_command_correct(self):
        self.assertEqual(self.ui.command("change username adress NewAdress"), "adress has been changed")

    def test_change_adress_command_no_adress(self):
        self.assertEqual(self.ui.command("change username adress"), "Error changing adress")

    def test_change_adress_command_invalid_username(self):
        self.assertEqual(self.ui.command("change InexistantAccount adress newAdress "), "Error changing adress")

    def test_change_adress_command_no_username(self):
        self.assertEqual(self.ui.command("change adress NewAdress "), "Error changing adress")


    def test_change_name_command_correct(self):
        self.assertEqual(self.ui.command("change username name NewName"), "Name has been changed")

    def test_change_name_command_no_name(self):
        self.assertEqual(self.ui.command("change username name"), "Error changing name")

    def test_change_name_command_invalid_username(self):
        self.assertEqual(self.ui.command("change InexistantAccount name newName "), "Error changing name")

    def test_change_name_command_no_username(self):
        self.assertEqual(self.ui.command("change name NewName "), "Error changing name")


    def test_change_title_command_correct(self):
        self.assertEqual(self.ui.command("change username title NewTitle"), "adress has been changed")

    def test_change_title_command_no_adress(self):
        self.assertEqual(self.ui.command("change username title"), "Error changing adress")

    def test_change_title_command_invalid_username(self):
        self.assertEqual(self.ui.command("change InexistantAccount title newTitle "), "Error changing adress")

    def test_change_title_command_no_username(self):
        self.assertEqual(self.ui.command("change title NewTitle "), "Error changing adress")


    def test_change_Hphone_command_correct(self):
        self.assertEqual(self.ui.command("change username Hphone newPhoneNumber"), "Hphone number has been changed")

    def test_change_Hphone_command_no_number(self):
        self.assertEqual(self.ui.command("change username Hphone"), "Error changing Hnumber")

    def test_change_Hphone_command_invalid_username(self):
        self.assertEqual(self.ui.command("change InexistantAccount Hphone newPhoneNumber "), "Error changing Hnumber")

    def test_change_Hphone_command_no_username(self):
        self.assertEqual(self.ui.command("change Hphone NewPhoneNumber "), "Error changing Hnumber")

    def test_change_Hphone_command_wrong_number_format(self):
        self.assertEqual(self.ui.command("change username Hphone IncorectNumberFormat"), "Error changing Hnumber")


    def test_addclass_command_correct(self):
        self.assertEqual(self.ui.command("add class username classname"), "class added")

    def test_addclass_command_no_username(self):
        self.assertEqual(self.ui.command("add class classname"), "no such account exists")

    def test_addclass_command_invalid_username(self):
        self.assertEqual(self.ui.command("add class InexistantAccount classname"), "no such account exists")

    def test_addclass_command_invalid_class(self):
        self.assertEqual(self.ui.command("add class username InexistantClassname"), "no such class exists")

    def test_addclass_command_invalid_class(self):
        self.assertEqual(self.ui.command("add class username addedClassname"), "class has already been added")


    def test_removeclass_command_correct(self):
        self.assertEqual(self.ui.command("remove class username classname"), "class removed")

    def test_removeclass_command_no_username(self):
        self.assertEqual(self.ui.command("remove class classname "), "no such account exists")

    def test_removeclass_command_invalid_username(self):
        self.assertEqual(self.ui.command("remove class InexistantAccount classname"), "no such account exists")

    def test_removeclass_command_invalid_classname(self):
        self.assertEqual(self.ui.command("remove class username InexistantClassname"), "no such class exists")

    def test_removeclass_command_invalid_classname2(self):
        self.assertEqual(self.ui.command("remove class username unaddedClassname"), "no such class has been added here")


    def test_change_Eadress_command_correct(self):
        self.assertEqual(self.ui.command("change username emailadress NewEmailAdress"), "emailadress has been changed")

    def test_change_Eadress_command_no_adress(self):
        self.assertEqual(self.ui.command("change username emailadress"), "Error changing emailadress")

    def test_change_Eadress_command_invalid_username(self):
        self.assertEqual(self.ui.command("change InexistantAccount emailadress newEmailAdress "), "Error changing emailadress")

    def test_change_Eadress_command_no_username(self):
        self.assertEqual(self.ui.command("change emailadress NewEmailAdress "), "Error changing emailadress")
