# 6-extra1.py
# Variables can be of type function, and we can call those variables.
# Author: Marcin Kaminski

def fun1():
    print("this is fun1")
def fun2():
    print("this is fun2")

whichFun = fun1
whichFun()
whichFun = fun2
whichFun()

"""This means that lists, tuples and dicts can have variables of type function in them, 
so we could have a dict that stores the letter of the menu and the function associated with that 
letter. We could access that function by that letter. (NOTE: that this is not more efficient 
to run, just more efficient to write)"""