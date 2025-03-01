# topthree.py
# Author: Marcin Kaminski

# This program generates 10 random numbers (0-100).
# prints them out, then
# prints out the top 3

# I will use a list to store and
# manipulate the numbers

import random
# I'm programming the general case

howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range(0, howMany):
    numbers.append(random.randint(rangeFrom, rangeTo))
print(f"{howMany} random numbers\t {numbers}")

# I am keeping the original list

topOnes = numbers.copy()

topOnes.sort(reverse = True)
print(f"The top {topHowMany} are \t\t {topOnes[0:topHowMany]}")


