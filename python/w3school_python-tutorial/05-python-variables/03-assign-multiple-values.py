# many values to multiple variables
"""
* python allows you to assign values to multiple variables in one line
"""

x, y, z = "orange", "banana", "cherry"
print(x)
print(y)
print(z)


# one value to multiple variables
"""
* you can assign the same value to multiple variables in one line
"""

x = z = y = "orange"
print(x)
print(y)
print(z)


# unpack a collection
"""
* if you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking
"""

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)


