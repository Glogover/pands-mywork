# 8.4-salaries.py
# Author: Marcin Kaminski

import numpy as np

# it is a good idea to have your absolute values set into variables at the beginning of yur program

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10


np.random.seed(1) # this is so that the "random" numbers are the same each time to make it easier to debug
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
#salariesPlus = salaries + 5000 # this will add 5000 to each value
#print(salariesPlus)

# you can also multiply
salariesMult = salaries * 1.05 # add 5% by multiplying by 1.05
print(salariesMult) 

# This is a float array, here I convert it to an int array (it does a floor)
newSalaries = salariesMult.astype(int)
print(newSalaries)


