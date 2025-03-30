# countEmailDomains.py
# Author: Marcin Kaminski
"""this script will count each email domain from employees.csv file"""

import csv
fileName = "employees.csv"

with open(fileName, "rt") as employeeFile:
    csvReader = csv.reader(employeeFile, delimiter = ",")
    firstLine = True
    count = 0
    for line in csvReader:
        if firstLine:
            firstLine = False
            continue
        print(line[8])





