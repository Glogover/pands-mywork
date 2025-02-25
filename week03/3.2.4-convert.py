# convert.py
# This program takes in a float amount of dollars and returns that absolute amount in cent.
# Author: Marcin Kaminski

amountOfDollars = float(input("Please enter an amount: "))
amountInCent = int(abs(amountOfDollars * 100))
print(f"That amount in cent is: {amountInCent}")
