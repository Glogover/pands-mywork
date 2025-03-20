# Messing with functions
# to demonstrate the defining and using functions
# Author: Marcin Kaminski

#x, y, z = (1, 2, 3)
#print(x, y, z, sep="", end="") # no space
#print(f"{x}-{y} {z}")
#print("{} {}--{}".format(x, y, z))

def topower(number, power=3): # 3 is a default argument
    #print(number)
    return (number ** power)

#ans = topower(23)
#print(f"we got {ans}")
num = 45

print(f"and {num} is {topower(num)}")
    