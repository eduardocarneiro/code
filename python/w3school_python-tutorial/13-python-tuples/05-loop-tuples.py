# python - loop tuples

# loop through a tuple 
"""
* you can loop through the tuple items by using a "for" loop 

example 
- iterate through the items and print the values
"""
tuple1 = ("apple", "banana", "cherry")

for i in tuple1:
    print(i)


# loop through the index numbers
"""
* you can also loop through the tuple items by referring to their index numbers
* use the "range()" and len() functions to create a suitable iterable
"""
tuple2 = ("apple", "banana", "cherry")

for i in range(len(tuple2)):
    print(tuple2[i])


# using a while loop 
"""
* you can loop through the tuple items by using a while loop 

* use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by 
referring to their indexes

NOTE: remember to increase the index by 1 after each iteration 

example 
- print all items, using a while loop to go through all index numbers
"""

tuple3 = ("apple", "banana", "cherry")

i = 0

while i < len(tuple3):
    print(tuple3[i])
    i += 1 


