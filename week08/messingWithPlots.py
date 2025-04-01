# messing with matplotlib
# Author: Marcin Kaminski

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101)) # points from 1 to 100
ypoints = xpoints * xpoints # x squared

plt.plot(xpoints, ypoints, label="xsquared")
plt.plot(xpoints, xpoints, label="straight", color="blue") # Plotting a straight blue line
plt.legend()

randompoints = np.random.randint(1, 1000, 100) # 100 random points ranging from 1 to 1000
plt.scatter(xpoints, randompoints, label="random")

#plt.show() # Showing the figure
plt.savefig('lecture3.png') # Saving the figure


