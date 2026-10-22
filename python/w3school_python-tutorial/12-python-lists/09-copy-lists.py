# python - copy lists

# copy a list
"""
* you cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and 
changes made in list1 will automatically also be made in list2 
"""



# use the copy() method
"""
* you can use the built-in list method copy() to copy a list 

example
- make a copy of a list with the copy() method 
"""
list1 = ["banana", "orange", "apple"]
print(f"list1: ", list1)
list2 = list1.copy()
print(f"list2: ", list2)



# use the list() method
"""
* another way to make a copy is to use the built-in method list()

example
- make a copy of a list with the list() method
"""
list3 = ["apple", "banana", "cherry"]
print(f"list3: ", list3)
list4 = list(list3)
print(f"list4: ", list4)



# use the slice operator 
"""
* you can also make a copy of a list by using the : (slice) operator

example 
- make a copy of a list with the ":" operator 
"""
list5 = ["banana", "apple", "orange"]
print(f"list5: ", list5)
list6 = list5[:]
print(f"list6: ", list6)



