# 8.8-scatterplot2.py
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
# I prefer putting the abolute values into variables that are set at the top
ages = np.random.randint(low=21, high = 65, size = numberOfEntries)

plt.scatter(ages, salaries) # this will be random 
#plt.show()  #if you do this the program will halt here until the plot is closed

# add x squared
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints # multiply each entry by itself

plt.plot(xpoints, ypoints, color = 'r')
#plt.show() # see how the axis have changed
plt.savefig("scatterplot&xsquared.png")
