# student2.py
# Author: Marcin Kaminski

""" 
This program stores a student name and a list of her courses 
and grades in a dictionary. The program prints out her data.
This program also reads in a student's name, then keeps reading in their modules and grades
(until the user enters a blank module name),
It can just read in one student (and their module details).
"""

# Store the student data
student_data = {}

# Read in the student's name
student_name = input("Enter student's name: ")

# Keep reading course names until an empty string is entered

while True:
    course_name = input("Enter course name (or blank to finish): ")
    if course_name == "":
        break

    # Read in the grade once we have a course name
    grade = input("Enter grade for {}: ".format(course_name))
    student_data[course_name] = grade

# Finally, store all data under student's name
students = {student_name: student_data}

# Print out the data
for name, data in students.items():
    print("Student: {}".format(name))
    
    for course, grade in data.items():
        print("Course: {}\nGrade: {}".format(course, grade))
