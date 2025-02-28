# grade-rounded.py
# Author: Marcin Kaminski

# This program reads in and rounds
# a students percentage
# and prints out the
# corresponding grade.

percentage = round(float(input("Enter the percentage: ")))

if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif percentage < 40:
    print("Fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60:
    print("Merit 2")
elif percentage < 70:
    print("Merit 1")
else:
    print("Distinction")