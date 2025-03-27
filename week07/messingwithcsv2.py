# Messing with CSV (2)
# Author: Marcin Kaminski

import csv

mydict =[{'first': 'Andrew', 'last': 'Beatty', 'age':'2'},
         {'first': 'joe', 'last': 'Bloggs', 'age':'22'},
         {'first': 'Mary', 'last': 'mc', 'age':'2222'} 
        ] 
    
# field names 
fields = ['first', 'last', 'age'] 
    
# name of csv file 
FILENAME = "data2.csv"
    
# writing to csv file 
with open(FILENAME, 'w', newline='') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
        
    # writing headers (field names) 
    writer.writeheader() 
    for dictrow in mydict:
        print(dictrow)
        writer.writerow(dictrow) 