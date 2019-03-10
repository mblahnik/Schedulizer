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
           When the createCourse command is entered, it takes four arguments:
           -Course Name 
           -Course Number 
           -Meetings days or "online" for an online class
           -Time of class (start, end)
           
           If the course name matches a database entry a then the course is not created 
           and an error message is displayed and some other stuff
           
           If a command argument is missing, an error message is displayed. 
           
           
           Alex - I think this is all we need.
           Natasha - I think createCourse needs to include course numbers, days of the week and time periods (or online), 
           as arguments. Even though we aren't dealing with scheduling conflicts, times of courses are important
           course information. I don't think they should be allowed to be created without that information.
           Elizabeth -- I added some fields. 
           Eonshik  - I think it would be better if we add more information like description of courses,
            name of instructors and the units of the courses.
            
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
           -Course number associated with the lab 
           -Lab section number
           -Day(s) of week
           -Begin time
           -End time
           If the lab already exists, a new lab is not created. If arguments are missing, return error. If the 
           associated course is online, a lab cannot be created for it.
       """

    def test_command_createLab_success(self):
        self.assertEqual(self.Project.command("createLab courseNumber labSection day begin end"),
                         "Course successfully created")

    def test_command_createLab_no_args(self):
        self.assertEqual(self.Project.command("createLab"),
                         "Please specify a course number, lab section number, and meeting times")

    def test_command_createLab_lab_exists(self):
        self.assertEqual(self.Project.command("createLab courseNumber labSection day begin end"),
                         "Lab already exists")

    def test_command_createLab_missing_course(self):
        self.assertEqual(self.Project.command("createLab labSection day begin end"),
                         "Please specify the course the lab is associated with.")

    def test_command_createLab_missing_section(self):
        self.assertEqual(self.Project.command("createLab courseNumber day begin end"),
                         "Please specify the lab section number.")

    def test_command_createLab_missing_day(self):
        self.assertEqual(self.Project.command("createLab courseNumber labSection begin end"),
                         "Please specify meeting day.")

    def test_command_createLab_missing_begin(self):
        self.assertEqual(self.Project.command("createLab courseNumber labSection day end"),
                         "Please specify begin time.")

    def test_command_createLab_missing_end(self):
        self.assertEqual(self.Project.command("createLab courseNumber labSection day begin"),
                         "Please specify end time.")

    def test_command_createLab_invalid_lab(self):
        self.assertEqual(self.Project.command("createLab courseNumber labSection day begin end"),
                         "Lab cannot be created for an online course.")

    """
        When the edit command is entered, it takes 4 arguments.
        Only supervisors and administrators can utilize this command
        -Username
        -Field that needs editing 
            - Home phone
            - Email 
            - Office hours (a start time, an end time and days of office hours) 
            - Address 
            - Office Number
            - Office phone Number 
        -Updated information 
        
        If the user does not exist, an error message is displayed.
        If command arguments are missing, an error message is displayed. 
    
       """

    def test_command_edit_homePhone_success(self):
        self.asserEqual(self.Project.command("edit username homephone 262-555-7134"), "Home phone successfully updated")

    def test_command_edit_email_success(self):
        self.assertEqual(self.Project.command("edit username email timmy345@uwm.edu"), "Email successfully updated")

    def test_command_edit_office_hours_success(self):
        self.assertEqual(self.Project.command("edit username officehours 1500 1600 MW"), "Office hours successfully updated")

    def test_command_edit_address_success(self):
        self.assertEqual(self.Project.command("edit username address 6789 Hilly Avenue Milwaukee WI 53218"),
                "Address successfully updated")

    def test_command_edit_officeNumber_success(self):
        self.assertEqual(self.Project.command("edit username officeNumber 5679"), "Office number successfully updated")

    def test_command_edit_officePhone_success(self):
        self.assertEqual(self.Project.command("edit username officePhone 262-789-5476"), "Office phone successfully updated")

    def test_command_edit_error_missing_args1(self):
        self.assertEqual(self.Project.command("edit"), "There are missing arguments in your command. Please enter your "
                "command in the following format: edit username field newInformation")

    def test_command_edit_error_missing_args2(self):
        self.assertEqual(self.Project.command("edit username"), "There are missing arguments in your command, Please "
                "enter you command in the following format: edit username field newInformation")

    def test_command_edit_error_missing_args3(self):
        self.assertEqual(self.Project.command("edit username homephone"), "There are missing arguments in your command, Please "
                "enter you command in the following format: edit username field newInformation")

    def test_command_edit_error_user_does_not_exist(self):
        self.assertEqual(self.Project.command("edit username homephone 262-555-7134"), "The user you specified does not"
                 "exist in the system, please try again")



    """
    sendOutNotification command 
    When the sendOutNotification command is entered it takes 2-3 arguments: 

    -sendNotification -a
    To send notification to all users.

    -sendNotification accountNames -s
    To send notification to specific users.

    -sendNotification  accountName
    to send notification to one person
    
    Elizabeth -- we don't need to worry about password access here - just the "sendOutNotification" command 
    
    Eonshik - I removed password part and add more tests.
    
    Elizabeth -- The send out to specific users option implies that this command could have endless arguments - do we 
    want to deal with that? 
    
    """

    def test_command_notification(self):
        self.assertEqual(self.Project.command("sendNotification accountName"), "Notification was sent successfully")

    def test_command_notification_was_sent_all(self):
        self.assertEqual(self.Project.command("sendNotification -a"), "Notification was sent to all  successfully")

    def test_command_notification_was_sent_specific(self):
        self.assertEqual(self.Project.command("sendNotification accountName(s) -s"),
                         "Notification was sent to specific people successfully")

    def test_command_notification_was_not_sent(self):
        self.assertEqual(self.Project.command("sendNotification accountName"), "We weren't able to send a notification")

    def test_command_notification_was_not_sent_all(self):
        self.assertEqual(self.Project.command("sendNotification accountName -a"),
                         "We weren't able to send a notification to all")

    def test_command_notification_was_not_sent_specific(self):
        self.assertEqual(self.Project.command("sendNotification accountNames -s"),
                         "We weren't able to send a notification to specific people")

    def test_command_no_argument(self):
        self.assertEqual(self.Project.command("sendNotification -s"), "Please type the user names that you want to sent")

    def test_command_no_argument_2(self):
            self.assertEqual(self.Project.command("sendNotification -a"),
                             "Please type the user names  that you want to sent")

    def test_command_no_argument_3(self):
        self.assertEqual(self.Project.command("sendNotification"), "Please type the username that you want to sent")




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
           Eonshik - I think the argument "name" need be changed "userName" to make the the argument command consistent.
          Don't we need to consider the case if there are two users have the same user name?
           
        """

    def test_command_deleteAccount(self):
            self.assertEqual(self.Project.command("deleteAccount userName title"), "Account successfully deleted")

    def test_command_deleteAccount_no_title(self):
            self.assertEqual(self.Project.command("deleteAccount userName"), "Need to specify a title")

    def test_command_deleteAccount_no_name(self):
            self.assertEqual(self.Project.command("deleteAccount title"), "Need to specify a userName")

    def test_command_deleteAccount_no_args(self):
            self.assertEqual(self.Project.command("deleteAccount"), "Please enter a name and title")

    def test_command_deleteAccount_doesNotExist(self):
            self.assertEqual(self.Project.command("deleteAccount userName title"), "Account does not exist")



        """
        Type numOfAssigned to check how many classes an instructor is currently assigned to
        type viewSchedule to see the availability schedule

        When the assignInstructorCourse command is entered it takes 3 arguments: 
        - className
        - class Number
        - Instructor user Name
        
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
        Elizabeth -- I don't think we should worry about extra commands like numOfAssigned and viewSchedule here - just
        the assignClass command 
        Eonshik - some test removed and add more tests
        Elizabeth -- I added a username field to this command so they can specify who they want to be assigned to the class
        also changed the command name to assignInstructorCourse so it matches the assignTACourse below. 
        """

        """
        Elizabeth -- I don't think we need to worry about these two tests here, otherwise we are adding extra commands, just
        worry about testing the assign command. 
   
            def test_command_can_not_view(self):
                self.assertEqual(self.Project.command("viewSchedule"), "The schedule hasn't been uploaded yet")

            def test_command_can_not_view_assigned(self):
                self.assertEqual(self.Project.command("numOfAssigned"), "Can't view number of classed that are assigned to you")
        
        """

    def test_command__assignInstructorCourse_class_number_missing(self):
        self.assertEqual(self.Project.command("assignInstructorCourse className userName"), "Class Number is missing")

    def test_command_assignInstructorCourse_class_name_missing(self):
        self.assertEqual(self.Project.command("assignInstructorCourse classNumber userName"), "Class Name is missing")

    def test_command_assignInstructorCourse_no_userName(self):
        self.assertEqual(self.Project.command("assignInstructorCourse className classNumber"), "Username is missing")

    def test_command_assignInstructorCourse_no_args(self):
        self.assertEqual(self.Project.command("assignInstructorCourse"), "Please provide the class name, class number and the "
                                                              "username of who you want to assign to the class")
    """
    Elizabeth -- do we need to worry about conflicts? 
    def test_command_conflicted_class(self):
        self.assertEqual(self.Project.command("assign className classNumber"), "This class was already assigned")
    """

    def test_command_assignInstructorCourse_success(self):
        self.assertEqual(self.Project.command("assignInstructorCourse className classNumber userName"), "Assignment was successful")

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
        self.assertEqual(self.Project.command("AssignTACourse accountName courseNumber"), "Assignment successful")

    def test_command_AssignTACourse_missingTA(self):
        self.assertEqual(self.Project.command("createAccount title"), "Missing TA Username.")

    def test_command_AssignTACourse_invalidTA(self):
        self.assertEqual(self.Project.command("AssignTACourse accountName  courseNumber"), "Invalid TA username.")

    def test_command_AssignTACourse_missingCourse(self):
        self.assertEqual(self.Project.command("AssignTACourse accountName"), "Missing course number.")

    def test_command_AssignTACourse_invalidCourse(self):
        self.assertEqual(self.Project.command("AssignTACourse accountName  courseNumber"), "Invalid course number.")

    def test_command_AssignTACourse_Maximum(self):
        self.assertEqual(self.Project.command("AssignTACourse accountName  courseNumber"),
                         "Maximum TAs assigned to course.")

    def test_command_AssignTACourse_schedulingConflict(self):
        self.assertEqual(self.Project.command("AssignTACourse accountName  courseNumber"), "Scheduling conflict.")

    def test_command_AssignTACourse_noArgs(self):
        self.assertEqual(self.Project.command("AssignTACourse"), "Missing TA username and course number.")



        """
    
        When the viewPublicData command is entered it takes one argument: 
        -accountName 
        
        If the account does not exist, an error message is displayed, otherwise, public data is displayed
      
        """



    def test_command_viewPublicData_success(self):
        self.asserEqual(self.Project.command("viewPublicData accountName"),"Name: accountName"
                                                              "email: accountEmail"
                                                              "Office: officeNumber"
                                                              "Phone: officePhone"
                                                              "Office Hours: officeHours")

    def test_command_viewPublicData_user_does_not_exist(self):
        self.asserEqual(self.Project.command("viewPublicData accountName"), "Account does not exist")

    def test_command_viewPublicData_no_accountName(self):
        self.assertEqual(self.Project.command("viewPUblicData"), "Please enter account name to view data")


        """
        
        Edit own contact information starts here
        Elizabeth -- I think that all the specific commands are out of our scope, we should just be testing the 
        "editMyInformation" command
        Eonshik - It would be better to change my address - > myAddress, my phone -> myPhone.
        """

    """
        Elizabeth -- I think something like this would suffice for this command for now, I don't think we need to dive 
        into all the specific commands that could go along with this like "editPhoneNumber" etc etc. I do not recall 
        why this is different than editAccount. 

        def test_command_editInformation_success(self):
            self.assertEqual(self.Project.command("editInformation username title"), 
                             "Account located.  Please edit below")

        def test_command_editInformation_user_does_not_exist(self):
            self.assertEqual(self.Project.command("editInformation username title"), "User does not exist")

        def test_command_editInformation_no_username(self):
            self.assertEqual(self.Project.command("editInformation title"), "No username entered, username required")

        def test_command_editInformation_no_title(self):
            self.assertEqual(self.Project.command("editInformation userName"), "No title entered, title required")


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
     When the viewCourseAssignments command is entered, it takes one argument:
     
     If the account does not exist, an error message is displayed, otherwise the assignments are displayed 
     
       Alex - Logging in with a password is a completely different feature that we currently do not support. I think
       that if we did have a login command it would be preformed in the setup section rather than the tests. Example
       self.ui.command("createAccount accountName title")
       self.ui.command("editAccount accountName password newPassword")
       self.ui.command("login accountName newPassword")
       The command you should be focusing on here is viewCourseAssignments 
       Elizabeth -- we don't need to test for passwords here or have a search command, just the "viewCourseAssignments"
       command 
       Eonshik Kim - some parts removed and some test added
       Elizabeth -- we could do this one two ways, either see the assignmetns for a certain class or for a certain 
       person or view all the the assignments for every class.  Which should we do? 
       
       """

    def test_command_viewCourseAssignments(self):
        self.assertEqual(self.Project.command("viewCourseAssignments"), "Here are the assignments")

    """
    Elizabeth - I don't think we need to support a search command or create another command that is viewMySchedule
    
    def test_command_schedule(self):
        self.assertEqual(self.Project.command("viewMySchedule"), "The schedule hasn't been uploaded yet")

    def test_command_cannot_find_name(self):
        self.assertEqual(self.Project.command("search accountName"), "Can't fine the name of the professor, retype it")

    def test_command_username_not_typed(self):
        self.assertEqual(self.Project.command("search"), "Type the username")
    """

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
