# Messing with dictionaries
# Author: Marcin Kaminski

car = {
   "make" : "ford",
   "model" : "mondeo",
   "year" : 2006,
   "owner" : { 
       "name" : "andrew",
       "driver-number": 1123
       }
 }

print(car)
print(car["make"])

attr = "model"
print(car[attr])
print(car["owner"])
print(car["owner"]["name"])
print(car["owner"].get("name"))
print(car["owner"].get("names"))  # "names" does not exist
print(type(car["owner"].get("names")))


