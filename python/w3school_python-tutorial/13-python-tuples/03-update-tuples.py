# python - update tuples

"""
* tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created. But there are some workarounds
"""



# change tuple values
"""
* once a tuple is created, you cannot change its values. Tuples are "unchangeable", or "immutable" as it also is called

BUT there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple

example
- convert the tuple into a list to be able to change it 
"""
tuple1 = ("apple", "banana", "cherry")
list1 = list(tuple1)

list1[1] = "kiwi"
tuple1 = tuple(list1)

print(tuple1)



# add items 
"""
since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple 
1. convert into a list: just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple 

example
- convert the tuple into a list, add "orange", and convert it back into a tuple 
"""
tuple2 = ("apple", "banana", "cherry")
list2 = list(tuple2)

list2.append("orange")
tuple2 = tuple(list2)
print(tuple2)


"""
2. add tuple to a tuple: you are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple

example
- create a new tuple with the value "kiwi", and add that tuple 

NOTE: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as tuple
"""
tuple3 = ("apple", "banana", "cherry")
tuple4 = ("kiwi", )
tuple3 += tuple4
print(tuple3)



# remove items 
"""
NOTE: you cannot remove items in a tuple 

* tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items
"""
tuple5 = ("apple", "banana", "cherry")
tuple6 = list(tuple5)
tuple6.remove("apple")
tuple5 = tuple(tuple6)
print(tuple5)

"""
* you can delete the tuple completely

example 
- the "del" keyword can delete the tuple completely 
"""
tuple7 = ("apple", "banana", "cherry")
del tuple7
#print(tuple7) #it will raise an error, tuple no exists anymore



















































