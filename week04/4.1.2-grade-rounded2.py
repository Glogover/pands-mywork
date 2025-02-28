# grade-rounded2.py
# Author: Marcin Kaminski

# This program reads in and rounds
# a students percentage
# and prints out the
# corresponding grade.

percentage = float(input("Enter the percentage: "))
percentage_rounded = round(percentage)


if percentage_rounded < 0 or percentage_rounded > 100:
    print("Please enter a number between 0 and 100")
elif percentage_rounded < 40:
    print("Fail")
elif percentage_rounded < 50:
    print("Pass")
elif percentage_rounded < 60:
    print("Merit 2")
elif percentage_rounded < 70:
    print("Merit 1")
else:
    print("Distinction")


