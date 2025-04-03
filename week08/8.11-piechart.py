# 8.11-piechart.py
# Author: Marcin Kaminski

import numpy as np
import matplotlib.pyplot as plt

# make the array of occurences
possibleCounties = ["Kerry", "Galway", "Cork", "DirtyDublin", "Donegal"]
# pick 100 randomly from possible counties with the frequency set in p
counties = np.random.choice(
    possibleCounties,
    p=[0.1, 0.3, 0.2, 0.12, 0.28],
    size=(100)
)

# right now we need the number of occurences of each county
# this returns a tuple of the unique values and how many times they appear
unique, counts = np.unique(counties, return_counts=True)
plt.pie(counts, labels= unique)

#plt.show()
plt.savefig("piechart")
