# Modules
# One of the techniques for following DRY principles.
# Group similar codes and functions together in a sparate file.
# solves the problem of code file being too lengthy and complex.
# can be reused across several programs.
# Pyhton comes with alot of modules= python standard library.


import args 

num1 = 5
num2 = 6

result_add = args.add(num1, num2, 2,2,2,2,)
print(result_add)

result_sub = args.subtract(num1, num2)
print(result_sub)

result_mult = args.multiply(num1, num2)
print(result_mult)

result_div = args.divide(num1, num2)
print(result_div)


# another way to import specific functions from a module
print("---------------")
from args import add, subtract, multiply, divide

result_add = add(num1, num2)
print(result_add)
print("-----------")

# import math module from python library
import math, random

num1 = math.pow(4,3)
print(num1)

num2 = math.sqrt(64)
print(num2)

randValue = random.randrange(1, 10)
print(randValue)

 


