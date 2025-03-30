# countEmailDomains.py
# Author: Marcin Kaminski
"""this script will count each email domain from employees.csv file"""


import csv
fileName = "employees.csv"
domainCount = {} # a dictionary object

with open(fileName, "rt") as employeeFile:
    csvReader = csv.reader(employeeFile, delimiter = ";")
    firstLine = True
    count = 0
    for line in csvReader:
        if firstLine:
            firstLine = False
            continue
        #print(line[8])
        email = line[8]
        start = email.find("@")
        domain = email[start+1:]
        if domain not in domainCount:
            domainCount[domain] = 0
        else:
            domainCount[domain] += 1

for key, value in domainCount.items():        
    print(key, "\t\t", value)





