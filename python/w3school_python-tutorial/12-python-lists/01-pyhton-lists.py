# python lists
"""
* lists are used to store multiple items in a single variable
* lists are one of 4 built-in data types in python used to store collections of data, the other 3 are "tuples", "set" and "dictionary", all with different qualities and usage
* lists are created using - square brackets []

mylist = ["apple", "banana", "cherry"]
"""
thislist = ["apple", "banana", "cherry"]
print(thislist)




# list items
"""
* list items are ordered, changeable, and allow duplicate values.
* list items are indexed, the first item has index [0], the second item has index [1] etc
"""



# ordered 
"""
* when we say that list are ordered, it means that the items have a defined order, and that order will not changeable
* if you add new items to a list, the new items will be placed at the end of the list

NOTE: there are some "list methods - https://w3schools.com/python/python_lists_methods.asp" that will change the order, but in general: the order of the items will not change  
"""



# changeable
"""
* the list is changeable, meaning that we can change, add, and remove items in a list after it has been created 
"""



# allow duplicates
"""
* since lists are indexed, lists can have items with the same value 

example
- lists allow duplicate values 
"""
thilist2 = ["apple", "banana", "cherry", "apple", "banana"]



# list length
"""
* to determine how many items a list has, use the "len()" function

example 
- print the number of items in the list 
"""
thislist3 = ["apple", "banana", "cherry"]
print(thislist3)
print(len(thislist3))



# list items - data types 
"""
* list items can be of any data type 

example
- string, int and boolean data types 
"""
list1 = ["apple", "banana", "pineapple"]
list2 = [1, 3, 4, 6, 7]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

"""
* a list can contain different data types

example
- a list with strings, integers and boolean values 
"""
list4 = ["eoc", 41, True, "male"]
print(list4)



# type()
"""
* from python's perspective, lists are defined as objects with the data type "list"

<class 'list'>

example 
- what is the data type of a list 
"""
list5 = ["apple", "banana", "pineapple"]
print(type(list5))




# the "list()" constructor
"""
* it is also possible to use the "list()" constructor when creating a new list

example
- using the "list()" constructor to make a list 
"""
list6 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(list6)
print(type(list6))



# python collections (arrays)
"""
* there are four collection data types in the python programming language
    - "list"       is a collection which is ordered and changeable. Allows duplicate members
    - "tuple"      is a collection which is ordered and UNchangeable. Allows duplicate members
    - "set"        is a collection which is UNordered, UNchangeable[1], and UNindexed. No duplicate members
    - "dictionary" is a collection which is ordered[2] and changeable. No duplicate members 

[1] - "set" items are unchangeable, but you can remove and/or add items whenever you like
[2] - As of python version 3.7, dictionaries are ordered. In python 3.6 and earlier, dictionaries are UNordered 
"""
































