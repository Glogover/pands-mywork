# Messing with lists
# Author: Macin Kaminski
"""  
boats = ['Sigma', 23, [1,2,3], {}]

boats = boats + [1,2,3]

print(boats)

print(len(boats))

for boat in boats:
    print(type(boat))
"""

ages = [12,21,23,34]

sum = 0
for age in ages:
    sum += age

print(sum)

print(ages[0])
print(ages[1])
print(ages[-1])
print(ages[-2])

print(ages[0:3])
print(ages[:3])
print(ages[-3:])

string ="1234567890"
print(string[-6:])
print(string[-4:])
print(string[6:])

print(ages[::2])  # Prints every second element
print(ages[::-1])  # Specifies a negative step, which will reverse the array; every element backwards

ages[0] = 100  # Changes element

print(ages)

ages[1:3] = [55,56] # Changes multiple elements
print(ages)





