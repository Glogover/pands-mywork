# isEven.py
# The program asks the user to enter in a number and tells the user if the number is even or odd.
# Author: Marcin Kaminski

number = int(input("Enter a number: "))

if (number % 2 ) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")


