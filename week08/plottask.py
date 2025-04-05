# plottask.py
# Author: Marcin Kaminski

"""
This program displays:
- a histogram of a normal distribution of a 1000 values with 
a mean of 5 and standard deviation of 2, 
- and a plot of the function  h(x)=x³ in the range 0 to 10, 
on the one set of axes.
"""

# Import required libraries
import seaborn as sns # seaborn: a library for creating beautiful and informative statistics
import matplotlib.pyplot as plt # matplotlib.pyplot: a library for creating visualizations in Python
import numpy as np # numpy: a package for handling mathematics and multidimensional arrays
import pandas as pd # pandas: a data analysis and manipulation package
from scipy.stats import norm

# Create a sample from a normal distribution
mu, sigma = 5, 2  # mean and standard deviation
np.random.seed(1) # Seeding random number generator.The results will be the same every time the program is run, if the seed value is identical.
s = np.random.normal(mu, sigma, 1000) # Then we create a sample of 1000 values ​​from the normal distribution

# Create a range for the function h(x) = x^3
x = np.linspace(0, 10, num=1000) # This code creates a sequence of 1000 numbers (between 0 and 10). This means that we have 1000 evenly distributed points between 0 and 10.
y = x**3 # Then we generate the 'y' values ​​for these points.

# Create a DataFrame using Pandas
"""
In the next step, we create two dataframes using Pandas library.
The first dataframe 'df' contains two columns: "x" and "h(x)"
The second dataframe 'df_sample' contains one column 'Normal Distribution', which represents our sample from the normal distribution.
"""
df = pd.DataFrame({'x': x, 'h(x)': y})
df_sample = pd.DataFrame({'Normal Distribution': s})

# Figure
plt.figure(figsize=(10, 6)) # This code creates a 10 x 6 figure

# Draw a histogram
sns.histplot(data=df_sample, x="Normal Distribution", color="skyblue", label="Histogram", bins=30)
# The color is set to light blue and the label is 'Histogram'. The number of bins is 30.

# Add vertical lines for mean and standard deviation 
plt.axvline(mu, color='blue', linestyle='dashed', linewidth=1, label='Mean') # Mean
plt.axvline(mu + 3*sigma, color='green', linestyle='dotted', linewidth=1, label='+3σ')
plt.axvline(mu - 3*sigma, color='green', linestyle='dotted', linewidth=1, label='-3σ')


# Draw a plot h(x) = x^3
sns.lineplot(data=df, x="x", y="h(x)", color="green", label="h(x) = x³")
# The color is set to green and the label is "h(x) = x^3".


"""
*** The following section (Gaussian curve plotting) was developed with 
guidance from ChatGPT (OpenAI) ***
---------------------------------------------------------------------------
"""

# Generate x values over the range of the histogram
x_pdf = np.linspace(min(s), max(s), 1000)

# Compute the PDF for the normal distribution
pdf = norm.pdf(x_pdf, mu, sigma)

# Scale PDF to match histogram area
# Multiply by bin width and number of samples to match histogram height
bin_width = (max(s) - min(s)) / 30  # 30 bins as used in histplot
pdf_scaled = pdf * len(s) * bin_width

# Plot the Gaussian curve
plt.plot(x_pdf, pdf_scaled, color="red", label="Gaussian Curve")

"""
Note: 
PDF stands for Probability Density Function.
It gives you the relative likelihood of a random variable 
(in this case from a normal distribution).
Source: https://stackoverflow.com/questions/43602270/what-is-probability-density-function-in-the-context-of-scipy-stats-norm
--------------------------------------------------------------------------
"""



# Add labels of x and y axes
plt.xlabel("x")
plt.ylabel("y")

# Add title and legend
plt.title("Histogram and h(x) = x³ function")
plt.legend()
plt.grid(True) # Finally, we enable the grid on the chart using "plt.grid(True".

""" 
Last but not least, we save the generated plot to the file 'plottask.png' 
and display it on the screen
"""
plt.savefig("plottask.png")
plt.show()
