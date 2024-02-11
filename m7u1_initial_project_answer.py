#
"""Create a student grading system using Python that has the following functionalities:
1. Entering the Grades of a student
2. Removing a student from the system
3. Calculating the average grades of a students
The user should be able to select whether he/she wants to remove a student, enter grades for a
student or find the average grades.
Also perform the following as part of this project:
 There should be a log-in system to allow only admin access to the grading system.
 Make sure you use dictionaries and lists for storing student’s data.
 Use Python functions as much as you can
Hint: Statistics module might be helpful
"""
from statistics import mean

user_list = {"admin":"Test123"}
student_list = {}

def login():
    print("Welcome to Grade Central")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    if username in user_list and password == user_list[username]:
        logged_in = True
        initial()
    else:
        print("You username and/or password is incorrect. Please try again")
        login()

def initial():
    print("1) Enter a student's grade\n"
          "2) Remove a student from the database\n"
          "3) Calculate a student's average grade\n"
          "4) Log off")
    selection = int(input("What would you like to do today? (Enter a number): "))
    if selection == 1:
        enter_grade()
    elif selection == 2:
        remove_student()
    elif selection == 3:
        student_avg()
    elif selection == 4:
        login()
    else:
        print("Please enter a number between 1 and 4")

def enter_grade():
    student = input("Please enter the name of the student you wish to select: ")
    if student in student_list:
        grade = int(input("Enter the student's grade: "))
        student_list[student].append(int(grade))
        print("Grade ",{grade}," added for ",{student})
        print("Please see the updated student database below:")
        print(student_list)
        initial()
    else:
        confirm_add = input("Student does not exist in database. Do you want to add the student to the database? (Y/N): ")
        if confirm_add == "Y":
            add_student()
        else:
            initial()

def add_student():
    new_student = input("Please enter the name of the student you wish to add: ")
    student_list[new_student] = []
    new_grade = int(input("Please input their grade: "))
    student_list[new_student].append(new_grade)
    print("You have added",new_student,"with a grade of",new_grade,"to the database")
    print("Please see the updated student database below:")
    print(student_list)
    initial()

def remove_student():
    old_student = input("Please enter the name of the student you wish to remove: ")
    if old_student in student_list:
        del student_list[old_student]
        print("You have removed ",old_student," from the database.")
        print("Please see the updated student database below:")
        print(student_list)
        initial()
    else:
        print("The student does not exist in the database, please try again.")
        initial()

def student_avg():
    student = input("Please enter the name of the student you wish to select: ")
    if student in student_list:
        grade = student_list[student]
        avg_grade = mean(grade)
        print(student,"has grades of ",avg_grade)
        initial()
    else:
        print("Student not found in the database.")
        initial()

login()
