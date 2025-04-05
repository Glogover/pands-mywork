# 8.15-normalDistribution2.py
# Author: Marcin Kaminski

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Preparing data
minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high=65, size=numberOfEntries)

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

data = np.random.randn(100)  # Normal distribution data

# Creating two plots next to each other
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: scatter + x^2
axs[0].scatter(ages, salaries, label="salaries")
axs[0].plot(xpoints, ypoints, color="r", label="x squared")
axs[0].set_title("Scatter + x²")
axs[0].set_xlabel("Age")
axs[0].set_ylabel("Salaries")
axs[0].legend()

# Plot 2: histogram + bell curve
sns.histplot(data, kde=False, stat="density", ax=axs[1])
xmin, xmax = axs[1].get_xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, np.mean(data), np.std(data))
axs[1].plot(x, p, "k", linewidth=2)
axs[1].set_title("Normal Distribution")
axs[1].set_xlabel("Value")
axs[1].set_ylabel("Density")

plt.tight_layout()
#plt.show()
plt.savefig("prettier-plot2.png")
