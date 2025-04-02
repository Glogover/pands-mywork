# 8.2-salaries.py
# Author: Marcin Kaminski

import numpy as np

# it is a good idea to have your absolute values set into variables at the beginning of yur program

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10


np.random.seed(1) # this is so that the "random" numbers are the same each time to make it easier to debug
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

print(salaries)