# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   JWatts, 3/4/2025,Created Script
#   JWatts, 3/5/2025 Fleshed out classes, completed updating while loop
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
import json


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

#Classes
class FileProcessor:
    """
    Class containing functions responsible for processing JSON files
    ChangeLog: (Who, When, What)
    JWatts,3.4.2025,Created Class. Added Functions
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        Reads JSON file and loads into a list of dictionary's
        :param file_name:
        :param student_data:
        :return: student_data
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("JSON file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error, oh no!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Writes list of dictionary's to JSON file
        :param file_name:
        :param student_data:
        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=4)
            file.close()
            print("Data has been saved to file!")
        except TypeError as e:
            IO.output_error_messages("Please check that the data is in a valid JSON format", e)
        except Exception as e:
           IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()


class IO:
    """
    Class containing functions responsible for handling data input and output
    ChangeLog: (Who, When, What)
    JWatts,1.4.2025,Created class and functions
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user
        :return: None
        """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error,), sep='\n')


    @staticmethod
    def output_menu(menu: str):
        """Prints out a menu string for the user to interface with
        :param menu:
        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        Prompts the users to make a selection, returns the input
        :return: menu_choice
        """
        menu_choice = "0"
        try:
            menu_choice = input("Enter Menu Selection: ")
            if menu_choice not in ("1", "2", "3", "4"):
                raise Exception("Please choose either 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return menu_choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        Displays the current data within a list of dictionaries
        :param student_data:
        :return: None
        """
        print("Students In File:")
        print("-" * 50)
        for student in student_data:
            print(f"Student {student["FirstName"]} {student["LastName"]}"
                  f" is registered for {student["CourseName"]}")
        print("-" * 50)


    @staticmethod
    def input_student_data(student_data: list):
        """
        Prompts the student to enter first name, last name and the course they are taking.
        This is then processed into a dictionary and then appended to a list.
        :param student_data:
        :return: student_data
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if student_first_name == "":
                raise Exception("Please enter a first name")
            if not student_first_name.isalpha():
                raise ValueError("Please do not include numbers in your name.")

            student_last_name = input("Enter the student's last name: ")
            if student_last_name == "":
                raise Exception("Please enter a last name")
            if not student_last_name.isalpha():
                raise ValueError("Please do not include numbers in your name.")

            course_name = input("Please enter the name of the course: ")
            if course_name == "":
                raise Exception("Please enter a course name")

            # Process input data into dictionary
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)

        except ValueError as e:
          IO.output_error_messages("That value is not the correct data type!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        print("-" * 50)
        print(f"You have registered {student_first_name} "
              f"{student_last_name} for "
              f"{course_name}.")
        print("-" * 50)
        return student_data


# Load data from file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:
    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice=IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
