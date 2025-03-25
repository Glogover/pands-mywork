# messing with files
# Author: Marcin Kaminski

FILENAME= "data.txt"

#with open(FILENAME, "rt") as f:
    #data = f.read()
    #print(data)

#with open(FILENAME, "rt") as f:
    #or  data in f: # reading one line at a time
          #print(data) 
          #print(data, end="")
          #print(data.strip() ) 
          #print(data[:-1])

with open("data2.txt", "a") as f:
       f.write("how now\n")
       f.write("brown cow")

print("done")







