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
from statistics import mean as m #Add imports at the top of the script

admins = {"Python":"Pass123@","User2":"Pass2"} #Then add constants e.g. user login details
studentDict = {"Jeff":[78,88,93],
               "Alex":[92,76,88],
               "Sam":[89,92,93]}

def enterGrades():
    nameToEnter = input("Student Name: ")
    gradeToEnter = input("Grade: ")

    if nameToEnter in studentDict:
        print("Adding Grade...")
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print("Student does not exist")

    print(studentDict)

def removeStudent():
    nameToRemove = input("What student to remove?: ")
    if nameToRemove in studentDict:
        print("Removing student...")
        del studentDict[nameToRemove]

    print(studentDict)

def studentAVGs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList) #m defined when importing mean from statistics

        print(eachStudent,"has an average grade of:",avgGrade)

def main():#Define functions / classes - main() used to define end goal
    print("""
    Welcome to Grade Central
          
    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    """)

    action = input("What would you like to do today? (Enter a number) ")

    if action == "1":
        enterGrades()
    elif action == "2":
        removeStudent()
    elif action == "3":
        studentAVGs()
    elif action == "4":
        exit()
    else:
        print("No valid choice was given, try again")

login = input("Username: ")
passw = input("Password: ")

if login in admins:#If login username is in admins dictionary 
    if admins[login] == passw: #If password matches username's password in admins dictionary
        print("Welcome,",login)
        while True:
            main()
    else:
        print("Invalid password, will detonate in 5 seconds")
else:
    print("Invalid username, calling the FBI to report this")
