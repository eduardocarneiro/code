# python - access tuple items 

# access tuple items
"""
* you can access tuple items by referring to the index number, inside square brackets

example
- print the second item in the tuple 

NOTE: the first item has index 0
"""
tuple1 = ("apple", "orange", "banana")
print(f"tuple1: ", tuple1)
print(tuple1[1])



# negative indexing
"""
* negative indexing means start from the end

-1 refers to the last item 
-2 refers to the second last item etc.

example
- print the last item of the tuple
"""
tuple2 = ("apple", "banana", "cherry")
print(f"tuple2: ", tuple2)
print(tuple2[-1])



# range of indexes 
"""
* you can specify a range of indexes by specifying where to start and where to end the range 

* when specifying a range, the return value will be a new tuple with the specified items 

example 
- return the third, fourth and fifth item 

NOTE1: Remember that the first item has index 0
NOTE2: the search will start at index 2 (included) and end at index 5 (not included)
"""
tuple3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(f"tuple3: ", tuple3)
print(tuple3[2:5])


"""
* by leaving out the start value, the range will start at the first item

example
- this example returns the items from the beginning to, but NOT included, 'kiwi'
"""
tuple4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(f"tuple4: ", tuple4)
print(tuple4[:4])


"""
* by leaving out the end value, the range will go on to the end of the tuple 

example 
- this example returns the items from 'cherry' and to the end
"""
tuple5 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(f"tuple5: ", tuple5)
print(tuple5[2:])



# range of negative indexes 
"""
* specify negative indexes if you want to start the search from the END of the tuple 

example
- this example returns the items from index -4(included) to index -1 (excluded)
"""
tuple6 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(f"tuple6: ", tuple6)
print(tuple6[-4:-1]) # output "banana", "cherry", "orange"



# check if item exists
"""
* to determine if a specified item is present in a tuple use the "in" keyword

example 
- check if "apple" is present in the tuple 
"""
tuple7 = ("apple", "banana", "cherry")
print(f"tuple7: ", tuple7)

if "apple" in tuple7:
    print("YES, 'apple' is in the tuple7")


































