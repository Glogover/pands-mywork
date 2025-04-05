# 8.15-normalDistribution.py
# Author: Marcin Kaminski

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats # importing stats module

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

# this is so that the "random" numbers are the same each time to make it easier to debug.
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
# I prefer putting the abolute values into variables that are set at the top
ages = np.random.randint(low=21, high = 65, size = numberOfEntries)

plt.scatter(ages, salaries, label="salaries") # this will be random 
#plt.show()  #if you do this the program will halt here until the plot is closed

# add x squared
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints # multiply each entry by itself

plt.plot(xpoints, ypoints, color = "r", label = "x squared")

plt.title("Random Plot")
plt.xlabel("Age")
plt.ylabel("Salaries")
plt.legend()
plt.show()

"""-----------------------------------------------------"""

plt.figure()  # Separating scatterplot and x^2 from the histogram

data = np.random.randn(100) # Generate random data
sns.histplot(data, kde=False, stat="density")

# Creating a normal distribution line
xmin, xmax =plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, np.mean(data), np.std(data))

# Adding the normal distribution line to the plot
plt.plot(x, p, "k", linewidth=2)
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Density")

plt.show() # see how the axis have changed
# Saving the plot
#plt.savefig("prettier-plot2.png")