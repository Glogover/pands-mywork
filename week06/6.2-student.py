# 6.2-student.py
# Author: Marcin Kaminski

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()
    return choice

#test the function
choice = displayMenu()
print(f"you chose {choice}")







    
