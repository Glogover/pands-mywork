# More messing with functions
# Anomymous functions
# Author: Marcin Kaminski
""" 
x = lambda arg1: arg1 ** 2 # lambda functions are useful when using Pandas

answer = x(4)
print(answer)
"""
#businesstype = "standard"
businesstype = "reduced"

vatcalc= lambda amount: amount * 0.23 # 23% VAT rate

if businesstype == "reduced":
    vatcalc = lambda amount: amount * 0.135 # 13.5% VAT rate

cash = 10
print(vatcalc(cash))

# sort a list
numbers = [2, 33, 55, 1, 4]
sortednumbers = sorted(numbers) # built-in function

print(f"{numbers} sorted is {sortednumbers}")

# sort dctionary
data = [{"first": "Guido", "last": "Van Rossum", "YOB": 1956},
        {"first": "Grace", "last": "Hopper",     "YOB": 1906},
        {"first": "Alan", "last": "Turing",      "YOB": 1912}]

sorteddata = sorted(data, key=lambda x: x["YOB"])
for item in sorteddata:
    print(item)

