# testWhile.py
# Author: Marcin Kaminski

# counter controlled loop

count = 0
while(count < 10):
    print("count is ", count)  # if no "counter" there wull be an "infinite loop"
    count = count + 1
print ("at the end count is ", count)

count = 10
while count >= 0:
    print ("countdown", count)
    count -= 1
print("blast off")

# sentinal controlled loop

val = input("type somethiing (q to quit): ")
while val != 'q':
    print ("hi mom")
    val = input("q to quit: ")

print("all done")








