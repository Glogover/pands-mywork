# testing "if statements"
# Author: Marcin Kaminski
b = 1

if True:
    print("we are in the if statement")
    b = 2

c = 1
if isinstance(c, int) and c == 1:
    print("c is one")
else:
    print("c is not one")

d = 10
if not isinstance(d, int):
    print("please give me an int")
elif d < 0:
    print("d is negative")
elif d >= 10:
    print("d is 10 or higher")
else:
    print("d is between 0 and 9 inclusive")



print("sanity ", b)
