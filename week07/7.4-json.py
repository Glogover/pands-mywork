# 7.4-json.py
# Author: Marcin Kaminski
# This program uses a function that reads in a dict object from file.

import json
FILENAME = "testdict.json"

def readDict():
    # this will throw an error if the file does not exist
    # it should readly just return an empty dict
    with open (FILENAME) as f:
        return json.load(f)

# test the function
somedict = readDict()
print(somedict)

