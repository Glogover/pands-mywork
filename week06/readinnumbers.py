# read in two numbers and multiply them
# Author: Marcin Kaminski

def readNum(message = "enter a number "): 

    num = False

    while (num == False):

        try:
            num = int(input(message))
        except ValueError:
            print("that was not a number, ", end="") # keeping it on the same line
    
    return num

        

"""num2 = False

while (num2 == False):

    try:
        num2 = int(input("another "))
    except ValueError:
        print("that was not a number, ", end="") # keeping it on the same line"""

num1 = readNum()
num2 = readNum()

answer = num1 * num2

print(f"answer is {answer}")

