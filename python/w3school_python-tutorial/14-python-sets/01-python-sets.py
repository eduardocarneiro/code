# python sets

# set 
"""
* sets are written with curly brackets 
myset = {"apple", "banana", "cherry"}

* sets are used to store multiple items in a single variable

* set is one of 4 built-in data types in python used to store collections of data, the other 3 are "list", "tuple" and "dictionary", all with different qualities and usage

* a set is a collection which is unordered, unchangeable[1] and unindexed 

NOTE1: set items ae unchangeable, but you can remove items and add new items 
NOTE2: sets are unordered, so you cannot be sure in which order the items will appear 

example
- create a set 
"""

set1 = {"apple", "banana", "cherry"}
print(set1)
print(type(set1))



# set items
"""
* set items are unordered, unchangeable, and do not allow duplicate values
"""



# unordered 
"""
* unordered means that the items in a set do not have a defined order 
* set items can appear in a different order every time you use them, and cannot be referred to by index or key
"""



# unchangeable 
"""
* set items are unchangeable, meaning that we cannot change the items after the set has been created

NOTE: once a set is created, you cannot change its items, but you can remoe items and add new items 
"""



# duplicates NOT allowed
"""
* sets cannot have two items with same value 

example 
- duplicate values will be ignored
"""
set2 = {"apple", "banana", "cherry", "apple"}
print(set2)


"""
* the values "True" and 1 are considered the same value in sets, and are treated as duplicates 

example 
- True and 1 is considered the same value 
"""
set3 = {"apple", "banana", "cherry", True, 1, 2}

print(set3)


"""
* the values "False" and 0 are considered the same value in sets, and are treated as duplicates 

example 
- False and 0 is considered the same value 
"""
set4 = {"apple", "banana", "cherry", False, True, 0}
print(set4)



# get the length of a set
"""
* to determine how many items a set has, use the len() function

example 
- get the number of items in a set 
"""
set5 = {"apple", "banana", "cherry"}
print(set5)
print(len(set5))



# set items - data types
"""
* set items can be of any data type 

example
- string, int and boolean data types 
"""
set6 = {"apple", "banana", "cherry"}
set7 = {1, 2, 3, 4, 5}
set8 = {True, False, False, True}


"""
* set can contain different data types

example
- a set with strings, integers and boolean values
"""
set9 = {"apple", 1, True, "Banana"}



# type()
"""
* from python's perspective, sets are defined as objects with the data type 'set'

<class 'set'>

example 
- what is the data type of a set 
"""
set10 = {"apple", "banana"}
print(type(set10))



# the set() constructor
"""
it is also possible to use the set() constructor to make a set

example
- using the set() constructor to make a set 
"""
set11 = set(("apple", "banana", "cherry")) # note the double round-brackets 
print(set11)
print(type(set11))



# python collections (arrays)
"""
* there are four collection data type in the python programming language
    - "list" is a collection which is ordered and changeable. Allows duplicates members
    - "tuples" is a collection which is ordered and unchangeable. Allows duplicates members 
    - "set" is a collection which is unordered, unchageable[1], and unindexed. No duplicate members
    - "dictionary" is a collection which is ordered[2] and changeable. No duplicate members

[1] - set items are unchangeable, but you can remove items and add new items
[2] - as a python version 3.7, dictionaries are ordered. In python 3.6 and earlier, dictionaries are unordered
"""


































































































