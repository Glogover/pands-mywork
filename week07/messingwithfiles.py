# messing with files
# Author: Marcin Kaminski

FILENAME= "data.txt"

#with open(FILENAME, "rt") as f:
    #data = f.read()
    #print(data)

#with open(FILENAME, "rt") as f:
    #for  data in f: # reading one line at a time
          #print(data) 
          #print(data, end="")
          #print(data.strip() ) # preferred way
          #print(data[:-1])

with open("data2.txt","w+") as f:
       f.write("what he hell\n")
       f.write("brown cow\n")
       f.seek(0)

       data = f.read()
       print(data)

print("done")







