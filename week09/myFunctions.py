# module of useful functions
# Author: Marcin Kaminski


balance = 100 # 100 cents = 1 euro

def withdraw(amount):
    global balance
    if amount < 0:
        raise ValueError("amount should always be greater than 0")

    balance = balance - amount
    return balance

if __name__ == "__main__":
    # this code will only run if the script is run directly
    # it will not run if the script is imported as a module
    print("dont want this")