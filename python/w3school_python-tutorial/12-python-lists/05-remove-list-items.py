# remove specified item
"""
* the "remove()" method removes he specified item 

example
- remove "banana"
"""
list1 = ["apple", "banana", "cherry"]
print(f"list1 before: ", list1)

list1.remove("banana")
print(f"list1 after:  ", list1)


"""
* if there are more than one item with the specified value, the "remove()" method removes the first occurrence

example
- remove the first occurrence of "banana"
"""
list2 = ["apple", "banana", "cherry", "banana", "kiwi"]
print(f"list2 before: ", list2)

list2.remove("banana")
print(f"list2 after:  ", list2)



# remove specified index
"""
* the "pop()" method removes the specified index 

example
- remove the second item 
"""
list3 = ["apple", "banana", "cherry"]
print(f"list3 before: ", list3)

list3.pop(1)
print(f"list3 after:  ", list3)

"""
* if you do not specify the index, the "pop()" method removes the last item

example
- remove the last item 
"""

list4 = ["apple", "banana", "cherry"]
print(f"list4 before: ", list4)

list4.pop()
print(f"list4 after:  ", list4)


"""
* the "del" keyword also removes the specified index

example
- remove the first item
"""
list5 = ["apple", "banana", "cherry"]
print(f"list5 before: ", list5)

del list5[0]
print(f"list5 after:  ", list5)


"""
* the "del" keyword can also delete the list completely

example
- delete the entire list
"""

list6 = ["apple", "banana", "cherry"]
print(f"list6 before: ", list6)

del list6
#print(f"list6 after:  ", list6) # it will output a issue: list not defined



# clear the list 
"""
* the "clear()", method empties the list 
* the list still remains, but it has no content

example
- clear the list content 
"""
list7 = ["apple", "banana"]
print(f"list7 before: ", list7)
list7.clear()
print(f"list7 after:  ", list7)




























