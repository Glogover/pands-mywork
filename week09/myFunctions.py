# module of useful functions
# Author: Marcin Kaminski


balance = 100 # 100 cents = 1 euro

def withdraw(amount):
    global balance
    if amount < 0:
        raise ValueError("amount should always be greater than 0")

    balance = balance - amount
    return balance