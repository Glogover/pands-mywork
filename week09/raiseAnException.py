# raiseAnException.p
# Demonstrate raising an exception
# This program prompts the user for an amount and withdraws it from an account
# Author: Marcin Kaminski

balance = 100 # 100 cents = 1 euro
def withdraw(amount):
    global balance
    if amount < 0:
        raise ValueError("amount should always be greater than 0")

    balance = balance - amount
    return balance

amount = int(input("amount to withdraw: "))

print(withdraw(amount))