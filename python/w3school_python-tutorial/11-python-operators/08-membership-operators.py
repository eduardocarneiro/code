# membership operators
"""
* membership operators are used to test if a sequence is presented in an object


 --------------------------------------------------------------------------------------------------------------
| operator      description                                                                         example    |
| in            returns "true" if a sequence with the specified value is present in the object      x in y     |
| not in        returns "true" if a sequence with the specified value is not present in the object  x not in y |
 --------------------------------------------------------------------------------------------------------------
"""

# examples 
"""
example 
- check if "banana" is present in a list
"""
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits) # true

"""
example
- check if "pineapple" is NOT present in a list
"""
fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits) # true 



# membership in strings
"""
* the membership operators also work with strings 
"""
text = "Hello World"
print("H" in text)      # true 
print("h" in text)      # false
print("hello" in text)  # false 
print("z" not in text)  # true
