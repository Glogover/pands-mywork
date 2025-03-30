# testing reading a csv
# Author: Marcin Kaminski

import csv

filename = "test.csv"

with open(filename, "rt") as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ",")
    firstLine = True
    for line in csvReader:
        if firstLine:
              firstLine = False
              continue   # do not do the rest (excluding first line)
        print(line[2])  # showing occupation only




