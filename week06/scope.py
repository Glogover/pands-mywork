# more messing with functions
# variable scope
# Author: Marcin Kaminski

# Do not use global variables

x = 999

#def fun():
    #print(x) # This variable is from outside the function (global variable)

#fun()


def fun(num):
    print(num)

def fun2(x):
    print(f"in fun2 x {x}")
    x = 21
    print(f"in fun2 x {x}")


fun2(x)
print(f"after fun2 x is {x}")




