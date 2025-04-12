# module of useful functions
# Author: Marcin Kaminski


balance = 100 # 100 cents = 1 euro

def withdraw(amount):
    global balance
    if amount < 0:
        raise ValueError("amount should always be greater than 0")
    if amount > balance:
        raise ValueError("not enough funds")

    balance = balance - amount
    return balance

if __name__ == "__main__":
    # this code will only run if the script is run directly
    # it will not run if the script is imported as a module
    assert withdraw(20) == 80, "incorrect calculation"
    try:
        withdraw(-1)
        assert False, "should have thrown a value error"
    except ValueError as ve:
        pass

    try:
        withdraw(110)
        assert False, "can't wihdraw more than is in balance"
    except ValueError as ve:
        pass

    print ("all good")


