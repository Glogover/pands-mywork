# isEven.py
# The program asks the user to enter in a number and tells the user if the number is even or odd.
# Additionally, the program keeps prompting the user for a number until the user enters -1
# Author: Marcin Kaminski

number = 0
while number != -1:
  number = int(input("Enter a number: "))

if (number % 2 ) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")