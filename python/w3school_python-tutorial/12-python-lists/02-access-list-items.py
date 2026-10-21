# access items
"""
* "list" items are indexed and you can access them by referring to the index number

example
- print the second item of the list 

NOTE: the first item has index 0
"""
list1 = ["apple", "banana", "cherry"]

print(list1[2]) # output cherry



# negative indexing
"""
- negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc

example
- print the last item of the list 
"""
list2 = ["apple", "banana", "cherry"]

print(list2[-1]) # output cherry



# range of indexes
"""
* you can specify a range of indexes by specifying where to start and where to end the range 
* when specifying a range, the return value will be a new list with the specified items 

example
- return the third, fourth and fifth item 

NOTE1: the search will start at index 2 (included) and end at index 5 (not included)
NOTE2: remember that the first item has index 0
"""
list3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list3)
print(list3[2:5])


"""
* by leaving out the "start" value, the rande will start at the first item

example
- this example returns the items from the beginning to, but NOT including, "kiwi"
"""
list4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(f"list4: {list4}")
print(list4[:4])


"""
* by leaving out the "end" value, the range will go on to the end of the list 

example
- this example returns the items from "cherry" to the end 
"""
list5 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(f"list5: {list5}")
print(list5[2:])



# range of negative indexes 
"""
* specify negative indexes if you want to start the search from the end of the list

example
- this example returns the item from "orange" (-4) to, but NOT including "mango" (-1)
"""
list6 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(f"list6: {list6}")
print(list6[-4:-1])



# check if item exists
"""
* to determine if a specified item is present in a "list" use the "in" keyword

example
- check if "apple" is present in the list 
"""
list7 = ["apple", "banana", "cherry"]
print(f"list7: {list7}")
if "apple" in list7:
    print("Yes, 'apple' is in the list7")















































