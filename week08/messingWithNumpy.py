# Messing with Numpy
# Author: Marcin Kaminski

import numpy as np

list_of_numbers = [1,2,3, "asdf"]
list_of_numbers = list_of_numbers + [3]
print("list", list_of_numbers)

numbers = np.array([1,2,3,4]) # you can only store one variable type inside numpy
#numbers = numbers * 3
numbers = numbers * [1,2,3,5]


print("array", numbers)  # when printing, no commas between numbers


#rando = np.random.randint(100,200,30) # producing 30 random integers between 100 and 200
#print(rando)
#normalrando = np.random.normal(size = 100)  # producing a 100 random numbers around a mean of 0 (normal distribution)
#print(normalrando)

normalrando = np.random.normal(loc = 50, scale = 20,  size = 100) # mean = 50, standard dev = 20
print(normalrando)









