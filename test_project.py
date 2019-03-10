from unittest import TestCase
from Project import Project


class TestProject(TestCase):

    def setUp(self):
        self.Project = Project()


    """ 
    createAccount command
    When the createAccount command is entered, it takes 3 arguments:
    -User name 
    -Title
    -Email 
    
    If arguments are missing from the command, an error message is displayed and the command is not executed.  
    """

    def test_command_createAccount_success(self):
        self.assertEqual(self.Project.command("createAccount username title email"), "Account successfully created")

    def test_command_createAccount_missingArguments(self):
        self.asserEqual(self.Project.command("createAccount username"), "Your command is missing arguments, please enter"
                        "your command in the following format: createAccount username title email")

    def test_command_createAccount_missingArguments2(self):
        self.asserEqual(self.Project.command("createAccount username title"), "Your command is missing arguments, please enter"
                        "your command in the following format: createAccount username title email")

    def test_command_createAccount_invalidTitle(self):
        self.assertEqual(self.Project.command("createAccount accountName cashier"), "Please enter a valid title")

    def test_command_createAccount_no_args(self):
        self.assertEqual(self.Project.command("createAccount"), "Your command is missing arguments, please enter"
                        "your command in the following format: createAccount username title email")

    def test_command_createAccount_already_exists(self):
        self.assertEqual(self.Project.command("createAccount accountName title email"), "Account already exists")

    """
        createCourse command 
        When the createCourse command is entered, it takes five arguments:
        -Course Name 
        -Course Number 
        -Meetings days or "online" for an online class
        -Start time 
        -End time
           
        If the course name matches a database entry a then the course is not created 
        and an error message is displayed and some other stuff
           
        If a command argument is missing, an error message is displayed. 
            
    """

    def test_command_createCourse_success(self):
        self.assertEqual(self.Project.command("createCourse courseName courseNumber daysOfWeek start end"),
                         "Course successfully created")

    def test_command_createCourse_missingArguments(self):
        self.assertEqual(self.Project.command("createCourse courseNumber daysOfWeek start end"),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber daysOfWeek start end")

    def test_command_createCourse_missingArguments2(self):
        self.assertEqual(self.Project.command("createCourse courseName daysOfWeek start end"),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber daysOfWeek start end")

    def test_command_createCourse_missingArguments3(self):
        self.assertEqual(self.Project.command("createCourse courseName courseNumber start end"),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber daysOfWeek start end")

    def test_command_createCourse_missingArguments4(self):
        self.assertEqual(self.Project.command("createCourse courseName courseNumber daysOfWeek end"),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber daysOfWeek start end")

    def test_command_createCourse_missingArguments5(self):
        self.assertEqual(self.Project.command("createCourse courseName courseNumber daysOfWeek start"),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber daysOfWeek start end")

    def test_command_createCourse_no_args(self):
        self.assertEqual(self.Project.command("createCourse"), "Your command is missing arguments, please enter "
                        "your command in the following form: createCourse courseName courseNumber daysOfWeek start end")

    def test_command_createCourse_course_exists(self):
        self.assertEqual(self.Project.command("createCourse courseName courseNumber daysOfWeek start end"),
                         "Course already exists, course not added.")


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
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")

    def test_command_createLab_lab_exists(self):
        self.assertEqual(self.Project.command("createLab courseNumber labSection day begin end"),
                         "Lab already exists, lab not added")

    def test_command_createLab_missing_course(self):
        self.assertEqual(self.Project.command("createLab labSection day begin end"),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")

    def test_command_createLab_missing_section(self):
        self.assertEqual(self.Project.command("createLab courseNumber day begin end"),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")

    def test_command_createLab_missing_day(self):
        self.assertEqual(self.Project.command("createLab courseNumber labSection begin end"),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")

    def test_command_createLab_missing_begin(self):
        self.assertEqual(self.Project.command("createLab courseNumber labSection day end"),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")

    def test_command_createLab_missing_end(self):
        self.assertEqual(self.Project.command("createLab courseNumber labSection day begin"),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")

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
    send command 
    Only supervisors and administrators can utilize this command 
    When the sendOutNotification command is entered it takes 2-3 arguments: 

    -send -a
    To send notification to all users.

    -send accountNames -s
    To send notification to specific users.

    -send  accountName
    to send notification to one person

    
    """

    def test_command_send_success(self):
        self.assertEqual(self.Project.command("sendNotification accountName"), "Notification was sent successfully")

    def test_command_send_all_success(self):
        self.assertEqual(self.Project.command("sendNotification -a"), "Notification was sent to all users successfully")

    def test_command_send_specific_success(self):
        self.assertEqual(self.Project.command("sendNotification accountName(s) -s"),
                         "Notification was sent to specific people successfully")

    def test_command_send_error(self):
        self.assertEqual(self.Project.command("sendNotification accountName"), "We weren't able to send a notification")

    def test_command_send_all_error(self):
        self.assertEqual(self.Project.command("sendNotification accountName -a"),
                         "We weren't able to send a notification to all")

    def test_command_send_specific_error(self):
        self.assertEqual(self.Project.command("sendNotification accountNames -s"),
                         "We weren't able to send a notification to specific people")

    def test_command_send_no_argument(self):
        self.assertEqual(self.Project.command("sendNotification -s"), "Please type the user names that you want to sent")

    def test_command_send_no_argument_2(self):
            self.assertEqual(self.Project.command("sendNotification -a"),
                             "Please type the user names  that you want to sent")

    def test_command_send_no_argument_3(self):
        self.assertEqual(self.Project.command("sendNotification"), "Please type the username that you want to sent")


    """
    sendTA command
    The sendTA command takes one argument 
    -classNumber
    
    """

    def test_command_sendTA_success(self):
        self.assertEqual(self.Project.command("sendTA courseNumber"), "Email sent successfully to all TAs associated"
                                                                      "with the specified course")

    def test_command_sendTA_error_course_does_not_exist(self):
        self.assertEqual(self.Project.command("sendTA courseNumber"), "Error, course does not exist, email not sent")

    def test_command_sendTA_missingArguments(self):
        self.assertEqual(self.Project.command("sendTA"), "Your command is missing arguments, please enter the command"
                                "in the following format: sendTA courseNumber")

    """
    When the deleteAccount command is entered, it takes two arguments, 
    -name 
    -title
    If a name or title is missing, an error message is displayed
    If the account that the user is trying to delete does not exist, an error 
           message is displayed. 
                  
    """

    def test_command_deleteAccount(self):
            self.assertEqual(self.Project.command("deleteAccount userName"), "Account successfully deleted")

    def test_command_deleteAccount_no_name(self):
            self.assertEqual(self.Project.command("deleteAccount"), "There are arguments missing, please enter your "
                                            "command in the following format: deleteAccount userName")

    def test_command_deleteAccount_doesNotExist(self):
            self.assertEqual(self.Project.command("deleteAccount userName"), "Error, Account does not exist")



    """
    When the assignInstructorCourse command is entered it takes 2 arguments: 
    - class Number
    - Instructor user Name
        
        
    """

    def test_command_assignInstructorCourse_missingArguments(self):
        self.assertEqual(self.Project.command("assignInstructorCourse classNumber"), "There are arguments missing,"
                        "Please enter your command in the following format: assignInstructorCourse classNumber userName")

    def test_command_assignInstructorCourse_missingArguments2(self):
        self.assertEqual(self.Project.command("assignInstructorCourse userName"), "There are arguments missing,"
                        "Please enter your command in the following format: assignInstructorCourse classNumber userName")

    def test_command_assignInstructorCourse_no_args(self):
        self.assertEqual(self.Project.command("assignInstructorCourse"), "There are arguments missing,"
                        "Please enter your command in the following format: assignInstructorCourse classNumber userName")

    def test_command_assignInstructorCourse_conflict(self):
        self.assertEqual(self.Project.command("assignInstructorCourse classNumber userName"), "This class was already assigned")

    def test_command_assignInstructorCourse_success(self):
        self.assertEqual(self.Project.command("assignInstructorCourse classNumber userName"), "Assignment was successful")

    """
    When assignTACourse command is entered, it takes two arguments:
    --TA username
    --Course number
    Assignment may fail if:
    --Scheduling conflict for TA
    --Max TAs assigned to course
    --TA username is invalid or missing
    --Course number is invalid or missing
    --No arguments
         
    """

    def test_command_assignTACourse_success(self):
        self.assertEqual(self.Project.command("assignTACourse userName courseNumber"), "Assignment successful")

    def test_command_assignTACourse_missingTA(self):
        self.assertEqual(self.Project.command("assignTACourse courseNumber"), "Your command is missing arguments, please enter"
                                "your command in the following format: assignTACourse userName classNumber")

    def test_command_assignTACourse_invalidTA(self):
        self.assertEqual(self.Project.command("assignTACourse userName courseNumber"), "Invalid TA username.")

    def test_command_assignTACourse_missingCourse(self):
        self.assertEqual(self.Project.command("assignTACourse accountName"), "Your command is missing arguments, please enter"
                                "your command in the following format: assignTACourse userName classNumber")

    def test_command_assignTACourse_invalidCourse(self):
        self.assertEqual(self.Project.command("assignTACourse accountName courseNumber"), "Invalid course number.")

    def test_command_assignTACourse_Maximum(self):
        self.assertEqual(self.Project.command("assignTACourse userName courseNumber"),
                         "TA has exceeded assignment limit, TA not assigned")

    def test_command_assignTACourse_schedulingConflict(self):
        self.assertEqual(self.Project.command("assignTACourse userName courseNumber"), "Scheduling conflict encounterd,"
                                                                                       "TA not assigned.")
    def test_command_assignTACourse_noArgs(self):
        self.assertEqual(self.Project.command("assignTACourse"), "Your command is missing arguments, please enter"
                                "your command in the following format: assignTACourse userName classNumber")



    """
    When the viewInfo command is entered it takes one argument: 
    -accountName 
        
    If the account does not exist, an error message is displayed, otherwise, public data is displayed
      
    """

    def test_command_viewInfo_success(self):
        self.asserEqual(self.Project.command("viewInfo userName"), "")

    def test_command_viewInfo_user_does_not_exist(self):
        self.asserEqual(self.Project.command("viewInfo userName"), "Account does not exist")

    def test_command_viewInfo_no_accountName(self):
        self.assertEqual(self.Project.command("viewInfo"), "Your command is missing arguments, please enter your command"
                                                           "in the following format: viewInfo userName")


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
