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
import statistics

# Dictionaries to store data
students = {}
grades = {}

# Function to add a student
def add_student(name):
    students[name] = ""
    grades[name] = []

# Function to remove a student
def remove_student(name):
    if name in students:
        del students[name]
        del grades[name]
        print("Student removed successfully.")
    else:
        print("Student not found.")

# Function to enter grades for a student
def enter_grades(name, grade):
    if name in students:
        grades[name].append(grade)
        print("Grade added successfully.")
    else:
        print("Student not found.")

# Function to calculate the average grades of a student
def calculate_average(name):
    if name in students:
        average = statistics.mean(grades[name])
        print("Average grade for", name, "is", average)
    else:
        print("Student not found.")

# Function to log-in
def login(name, password):
    if name == "admin" and password == "Test123":
        return True
    else:
        return False

# Main program loop
logged_in = False
while True:
    if not logged_in:
        name = input("Enter 'admin' to log-in: ")
        password = input("Enter password: ")
        logged_in = login(name, password)
        if not logged_in:
            print("Invalid credentials.")
            continue

    print("\n1. Add Student")
    print("2. Remove Student")
    print("3. Enter Grades")
    print("4. Calculate Average")
    print("5. Log-out")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        add_student(name)
    elif choice == 2:
        name = input("Enter student name: ")
        remove_student(name)
    elif choice == 3:
        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))
        enter_grades(name, grade)
    elif choice == 4:
        name = input("Enter student name: ")
        calculate_average(name)
    elif choice == 5:
        print("Logged out successfully.")
        logged_in = False
    elif choice == 6:
        break
    else:
        print("Invalid choice.")
