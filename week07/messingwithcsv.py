# Messing with CSV
# Author: Marcin Kaminski

import csv

FILENAME="data.csv"
with open(FILENAME, "rt") as file:
    for line in file:
        print (line, end='')


FILENAME="data.csv"
with open(FILENAME, "rt") as file:
    csvReader = csv.reader(file, delimiter = ',') # delimiter can be anything, in this case a comma
    for line in csvReader: # line will be a list containing the variables in each line
        age = line[2]   # the age
        print(age)      # note this is printing the header row, I provide a solution to this in the tutorial