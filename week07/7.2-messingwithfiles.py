# 7.2-messingwithfiles.py
# Author: Marcin Kaminski

"""This program counts how many times it was run.
For this exercise will have to store data outside of memory, and that is accessible each time the program is run, (persistent data). 
We would normally use a database for something like this, but we can use a file.
To make life easier the file count.txt already exists. So, we can just read the current count from it then overwrite it 
with the new count."""

# Writing a function "readNumber()" that reads in a number from a file that already exists (count.txt).

FILENAME = "count.txt"
def readNumber():
    with open(FILENAME) as f: # Instead of using data that was passed in as an argument, using a variable (FILENAME) that we treat as a constant.
        number = int(f.read())
        return number
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
