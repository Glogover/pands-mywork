# messing with histograms
# Author: Marcin Kaminski

import numpy as np
import matplotlib.pyplot as plt
"""
np.random.seed(1) # Seeding random number generaor with value 1 (so the numbers are all the time the same)
normData = np.random.normal(size=10) # normal distribution data, 10000 points

plt.hist(normData)
#plt.show()
plt.savefig("histogram.png")
"""

fruit = np.array(["Apples", "Orange", "Banana"])
numbers = np.array([23,77,500])

plt.pie(numbers, labels = fruit) # Plotting a pie chart
plt.legend()
#plt.show()
plt.savefig("piechart.png")

