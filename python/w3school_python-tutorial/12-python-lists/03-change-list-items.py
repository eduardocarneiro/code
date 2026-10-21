# change item value
"""
* to change the value of a specific item, refer to the index number

example
- change the second item 
"""
list1 = ["apple", "banana", "cherry"]
list1[1] = "orange"
print(list1)



# change a range of item values 
"""
* to change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values 

example
- change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"
"""
list2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(f"list2: ", list2)

list2[1:3] = ["blackcurrant", "watermelon"]
print(f"list2 after changes: ", list2)


"""
* if you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly

NOTE: the length of the list will change when the number of items inserted does not match the number of items replaced  

example
- change the second value by replacing it with two new values 
"""
list3 = ["apple", "banana", "orange"]
print(f"list3 before: ", list3)

list3[1:2] = ["kiwi", "watermelon"]
print(f"list3 after: ", list3)


"""
* if you insert LESS items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly

example
- change the second and third value by replacing it with one value 
"""
list4 = ["apple", "banana", "orange"]
print(f"list4 before: ", list4)

list4[1:3] = ["watermelon"]
print(f"list4 after:  ", list4)



# insert items
"""
* to insert a new list item, without replacing any of the existing values, we can use the "insert()" method

* the "insert()" methof inserts an item at the specified index

NOTE: as a result of the example above, the list will now contain 4 items

example
- insert "watermelon" as the third item 
"""
list5 = ["apple", "banana", "cherry"]
print(f"list5 before: ", list5)
list5.insert(2, "watermelon")
print(f"list5 after:  ", list5)




















