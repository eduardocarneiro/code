# identity operators
"""
* identity operators are used o compare the objects, not if they are equal, but if they are actually the same object, with the same memory location


 --------------------------------------------------------------------------------------
| operator      description                                                 example    |
| is            returns "true" if both variables are the same object        x is y     |
| is not        returns "true" if both variables are not the same object    x is not y |
 --------------------------------------------------------------------------------------
 
"""

# examples
"""
example
- the "is" operator returns "true" if both variables point to the same object
"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # true
print(x is y) # false
print(x == y) # true 

"""
example
- the "is not" operator returns "true" if both variables do not point to the same object 
"""
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y) # true 



# difference between "is" and "=="
"""
- "is" checks if both variables point to the same object in memory 
- "==" checks if the values of both variables are equal 
"""
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y) # true 
print(x is y) # false
