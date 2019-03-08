from unittest import TestCase
from Project import Project


class TestProject(TestCase):
    """
    When the createAccount command is entered, it takes two arguments
    -Account Name
    -Account Title
    If the account name is already present in the database then the account is not created and
    and error message is displayed
    Elizabeth -- don't we need to include a bunch more arguments in this now? Or are we leaving it up
    to the user to fill in all their info after their account is created?
    """
    def setUp(self):
        self.Project = Project()

    def test_command_createAccount_success(self):
        self.assertEqual(self.Project.command(""), "Account successfully created")

    def test_command_createAccount_no_title(self):
        self.assertEqual(self.Project.command("createAccount accountName"), "Please specify a title")

    def test_command_createAccount_invalidTitle(self):
        self.assertEqual(self.Project.command("createAccount accountName cashier"), "Please enter a valid title")

    def test_command_createAccount_no_name(self):
        self.assertEqual(self.Project.command("createAccount title"), "Need to specify a name")

    def test_command_createAccount_no_args(self):
        self.assertEqual(self.Project.command("createAccount"), "Please enter a name and title")

    def test_command_createAccount_already_exists(self):
        self.assertEqual(self.Project.command("createAccount accountName title"), "Account already exists")

        """
           When the createCourse command is entered, it takes one argument:
           -Course Name 
           -Course Number 
           -Days of week
           -Time of class (start end)
           If the course name matches a database entry a then the course is not created 
           and an error message is displayed and some other stuff
           Alex - I think this is all we need.
           Natasha - I think createCourse needs to include course numbers, days of the week and time periods (or online), 
           as arguments. Even though we aren't dealing with scheduling conflicts, times of courses are important
           course information. I don't think they should be allowed to be created without that information.
           Elizabeth -- I added some fields. 
       """

    def test_command_createCourse_success(self):
        self.assertEqual(self.Project.command("createCourse courseName courseNumber daysOfWeek start end"),
                         "Course successfully created")

    def test_command_createCourse_no_course_name(self):
        self.assertEqual(self.Project.command("createCourse courseNumber daysOfWeek start end"),
                         "You must enter a course name to create a course")

    def test_command_createCourse_no_course_number(self):
        self.assertEqual(self.Project.command("createCourse courseName daysOfWeek start end"),
                         "You must enter a course number to create a course")

    def test_command_createCourse_no_daysOfWeek(self):
        self.assertEqual(self.Project.command("createCourse courseName courseNumber start end"),
                         "You must enter a meeting days to create a course")

    def test_command_createCourse_no_start_time(self):
        self.assertEqual(self.Project.command("createCourse courseName courseNumber daysOfWeek end"),
                         "You must enter a start time to create a course")

    def test_command_createCourse_no_end_time(self):
        self.assertEqual(self.Project.command("createCourse courseName courseNumber daysOfWeek start"),
                         "You must enter an end time to create a course")

    def test_command_createCourse_no_args(self):
        self.assertEqual(self.Project.command("createCourse"), "Please specify a course name, course number, "
                                                               "meeting days, and start and end times")

    def test_command_createCourse_course_exists(self):
        self.assertEqual(self.Project.command("createCourse courseName courseNumber daysOfWeek start end"),
                         "Course already exists")



        """
           When the createLab command is entered, it takes the following arguments:
           -Course number associated with
           -Lab section number
           -Day(s) of week
           -Begin time
           -End time
           If the lab already exists, a new lab is not created. If arguments are missing, return error. If the 
           associated course is online, a lab cannot be created for it.
       """

    def test_command_createLab_success(self):
        self.assertEqual(self.Project.command("createLab courseNumber labSection day begin end"), "Course successfully created")

    def test_command_createLab_no_args(self):
        self.assertEqual(self.Project.command("createLab"), "Please specify a course number, lab section number, and meeting times")

    def test_command_createLab_lab_exists(self):
        self.assertEqual(self.Project.command("createLab courseNumber labSection day begin end"), "Lab already exists")

    def test_command_createLab_missing_course(self):
        self.assertEqual(self.Project.command("createLab labSection day begin end"), "Please specify the course the lab is associated with.")

    def test_command_createLab_missing_section(self):
        self.assertEqual(self.Project.command("createLab courseNumber day begin end"), "Please specify the lab section number.")

    def test_command_createLab_missing_day(self):
        self.assertEqual(self.Project.command("createLab courseNumber labSection begin end"), "Please specify meeting day.")

    def test_command_createLab_missing_begin(self):
        self.assertEqual(self.Project.command("createLab courseNumber labSection day end"), "Please specify begin time.")

    def test_command_createLab_missing_end(self):
        self.assertEqual(self.Project.command("createLab courseNumber labSection day begin"), "Please specify end time.")

    def test_command_createLab_invalid_lab(self):
        self.assertEqual(self.Project.command("createLab courseNumber labSection day begin end"), "Lab cannot be created for an online course.")

    """
        Edit Information 
       Alex- These tests should test whatever command we are using to edit account information. "find" is currently
       not a command that we are supporting. 
       - Now that I look at this, its kind of big. Maybe we should think about breaking this up.  
       This also isn't properly setup for the unittest framework but I dont think that matters since we are not
       running it
       Elizabeth - I think these tests go beyond the scope of the base command -- really what should be tested here 
       is simply the "editInformation" command, I don't think we need to go in depth and make separate commands for
       editing all the different fields at this time.  
       """

    def test_find_command_correct(self):
        self.assertEqual(self.Project.command("find username"), "account exists")

    def test_find_command_no_username(self):
        self.assertEqual(self.Project.command("find "), "no such account exists")

    def test_find_command_invalid_username(self):
        self.assertEqual(self.Project.command("find InexistantAccount"), "no such account exists")

    def test_change_phone_command_correct(self):
        self.assertEqual(self.Project.command("change username phone newPhoneNumber"), "phone number has been changed")

    def test_change_phone_command_no_number(self):
        self.assertEqual(self.Project.command("change username phone"), "Error changing number")

    def test_change_phone_command_invalid_username(self):
        self.assertEqual(self.Project.command("change InexistantAccount phone newPhoneNumber "), "Error changing number")

    def test_change_phone_command_no_username(self):
        self.assertEqual(self.Project.command("change phone NewPhoneNumber "), "Error changing number")

    def test_change_phone_command_wrong_number_format(self):
        self.assertEqual(self.Project.command("change username phone IncorectNumberFormat"), "Error changing number")

    def test_change_address_command_correct(self):
        self.assertEqual(self.Project.command("change username adress NewAdress"), "adress has been changed")

    def test_change_address_command_no_adress(self):
        self.assertEqual(self.Project.command("change username adress"), "Error changing adress")

    def test_change_address_command_invalid_username(self):
        self.assertEqual(self.Project.command("change InexistantAccount adress newAdress "), "Error changing adress")

    def test_change_address_command_no_username(self):
        self.assertEqual(self.Project.command("change adress NewAdress "), "Error changing adress")

    def test_change_name_command_correct(self):
        self.assertEqual(self.Project.command("change username name NewName"), "Name has been changed")

    def test_change_name_command_no_name(self):
        self.assertEqual(self.Project.command("change username name"), "Error changing name")

    def test_change_name_command_invalid_username(self):
        self.assertEqual(self.Project.command("change InexistantAccount name newName "), "Error changing name")

    def test_change_name_command_no_username(self):
        self.assertEqual(self.Project.command("change name NewName "), "Error changing name")

    def test_change_title_command_correct(self):
        self.assertEqual(self.Project.command("change username title NewTitle"), "adress has been changed")

    def test_change_title_command_no_adress(self):
        self.assertEqual(self.Project.command("change username title"), "Error changing adress")

    def test_change_title_command_invalid_username(self):
        self.assertEqual(self.Project.command("change InexistantAccount title newTitle "), "Error changing adress")

    def test_change_title_command_no_username(self):
        self.assertEqual(self.Project.command("change title NewTitle "), "Error changing adress")

    def test_change_Hphone_command_correct(self):
        self.assertEqual(self.Project.command("change username Hphone newPhoneNumber"), "Hphone number has been changed")

    def test_change_Hphone_command_no_number(self):
        self.assertEqual(self.Project.command("change username Hphone"), "Error changing Hnumber")

    def test_change_Hphone_command_invalid_username(self):
        self.assertEqual(self.Project.command("change InexistantAccount Hphone newPhoneNumber "), "Error changing Hnumber")

    def test_change_Hphone_command_no_username(self):
        self.assertEqual(self.Project.command("change Hphone NewPhoneNumber "), "Error changing Hnumber")

    def test_change_Hphone_command_wrong_number_format(self):
        self.assertEqual(self.Project.command("change username Hphone IncorectNumberFormat"), "Error changing Hnumber")

    def test_addclass_command_correct(self):
        self.assertEqual(self.Project.command("add class username classname"), "class added")

    def test_addclass_command_no_username(self):
        self.assertEqual(self.Project.command("add class classname"), "no such account exists")

    def test_addclass_command_invalid_username(self):
        self.assertEqual(self.Project.command("add class InexistantAccount classname"), "no such account exists")

    def test_addclass_command_invalid_class(self):
        self.assertEqual(self.Project.command("add class username InexistantClassname"), "no such class exists")

    def test_addclass_command_invalid_class(self):
        self.assertEqual(self.Project.command("add class username addedClassname"), "class has already been added")

    def test_removeclass_command_correct(self):
        self.assertEqual(self.Project.command("remove class username classname"), "class removed")

    def test_removeclass_command_no_username(self):
        self.assertEqual(self.Project.command("remove class classname "), "no such account exists")

    def test_removeclass_command_invalid_username(self):
        self.assertEqual(self.Project.command("remove class InexistantAccount classname"), "no such account exists")

    def test_removeclass_command_invalid_classname(self):
        self.assertEqual(self.Project.command("remove class username InexistantClassname"), "no such class exists")

    def test_removeclass_command_invalid_classname2(self):
        self.assertEqual(self.Project.command("remove class username unaddedClassname"), "no such class has been added here")

    def test_change_Eadress_command_correct(self):
        self.assertEqual(self.Project.command("change username emailadress NewEmailAdress"), "emailadress has been changed")

    def test_change_Eadress_command_no_adress(self):
        self.assertEqual(self.Project.command("change username emailadress"), "Error changing emailadress")

    def test_change_Eadress_command_invalid_username(self):
        self.assertEqual(self.Project.command("change InexistantAccount emailadress newEmailAdress "),
                         "Error changing emailadress")

    def test_change_Eadress_command_no_username(self):
        self.assertEqual(self.Project.command("change emailadress NewEmailAdress "), "Error changing emailadress")

    """
    When the user type the command sendOutNotification
    It will ask you the password first
    Once you successfully login
    It takes 2-3 arguments

    sendNotification -a
    To send notification to all users.

    sendNotification accountNames -s
    To send notification to specific users.
    UserNames can be written as userName, userName form.

    sendNotification  accountName

    to send notification to one person
    
    Elizabeth -- we don't need to worry about password access here - just the "sendOutNotification" command 
    """

    def test_command_password_was_correct(self):
        self.assertEqual(self.Project.command("password"), "You have just entered sendOutNotification system")

    def test_command_password_was_incorrect(self):
        self.assertEqual(self.Project.command("password"), "Password is incorrect, there are 3 more chances to type it")

    def test_command_notification_was_not_sent(self):
        self.assertEqual(self.Project.command("sendNotification accountName"), "We weren't able to send a notification")

    def test_command_notification_was_not_sent_all(self):
        self.assertEqual(self.Project.command("sendNotification accountName -a"), "We weren't able to send a notification")

    def test_command_notification_was_not_sent_specific(self):
        self.assertEqual(self.Project.command("sendNotification accountNames -s"), "We weren't able to send a notification")

    def test_command_no_argument(self):
        self.assertEqual(self.Project.command("sendNotification"), "Please type the email that you want to sent")

        """
           When the deleteAccount command is entered, it takes two arguments, 
            -name 
            -title
           If a name or title is missing, an error message is displayed
           If the account that the user is trying to delete does not exist, an error 
           message is displayed. 
           Alex- I feel like this command should only need one argument, the name.
           Natasha - I agree that this command should only require the username. 
           Elizabeth - that's fine it can be changed, I was thinking it would be easier to locate the 
           account given what type of account it is 
        """

    def test_command_deleteAccount(self):
            self.assertEqual(self.Project.command("deleteAccount name title"), "Account successfully deleted")

    def test_command_deleteAccount_no_title(self):
            self.assertEqual(self.Project.command("deleteAccount name"), "Need to specify a title")

    def test_command_deleteAccount_no_name(self):
            self.assertEqual(self.Project.command("deleteAccount title"), "Need to specify a name")

    def test_command_deleteAccount_no_args(self):
            self.assertEqual(self.Project.command("deleteAccount"), "Please enter a name and title")

    def test_command_deleteAccount_doesNotExist(self):
            self.assertEqual(self.Project.command("deleteAccount name title"), "Account does not exist")

    """
       When the AccessAllData command is entered, it takes one argument, 
       - name
       If no name is entered, an error is displayed 
       If user does not exist, an error is displayed
       Alex - I believe AccessAllData should print all of the data for an account - the password
       rather than just saying "account found" it should probably print off all of the data in an easy to read format 
       Natasha - I also think that it should display all of the data.
       Elizabeth -- Of course it needs to display all data - I was thinking that could happen via a different 
       medium though (the command would return the "accountfound" response then some background method would display 
       the data), not just a long string representation of all the data as the response.  Either way is cool. 
       --we also might want to have this take a title field too, for ease of finding the data later on, assuming we
       are storing TAs separately. 
    """

    def test_command_AccessAllData_success(self):
        self.assertEqual(self.Project.command("AccessAllData name"), "Account found!")

    def test_command_AccessAllData_noname(self):
        self.assertEqual(self.Project.command("AccessAllData"), "No name was entered, error")

    def test_command_AccessAllData_no_such_user(self):
        self.assertEqual(self.Project.command("AccessAllData name"), "User does not exist")

    """
        Type numOfAssigned to check how many classes an instructor is currently assigned to
        type viewSchedule to see the availability schedule

        To assign the class; it takes 3 arguments
        assign className classNumber
        Alex - Logging in with a password is a completely different feature that we currently do not support. I think
        that if we did have a login command it would be preformed in the setup section rather than the tests. Example
        self.ui.command("createAccount accountName title")
        self.ui.command("editAccount accountName password newPassword")
        self.ui.command("login accountName newPassword")
        These tests should only test assigning an instructor to a class and really nothing else.
        The same goes for  viewing schedule and assigned classes.
        Natasha - Logging in should be separate. Maybe we'll figure that out with design. Ideally, no one would be
        able to access the application until they have signed in and would only be able to run commands based on 
        their privilege.
        Elizabath -- I don't think we should worry about extra commands like numOfAssigned and viewSchedule here - just
        the assignClass command 
        """

    def test_command_password_was_correct(self):
        self.assertEqual(self.Project.command("password"), "You have just entered sendOutNotification system")

    def test_command_password_was_incorrect(self):
        self.assertEqual(self.Project.command("password"), "Password is incorrect,there are 3 more chances to type it")

    def test_command_can_not_view_schedule(self):
        self.assertEqual(self.Project.command("viewSchedule"), "The schedule hasn't been uploaded yet")

    def test_command_can_not_view_assigned(self):
        self.assertEqual(self.Project.command("numOfAssigned"), "Can't view number of classed that are assigned to you")

    def test_command_class_number_invalid(self):
        self.assertEqual(self.Project.command("assign className"), "type the class number")

    def test_command_class_name_invalid(self):
        self.assertEqual(self.Project.command("assign classNumber"), "type the class number")

    def test_command_class_name_number_invalid(self):
        self.assertEqual(self.Project.command("assign"), "type the class number & name")

    def test_command_conflicted_class(self):
        self.assertEqual(self.Project.command("assign className classNumber"), "This class was already assigned")

    """
           When AssignTACourse command is entered, it takes two arguments:
               --TA username
               --Course number
           Assignment may fail if:
               --Scheduling conflict for TA
               --Max TAs assigned to course
               --TA username is invalid or missing
               --Course number is invalid or missing
               --No arguments
           Alex - We don't have worry about scheduling conflicts for our program. That test is unneeded
       """

    def test_command_AssignTACourse_success(self):
        self.assertEqual(self.Project.command("AssignTACourse accountName  courseNumber"), "Assignment successful")

    def test_command_AssignTACourse_missingTA(self):
        self.assertEqual(self.Project.command("createAccount title"), "Missing TA Username.")

    def test_command_AssignTACourse_invalidTA(self):
        self.assertEqual(self.Project.command("AssignTACourse accountName  courseNumber"), "Invalid TA username.")

    def test_command_AssignTACourse_missingCourse(self):
        self.assertEqual(self.Project.command("AssignTACourse accountName"), "Missing course number.")

    def test_command_AssignTACourse_invalidCourse(self):
        self.assertEqual(self.Project.command("AssignTACourse accountName  courseNumber"), "Invalid course number.")

    def test_command_AssignTACourse_Maximum(self):
        self.assertEqual(self.Project.command("AssignTACourse accountName  courseNumber"), "Maximum TAs assigned to course.")

    def test_command_AssignTACourse_schedulingConflict(self):
        self.assertEqual(self.Project.command("AssignTACourse accountName  courseNumber"), "Scheduling conflict.")

    def test_command_AssignTACourse_noArgs(self):
        self.assertEqual(self.Project.command("AssignTACourse"), "Missing TA username and course number.")

    """
             When the vpd command is entered is takes one argument 
             -account Name
             If the name entered does not match one in the database an error is displayed
             other wise all of the account information that is public will be displayed
        """

    def test_command_vpd_success(self):
        self.assertEqual(self.Project.command("vpd accountName"), "Name: accountName"
                                                              "email: accountEmail"
                                                              "Office: officeNumber"
                                                              "Phone: officePhone"
                                                              "Office Hours: officeHours")

    def test_command_vps_no_account(self):
        self.assertEqual(self.Project.command("vpd invalidAccount"), "Account does not exist")

    def test_command_vps_no_args(self):
        self.assertEqual(self.Project.command("vpd"), "Please specify and account name")

        """
        Edit own contact information starts here
        Elizabeth -- I think that all the specific commands are out of our scope, we should just be testing the 
        "editMyInformation" command
        """

    def test_change_phone_command_correct(self):
        self.assertEqual(self.Project.command("change my phone newPhoneNumber"), "phone number has been changed")

    def test_change_phone_command_no_number(self):
        self.assertEqual(self.Project.command("change my phone"), "Error changing number")

    def test_change_phone_command_wrong_number_format(self):
        self.assertEqual(self.Project.command("change my phone IncorectNumberFormat"), "Error changing number")

    def test_change_phone_command_no_username(self):
        self.assertEqual(self.Project.command("change phone NewPhoneNumber "), "Error changing number")

    def test_change_adress_command_correct(self):
        self.assertEqual(self.Project.command("change my adress NewAdress"), "adress has been changed")

    def test_change_adress_command_no_adress(self):
        self.assertEqual(self.Project.command("change my adress"), "Error changing adress")

    def test_change_adress_command_no_username(self):
        self.assertEqual(self.Project.command("change adress NewAdress "), "Error changing adress")

    def test_change_Hphone_command_correct(self):
        self.assertEqual(self.Project.command("change my Hphone newPhoneNumber"), "Hphone number has been changed")

    def test_change_Hphone_command_no_number(self):
        self.assertEqual(self.Project.command("change my Hphone"), "Error changing Hnumber")

    def test_change_Hphone_command_no_username(self):
        self.assertEqual(self.Project.command("change Hphone NewPhoneNumber "), "Error changing Hnumber")

    def test_change_Hphone_command_wrong_number_format(self):
        self.assertEqual(self.Project.command("change my Hphone IncorectNumberFormat"), "Error changing Hnumber")

    def test_change_Eadress_command_correct(self):
        self.assertEqual(self.Project.command("change my emailadress NewEmailAdress"), "emailadress has been changed")

    def test_change_Eadress_command_no_adress(self):
        self.assertEqual(self.Project.command("change my emailadress"), "Error changing emailadress")

    def test_change_Eadress_command_no_username(self):
        self.assertEqual(self.Project.command("change emailadress NewEmailAdress "), "Error changing emailadress")

    """
      When the user type the command viewCourseAssignments,
      User needs to enter the password to see the schedule
          The command for view my schedule :viewMySchedule
       For searching the the assignments for other professors;
       It takes 2 arguments to search;
       search accountName
       Alex - Logging in with a password is a completely different feature that we currently do not support. I think
       that if we did have a login command it would be preformed in the setup section rather than the tests. Example
       self.ui.command("createAccount accountName title")
       self.ui.command("editAccount accountName password newPassword")
       self.ui.command("login accountName newPassword")
       The command you should be focusing on here is viewCourseAssignments 
       Elizabeth -- we don't need to test for passwords here or have a search command, just the "viewCourseAssignments"
       command 
       """

    def test_command_password_was_correct(self):
        self.assertEqual(self.Project.command("password"), "You have just entered sendOutNotification system")

    def test_command_password_was_incorrect(self):
        self.assertEqual(self.Project.command("password"), "Password is incorrect, there are 3 more chances to type it")

    def test_command_password_was_incorrect_3times(self):
        self.assertEqual(self.Project.command("password"), "Password is incorrect for 3 times contact to administrator")

    def test_command_can_not_view_my_schedule(self):
        self.assertEqual(self.Project.command("viewMySchedule"), "The schedule hasn't been uploaded yet")

    def test_command_cannot_find_name(self):
        self.assertEqual(self.Project.command("search accountName"), "Can't fine the name of the professor, retype it")

    def test_command_username_not_typed(self):
        self.assertEqual(self.Project.command("search"), "Type the username")

    """
       When the ViewTAAssignments command is entered, it takes one argument
       - class Number 

       If the class Number is not entered, an error message is displayed
       If the class does not exist, an error message is displayed 

       """

    def test_command_ViewTAAssignments_success(self):
        self.assertEqual(self.Project.command("ViewTAAssignments classNumber"), "The TA Assignments are: ")

    def test_command_ViewTAAssignments_noClassNum(self):
        self.assertEqual(self.Project.command("ViewTAAssignments"), "Error, no class number entered")

    def test_command_ViewTAAssignments_classDoesNotExist(self):
        self.assertEqual(self.Project.command("ViewTAAssignments classNumber"), "Class does not exist")
