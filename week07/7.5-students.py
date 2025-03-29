# 7.5-students.py
# Author: Marcin Kaminski

import json
students = []
FILENAME = "students.json"

def writeDict(obj):
    with open(FILENAME, "wt") as f:
        json.dump(obj,f)


def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/s/q): ").strip()
    return choice

def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name: ")
    currentStudent["modules"]=readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit): ").strip()

    while moduleName !="":
        module = {}
        module["name"]= moduleName
        # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade: "))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit): ").strip()

    return modules

def displayModules(modules):
    print("\tName       \tGrade")
    for module in modules:
        print(f"\t{module['name']}      \t{module['grade']}")

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"]);

def doSave(students):
    writeDict(students)
    print("students saved")


# main program

students = []   
choice = displayMenu()
while (choice != "q"):
    if choice == "a":
        doAdd(students)
    elif choice == "v":
        doView(students)
    elif choice == "s":
        doSave(students)
    elif choice != "q":
        print("\n\nplease select either a, v, s or q")
    choice = displayMenu()