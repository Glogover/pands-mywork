# student3.py
# Author: Marcin Kaminski

"""
This program stores students' names and lists of their courses 
and grades in a dictionary. The program prints out their data.
This program also reads in students' names, then keeps reading in their modules and grades
(until the user enters a blank name),
It can read in multiple students (until the student name is blank).
"""


# Step 1: Store students' data
students_data = {}


# Step 2: Keep asking for new students until the user enters blank for student name
while True:


    # Step 3: Ask the user for a student name
    student_name = input("Enter student name (or blank to stop): ")
    

    # Step 4: Check if the student name is blank. If so, break from the loop
    if student_name == "":
        break


    # Step 5: Create an empty list for this student's courses
    courses = []


    # Step 6: Keep asking for new courses until the user enters blank for course name
    while True:


        # Step 7: Ask the user for a course name and grade
        course_name = input("Enter course name (or blank to stop): ")
        

        # Step 8: Check if the course name is blank. If so, break from the loop
        if course_name == "":
            break


        # Step 9: Ask the user for the grade in this course
        grade = input("Enter grade for this course: ")


        # Step 10: Add this course and grade to the student's courses list
        courses.append((course_name, grade))
    

    # Step 11: Add this student and their courses to the students data dictionary
    students_data[student_name] = courses



# Step 12: Print out all students data 
for student, courses in students_data.items():
    print(f"\n{student}:")

    for course in courses:
        print(f"{course[0]}: {course[1]}")