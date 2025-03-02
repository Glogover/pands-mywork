# student.py
# Author: Marcin Kaminski

""" This program stores a student name and a list of her courses 
and grades in a dictionary. The program prints out her data."""

student = {
    "name": "Mary",
    "modules": [
        {
        "courseName": "Programming",
        "grade": 45
        },
        {
            "courseName": "History",
            "grade": 99
        }
         
    ]
}

print (f"Student: {student["name"]}")
for module in student["modules"]:
    print(f"\t {module["courseName"]} \t: {module["grade"]}")


      