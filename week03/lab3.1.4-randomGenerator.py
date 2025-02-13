# randomGenerator.py
# Author: Marcin Kaminski

# program that prints out a random number between 1 and 10

import random

x = int(input("Enter the first number of the range: "))
y = int(input("Enter the last number of the range: "))

number = random.randint(x,y)
print("here is a random number {}".format(number))
