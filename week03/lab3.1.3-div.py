# div.py
# Author: Marcin Kaminski

# program that reads in two numbers and
# outputs the integer answer and remainder

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y) # // gives the int division 
remainder = x%y    # % gives the remainder

print(" {} divided by {} is {} wih remainder {} ".format(x, y, answer, remainder))
