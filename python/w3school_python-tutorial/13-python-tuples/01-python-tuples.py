# python tuples
"""
mytuple = ("apple", "banana", "cherry")

* tuples are used to store multiple items in a single variable

* tuple is of 4 built-in data types in python used to store collections of data, the other 3 are 'lists', 'sets' and 'dictionary'
all with different qualities and usage

* a tuple is a collection which is ordered and unchangeable

* tuples are written with round brackets

example
- create a tuple 
"""
tuple1 = ("apple", "banana", "cherry")
print(tuple1)


"""
* tuples can also be created without the parentheses

example 
- tuples can also be created without the parentheses
"""
tuple2 = "apple", "banana", "cherry"
print(tuple2)
print(type(tuple2))



# tuples items
"""
* tuple items are ordered, unchangeable, and allow duplicate values 

* tuple items are indexed, the first item has index [0], the second item has index [1] etc
"""



# ordered
"""
* when we say that tuples are ordered, it means that the items have a defined order, and that order will not change 
"""



# unchangeable 
"""
* tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created 
"""



# allow duplicates
"""
* since tuples are indexed, they can have items with the same values

example
- tuples allow duplicate value 
"""
tuple3 = ("apple", "banana", "cherry", "apple", "banana")
print(tuple3)



# tuple length
"""
* to determine how many items a tuple has, use the len() function

example 
- print the number of items in the tuple 
"""
tuple4 = ("apple", "banana", "cherry")
print(f"tuple4: ", tuple4)
print(len(tuple4))



# create tuple with one item 
"""
* to create a tuple with only one item, you have to add a comma after the item, otherwise python will not recognize it as a tuple 

example
- one item tuple, remember the comma 
"""
tuple5 = ("apple",)
print(f"tuple5: ", tuple5)
print(type(tuple5))

tuple6 = ("apple")
print(f"tuple6: ", tuple6)
print(type(tuple6))



# create an empty tuple 
"""
* to create an empty tuple, use round brackets with no content

example
- create an empty tuple 
"""
tuple7 = ()
print(type(tuple7))



# tuple items - data types 
"""
* tuple items can be of any data type 

example 
- string, int and boolean data types 
"""
tuple8 = ("apple", "banana", "orange")
tuple9 = (1, 2, 3, 4, 5)
tuple10 = (True, False, False, True)


"""
* a tuple can contain different data types 

example 
- a tuple with strings, integers, and boolean values 
"""
tuple11 = ("abc", 1, True, 41, "male")
print(tuple11)



# type()
"""
* from python's perspective, tuples are defined as objects with the data type 'tuple'

<class 'tuple'>

example
- what is the data type of a tuple 
"""
tuple12 = ("apple", "banana", "cherry")
print(type(tuple12))



# the tuple() constructor 
"""
* it is also possible to use the tuple() constructor to make a tuple 

example 
- using the tuple() method to make a tuple 
"""
tuple13 = tuple(("apple", "banana", "orange")) # note the double round-brackets
print(f"tuple13: ", tuple13)
print(type(tuple13))



# python collections (arrays)
"""
* there are four collections data types in the python programming language:
    - 'list'       is a collection which is ordered and changeable. Allows duplicate members
    - 'tuple'      is a collection which is ordered and UNchangeable. Allows duplicates members
    - 'set'        is a collection which is UNordered, UNchageable[1], and UNindexed. NO duplicate members 
    - 'dictionary' is a collection which is ordered[2] and changeable. NO duplicate members 

[1] - set items are unchageable, but you can remove and/or add items whenever you like 
[2] - as of python version 3.7, dictionaries are ordered. In python 3.6 and earlier, dictionaries are UNordered 


NOTE: When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type 
for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security
"""






























































