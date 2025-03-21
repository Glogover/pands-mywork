# More messing wih functions
# flexible arguments
# Author: Marcin Kaminski

print(1,2,3, sep="", end="\t")
print("hi")

# unnamed arguments (args)
def fun1(*args): 
    print(type(args))
    #print(args)
    for val in args:
        print(val)

#fun1("a", "b", "c")

# keyword arguments (kwargs)
def fun2(**kwargs): 
    print(type(kwargs))
    print(kwargs)
    #for val in kwargs:
    #   print(val)

fun2(name="joe", age=21, gender="M") # dictionary

# sample code




    
    

