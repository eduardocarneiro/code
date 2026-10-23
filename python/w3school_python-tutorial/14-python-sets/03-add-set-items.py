# python - add set items

# add items
"""
* once a set is created, you cannot change its items, but you can add new items

* to add one item to a set use the add() method

example
- add an item to a set, using the add() method
"""

set1 = {"apple", "banana", "cherry"}
set1.add("orange")
print(set1)



# add sets
"""
* to add items from another set into the current set, use the update() method 

example 
- add elements from set3 into set2 
"""
set2 = {"apple", "banana", "cherry"}
set3 = {"pineapple", "mango", "papaya"}

set2.update(set3)
print(set2)



# add any iterable
"""
* the object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc)

example
- add elements of a list to a set 
"""
set4 = {"apple", "orange"}
list1 = ["banana", "cherry"]

set4.update(list1)
print(set4)


