# append items
"""
* to add an item to the end of the list, use the "append()" method

example
- using the "append()" method to append an item 
"""
list1 = ["apple", "banana", "cherry"]
print(f"list1 before: ", list1)

list1.append("orange")
print(f"list1 after:  ", list1)



# insert items
"""
* to insert a list item at a specified index, use the "insert()" method

the "insert()", method inserts an item at the specified index

example
- insert an item as the second position
"""
list2 = ["apple", "banana", "cherry"]
print(f"list2 before: ", list2)

list2.insert(1, "kiwi")
print(f"list2 after:  ", list2)



# extend list
"""
to append elements from another "list" to the current list, use the "extend()" method

NOTE: the elements will be added to the end of the list

example
- add the elements of "tropical" to list3 
"""
list3 = ["apple", "banana", "cherry"]
print(f"list3 before: ", list3)

tropical = ["mango", "pineapple", "papaya"]
print(f"tropical: ", tropical)

list3.extend(tropical)
print(f"list3 after: ", list3)



# add any iterable
"""
* the "extend()" method does not have to append "lists", you can add any iterable object (tuples, sets, dictionaries etc)

example
- add elements of a tuple to a list 
"""
list4 = ["apple", "banana", "cherry"]
print(f"list4 before: ", list4)
print(type(list4))

tuple1 = ("kiwi", "orange")
print(f"tuple1 before: ", tuple1)
print(type(tuple1))

list4.extend(tuple1)
print(list4)
print(type(list4))







































