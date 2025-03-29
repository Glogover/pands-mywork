# 7.2-messingwithfiles-2.py
# Author: Marcin Kaminski

"""This program counts how many times it was run.
For this exercise will have to store data outside of memory, and that is accessible each time the program is run, (persistent data). 
We would normally use a database for something like this, but we can use a file.
"""

import os.path
FILENAME = "count.txt"

# Checking if the file (count.txt) exists.
if not os.path.isfile(FILENAME):  # isfile() function
    print("File does not exist")
    #initialise file here



# Writing a function "readNumber()" that reads in a number from a file that already exists (count.txt).

def readNumber():
    try:
        with open(FILENAME) as f: # Instead of using data that was passed in as an argument, using a variable (FILENAME) that we treat as a constant.
             number = int(f.read())
             return number
    except IOError:
        # this file will be created when we write back.
        # no file assumes first time running
        # ie 0 previou runs
        return 0
        
# test it
#num = readNumber()
#print (num)

# Writing a function that takes in a number and overwrites a file with that number (count.txt). 

def writeNumber(number):
    with open(FILENAME, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

# test it
#writeNumber(3)

# main
        
num = readNumber()
num +=1
print(f"we have run this program {num} times")
writeNumber(num)
