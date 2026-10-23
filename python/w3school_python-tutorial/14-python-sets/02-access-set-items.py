# python - access set items

# access items 
"""
* you cannot access items in a set by referring to an index or a key

* but you can loop through the set items using a "for" loop, or ask if a specified value is present in a set, by using the "in" keyword

example
- loop through the set, and print the value
"""
set1 = {"apple", "banana", "cherry"}

for i in set1:
    print(i)



"""
example
- check if "banana" is present in the set
"""
set2 = {"apple", "banana", "cherry"}

print("banana" in set2)


"""
example 
- check if "banana" is NOT present in the set 
"""
set3 = {"apple", "banana", "cherry"}
print("banana" not in set3)



# change items
"""
* once set is created, you cannot change its items, but you can add new items
"""
