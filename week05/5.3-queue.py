# queue.py
# Author: Marcin Kaminski

""" This program puts 10 random numbers (0-100) into a queue (list), then outputs 
all the values in the queue, then takes the number from the queue one at a time, prints it 
and the current numbers still in the queue."""

import random
queue = []
numberOfNumbers = 10
rangeTo = 100

for n in range(0, numberOfNumbers):
    queue.append(random.randint(0, rangeTo))

print (f"queue is {queue}")

while len(queue) !=0:

    currentNumber = queue.pop(0)
    print(f"current number is {currentNumber} and the queue is {queue}")

print("the queue is now empty")


