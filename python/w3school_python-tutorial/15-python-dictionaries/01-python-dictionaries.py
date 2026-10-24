# python dictionaries


# dictionary

"""
* dictinaries are used to store data values in key:value pairs

* a dictionary is a collection which is ordered[1], changeable and do not allow duplicates

* dictionaries are written with curly brackets, and have keys and values 

[1] - as of python version 3.7, dictionaries are ordered. in python 3.6 and earlier, dictionaries are unordered


example
- create and print a dictionary 
"""
dict1 = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1964
}
print(dict1)
print(type(dict1))



# dictionary items
"""
* dictionary items are ordered, changeable, and do not allow duplicates 

* dictionary items are presented in key:value pairs, and can be referred to by using the key name 

example
- print the "brand" value of the dictionary 
"""
dict2 = {
    "brand": "mitsubishi",
    "model": "l200 triton",
    "year": 2015
}
print(dict2["brand"])



# ordered or unordered
"""
* when we say that dictionaries are ordered, it means that the items have a defined order, and that order will not changeable

* unordered means that the items do not have a defined order, you cannot refer to an item by using a index

NOTE: as of python version 3.7, dictionaries are ordered. in python 3.6 and earlier, dictionaries are unordered 
"""



# changeable
"""
* dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created
"""



# duplicates NOT allowed
"""
* dictionaries cannot have two items with the same key 

example 
- duplicate values wiil overwrite existing value 
"""
dict3 = {
    "brand": "mitsubishi",
    "model": "l200 triton",
    "year": 2015,
    "year": 2016
}
print(dict3)



# dictionary length

"""
* to determine how many items a dictionary has, use the "len()" function

example
- print the number of items in the dictionary 
"""
print(len(dict3))



# dictionary items - data types
"""
* the values in dictionary items can be of any data type 

example 
- string, int, boolean, and list data type
"""
dict4 = {
    "brand": "mitsubishi",
    "eletric": False,
    "year": 2015,
    "colors": ["black", "white", "silver"]
}
print(dict4)



# type()
"""
* from python's perspective, dictionaries are defined as objects with the data type 'dict'

<class 'dict'>

example 
- print the data type of a dictionary 
"""
print(type(dict4))



# the dict() constructor
"""
* it is also possible to use the dict() constructor to make a dictionary

example 
- using the dict() method to make a dictionary 
"""
dict5 = dict(name = "Edu", age=41, country = "Brazil")
print(dict5)



# python collections (arrays)
"""
* there are four collection data types in the python programming language
    - "list" is a collection which is ordered and changeable. Allows duplicates members
    - "tuple" is a collection which is ordered and unchangeable. Allows duplicate members
    - "set" is a collection which is unordered, unchangeable[1], and unindexed. no duplicate members 
    - "dictionary" is a collection which is ordered[2] and changeable. no duplicate members 

[1] - set items are unchagenable, but you can remove and/or add items whenever you like 
[2] - as a python version 3.7 dictionaries are ordered. in python 3.6 and earlier, dictionaries are unordered 
"""


























































