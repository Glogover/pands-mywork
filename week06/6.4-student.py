# 6.4-student.py
# Author: Marcin Kaminski

students = []

def readModules():
    return []

def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name: ")
    currentStudent["modules"]=readModules()

    students.append(currentStudent)

#test
    
doAdd(students)
doAdd(students)

print(students)
