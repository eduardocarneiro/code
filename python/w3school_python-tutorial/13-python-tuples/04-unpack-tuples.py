# python - unpack tuples 

# unpacking a tuple 
"""
* when we create a tuple, we normally assign values to it. this is called "packing" a tuple 

example
- packing a tuple 
"""
import re


fruits = ("apple", "banana", "cherry")


"""
* but, in python we are also allowed to extract the values back into variables. this is called "unpacking" 

example 
- unpacking a tuple

NOTE: the number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list
"""
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits 

print(green)
print(yellow)
print(red)



# using asterisk
"""
* if the number of variables is less than the number of values, you can add an "*" to the variable name and the values will be assigned to the variable as a list

example
- assign the rest of the values as a list called "red"
"""
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits 
print(green)
print(yellow)
print(red)


"""
* if the asterisk is added to another variable name than the last, python will assign values to the variable until the number of values left matches the number of variables left 

example 
- add a list of values the "tropic" variable
"""
fruits = ("apple", "banana", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)














