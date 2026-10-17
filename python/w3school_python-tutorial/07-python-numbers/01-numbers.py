# python numbers
"""
* there are three numeric types in pyhton
- int
- float
- complex
* variables of numeric types are created when ou assign a value to them
"""
x = 1   # int
y = 2.8 # float 
z = 1j  # complex

# verify the type of any object in python, use the type() function
print(type(x))
print(type(y))
print(type(z))


# int
"""
* Int, or integer, is a whole number, positive or negative whitout decimals, of unlimited length
"""
a = 1
b = 12342345435435345223
c = -3432423423

print(type(x))
print(type(y))
print(type(z))


# float
"""
* Float, or "floating point number" is a number, positive or negative, containing one or more decimals 
"""

d = 1.10
e = 1.0 
f = -42.321

print(type(d))
print(type(e))
print(type(f))

"""
* Float can also be scientific numbers with an "e" to indicate the power of 1.0
"""

g = 23e3
h = 12E4
i = -87.34e100

print(type(g))
print(type(h))
print(type(i))



# complex
"""
* complex numbers are written with a "j" as the imaginary part
"""
j = 3+5j
k = 5j
l = -5j

print(type(j))
print(type(k))
print(type(l))



# type conversion
"""
* you can convert from one type to another with the int(), float() and complex() methods
* you cannot convert complex numbers into another number type
"""

m = 1       # int 
n = 2.8     # float 
o = 1j      # complex 

# convert from int to float 
m1 = float(m)

# convert from float to int 
n1 = int(n)

# convert from int to complex 
o1 = complex(m)

print(m1)
print(n1)
print(o1)

print(type(m1))
print(type(n1))
print(type(o1))



# random number 
"""
* python does not have a random() function to make a random number, but python has a built-in module called "random" that can be used to make random numbers

* sample
* import the random module, and display a random number from 1 to 9
"""
import random
print(random.randrange(1, 10))


























































