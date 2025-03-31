# messing with matplotlib
# Author: Marcin Kaminski

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101)) # points from 1 to 100
ypoints = xpoints * xpoints # x squared

plt.plot(xpoints, ypoints)
plt.show()


