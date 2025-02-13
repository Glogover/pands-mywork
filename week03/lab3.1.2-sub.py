# sub.py
# Author: Marcin Kaminski

# Program to subtract one number from another
# input reads in a string so we need to convert it into an int
# so we can perform mathematical operations

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
answer = x-y
print("{} minus {} is {} ".format(x, y, answer))
