# python - math
"""
* python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers 
"""



# built-in math functions 
"""
* the "min()" and "max()" functions can be used to find the lowest or highest value in an iterable

example:
"""
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)


"""
* the "abs()" function returns the absolute (positive) value of the specified number 

example:
"""
x = abs(-7.25)
print(x)


"""
* the "pow(x, y)" function returns the value of x to power of y (xY)

example:
- return the value of 4 to the power of 3 (same as 4 * 4 * 4)
"""

x = pow(4, 3)
print(x)



# the math module 
"""
* python has also a built-in module called "math", which extends the list of mathematical functions 

* to use it, you must import "math" module 
 -------------
| import math |
 -------------

* when you have imported the "math" module, you can start using methods and constants of the module 

* the "math.sqrt()" method for example, returns the square root of a number 

example 
"""
import math 
x = math.sqrt(64)
print(x)




"""
* the "math.ceil()" method rounds a number upwards to its nearest integer

* the "math.floor()" method rounds a number downwards to its nearest integer, and returns the result 

example: 
"""
import math 
x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2 
print(y) # returns 1


"""
* the "math.pi" constant, returns the value of PI(3.14...)

example: 
"""
import math 
x = math.pi 
print(x)



# complete math module reference
"""
* "Math module reference - https://www.w3schools.com/python/module_math.asp " you will find a complete reference of all methods and constants that belongs to the math module  
"""





































