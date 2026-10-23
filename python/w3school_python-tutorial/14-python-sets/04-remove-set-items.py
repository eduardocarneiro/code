# python - remove set items


# remove item
"""
* to remove an item in a set, use the remove(), or the discard() method

example
- remove "banana" by using the remove() method 

NOTE: if the item to remove does not exist, remove() will raise an error
"""
set1 = {"apple", "banana", "cherry"}
print(f"set1 before remove(): ", set1)
set1.remove("banana")
print(f"set1 after remove(): ", set1)

"""
example
- remove "banana" byusing the discard() method 

NOTE: if the item to remove does not exist, discard() will not raise an error 
"""
set2 = {"apple", "banana", "cherry"}
print(f"set2 before discard(): ", set2)
set2.discard("banana")
print(f"set2 after discard(): ", set2)


"""
* you can also use the pop() method to remove an item , but this method will remove a random item, so you cannot be sure what item that gets removed

* the return value of the pop() method is the removed item 

example
- remove a random item by using the pop() method 
"""
set3 = {"orange", "pineapple", "melon"}
print(f"set3 before pop(): ", set3)
set3.pop()
print(f"set3 after pop()", set3)


"""
* sets are unordered, so when using the pop() method, you do not know which item that gets removed 

example: 
- the clear() method empties the set 
"""
set4 = {"apple", "banana", "cherry"}
print(f"set4 before clea(): ", set4)
set4.clear()
print(f"set4 after clear(): ", set4)


"""
example 
- the del keyword will delete the set completely
"""
set5 = {"apple", "banana", "cherry"}
print(f"set5 before del: ", set5)
del set5 
#print(f"set5 after del: ", set5)



































