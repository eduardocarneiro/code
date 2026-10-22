# python - loop lists
# loop through a list
"""
* you can loop through the list items by using a "for" loop 

example
- print all items in the list, on by one
"""
list1 = ["apple", "banana", "orange"]

for i in list1:
    print(i)


# loop through the index numbers
"""
* you can also loop through the list items by referring to their index numbers
* use the "range()" and "len()" functions to create a suitable iterable

example
- print all items by referring to their index number
"""
list2 = ["banana", "apple", "orange"]

for i in range(len(list2)):
    print(list2[i])


# using a while loop
"""
* you can loop through the list items by using a "while" loop
* use the "len()" function to determine the length of the list, then start at 0  and loop your way through the list items by referring to their indexes 
* remember to increase the index by 1 after each iteration 

example
- print all items, using a "while" loop to go through all the index numbers 
"""
list3 = ["apple", "banana", "orange"]
i = 0 
while i < len(list3):
    print(list3[i])
    i = i + 1 



# looping using list comprehension
"""
* list comprehension offers the shortest syntax for looping through lists

example
- a short hand "for" loop that will print all items in a list 
"""
list4 = ["banana", "orange", "apple"]
[print(x) for x in list4]

