from unittest import TestCase


class test_AssignInstructorClass(TestCase):

    def setUp(self):
        self.ui.command("createAccount accountName title")

    """
    Type numOfAssigned to check how many classes an instructor is currently assigned to
    type viewSchedule to see the availability schedule

    To assign the class; it takes 3 arguments
    assign className classNumber
    """

    def test_command_password_was_correct(self):
        self.assertEquals(self.ui.command("password"), "You have just entered sendOutNotification system")

    def test_command_password_was_incorrect(self):
        self.assertEquals(self.ui.command("password"), "Password is incorrect,there are 3 more chances to type it")

    def test_command_can_not_view_schedule(self):
        self.assertEquals(self.ui.command("viewSchedule"), "The schedule hasn't been uploaded yet")

    def test_command_can_not_view_assigned(self):
        self.assertEquals(self.ui.command("numOfAssigned"), "Can't view number of classed that are assigned to you")

    def test_command_class_number_invalid(self):
        self.assertEquals(self.ui.command("assign className"), "type the class number")

    def test_command_class_name_invalid(self):
        self.assertEquals(self.ui.command("assign classNumber"), "type the class number")

    def test_command_class_name_number_invalid(self):
        self.assertEquals(self.ui.command("assign"), "type the class number & name")

    def test_command_conflicted_class(self):
        self.assertEquals(self.ui.command("assign className classNumber"), "This class was already assigned")

