# quiz.py
# Author: Marcin Kaminski

#with open("test-a.txt") as f:
    #data = f.read()
    #print(data)

#with open("test-b.txt", "w") as f:
    #data = f.write("test b\n") # return the number of chars written
    #print(data)

#with open("test-b.txt", "w") as f2: # open file again
    #data = f2.write("another line\n") 
    #print(data)

with open("test-d.txt", "w") as f:
    data = f.write("test d\n") # return the number of chars written (space is not included!)
    print(data)

with open("test-d.txt", "a") as f2: # open file again
    data = f2.write("another line\n") 
    print(data)