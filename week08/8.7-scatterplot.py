# 8.7-scatterplot.py
# Author: Marcin Kaminski
# This program makes a list called ages that has the same number random values as salaries (range: 21 to 65) shown on a scatter plot.

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

# this is so that the "random" numbers are the same each time to make it easier to debug.
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high = 65, size = numberOfEntries)

plt.scatter(ages, salaries) # this will be random 
#plt.show()
plt.savefig("scatterplot.png")