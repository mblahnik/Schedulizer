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
        Natasha -- We may need to discuss this, but I think it makes sense for the supervisor and administrator
        to just create accounts using a username, the person's actual first and last name, email, and title. Then
        instructors and TAs can be notified that their account was created by the system/person who created it. 
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
                Natasha -- Eonshik: I don't think it would make sense to have the descriptions or units, since this is 
                only to assign instructors and TAs, really, and keep track of users. That information is really only
                useful to students who will not be using the program.
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
        When the editAccount command is entered, it takes arguments
        -Username
        -Title 
        
        If the user does not exist, an error message is displayed.
        If command arguments are missing, an error message is displayed. 
    
       Edit Information 
       Alex- These tests should test whatever command we are using to edit account information. "find" is currently
       not a command that we are supporting. 
       - Now that I look at this, its kind of big. Maybe we should think about breaking this up.  
       This also isn't properly setup for the unittest framework but I dont think that matters since we are not
       running it
       Elizabeth - I think these tests go beyond the scope of the base command -- really what should be tested here 
       is simply the "editInformation" command, I don't think we need to go in depth and make separate commands for
       editing all the different fields at this time.  
       Eonshik - I think this part is kind of Epic as a user story, it needs to be break into smaller pieces.
       and the argument username would be better to change accountName to make the argument command consistent.
       Natasha -- This command should probably be called editAccount or something. These "change" tests look the
       same as others below. This is a different command that can edit everything and only supervisors and administrators
       can perform this command. It should probably have an error that says "Permission denied: must be supervisor or admin"
       if the user is an instructor or TA.
       """


    """
    Elizabeth -- I think something like this would suffice for this command for now, I don't think we need to dive 
    into all the specific commands that could go along with this like "editPhoneNumber" etc etc. Also it should 
    probably be called editAccount since editInformation is down below. 
    
    def test_command_editAccount_success(self):
        self.assertEqual(self.Project.command("editAccount username title"), 
                         "Account located.  Please edit below")
        
    def test_command_editAccount_user_does_not_exist(self):
        self.assertEqual(self.Project.command("editAccount username title"), "User does not exist")
        
    def test_command_editAccount_no_username(self):
        self.assertEqual(self.Project.command("editAccount title"), "No username entered, username required")

    def test_command_editAccount_no_title(self):
        self.assertEqual(self.Project.command("editAccount userName"), "No title entered, title required")
    
    
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
        self.assertEqual(self.Project.command("change username address NewAddress"), "address has been changed")

    def test_change_address_command_no_address(self):
        self.assertEqual(self.Project.command("change username address"), "Error changing address")

    def test_change_address_command_invalid_username(self):
        self.assertEqual(self.Project.command("change InexistantAccount address newAdress "), "Error changing address")

    def test_change_address_command_no_username(self):
        self.assertEqual(self.Project.command("change address NewAddress "), "Error changing address")

    def test_change_name_command_correct(self):
        self.assertEqual(self.Project.command("change username name NewName"), "Name has been changed")

    def test_change_name_command_no_name(self):
        self.assertEqual(self.Project.command("change username name"), "Error changing name")

    def test_change_name_command_invalid_username(self):
        self.assertEqual(self.Project.command("change InexistantAccount name newName "), "Error changing name")

    def test_change_name_command_no_username(self):
        self.assertEqual(self.Project.command("change name NewName "), "Error changing name")

    def test_change_title_command_correct(self):
        self.assertEqual(self.Project.command("change username title NewTitle"), "address has been changed")

    def test_change_title_command_no_adress(self):
        self.assertEqual(self.Project.command("change username title"), "Error changing address")

    def test_change_title_command_invalid_username(self):
        self.assertEqual(self.Project.command("change InexistantAccount title newTitle "), "Error changing address")

    def test_change_title_command_no_username(self):
        self.assertEqual(self.Project.command("change title NewTitle "), "Error changing address")

    def test_change_Hphone_command_correct(self):
        self.assertEqual(self.Project.command("change username Hphone newPhoneNumber"), "Home phone number has been changed")

    def test_change_Hphone_command_no_number(self):
        self.assertEqual(self.Project.command("change username Hphone"), "Error changing Home phone number")

    def test_change_Hphone_command_invalid_username(self):
        self.assertEqual(self.Project.command("change InexistantAccount Hphone newPhoneNumber "), "Error changing Home phone number")

    def test_change_Hphone_command_no_username(self):
        self.assertEqual(self.Project.command("change Hphone NewPhoneNumber "), "Error changing Home phone number")

    def test_change_Hphone_command_wrong_number_format(self):
        self.assertEqual(self.Project.command("change username Hphone IncorectNumberFormat"), "Error changing Home phone number")

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

    def test_change_Eaddress_command_correct(self):
        self.assertEqual(self.Project.command("change username emailaddress NewEmailAddress"), "email address has been changed")

    def test_change_Eaddress_command_no_adress(self):
        self.assertEqual(self.Project.command("change username emailaddress"), "Error changing email address")

    def test_change_Eaddress_command_invalid_username(self):
        self.assertEqual(self.Project.command("change InexistantAccount emailaddress newEmailAddress "),
                         "Error changing email address")

    def test_change_Eaddress_command_no_username(self):
        self.assertEqual(self.Project.command("change emailaddress NewEmailAddress "), "Error changing email address")

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
    
    Natasha -- for the specific users option, if they just enter a string like "elizabeth natasha eonshik alex adrian" then 
    the program can just split it. I don't think it would be too bad. But we need to make it clear that that needs to be
    entered as a string in our manual or whatever.
    """

    def test_command_notification(self):
        self.assertEqual(self.Project.command("sendNotification accountName"), "Notification was sent successfully")

    def test_command_notification_was_sent_all(self):
        self.assertEqual(self.Project.command("sendNotification -a"), "Notifications were sent successfully")

    def test_command_notification_was_sent_specific(self):
        self.assertEqual(self.Project.command("sendNotification accountName(s) -s"),
                         "Notifications were sent successfully")

    def test_command_notification_was_not_sent(self):
        self.assertEqual(self.Project.command("sendNotification accountName"), "Unable to send notifications")

    def test_command_notification_was_not_sent_all(self):
        self.assertEqual(self.Project.command("sendNotification accountName -a"),
                         "Unable to send notifications")

    def test_command_notification_was_not_sent_specific(self):
        self.assertEqual(self.Project.command("sendNotification accountNames -s"),
                         "Unable to send notifications")

    def test_command_no_argument(self):
        self.assertEqual(self.Project.command("sendNotification -s"), "Please type the user names that you want to notify")

    def test_command_no_argument_2(self):
            self.assertEqual(self.Project.command("sendNotification -a"),
                             "Please type the user names that you want to notify")

    def test_command_no_argument_3(self):
        self.assertEqual(self.Project.command("sendNotification"), "Please type the username that you want to notify")




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
          Natasha-- Eonshik: no two users should have the same user name. It's supposed to be a specific identifier.
                Elizabeth: I think that is true, but it doesn't make sense to the user. That would make it more helpful
                for us, but I think that kind of shares some information about how we are storing data that is unwanted.
           
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
       Eonshik - I think it looks good. I don't think we need add more test to find all of information was successfully 
       passed. I think It would just need to simply test the AccessAllData command show the all its data or not.
       I think the argument "name" need be changed "userName" to make the the argument command consistent.
        """

    def test_command_AccessAllData_success(self):
        self.assertEqual(self.Project.command("AccessAllData userName"), "Account found!")

    def test_command_AccessAllData_noname(self):
        self.assertEqual(self.Project.command("AccessAllData"), "No userName was entered, error")

    def test_command_AccessAllData_no_such_user(self):
        self.assertEqual(self.Project.command("AccessAllData userName"), "User does not exist")

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
        Natasha--I don't think a class name is necessary, only the number. The number should be the identifier. It would
        also help avoid user error/make it easier to use.
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
    Natasha -- I think this is something to worry about. It wouldn't make sense to assign multiple instructors to a course.
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
        Natasha -- I think this is adequate.
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
        Natasha -- This command shouldn't take username arguments, I don't think. This is only for a TA or instructor to update their
        own contact information. No one should be able to enter any username in there. It is only for their own information.
        I'm not sure exactly how this should be done, but this looks like it may be giving anyone the ability to access other
        information that is not their own.

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
        self.assertEqual(self.Project.command("change myPhone newPhoneNumber"), "phone number has been changed")

    def test_change_phone_command_no_number(self):
        self.assertEqual(self.Project.command("change myPhone"), "Error changing number")

    def test_change_phone_command_wrong_number_format(self):
        self.assertEqual(self.Project.command("change myPhone IncorectNumberFormat"), "Error changing number")

    def test_change_phone_command_no_username(self):
        self.assertEqual(self.Project.command("change myPhone NewPhoneNumber "), "Error changing number")

    def test_change_address_command_correct(self):
        self.assertEqual(self.Project.command("change myAddress NewAddress"), "Address has been changed")

    def test_change_address_command_no_address(self):
        self.assertEqual(self.Project.command("change myAddress"), "Error changing address")

    def test_change_address_command_no_username(self):
        self.assertEqual(self.Project.command("change address NewAddress"), "Error changing address")

    def test_change_Hphone_command_correct(self):
        self.assertEqual(self.Project.command("change myHphone newPhoneNumber"), "Home phone number has been changed")

    def test_change_Hphone_command_no_number(self):
        self.assertEqual(self.Project.command("change myHphone"), "Error changing home phone number")

    def test_change_Hphone_command_no_username(self):
        self.assertEqual(self.Project.command("change Hphone NewPhoneNumber"), "Error changing home phone number")

    def test_change_Hphone_command_wrong_number_format(self):
        self.assertEqual(self.Project.command("change myHphone IncorectNumberFormat"), "Error changing home phone number")

    def test_change_Eaddress_command_correct(self):
        self.assertEqual(self.Project.command("change myEmailAddress NewEmailAddress"), "Email address has been changed")

    def test_change_Eaddress_command_no_address(self):
        self.assertEqual(self.Project.command("change myemailaddress"), "Error changing email address")

    def test_change_Eaddress_command_no_username(self):
        self.assertEqual(self.Project.command("change emailaddress NewEmailAddress "), "Error changing email address")

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
       Natasha -- I think it should probably just show all assignments. By the way it is listed on the assignment,
       it seems like this command is only supposed to show the user's (instructor) assignments.
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
       
       Natasha--by the way it sounds on the assignment description, it seems like this command should only display
       all TA assignments for all classes. So it shouldn't need any arguments at all. 

       """

    def test_command_ViewTAAssignments_success(self):
        self.assertEqual(self.Project.command("ViewTAAssignments classNumber"), "The TA Assignments are: ")

    def test_command_ViewTAAssignments_noClassNum(self):
        self.assertEqual(self.Project.command("ViewTAAssignments"), "Error, no class number entered")

    def test_command_ViewTAAssignments_classDoesNotExist(self):
        self.assertEqual(self.Project.command("ViewTAAssignments classNumber"), "Class does not exist")
