# More messing wih functions
# flexible arguments
# Author: Marcin Kaminski

print(1,2,3, sep="", end="\t")
print("hi")

def fun1(*args):
    print(type(args))
    print(args)

fun1("a", "b", "c")
