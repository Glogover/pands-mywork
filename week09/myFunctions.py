# module of useful functions
# Author: Marcin Kaminski

import logging
logging.basicConfig(filename="./bank.log",
                    level=logging.DEBUG,
                    format="%(asctime)s-%(levelname)s-%(message)s- %(lineno)d")

balance = 100 # 100 cents = 1 euro

def withdraw(amount):
    global balance
    if amount < 0:
        logging.critical(f"the amount ({amount}) should never be less than 0")

        raise ValueError("amount should always be greater than 0")
    if amount > balance:
        logging.warning(f"trying to withdraw more ({amount}) than is in account ({balance})")

        raise ValueError("not enough funds")
    balance = balance - amount
    logging.info(f"we have just withdrawn {amount}, new balance is {balance}")

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


